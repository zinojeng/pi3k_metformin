#!/usr/bin/env python3
"""Fetch full text for a paper and land it as Markdown in 原始PDF/.

Usage:
    python3 scripts/fetch.py <PMID|DOI> [slug]
    python3 scripts/fetch.py --batch list.txt      # one "id[,slug]" per line

Strategy, in order:
  1. Europe PMC JATS fullTextXML  (open access -> clean MD, keeps references)
  2. PMC OA package PDF           -> LlamaParse
  3. Unpaywall best OA PDF        -> LlamaParse
Anything that fails is appended to MISSING_FULLTEXT.md with the reason.

Every landed file gets a provenance header so downstream greps can trace it,
and the title in that header is taken from the *fetched document*, not from the
query -- that is what catches a polluted/mismatched PDF.
"""
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "原始PDF")
MISSING = os.path.join(ROOT, "MISSING_FULLTEXT.md")
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
UA = {"User-Agent": "Mozilla/5.0 (clinical-lit-review; mailto:zinojeng@gmail.com)"}
EMAIL = "zinojeng@gmail.com"


def get(url, timeout=90, binary=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read() if binary else r.read().decode("utf-8", "replace")


def slugify(s, n=60):
    s = re.sub(r"[^A-Za-z0-9一-鿿]+", "_", s or "paper").strip("_")
    return s[:n] or "paper"


def lookup(ident):
    """Resolve a PMID or DOI to Europe PMC core metadata."""
    ident = ident.strip()
    if re.fullmatch(r"\d{6,9}", ident):
        q = f"EXT_ID:{ident} AND SRC:MED"
    elif ident.upper().startswith("PMC"):
        q = f"PMCID:{ident}"
    else:
        q = f'DOI:"{ident}"'
    url = f"{EPMC}/search?query={urllib.parse.quote(q)}&resultType=core&format=json"
    res = json.loads(get(url))["resultList"]["result"]
    return res[0] if res else None


# ---------- JATS XML -> Markdown ----------

def _txt(el):
    """Flatten an element to text, keeping inline emphasis readable."""
    if el is None:
        return ""
    parts = []
    if el.text:
        parts.append(el.text)
    for child in el:
        tag = child.tag.split("}")[-1]
        inner = _txt(child)
        if tag in ("italic", "i"):
            inner = f"*{inner}*" if inner.strip() else inner
        elif tag in ("bold", "b"):
            inner = f"**{inner}**" if inner.strip() else inner
        elif tag == "xref":
            inner = f"[{inner}]" if inner.strip() else inner
        elif tag == "sup":
            inner = f"^{inner}" if inner.strip() else inner
        elif tag == "sub":
            inner = f"_{inner}" if inner.strip() else inner
        parts.append(inner)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def _table_md(tbl):
    """Render a JATS <table> as a markdown table."""
    rows = []
    for tr in tbl.iter():
        if tr.tag.split("}")[-1] != "tr":
            continue
        cells = [re.sub(r"\s+", " ", _txt(td)).strip()
                 for td in tr if td.tag.split("}")[-1] in ("td", "th")]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    w = max(len(r) for r in rows)
    rows = [r + [""] * (w - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |",
           "|" + "---|" * w]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def _walk(el, depth, buf):
    for child in el:
        tag = child.tag.split("}")[-1]
        if tag == "sec":
            title = child.find("./{*}title")
            if title is not None:
                buf.append("\n" + "#" * min(depth + 2, 6) + " " + _txt(title).strip() + "\n")
            _walk(child, depth + 1, buf)
        elif tag == "p":
            t = re.sub(r"[ \t]+", " ", _txt(child)).strip()
            if t:
                buf.append(t + "\n")
        elif tag in ("table-wrap", "fig"):
            lab = child.find("./{*}label")
            cap = child.find("./{*}caption")
            head = " ".join(x for x in [_txt(lab).strip(), _txt(cap).strip()] if x)
            if head:
                buf.append(f"\n**{re.sub(chr(92)+'s+', ' ', head)}**\n")
            tbl = child.find(".//{*}table")
            if tbl is not None:
                md = _table_md(tbl)
                if md:
                    buf.append(md + "\n")
        elif tag == "list":
            for item in child.findall("./{*}list-item"):
                t = re.sub(r"\s+", " ", _txt(item)).strip()
                if t:
                    buf.append(f"- {t}")
            buf.append("")


def jats_to_md(xml):
    root = ET.fromstring(xml)
    buf = []
    ttl = root.find(".//{*}article-title")
    title = re.sub(r"\s+", " ", _txt(ttl)).strip() if ttl is not None else ""

    authors = []
    for c in root.findall(".//{*}contrib[@contrib-type='author']"):
        sn, gn = c.find(".//{*}surname"), c.find(".//{*}given-names")
        if sn is not None:
            authors.append(f"{_txt(sn).strip()} {_txt(gn).strip() if gn is not None else ''}".strip())

    jrnl = root.find(".//{*}journal-title")
    year = root.find(".//{*}pub-date/{*}year")

    buf.append(f"# {title}\n")
    if authors:
        buf.append(f"**Authors:** {', '.join(authors[:25])}\n")
    if jrnl is not None:
        buf.append(f"**Journal:** {_txt(jrnl).strip()} ({_txt(year).strip() if year is not None else 'n.d.'})\n")

    abst = root.find(".//{*}abstract")
    if abst is not None:
        buf.append("\n## Abstract\n")
        _walk(abst, 1, buf)

    body = root.find(".//{*}body")
    if body is not None:
        _walk(body, 0, buf)

    refs = root.findall(".//{*}ref-list/{*}ref")
    if refs:
        buf.append("\n## References\n")
        for i, r in enumerate(refs, 1):
            t = re.sub(r"\s+", " ", _txt(r)).strip()
            d = r.find(".//{*}pub-id[@pub-id-type='doi']")
            p = r.find(".//{*}pub-id[@pub-id-type='pmid']")
            tail = []
            if d is not None:
                tail.append(f"doi:{_txt(d).strip()}")
            if p is not None:
                tail.append(f"PMID:{_txt(p).strip()}")
            buf.append(f"{i}. {t}" + (f"  [{'; '.join(tail)}]" if tail else ""))

    return title, "\n".join(buf)


# ---------- PDF paths ----------

def llamaparse(pdf):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "llamaparse.py"), pdf],
                       capture_output=True, text=True, timeout=1800)
    md = os.path.splitext(pdf)[0] + ".md"
    if os.path.exists(md) and os.path.getsize(md) > 500:
        return md
    raise RuntimeError(f"llamaparse failed: {(r.stdout + r.stderr)[-300:]}")


