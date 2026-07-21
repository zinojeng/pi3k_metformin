# 未取得全文紀錄 (MISSING_FULLTEXT)

**最後更新：2026-07-21（全文補齊後之重組稿階段；取代先前所有版本）**

僅有 abstract／metadata 者標 📌，**禁止對其內文細節作具體斷言**；本地有全文可 grep 者標 📄。

判準：`原始PDF/*.md` 檔案大小 < 5,000 bytes 即視為 abstract-only（📌）。

---

## 0. 清點結果

| 項目 | 數量 |
|---|---|
| `原始PDF/` 內 `.md` 檔總數 | **71** |
| 其中重複落地（同一 PMID 兩份檔） | **2 組**（見 §2） |
| **獨立文獻數** | **69** |
| 取得全文（📄） | **40** |
| 僅有 abstract／metadata（📌） | **29** |
| 全文取得率 | **約 58%（40/69）** |

---

## 1. 已解除之「未取得全文」項目（由使用者提供 PDF 後補齊）

| PMID | 檔名 | 前版狀態 | 現況 | 逐字事實擷取稿 |
|---|---|---|---|---|
| 32416251 | `SOLAR1_AE_Rugo_2020.md` | 📌 paywalled；OA 途徑皆失敗 | ✅ **📄 全文已落地（81,006 字元）** | `來源/fulltext_facts_SOLAR1.md` |
| 37743730 | `RealWorld_Shen_2023.md` ／ `MSKCC_RealWorld_Shen_2023.md` | 📌 paywalled；OA 途徑皆失敗 | ✅ **📄 全文已落地**（`MSKCC_...` 為 50,402 字元之較完整版） | `來源/fulltext_facts_MSKCC.md` |
| 39476340 | `INAVO120_Turner_2024.md` | 📌（章節撰寫當下） | ✅ **📄 全文已落地（77,567 字元）** | `來源/fulltext_facts_INAVO120.md` |

三篇皆已肉眼驗證與 metadata 相符。**初稿因其為 📌 而對內文細節一律迴避；全文到位後已改寫各章並補入實際數字**（見成品之 Z-1、Z-3、Z-5）。

> ⚠️ 稽核提醒：C-1／C-5／K-1／K-7 曾依前版標記寫出「僅有 abstract、不得引用」之聲明，**已全數更正**。
> ⚠️ 使用規則：**跨章節同一數字如有歧異，一律以三份 `fulltext_facts_*.md` 為準。**

### 1-1. 全文到位後仍無法補上的空白（不得以先驗知識填補）

| 論文 | 原文未報告之項目 |
|---|---|
| SOLAR-1 AE 專文 | metformin 之 titration 排程（全文無任何 mg 劑量）；單獨因高血糖之減量／中斷率；diabetic 次族群（n=12）之分級發生率；停藥後回復至 grade 0/1 之中位天數；**`ketoacid`／`DKA`／`hyperosmolar` grep 0 命中 → 只能寫「本文未報告 DKA/HHS」** |
| INAVO120 主論文 | **grade 3 與 grade 4 未拆分**（僅合併 5.6%）；median time to onset／resolution；因高血糖之中斷與永久停藥率；實際 metformin 使用率與「高風險」之操作型定義；Supplementary Appendix（Table S1–S3）未落地 |
| MSKCC Shen 2023 | DKA 之實際人數與比率；HHS；腹瀉／脫水／eGFR 資料；多變項迴歸之 OR／95% CI（統計法為 Pearson's χ²）；BMI／HbA1c 分層之實際發生率百分比 |

---

## 2. 重複落地檔（各計為 1 篇獨立文獻）

| PMID | 檔案 A | 檔案 B | 說明 |
|---|---|---|---|
| 38638399 | `METALLICA_Llombart_2024.md` | `METALLICA_LlombartCussac_2024.md` | 同一篇（DOI 10.1016/j.eclinm.2024.102520，PMCID PMC11024566）。G 章引用檔案 A、其餘章節引用檔案 B，G 章開頭已加註對照聲明 |
| 37743730 | `RealWorld_Shen_2023.md` | `MSKCC_RealWorld_Shen_2023.md` | 同一篇（DOI 10.1002/cncr.34928）。**本版起各章統一引用內容較完整之 `MSKCC_RealWorld_Shen_2023.md`**（前版曾記為統一引用 `RealWorld_Shen_2023.md`，已更正） |

---

## 3. 目前仍為 📌（僅 abstract／metadata）之 29 篇

**對以下文獻，本回顧僅引用其 abstract 層級之敘述，不對正文、表格、supplementary 或 subgroup 作任何具體斷言。**

