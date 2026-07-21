# 稽核報告：引用真實性查核（citation-verifier）

**稽核日期**：2026-07-21
**稽核範圍**：`/Users/ander/Documents/medical/diabetes/pi3k/章節/*.md`（B、C、D、E、F、G、H、I、K、M 共 10 章）
**稽核立場**：敵對稽核。預設每個 DOI／PMID／檔名皆為幻覺，直到經外部 API 或本地 `ls` 驗證為止。

---

## 0. 稽核方法（可重現）

| 步驟 | 方法 | 工具 |
|---|---|---|
| DOI 抽取 | 逐列解析 markdown table cell，`fullmatch(r'10\.\S+?(／\d{7,8})?')` | python3 |
| DOI 存活 | `curl -sIL -o /dev/null -w "%{http_code}" https://doi.org/{doi}` | curl |
| DOI 真實性 | `api.crossref.org/works/{doi}` 取回 title／first author／container-title／year | Crossref REST |
| PMID 比對 | NCBI `esummary.fcgi?db=pubmed`（批次 69 筆），比對 PubMed 回傳之 DOI／年份／期刊／第一作者 | E-utilities |
| 檔名存在性 | `ls 原始PDF/ 來源/` 一次列出，逐筆比對 `[檔名.md]` | shell |

> **關於 `curl -sIL` 之 HTTP code**：70 個 DOI 中 31 個回傳 **403**。經 Crossref API 逐一複驗，**全部 31 個皆為有效 DOI**，403 來自出版商（NEJM／JCO／Wiley／SAGE／AACR／ADA／MDPI／ACS）對 headless curl 的 bot 阻擋，**非死連結**。本報告以 Crossref／PubMed 之權威回應為判準，不以 403 判死。

---

## 1. 總覽統計

| 檢查項目 | 筆數 | 通過 | 失敗 |
|---|---|---|---|
| DOI（K 章表格） | **70** | **70（100%）** | 0 |
| PMID | **69**（另 1 列缺 PMID） | **69（100%）** | 0 |
| DOI ↔ PMID 一致性 | 69 | **69（100%）** | 0 |
| 期刊（container-title） | 69 | **69（100%）** | 0 |
| 第一作者 | 69 | **69（100%）** | 0 |
| 年份（表格「年份」欄 vs PubMed） | 69 | 64 | **5** |
| `[檔名.md]` 引用（76 個不同檔名，全章合計 1,900+ 次） | **76** | **76（100%）** | 0 |

**核心結論：本回顧無任何 fabricated citation、無任何 DOI mismatch。** 70 個 DOI 全數在 Crossref 解析成功且題名與內文描述相符；69 個 PMID 全數存在，且 PubMed 回傳之 DOI 與文中 DOI **逐字相符（大小寫差異除外）**。76 個 `[檔名.md]` 引用**全部落地存在**於 `原始PDF/`、`來源/` 或工作目錄根。

---

## 2. 逐筆檢查結果（僅列出有問題者；其餘 137 筆通過，明細見 §5）