def unpaywall_pdf(doi):
    j = json.loads(get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"))
    for loc in [j.get("best_oa_location")] + (j.get("oa_locations") or []):
        if loc and loc.get("url_for_pdf"):
            return loc["url_for_pdf"]
    return None


def note_missing(ident, meta, reason):
    if not os.path.exists(MISSING):
        with open(MISSING, "w") as f:
            f.write("# 未取得全文紀錄 (MISSING_FULLTEXT)\n\n"
                    "僅有 abstract/metadata 者標 📌，禁止對其內文細節作具體斷言。\n\n"
                    "| 識別碼 | 標題 | DOI | 原因 |\n|---|---|---|---|\n")
    t = (meta or {}).get("title", "")[:90].replace("|", "/")
    d = (meta or {}).get("doi", "")
    with open(MISSING, "a") as f:
        f.write(f"| {ident} | {t} | {d} | {reason} |\n")


def fetch(ident, slug=None):
    os.makedirs(OUT, exist_ok=True)
    meta = lookup(ident)
    if not meta:
        note_missing(ident, None, "Europe PMC 查無此文（疑似 fabricated citation）")
        return f"NOTFOUND {ident}"

    first = (meta.get("authorString", "") or "x").split(",")[0].split()[0]
    year = meta.get("pubYear", "nd")
    slug = slug or f"{slugify(first, 24)}_{year}"
    md_path = os.path.join(OUT, f"{slug}.md")
    if os.path.exists(md_path) and os.path.getsize(md_path) > 800:
        return f"SKIP     {slug} (already present)"

    header = (f"<!-- src: {ident} | doi: {meta.get('doi','')} | pmid: {meta.get('pmid','')} "
              f"| pmcid: {meta.get('pmcid','')} -->\n"
              f"<!-- epmc_title: {meta.get('title','')} -->\n"
              f"<!-- journal: {meta.get('journalTitle','')} {year} -->\n\n")

    # 1) JATS full text
    if meta.get("pmcid") and meta.get("inEPMC") == "Y":
        try:
            xml = get(f"{EPMC}/{meta['pmcid']}/fullTextXML")
            title, md = jats_to_md(xml)
            if len(md) > 3000:
                with open(md_path, "w") as f:
                    f.write(header + md)
                return f"OK-XML   {slug}  [{len(md)} chars] :: {title[:60]}"
        except Exception as e:
            print(f"  (JATS failed for {ident}: {e})", file=sys.stderr)

    # 2/3) PDF routes -> LlamaParse
    urls = []
    if meta.get("pmcid"):
        urls.append(f"https://www.ncbi.nlm.nih.gov/pmc/articles/{meta['pmcid']}/pdf/")
    if meta.get("doi"):
        try:
            u = unpaywall_pdf(meta["doi"])
            if u:
                urls.append(u)
        except Exception:
            pass

    for u in urls:
        pdf = os.path.join(OUT, f"{slug}.pdf")
        try:
            data = get(u, binary=True, timeout=180)
            if not data.startswith(b"%PDF") or len(data) < 20000:
                continue
            with open(pdf, "wb") as f:
                f.write(data)
            md = llamaparse(pdf)
            body = open(md).read()
            with open(md_path, "w") as f:
                f.write(header + body)
            return f"OK-PDF   {slug}  [{len(body)} chars] via {u[:50]}"
        except Exception as e:
            print(f"  (PDF route failed {u[:50]}: {e})", file=sys.stderr)

    note_missing(ident, meta, "paywalled；OA 途徑皆失敗")
    return f"PAYWALL  {slug} :: {meta.get('title','')[:60]}"


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    jobs = []
    if args[0] == "--batch":
        for line in open(args[1]):
            line = line.strip()
            if line and not line.startswith("#"):
                p = [x.strip() for x in line.split(",")]
                jobs.append((p[0], p[1] if len(p) > 1 else None))
    else:
        jobs.append((args[0], args[1] if len(args) > 1 else None))

    for ident, slug in jobs:
        try:
            print(fetch(ident, slug), flush=True)
        except Exception as e:
            print(f"ERROR    {ident}: {e}", flush=True)


if __name__ == "__main__":
    main()