| # | 檔名 | PMID | DOI | 檔案大小 |
|---|---|---|---|---|
| 1 | ADA_SOC2026_Ch3.md | 41358891 | 10.2337/dc26-s003 | 1,925 |
| 2 | Alpelisib_Juric_JAMAOnc_2019.md | 30543347 | 10.1001/jamaoncol.2018.4475 | 4,011 |
| 3 | Alpelisib_Juric_JCO_2018.md | 29401002 | 10.1200/jco.2017.72.7107 | 3,703 |
| 4 | BYLieve_EoC_2024.md | 38142701 | 10.1016/s1470-2045(23)00673-3 | 1,301 |
| 5 | BYLieve_Rugo_2021.md | 33794206 | 10.1016/s1470-2045(21)00034-6 | 3,819 |
| 6 | BYLieve_Rugo_2024.md | 39637900 | 10.1016/s1470-2045(24)00673-9 | 3,822 |
| 7 | Claims_Ismail_2026.md | 42159385 | 10.1177/10781552261451729 | 2,983 |
| 8 | DKA_Farah_2020.md | 33244501 | 10.4158/accr-2020-0452 | 2,846 |
| 9 | DPP_Knowler_2002.md | 11832527 | 10.1056/nejmoa012512 | 2,928 |
| 10 | Discont_Cheung_2022.md | 35000092 | 10.1007/s10549-021-06476-1 | 2,932 |
| 11 | Elderly_Cook_2021.md | 33752998 | 10.1016/j.jgo.2021.03.007 | 2,705 |
| 12 | FAERS_DKA_Ziegengeist_2024.md | 38245400 | 10.1016/j.clbc.2024.01.004 | 2,930 |
| 13 | FDA_Inavolisib_Wedam_2025.md | 40845250 | 10.1200/jco-25-00663 | 2,961 |
| 14 | FrenchEAP_BelloRoufai_2023.md | 36611120 | 10.1038/s41388-022-02585-3 | 2,554 |
| 15 | HHS_DKA_Chafai_2022.md | 35750516 | 10.1016/j.ando.2022.02.004 | 1,222 |
| 16 | INAVO120_OS_Jhaveri_2025.md | 40454641 | 10.1056/nejmoa2501796 | 2,904 |
| 17 | InsulinFeedback_Noch_2023.md | 37399061 | 10.1093/neuonc/noad117 | 2,823 |
| 18 | Landscape_Mosele_2020.md | 32067679 | 10.1016/j.annonc.2019.11.006 | 2,387 |
| 19 | Mech_Crouthamel_AKT_2009.md | 19118049 | 10.1158/1078-0432.ccr-08-1253 | 3,041 |
| 20 | Mech_Drullinsky_2020.md | 32274666 | 10.1007/s10549-020-05618-1 | 2,811 |
| 21 | **Mech_Goncalves_NEJM_2018.md** | 30462943 | 10.1056/nejmra1704560 | **993 —— 連 abstract 內文都未取得，本回顧不對其作任何斷言** |
| 22 | Meta_Martel_2018.md | 29108713 | 10.1016/j.ctrv.2017.09.009 | 2,836 |
| 23 | Mgmt_Busaidy_JCO_2012.md | 22778315 | 10.1200/jco.2011.39.7356 | 2,884 |
| 24 | Preclin_Fritsch_BYL719_2014.md | 24608574 | 10.1158/1535-7163.mct-13-0865 | 2,599 |
| 25 | Preclin_Hanan_Inavolisib_2022.md | 36455032 | 10.1021/acs.jmedchem.2c01422 | 2,143 |
| 26 | Prevention_Moore_2025.md | 39462728 | 10.1016/j.clbc.2024.09.017 | 3,046 |
| 27 | Prophylaxis_Burnette_2023.md | 36409396 | 10.1007/s10549-022-06798-8 | 2,855 |
| 28 | SOLAR1_Andre_2019.md | 31091374 | 10.1056/nejmoa1813904 | 3,557 |
| 29 | SOLAR1_OS_Andre_2021.md | 33246021 | 10.1016/j.annonc.2020.11.011 | 3,577 |

---

## 4. 未取得全文之原因

1. **付費牆／非開放取用（non-OA）**：多數 📌 檔之檔頭原因為「無 PMC 全文（非 OA）」或「ncbi_efetch 取回之 XML 無可用 body（publisher 不開放全文下載）」。
2. **LlamaParse 之 PDF 解析路徑兩輪皆未執行**：`.env` 於本工作階段不可讀（macOS TCC EPERM），故非 OA 文獻僅落地 abstract。少數（SOLAR-1 AE、INAVO120 主論文、Shen 2023）由使用者直接上傳 PDF 而取得全文。

---

## 5. 仍存在的關鍵缺口（不得以先驗知識補洞）

1. **Piqray／Itovebi／Truqap 之官方仿單 PDF 未落地至 `原始PDF/`**。本文所有【L1】內容來自 `來源/label_alpelisib.md`（51,926 bytes）、`來源/label_inavolisib.md`（37,305 bytes）與 `來源/guideline_ada_comparators.md` 之**逐字擷取稿**——此三檔完整落地且可 grep，【L1】論斷有可驗證來源。
2. **SOLAR-1 主論文（31091374）與 BYLieve（33794206）之劑量調整表、subgroup、supplementary 一律不得引用**。
3. **NCCN 指引因付費／登入牆無法查證；ESMO 未取得針對 PI3Ki 高血糖之專門聲明**。
4. **`Mech_Goncalves_NEJM_2018.md` 僅 993 bytes**，現階段不得對其內文作任何斷言。