| # | 引用 | 檢查結果 | 問題類型 | 建議動作 |
|---|---|---|---|---|
| 1 | `10.1056/nejmoa012512` ／ PMID 11832527（DPP, Knowler）[DPP_Knowler_2002.md] | DOI ✅ Crossref 有效；PMID ✅ 存在；DOI↔PMID ✅ 相符；**但 K-2 表「年份」欄填 2019，PubMed／Crossref 皆為 2002** | **journal/year shift** | **必修** —「年份」欄 2019 → **2002**。該列本文已自註「（2002 年發表）」、檔名亦為 `DPP_Knowler_2002.md`，欄位為單純填錯，但會誤導讀者以為是 DPPOS 近期報告 |
| 2 | `10.1200/JCO.24.00248`（ASCO Rapid Recommendation Update, Burstein）K 章第 128 列 | DOI ✅ Crossref 有效（*J Clin Oncol* 2024, Burstein HJ）；**「DOI／PMID」欄缺 PMID**；且此列未被計入 K-7 統計 | **incomplete citation** | **必修** — 補上 **PMID 38478799**（已用 `esearch` 由 DOI 反查確認），並修正 K-7 之納入篇數（見 #7） |
| 3 | `10.1158/1078-0432.ccr-20-3652` ／ PMID 33168657 [FDA_Alpelisib_Narayan_2021.md] | DOI ✅／PMID ✅／DOI↔PMID ✅；**「年份」欄 2020，PubMed 與 Crossref 皆為 2021**（*Clin Cancer Res* 2021;27(7)；online 2020-11） | year shift（epub vs print） | **待議** — 檔名已標 2021，建議欄位改 **2021**（或註記「online 2020-11」）以與檔名一致 |
| 4 | `10.1038/nature13948` ／ PMID 25409150 [Resist_Juric_PTEN_2015.md] | DOI ✅／PMID ✅／DOI↔PMID ✅；**「年份」欄 2014，PubMed／Crossref 為 2015**（*Nature* 2015;518；online 2014-11） | year shift（epub vs print） | **待議** — 檔名為 `_2015`，建議欄位改 **2015** |
| 5 | `10.1016/j.breast.2021.12.016` ／ PMID 35016012 [Multidisc_Rugo_2022.md] | DOI ✅／PMID ✅／DOI↔PMID ✅；**「年份」欄 2021，PubMed／Crossref 為 2022**（*The Breast* 2022;61） | year shift（epub vs print） | **待議** — 檔名為 `_2022`、`inventory.md` 亦誤記 2021，建議兩處同步改 **2022**（此檔全章被引用 **104 次**，為引用密度最高之單一來源，年份不一致影響可追溯性） |
| 6 | `10.1016/j.annonc.2020.10.596` ／ PMID 33186740 [SANDPIPER_Dent_2021.md] | DOI ✅／PMID ✅／DOI↔PMID ✅；**「年份」欄 2020，PubMed／Crossref 為 2021**（*Ann Oncol* 2021;32(2)） | year shift（epub vs print） | **待議** — 檔名為 `_2021`，建議欄位改 **2021** |
| 7 | K-7 §納入統計：「**共納入 69 篇獨立文獻**…**38 篇 📄**、**31 篇 📌**」 | 程式化清點 K-0～K-6 表格：**含 DOI 之列共 70 列**，標記 **📄 40／📌 30**。`inventory.md` 之 69／38／31 為 **`原始PDF/` 落地檔之統計**，未含僅存於 `來源/` 的 ASCO Burstein 2024 一筆，且 ADA SOC 2026 列在表中被標為「📄📌」混合 | **內部統計不一致** | **待議** — 明確區分兩套分母：「`原始PDF/` 落地文獻 69 篇（📄38／📌31）」與「K 章文獻表列入 70 筆（另含 1 筆僅存於 `來源/guideline_ada_comparators.md` 之 ASCO 指引）」 |
| 8 | K-7：「`原始PDF/` 內共 **70** 個 `.md` 檔」 | 稽核當下實測 **69** 個 `.md` 檔 | 計數不符 | **待議** — ⚠️ 稽核期間目錄仍在被其他流程寫入（`MSKCC_RealWorld_Shen_2023.md` 於 11:58 新增，與既有 `RealWorld_Shen_2023.md` 疑為同一 PMID 37743730 之第二份重複落地）。建議定稿前重新清點，並處理 Shen 2023 之重複檔（與 METALLICA 之重複情形相同） |
| 9 | ADA SOC 2026（`10.2337/dc26-s003` ／ PMID 41358891）K 章第 127 列 | DOI ✅／PMID ✅／DOI↔PMID ✅；**「標記」欄同時出現 📄 與 📌**，而 `inventory.md` 記為 **📌（僅 1,734 字元樣板 abstract）** | 標記混用 | **待議** — 該列內文已正確說明「`ADA_SOC2026_Ch3.md` 為 📌，Rec 3.7–3.10 逐字內容取自 `guideline_ada_comparators.md`」，論證本身合規；但**標記欄不應同時掛兩個符號**，建議拆為「📌（原文）＋📄（來源/擷取稿）」兩格或改為 📌 並於備註說明 |

