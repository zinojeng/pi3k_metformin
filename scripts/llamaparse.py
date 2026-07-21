#!/usr/bin/env python3
"""PDF -> Markdown via LlamaParse.

Usage:  python3 scripts/llamaparse.py <file.pdf> [more.pdf ...]
Writes <file>.md next to each PDF. Skips if the .md already exists.
Exits non-zero only if every file failed.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

API_KEY = os.environ.get("LLAMA_CLOUD_API_KEY", "").strip()
BASE = "https://api.cloud.llamaindex.ai/api/v1/parsing"
HDR = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}


def _get(url):
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8", "replace")


def upload(pdf):
    # curl handles multipart cleanly; keeps this dependency-free.
    out = subprocess.run(
        ["curl", "-sS", "-X", "POST", f"{BASE}/upload",
         "-H", f"Authorization: Bearer {API_KEY}",
         "-F", f"file=@{pdf};type=application/pdf",
         "-F", "parse_mode=parse_page_with_agent",
         "-F", "high_res_ocr=true",
         "-F", "outlined_table_extraction=true"],
        capture_output=True, text=True, timeout=600)
    if out.returncode != 0:
        raise RuntimeError(f"curl failed: {out.stderr[:400]}")
    try:
        return json.loads(out.stdout)["id"]
    except Exception:
        raise RuntimeError(f"no job id in response: {out.stdout[:400]}")


def wait(job, timeout=1200):
    deadline = time.time() + timeout
    while time.time() < deadline:
        st = json.loads(_get(f"{BASE}/job/{job}")).get("status", "")
        if st == "SUCCESS":
            return
        if st in ("ERROR", "FAILED", "CANCELED"):
            raise RuntimeError(f"job {job} ended as {st}")
        time.sleep(6)
    raise RuntimeError(f"job {job} timed out")


def convert(pdf):
    md_path = os.path.splitext(pdf)[0] + ".md"
    if os.path.exists(md_path) and os.path.getsize(md_path) > 500:
        return md_path, "skipped (exists)"
    job = upload(pdf)
    wait(job)
    md = json.loads(_get(f"{BASE}/job/{job}/result/markdown")).get("markdown", "")
    if len(md) < 200:
        raise RuntimeError(f"suspiciously short markdown ({len(md)} chars)")
    with open(md_path, "w") as f:
        f.write(md)
    return md_path, f"ok ({len(md)} chars)"


def main():
    if not API_KEY:
        sys.exit("LLAMA_CLOUD_API_KEY not set")
    files = sys.argv[1:]
    if not files:
        sys.exit("usage: llamaparse.py <file.pdf> ...")
    ok = 0
    for pdf in files:
        if not os.path.exists(pdf):
            print(f"MISSING  {pdf}")
            continue
        try:
            path, note = convert(pdf)
            print(f"OK       {path}  [{note}]")
            ok += 1
        except Exception as e:
            print(f"FAIL     {pdf}: {e}")
    print(f"\n{ok}/{len(files)} converted")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