---

## 3. 攔截三類幻覺 — 結果

| 幻覺類型 | 攔截數 | 說明 |
|---|---|---|
| **Fabricated citation**（捏造的 DOI／PMID／檔名） | **0** | 70/70 DOI 於 Crossref 存在；69/69 PMID 於 PubMed 存在；76/76 `[檔名.md]` 於磁碟存在 |
| **DOI mismatch**（DOI 與所述文獻不符） | **0** | 對 69 筆逐一比對 PubMed `articleids.doi` 與文中 DOI，**100% 相符**；另比對 Crossref 回傳題名與該列研究設計描述（如 SOLAR-1／INAVO120／METALLICA／CAPItello-291／SANDPIPER／BELLE-2），**全數對應正確** |
| **Journal/year shift** | **5**（1 必修 + 4 待議） | 期刊名 **0 筆錯誤**；年份 5 筆不符，其中 4 筆為 epub-ahead-of-print 與正式刊期之落差（可辯護但與自家檔名不一致），1 筆（DPP 2019 vs 2002）為明確填錯 |

---

## 4. 額外查核（超出指定範圍、但屬引用完整性）

- **`[檔名.md]` 全數可解析**：76 個不同檔名 → `原始PDF/` 69 個、`來源/` 6 個（`label_alpelisib.md`、`label_inavolisib.md`、`guideline_ada_comparators.md`、`trials_ongoing.md`、`inventory.md`、`citations_round1.md`）、工作目錄根 1 個（`MISSING_FULLTEXT.md`）。**無任何指向不存在檔案之引用。**
- **【L1】仿單來源確認落地**：`來源/label_alpelisib.md`（被引 **266** 次）與 `來源/label_inavolisib.md`（**240** 次）皆存在且可讀，前次稽核所謂「FDA/EMA 仿單未取得」之判斷確為誤判，本次不再重複該錯誤。
- **檔名年份 vs PubMed 年份**：對 `inventory.md` 全部 69 筆逐一比對，**0 筆不符**（年份錯誤僅出現在 K 章表格之「年份」欄，非檔名）。
- **檔名第一作者 vs PubMed 第一作者**：69 筆比對，3 筆字串不匹配經人工複核**皆為誤報**（`METALLICA_LlombartCussac` = Llombart-Cussac A；`ADA_SOC2026_Ch3` = 團體作者；`BYLieve_EoC_2024` = The Editors of The Lancet Oncology）→ **實質 69/69 相符**。
- **重複落地檔**：`METALLICA_Llombart_2024.md` 與 `METALLICA_LlombartCussac_2024.md` 同為 PMID 38638399（K 章已自行揭露）；新增之 `MSKCC_RealWorld_Shen_2023.md` 與 `RealWorld_Shen_2023.md` 疑為 PMID 37743730 之第二組重複，**K 章尚未揭露**（見 #8）。
- **未被引用之落地檔**：`ADA_SOC2026_Ch3.md`（於第 127 列以純文字提及，未使用 `[...]` 標註格式）、`MSKCC_RealWorld_Shen_2023.md`（稽核期間新增）。建議統一為 `[檔名.md]` 格式以利後續 grep 稽核。
- **B／C／D／E／F／G／H／I／M 九章**：**不含任何 DOI 或 PMID**，全部論斷僅以 `[檔名.md]` 標註 —— 符合「每個數字都必須 grep 得到」之硬規則設計，本稽核對這九章無引用格式異議。

---

## 5. 通過清單（摘要）

以下 **70 筆 DOI／PMID 引用**除 §2 所列年份問題外，**DOI 有效性、DOI↔PMID 對應、期刊、第一作者四項全部通過**：

nejmoa1813904/31091374、annonc.2020.11.011/33246021、annonc.2020.05.001/32416251、jco.20.01139/33780274、s1470-2045(21)00034-6/33794206、s1470-2045(24)00673-9/39637900、s1470-2045(23)00673-3/38142701、jco.2017.72.7107/29401002、jamaoncol.2018.4475/30543347、nejmoa2404625/39476340、nejmoa2501796/40454641、esmoop.2026.107735/42202490、jco.24.00110/39236276、esmoop.2025.105303/40513140、jco-25-00663/40845250、ccr-20-3652/33168657、eclinm.2024.102520/38638399、s10549-024-07405-8/39177931、oyaf023/40152314、s13058-024-01773-1/38439079、s10549-022-06798-8/36409396、clbc.2024.09.017/39462728、nejmoa012512/11832527、15347354211073163/35075945、jco.2011.39.7356/22778315、s41586-018-0343-4/30051890、noad117/37399061、cell.2017.07.029/28802037、ijbs.27173/30263000、ccr-08-1253/19118049、s10549-020-05618-1/32274666、nejmra1704560/30462943、mct-13-0865/24608574、jmedchem.2c01422/36455032、cd-21-0072/34544753、nature13948/25409150、cam4.4579/35212193、cncr.34928/37743730、10781552261451729/42159385、s41388-022-02585-3/36611120、s10549-021-06476-1/35000092、jgo.2021.03.007/33752998、clbc.2024.01.004/38245400、annonc.2019.11.006/32067679、fendo.2026.1747317/42181200、ott.s370244/36330532、aace.2024.10.002/39896940、aace.2020.11.028/34095470、accr-2020-0452/33244501、ando.2022.02.004/35750516、fendo.2022.802612/35178031、15347354211032283/34259084、2324709617725351/28856166、dc18-2316/30728224、s41523-024-00613-x/38297009、cancers14071598/35406370、breast.2021.12.016/35016012、esmoop.2025.105936/41604817、s41523-025-00864-2/41345397、mdz440/31626273、dc26-s003/41358891、JCO.24.00248（PMID 待補）、nejmoa2214131/37256976、esmoop.2024.103697/39241495、jco.24.00427/39159418、annonc.2020.10.596/33186740、s1470-2045(17)30376-5/28576675、fonc.2025.1556978/40535135、oncotarget.27770/33144920、ctrv.2017.09.009/29108713

（原始查核輸出保留於稽核暫存：`crossref.tsv`、`esum.json`、`doicheck.tsv`、`pairs.tsv`）

---

## 6. 統計結論

> ### **必修 2 筆／待議 7 筆／通過 137 筆**
>
> （分母 146 筆＝ K 章 70 筆文獻引用 ＋ 全章 76 個不同 `[檔名.md]` 引用）

**最嚴重之 3 個問題**

1. **DPP（Knowler）之發表年被填成 2019，實為 NEJM 2002**（PMID 11832527）—— 同一列本文與檔名皆寫 2002，屬表格欄位自我矛盾，且會讓讀者誤以為是近期糖尿病預防數據。
2. **ASCO Rapid Recommendation Update（`10.1200/JCO.24.00248`）缺 PMID**，是全表唯一無 PMID 之引用，亦未列入 K-7 之納入統計，造成「69 篇」與表列 70 列不符。
3. **`Multidisc_Rugo_2022.md` 之年份在 K 章表格與 `inventory.md` 皆記為 2021，PubMed／Crossref 為 2022** —— 該檔為全回顧引用次數最高的單一文獻（104 次），年份不一致將直接影響下游稽核員的可追溯性。

**未發現任何捏造引用、任何 DOI 與文獻不符之情形。** 本回顧之引用基礎經外部 API 驗證後判定為可信。
