# C. Alpelisib versus Inavolisib 比較

> **稽核聲明**：本節所有數字皆取自 `來源/label_alpelisib.md`、`來源/label_inavolisib.md`（FDA/EMA/TFDA 仿單逐字擷取，📄）與 `原始PDF/` 內之全文檔案（📄）。
>
> **本版更新**：以下三篇原本僅有 abstract（📌）的關鍵論文，現已於本地落地為**可 grep 之全文（📄）**，本節已據其正文與表格重寫相關數字：
> - `原始PDF/SOLAR1_AE_Rugo_2020.md`📄（Ann Oncol 2020，PMID 32416251；SOLAR-1 AE 時序與處置專文，81 KB）——擷取稿見 `來源/fulltext_facts_SOLAR1.md`📄
> - `原始PDF/INAVO120_Turner_2024.md`📄（N Engl J Med 2024;391:1584-96，PMID 39476340，NCT04191499，78 KB）——擷取稿見 `來源/fulltext_facts_INAVO120.md`📄
> - `原始PDF/MSKCC_RealWorld_Shen_2023.md`📄（Cancer 2023;129:3854-3861，PMID 37743730，n = 247，50 KB）——擷取稿見 `來源/fulltext_facts_MSKCC.md`📄
>
> 仍為 abstract-only（📌）者：SOLAR-1 主論文（`SOLAR1_Andre_2019.md`）、INAVO120 OS 論文（`INAVO120_OS_Jhaveri_2025.md`）、三篇 BYLieve 檔案 → **不對其內文細節作具體斷言**。
>
> ⚠️ **分母紀律**：SOLAR-1 的高血糖數字有 **preferred term**（分母 284）與 **AESI grouped term**（分母 284，但納入的 preferred terms 更廣）兩套；INAVO120 有 **safety population**（162/162）與 **full analysis population**（161/164）兩套。本節每個百分比後皆附分母，不同套之間**不可互相取代或相加**。

---

## C-1. 主比較表

| 項目 | **Alpelisib（PIQRAY®）** | **Inavolisib（ITOVEBI®）** |
|---|---|---|
| **靶點特性** | PI3Kα (p110α) 選擇性抑制劑。前臨床顯示 BYL719（alpelisib）**不**造成 p110α 蛋白降解（單次 40 mg/kg 口服未見 p110α 耗竭）【L5】[Preclin_Song_Inavolisib_2022.md] | 高效價、α-選擇性 PI3K 抑制劑，**且促進突變型 p110α 降解**（ubiquitin–proteasome 途徑）；GDC-0077 單次 50 mg/kg 口服可耗竭 p110α 達 8 小時【L5】[Preclin_Song_Inavolisib_2022.md]。「對 taselisib 與 BYL719 兩者皆有顯著的 PI3Kα isoform selectivity 改善」【L5】[Preclin_Song_Inavolisib_2022.md]；此特性被歸因為較寬的 therapeutic window【L3】[ToxMgmt_Jhaveri_2026.md] |
| **FDA 適應症** | 與 fulvestrant 併用；HR+/HER2−、PIK3CA-mutated 晚期或轉移性乳癌，內分泌治療後進展【L1】[label_alpelisib.md]。SOLAR-1 收的是「progressed or recurred on or after an aromatase inhibitor, with or without a CDK 4/6 inhibitor」【L1-adjacent】[FDA_Alpelisib_Narayan_2021.md] | 與 **palbociclib + fulvestrant** 三合一；**endocrine-resistant**、PIK3CA-mutated、HR+/HER2− 局部晚期或轉移性乳癌，**於完成 adjuvant endocrine therapy 之時或之後復發**【L1】[label_inavolisib.md]（EMA 措辭更嚴：「on or within 12 months of completing adjuvant endocrine treatment」）【L1】[label_inavolisib.md] |
| **併用藥** | fulvestrant 500 mg IM，D1、D15、D29，其後每月【L1】[label_alpelisib.md] | palbociclib 125 mg PO QD（21 天服藥／7 天停藥，28 天為一週期）+ fulvestrant 500 mg IM（C1D1、C1D15，其後每 28 天）【L1】[label_inavolisib.md] |
| **起始劑量／劑型** | **300 mg PO QD 隨餐**（2×150 mg）；錠劑 50／150／200 mg【L1】[label_alpelisib.md] | **9 mg PO QD，可空腹或隨餐**；錠劑 3 mg 與 9 mg【L1】[label_inavolisib.md] |
| **減量階梯** | 300 → 250 → 200 mg QD；**低於 200 mg 即停藥**（pancreatitis 只允許減量一次）【L1】[label_alpelisib.md] | 9 → 6 → 3 mg QD；**無法耐受第二次減量即永久停藥**【L1】[label_inavolisib.md]。⚠️ **EMA 額外允許**依臨床評估「re-escalate to a maximum daily dose of 9 mg」，FDA 仿單無此條文【L1】[label_inavolisib.md] |
| **關鍵試驗** | SOLAR-1（randomized, double-blind, placebo-controlled phase 3）【L1】[label_alpelisib.md]；補充：METALLICA（single-arm phase 2）【L2】[METALLICA_LlombartCussac_2024.md] | INAVO120（NCT04191499；randomized 1:1, double-blind, placebo-controlled phase 3）【L1】[label_inavolisib.md]【L2】[INAVO120_Safety_Im_2026.md] |
| **n（安全性族群）** | PIQRAY + fulvestrant **n = 284** vs placebo + fulvestrant n = 287（**總 571**；隨機分派為 284 / 288，placebo 組 1 人收案未給藥）【L1】[label_alpelisib.md]【L2】[SOLAR1_AE_Rugo_2020.md]。安全性分析將 PIK3CA-mutant（341）與 non-mutant（231）兩個 cohort **合併**【L2】[SOLAR1_AE_Rugo_2020.md] | ITOVEBI arm **n = 162** vs placebo arm n = 162（總 324）；**efficacy 的 full analysis population 為 161 vs 164**，兩套分母不同；2020-01-29 至 2023-09-14 共收 **325 人於 28 國**【L1】[label_inavolisib.md]【L2】[INAVO120_Turner_2024.md] |
| **中位治療暴露** | **alpelisib 中位 5.5 個月**（range 0–30.8）；同組 fulvestrant 8.2 個月（0.4–30.8），placebo 組 fulvestrant 5.6 個月（0.5–30.1）【L2】[SOLAR1_AE_Rugo_2020.md]。**Alpelisib dose reduction 59.2%、dose interruption 72.2%**（其中因 AE 者 57.7% / 66.5%）【L2】[SOLAR1_AE_Rugo_2020.md] | ITOVEBI **中位 9 個月**（range 0–39）【L1】[label_inavolisib.md]；INAVO120 全文：inavolisib **中位 9.2 個月**、palbociclib 9.1、fulvestrant 8.6；**中位相對劑量強度 95.8% / 87.3% / 100.0%**（placebo 組服藥中位 5.6 個月）；中位追蹤 21.3 vs 21.5 個月【L2】[INAVO120_Turner_2024.md] |
| **Any-grade 高血糖（臨床 AE term）** | FDA 5.3：**hyperglycemia 65%**【L1】[label_alpelisib.md]；EMA 4.8：**191 (67.3%)**【L1】[label_alpelisib.md]。SOLAR-1 原文（Table 2, CTCAE v4.03）：**preferred term 181/284 = 63.7%**（placebo 28/287 = 9.8%）【L2】[SOLAR1_AE_Rugo_2020.md]；**AESI grouped term 187/284 = 65.8%**（placebo 30/287 = 10.5%）【L2】[SOLAR1_AE_Rugo_2020.md] | FDA 5.1 用的是實驗室值（見下）；EMA 4.8：**hyperglycaemia any grade 59.9%**（CTCAE v5.0）【L1】[label_inavolisib.md]。INAVO120 原文（Table 2，**grouped term**，safety population）：**95/162 = 58.6%**（placebo **14/162 = 8.6%**）【L2】[INAVO120_Turner_2024.md]；單一 preferred term「hyperglycaemia」53.7%（87/162）【L2】[INAVO120_Safety_Im_2026.md] |
| **Any-grade 高血糖（實驗室 fasting glucose increased）** | **79%**（vs placebo 34%）【L1】[label_alpelisib.md]；EMA ADR 表 glucose plasma increased 225 (79.2%)【L1】[label_alpelisib.md] | **85%**（vs placebo 43%）【L1】[label_inavolisib.md] |
| **Grade 3–4 率** | FDA 5.3：**Grade 3 33%、Grade 4 3.9%**【L1】[label_alpelisib.md]；實驗室 glucose increased Grade 3–4 **39%**（EMA 112 (39.4%)）【L1】[label_alpelisib.md]。SOLAR-1 原文逐字（preferred term，分母 284）：**Grade 3 93 人 = 32.7%、Grade 4 11 人 = 3.9%**（合計 36.6%；placebo 各 1 人 = 0.3%）【L2】[SOLAR1_AE_Rugo_2020.md]；**AESI grouped term 之 grade ≥3 為 108/284 = 38.0%**（placebo 2/287 = 0.7%）【L2】[SOLAR1_AE_Rugo_2020.md]。另 Grade 1 32 (11.3%)、Grade 2 45 (15.8%)【L2】[SOLAR1_AE_Rugo_2020.md] | FDA 5.1：**Grade 3 12%、Grade 4 0.6%**；FDA Table 4 實驗室 Grade 3–4 **12%**（placebo 0%）【L1】[label_inavolisib.md]；EMA 4.8：Grade 2 38.3%、**Grade 3 5.6%**（CTCAE v5.0）【L1】[label_inavolisib.md]。INAVO120 原文只報**合併值**：**Grade 3 or 4 = 9/162 = 5.6%**（placebo 0/162 = 0%）；⚠️ **NEJM 原文未拆分 grade 3 與 grade 4**，任何「grade 4 = X%」之陳述在該全文中無可驗證來源【L2】[INAVO120_Turner_2024.md]（EMA 之「Grade 3 5.6%、無 Grade 4」屬仿單層級【L1】[label_inavolisib.md]） |
| **依 BMI 分層之 any-grade 高血糖** | Normal BMI **63/110 = 57.3%**（G3 24.5%、G4 2.7%）；Overweight **62/84 = 73.8%**（G3 35.7%、G4 3.6%）；Obese **50/74 = 67.6%**（G3 39.2%、**G4 9.5%**）；⚠️ 原文未給 BMI 分組之 kg/m² cut-off【L2】[SOLAR1_AE_Rugo_2020.md] | BMI ≥30.0 者 **65.5%** vs BMI <30.0 者 **56.8%**（僅 any-grade；⚠️ 原文**未報** BMI 分層下的 grade 3/4 率）【L2】[INAVO120_Turner_2024.md] |
| **依年齡分層之 grade 3/4 高血糖** | ≥75 歲 **19/34 = 55.9%** vs <75 歲 **89/250 = 35.6%**；同族群 all-grade GI toxicity 29/34 (85.3%) vs 185/250 (74.0%)【L2】[SOLAR1_AE_Rugo_2020.md] | 原文未報告年齡分層之高血糖率 → **本回顧未取得可驗證來源**【L2】[INAVO120_Turner_2024.md] |
| **Ketoacidosis** | FDA 5.3：**0.7%（n = 2）**；上市後有 **fatal ketoacidosis**；6.2 列 HHNKS【L1】[label_alpelisib.md]。EMA ADR 表 Ketoacidosis 3 (1.1%)，全為 Grade 3–4【L1】[label_alpelisib.md]。⚠️ **SOLAR-1 AE 專文全文 grep `ketoacid`／`DKA`／`HHNK`／`hyperosmolar` 皆 0 命中**，該文既未報告個案、亦未聲明「無此類事件」→ 應表述為「**該文未報告** DKA/HHS」，**不可**表述為「SOLAR-1 未發生 DKA」【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界確有 DKA：MSKCC 世代之敏感度分析明文「excluding standard care patients who developed **diabetic ketoacidosis**」，惟**未給出人數或比率**【L4】[MSKCC_RealWorld_Shen_2023.md] | INAVO120 中**無病人發生 DKA**【L2】[INAVO120_Safety_Im_2026.md]；NEJM 主論文全文**未出現 DKA／ketoacidosis／hyperosmolar 等詞彙**，且 grade 5（致死）AE 清單中不含 hyperglycemia【L2】[INAVO120_Turner_2024.md]。但 **04/2026 FDA label 已載明「Severe or fatal hyperglycemia, including ketoacidosis」，且 6.2 Postmarketing Experience 新增 Ketoacidosis**（5.1 節於 09/2025 列為 RECENT MAJOR CHANGE）【L1】[label_inavolisib.md] |
| **中位發生時間** | **Grade ≥2（FPG 160–250 mg/dL）中位 15 天**（range 5–517 天，FDA）【L1】[label_alpelisib.md]；EMA 同為 15 天（range 5–1,458 天）【L1】[label_alpelisib.md]。SOLAR-1 原文：**grade ≥3 事件中位 15 天（range 5–395 天），依 FPG 判定**；對照 rash 13 天（7–571）、diarrhea 139 天（10–470）【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界（MSKCC, n = 247，定義為起始日至首次 glucose ≥140 mg/dL）：**中位 16 天**【L4】[MSKCC_RealWorld_Shen_2023.md] | **中位 7 天**（range 2–955 天）【L1】[label_inavolisib.md]【L2】[INAVO120_Safety_Im_2026.md]；EMA：新發事件率在**前兩個月最高**【L1】[label_inavolisib.md]。⚠️ **INAVO120 主論文（NEJM）全文未報告 hyperglycemia 之 median time to onset／resolution**（已 grep 確認無 "time to onset" 敘述）；上述 7 天為仿單與安全性專文層級之數據，**不得回貼為 NEJM 原文數字**【L2】[INAVO120_Turner_2024.md] |
| **中位改善時間（≥1 grade）** | 8 天（range 2–65 天；n = 153）【L1】[label_alpelisib.md]；EMA 8 天（95% CI 8–10）【L1】[label_alpelisib.md]。SOLAR-1 原文另報 **grade ≥3 事件改善 ≥1 grade 之中位為 6 天（range 4–7 天）**（rash 11 天、diarrhea 18 天）——與仿單的 8 天分母／端點定義不同，**不可互換**【L2】[SOLAR1_AE_Rugo_2020.md] | 8 天（range 2–43 天；FPG > 160 mg/dL 者 52/54 = 96% 改善 ≥1 grade）【L1】[label_inavolisib.md]。中位 **resolution** 時間 16 天（IQR 5–50）【L2】[INAVO120_Safety_Im_2026.md] |
| **可逆性** | **所有發生高血糖者，停用 alpelisib 後高血糖均回到 grade 0 或 1**【L2】[SOLAR1_AE_Rugo_2020.md]。⚠️ 原文**未報告**停藥後回復至 grade 0/1 所需之中位天數 → **本回顧未取得可驗證來源**。平均 FPG **於治療前 2 週達峰**，其後在降糖藥支持下回落趨近基線；HbA1c 則緩升並維持輕度上升【L2】[SOLAR1_AE_Rugo_2020.md] | FPG > 160 mg/dL 者 96%（52/54）改善 ≥1 grade【L1】[label_inavolisib.md]；NEJM 全文未報告可逆性之量化數據 → **本回顧未取得可驗證來源**【L2】[INAVO120_Turner_2024.md] |
| **因高血糖：暫停用藥** | 仿單與 SOLAR-1 AE 專文**皆未拆分「因高血糖」之單獨 interruption 率**；SOLAR-1 只給整體 alpelisib dose interruption **72.2%**（因 AE 者 66.5%）【L2】[SOLAR1_AE_Rugo_2020.md] → 藥物層級**本回顧未取得可驗證來源**。真實世界可參考值：MSKCC 世代 **66/247 = 26.7%** 因高血糖暫停 alpelisib【L4】[MSKCC_RealWorld_Shen_2023.md] | **28%**（FDA 5.1／6.1）【L1】[label_inavolisib.md]；INAVO120 **27.2%（44/162）**【L2】[INAVO120_Safety_Im_2026.md] |
| **因高血糖：減量** | **29%**（為最常見之減量原因）【L1】[label_alpelisib.md]；SOLAR-1 整體 alpelisib dose reduction 59.2%（因 AE 者 57.7%），未拆分高血糖【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界：MSKCC **42/247 = 17%**【L4】[MSKCC_RealWorld_Shen_2023.md] | **2.5%（4/162）**【L1】[label_inavolisib.md]。INAVO120 原文逐字：「hyperglycemia led to a reduction in the inavolisib dose in **2.5%** of the patients; this was the **only** adverse event that led to a reduction in the inavolisib dose in at least 2% of the patients」；整體任何 AE 導致減量 inavolisib **14.2%** vs placebo **3.1%**【L2】[INAVO120_Turner_2024.md] |
| **因高血糖：永久停藥** | **6%**（為最常見之停藥原因；整體 21% 單獨停 PIQRAY）【L1】[label_alpelisib.md]。SOLAR-1 全試驗因 AE 停藥率 **alpelisib 25.0% vs placebo 4.2%**【L2】[SOLAR1_AE_Rugo_2020.md]；protocol 修訂後段（後 50% 隨機者）因高血糖停藥率由 **9.0% 降至 3.6%**【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界：MSKCC **11/247 = 4.5%**【L4】[MSKCC_RealWorld_Shen_2023.md] | **1.2%**（FDA 6.1）【L1】[label_inavolisib.md]；INAVO120 安全性分析：停 inavolisib 者 **0.6%（1/162）**，導致任一試驗藥退出者 1.2%（2/162）【L2】[INAVO120_Safety_Im_2026.md]。NEJM 原文層級可 grep 者為**整體**因 AE 停藥：任一試驗藥 **6.8%** vs placebo **0.6%**（inavolisib 6.2%、palbociclib 4.9%、fulvestrant 3.1%）；⚠️ **NEJM 未單獨列出「因 hyperglycemia 停藥」之比率**（細節在本地不含之 Table S3）【L2】[INAVO120_Turner_2024.md] |
| **需降血糖藥物** | 187 名高血糖病人中 **87%（163/187）** 用藥；**76%（142/187）** 用 metformin（單方或併用）【L1】[label_alpelisib.md]。SOLAR-1 原文以 **163 名用藥者為分母**：metformin **87.1%**（單用或併用）；**67 人（41.1%）僅需 1 種**降糖藥，**47 人（28.8%）需 ≥3 種**【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界（MSKCC，分母 = 152 名高血糖者）：**101 人（66.4%）**接受降糖治療，其中 metformin 90 人（89.1%）、SGLT2i 20 人（19.8%）、insulin 16 人（15.8%）、DPP4i 12 人（11.9%）、TZD 8 人（7.9%）、SU 6 人（5.9%）【L4】[MSKCC_RealWorld_Shen_2023.md] | **46%（74/162）** 用口服降血糖藥【L1】[label_inavolisib.md]；接受降血糖藥的 66 人中 **93.9%（62/66）用 metformin**【L2】[INAVO120_Safety_Im_2026.md]。⚠️ **NEJM 原文完全未報告任何降糖藥使用率**（含 metformin），僅寫 protocol「allowed prophylactic use of metformin in patients with a high risk of hyperglycemia」，且**未定義「高風險」**【L2】[INAVO120_Turner_2024.md] |
| **需 insulin** | EMA：56 人曾併用 insulin，其中 **13 人（23.2%）因高血糖停藥**（相對地，用口服藥的 154 人中僅 17 人 (11.0%) 停藥）【L1】[label_alpelisib.md]。SOLAR-1 原文依基線血糖狀態拆分：diabetic **5/12**、prediabetic **34/159**、normal **13/113**；合計 **52 人**用過 insulin，其中 **33 人為長期使用（>2 天）、19 人為 rescue 用藥**【L2】[SOLAR1_AE_Rugo_2020.md] | **7%（11/162）**【L1】[label_inavolisib.md]；INAVO120 中位使用期 **5 天**（range 1–539，上限來自 2 名長期 insulin 使用者）【L2】[INAVO120_Safety_Im_2026.md]；NEJM 原文未報告 insulin 使用【L2】[INAVO120_Turner_2024.md] |
| **預防性 metformin** | FDA 01/2024 起：「**Consider** premedication with metformin … based on patient risk factors for hyperglycemia, gastrointestinal tolerability, and clinical situation」；同段明載會**增加噁心／嘔吐／腹瀉的發生率與嚴重度**【L1】[label_alpelisib.md]。依據為 METALLICA（**single-arm, two-cohort, n = 68**）【L1】[label_alpelisib.md]【L2】[METALLICA_LlombartCussac_2024.md] | FDA PI 全文**未出現 "metformin" 字樣**（已 grep 確認）【L1】[label_inavolisib.md]。EMA 4.4：「Metformin premedication **can be considered** in patients with risk factors for hyperglycaemia」【L1】[label_inavolisib.md]。INAVO120 中預防性 metformin「allowed」、由 investigator 裁量，實際僅 **7.4%（12/162）** 接受【L2】[INAVO120_Safety_Im_2026.md]。⚠️ NEJM 主論文僅寫 protocol *allowed*，**未報告使用率、未隨機化、未報告其對高血糖發生率之影響**——「預防性 metformin 已被證明有效」在 INAVO120 全文中**無可驗證來源**【L2】[INAVO120_Turner_2024.md] |
| **基線納入條件（血糖）** | 見 C-3 之詳述。SOLAR-1 原文逐字：「Patients with a history of **well-controlled type 2 diabetes were eligible** to enroll; however, patients with **type 1 and uncontrolled type 2 diabetes were excluded**」【L2】[SOLAR1_AE_Rugo_2020.md]【L1】[label_alpelisib.md]。**HbA1c 收案門檻起初為 < 8%，於 317/約 560 人（56.6%）隨機後之 protocol 修訂改為 < 6.5%**【L2】[SOLAR1_AE_Rugo_2020.md] | **HbA1C < 6% 且 fasting blood glucose < 126 mg/dL**【L1】[label_inavolisib.md]。NEJM 原文逐字：「a **fasting glucose level of less than 126 mg per deciliter**, a **glycated hemoglobin level of less than 6.0%**」【L2】[INAVO120_Turner_2024.md]；排除條件逐字：「patients with **type 1 or type 2 diabetes that required ongoing treatment were excluded**」（作者自列為試驗限制）【L2】[INAVO120_Turner_2024.md]。原始 protocol 為 HbA1c < 5.7%，後修訂為 < 6.0%【L2】[INAVO120_Safety_Im_2026.md] |
| **基線族群實際血糖分布** | 56% 為 pre-diabetic、**4.2% 為 diabetic**（FPG ≥126 和／或 HbA1c ≥6.5%）【L1】[label_alpelisib.md]；EMA 4.4 列出 12 名 diabetic 病人中 **10 人（83.3%）發生 Grade 3–4 高血糖**【L1】[label_alpelisib.md]。SOLAR-1 原文（依 ADA 定義、以隨機化前數值判定，不論病史）：**normal 113 人（40%）、prediabetic 159 人（56%）、diabetic 12 人（4%）**；發生率 **prediabetic 74%（G3 43.4%、G4 5.0%）vs normal 52%（G3 16.8%、G4 1.8%）**；⚠️ diabetic（n=12）之分級發生率原文**未分項報告**【L2】[SOLAR1_AE_Rugo_2020.md] | ITOVEBI arm **僅 1 名 T2DM 病人**【L1】[label_inavolisib.md]；HbA1c ≥5.7% 僅 9.9%（16/162）、FPG ≥100 mg/dL 28.4%（46/162）、BMI ≥30 17.9%（29/162）【L2】[INAVO120_Safety_Im_2026.md]。⚠️ **NEJM Table 1 完全未列基線糖尿病／prediabetes 比例，亦未報告基線 HbA1c 或 FPG 之實際分佈值**（僅有納入門檻）【L2】[INAVO120_Turner_2024.md] |
| **基線體位與人口學** | 中位年齡 alpelisib 組 **62 歲**、placebo 組 **64 歲**；約 **86%** 有 endocrine resistance；**49%** 有肺／肝轉移；約 **6%** 曾用 CDK4/6 inhibitor【L2】[SOLAR1_AE_Rugo_2020.md]。BMI 分組人數（alpelisib 組）：normal 110、overweight 84、obese 74【L2】[SOLAR1_AE_Rugo_2020.md] | 中位年齡 **54.0 歲**（range 27–79）、**女性 98.2%**、**中位體重 63.0 kg**（38–124）；BMI <18.5 **5.5%**、18.5–<25.0 **47.1%**、25.0–<30.0 **28.9%**、≥30.0 **17.5%**；postmenopausal 60.0%、亞洲人 38.2%；ECOG 0 為 63.4%（分母 = FAS 325）【L2】[INAVO120_Turner_2024.md] |
| **腫瘤負荷** | 49% 有肺或肝轉移【L2】[SOLAR1_AE_Rugo_2020.md] | 高負荷 enrichment：**≥3 個器官轉移 51.4%、內臟轉移 80.0%、肝轉移 51.7%**；primary endocrine resistance 34.2%、secondary 65.5%【L2】[INAVO120_Turner_2024.md] |
| **治療前必檢** | FPG、HbA1c，並先 optimize blood glucose【L1】[label_alpelisib.md] | FPG／FBG、HbA1C，並先 optimize【L1】[label_inavolisib.md]。⚠️ EMA 更強：「**Treatment with Itovebi should not be initiated until fasting glucose levels are optimised**」【L1】[label_inavolisib.md] |
| **治療中監測（FDA）** | 前 2 週**每週至少 1 次**，其後**每 4 週至少 1 次**；HbA1c 每 3 個月【L1】[label_alpelisib.md] | **D1–7 每 3 天 1 次 → D8–28 每週 1 次 → 接下來 8 週每 2 週 1 次 → 其後每 4 週 1 次**；HbA1C 每 3 個月【L1】[label_inavolisib.md] |
| **治療中監測（EMA）** | 第 1、2、4、6、8 週後每月；**高風險族群（diabetes／pre-diabetes／BMI ≥30／≥75 歲）前 2 週每日自我監測**；HbA1c 於 4 週後、其後每 3 個月【L1】[label_alpelisib.md] | 同 FDA 頻率；高風險因子明列為 **(pre)diabetes、HbA1C ≥5.7%、BMI ≥30、≥45 歲、gestational diabetes 病史、糖尿病家族史**【L1】[label_inavolisib.md] |
| **發生高血糖後之監測** | 至少**每週 2 次**直到回復正常；用藥期間至少**每週 1 次共 8 週**，其後每 2 週【L1】[label_alpelisib.md] | 沿用上述遞減式排程（原文明載同樣適用於治療中才出現高血糖者）【L1】[label_inavolisib.md] |
| **專科照會門檻（明文條款）** | **EMA 有明文**：pre-diabetic、FG > 250 mg/dL、BMI ≥30 或 ≥75 歲 → recommended；**已知糖尿病 → should always take place**【L1】[label_alpelisib.md] | FPG 持續 > 200–250 mg/dL 達 7 天者「consider consultation」；EMA 另建議**起始治療前**即考慮照會【L1】[label_inavolisib.md] |
| **腎功能劑量調整** | mild–moderate（CLcr 30–<90）**不需調整**；severe（CLcr <30）影響**未知**【L1】[label_alpelisib.md] | moderate（eGFR 30–<60）→ **6 mg QD**；severe（eGFR <30）→ **3 mg QD**【L1】[label_inavolisib.md]。藥動學依據：moderate 時 AUC ↑73%、severe 時 ↑123%【L1】[label_inavolisib.md] |
| **腹瀉／營養相關（同期 AE）** | Diarrhea 58%（G3–4 7%）、Nausea 45%、Vomiting 27%、Decreased appetite 36%、Weight decreased 27%（G3–4 3.9%）、acute kidney injury 為 serious AE 2.5%【L1】[label_alpelisib.md]。SOLAR-1 原文 Table 2（分母 284）：**Diarrhea 164 (57.7%)／G3 19 (6.7%)、Nausea 127 (44.7%)、Decreased appetite 101 (35.6%)、Vomiting 77 (27.1%)、Decreased weight 76 (26.8%)／G3 11 (3.9%)、Stomatitis 70 (24.6%)**【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界佐證體重下降：MSKCC 世代治療中 BMI 中位變化 **−1.30 kg/m²（−5.5% of initial BMI，IQR −0.33 至 −3.0）**【L4】[MSKCC_RealWorld_Shen_2023.md] | Diarrhea 48%（G3–4 3.7%）、Stomatitis 51%（G3–4 6%）、Nausea 28%、Decreased appetite 24%、Weight decreased 17%（G3–4 3.7%）【L1】[label_inavolisib.md]。INAVO120 Table 2（分母 162）：**Diarrhea 78 (48.1%)／G3–4 6 (3.7%)、Stomatitis 83 (51.2%)／G3–4 9 (5.6%)、Nausea 45 (27.8%)、Decreased appetite 38 (23.5%)**（placebo 依序 16.0%／26.5%／16.7%／8.6%）；Serious AE 24.1% vs 10.5%、grade 5 AE 3.7% vs 1.2%（**無一例經研究者判定與試驗藥相關**）【L2】[INAVO120_Turner_2024.md] |

---

## C-2. ★ 劑量調整對照表（依 FPG 分層，逐列比對兩份仿單原文）★

> **共通前提**：兩份仿單皆明文規定**只能依空腹血糖（FPG 或 fasting blood glucose）**做劑量決策，不可用隨機血糖【L1】[label_alpelisib.md][label_inavolisib.md]。
> ⚠️ = 兩藥處置有**實質差異**，臨床上最易搞混之處。
> 📄 **本版補充**：SOLAR-1 之 **protocol 高血糖處置表（Table 1，CTCAE v4.03）已可逐字 grep**【L2】[SOLAR1_AE_Rugo_2020.md]，其分層與 FDA 仿單 Table 3 一致：Grade 1（FPG > ULN–160 mg/dL）不調整 alpelisib、FPG < 140 考慮 metformin／140–160 起始或加強 metformin；Grade 2（> 160–250）不調整，若給降糖藥後 **21 天內**未降至 grade ≤1 則減 1 個 dose level，並在超過 metformin MTD 時加 insulin sensitizer（如 pioglitazone）；Grade 3（> 250–500）停 alpelisib、照會內分泌科、metformin + pioglitazone，**「insulin may be used as rescue medication for 1 to 2 days」**；Grade 4（> 500）停藥 24 小時、照會內分泌科、24 小時後複驗。**alpelisib 減量階梯逐字為 300 → 250 → 200 mg/day**【L2】[SOLAR1_AE_Rugo_2020.md]。

| FPG 分層 | **Alpelisib（PIQRAY, FDA Table 3）**【L1】[label_alpelisib.md] | **Inavolisib（ITOVEBI, FDA Table 2）**【L1】[label_inavolisib.md] | 差異 |
|---|---|---|---|
| **> ULN – 160 mg/dL**<br>(> ULN – 8.9 mmol/L) | • **不需調整劑量**<br>• Initiate or intensify anti-hyperglycemic treatment | • **不需調整劑量**<br>• Consider dietary modifications and **ensure adequate hydration**<br>• 僅**對有高血糖風險因子者**起始／加強口服降血糖藥 | ⚠️ alpelisib 在此層即**無條件**要求起始／加強降糖藥；inavolisib 限於**有風險因子者**，並額外強調飲食與補水 |
| **> 160 – 250 mg/dL**<br>(> 8.9 – 13.9 mmol/L) | • **不需調整劑量（繼續服藥）**<br>• Initiate or intensify anti-hyperglycemic treatment<br>• 若在適當降糖治療下 **21 天內** FPG 未降至 ≤160 mg/dL → **減 1 個劑量階（300→250→200）**，並依 FPG 值再走對應建議 | • **Withhold ITOVEBI 直到 FPG ≤ 160 mg/dL**<br>• Initiate or intensify anti-hyperglycemic medications<br>• **以原劑量 resume**（same dose level）<br>• 若在適當治療下 FPG 持續 > 200–250 mg/dL 達 **7 天** → 考慮照會高血糖專科 | ⚠️⚠️ **最大差異**。同一個 FPG 180 mg/dL 的病人：**alpelisib 照吃不停**，inavolisib **必須停藥**至 ≤160。另：alpelisib 的失敗判準是「21 天 → 減量」，inavolisib 是「7 天 → 照會專科（不自動減量）」 |
| **> 250 – 500 mg/dL**<br>(> 13.9 – 27.8 mmol/L) | • **Interrupt PIQRAY**<br>• 起始／加強口服降糖藥，並**考慮加用其他降糖藥物 1–2 天**直到高血糖改善<br>• **靜脈輸液**，並考慮處理 electrolyte／ketoacidosis／hyperosmolar 異常<br>• 若 **3–5 天內** FPG 降至 ≤160 → **降 1 個劑量階後 resume**<br>• 若 **3–5 天內**未降至 ≤160 → **建議照會高血糖專科**<br>• 若 **21 天內**未降至 ≤160 → **永久停藥** | • **Withhold ITOVEBI**<br>• 起始／加強降糖藥<br>• 必要時給予適當**補水**<br>• 若 **≤ 7 天內**降至 ≤160 → **以原劑量 resume**<br>• 若 **≥ 8 天**才降至 ≤160 → **降 1 個劑量階 resume**<br>• 若 **30 天內再度**出現 > 250–500 → withhold 至 ≤160，**降 1 個劑量階 resume** | ⚠️⚠️ alpelisib 恢復治療時**一律降階**，且有明確的 **21 天永久停藥** 硬條款；inavolisib 若 7 天內回穩可**維持原劑量**，且此層**無永久停藥條款**，改以「30 天內復發 → 降階」處理。<br>⚠️ alpelisib 明文寫 **IV hydration**，inavolisib 僅寫 "appropriate hydration if required" |
| **> 500 mg/dL**<br>(> 27.8 mmol/L) | • **Interrupt PIQRAY**<br>• 起始／加強適當降糖治療（**給予靜脈輸液**，並考慮處理 electrolyte／ketoacidosis／hyperosmolar 異常）<br>• **24 小時內**重測 FPG，並依臨床需要重測<br>• 若降至 ≤500 → 依 **Grade 3（>250–500）** 之建議處理<br>• 若**確認**仍 > 500 mg/dL → **永久停藥**（EMA 版：24 小時後確認 >500 即永久停藥） | • **Withhold ITOVEBI**<br>• 起始／加強降糖藥<br>• **評估 volume depletion 與 ketosis**，並給予適當補水<br>• 若降至 ≤160 mg/dL → **降 1 個劑量階 resume**<br>• 若 **30 天內再度** > 500 mg/dL → **永久停藥** | ⚠️⚠️⚠️ **決策差異最大**。alpelisib：**單次確認 >500 即永久停藥**。inavolisib：**第一次 >500 不停藥**，降階續用；**要 30 天內再犯**才永久停藥。<br>⚠️ 恢復門檻也不同：alpelisib 只要降到 ≤500 就往回走 Grade 3 流程；inavolisib **一律要降到 ≤160** 才能 resume |
| **恢復（resume）門檻總結** | 一律 **≤ 160 mg/dL (8.9 mmol/L)**，且**恢復時必降 1 階** | 一律 **≤ 160 mg/dL (8.9 mmol/L)**；**恢復劑量視回復速度而定**（≤7 天原劑量、≥8 天降 1 階） | ⚠️ |
| **CTCAE 版本** | 表註明列 **CTCAE v4.03**（FDA 與 EMA 一致）【L1】[label_alpelisib.md] | FDA Table 2 表註 b 寫 **v5.0**、Table 4 實驗室異常表註 c 寫 **v4.03**、EMA Table 2 表註 a 寫 **v4.03** — **同一藥品的標示不一致，本回顧照錄不作推論**【L1】[label_inavolisib.md] | ⚠️ 影響 Grade 對照，見 C-3 |
| **降糖藥物種類（表註）** | 明列 **metformin、SGLT2i、insulin sensitizers（TZD 或 DPP-4i）**；並附 SOLAR-1 之 metformin 滴定法：500 mg QD → 500 mg BID → 早 500 mg／晚 1,000 mg → 1,000 mg BID | **FDA 全文未出現 metformin**，僅寫 "oral anti-hyperglycemic medications"。**EMA Table 2 表註 b** 才明列 metformin、SGLT2i、TZD、DPP-4i、insulin，並註明 **metformin 為 INAVO120 中的 preferred initial agent** | ⚠️ 若只讀 FDA 仿單，會找不到 inavolisib 的建議用藥；**必須查 EMA SmPC** |
| **Insulin 的地位** | 表註 ³：「as recommended in the SOLAR-1 trial, **insulin may be used for 1–2 days** until hyperglycemia resolves. However, this **may not be necessary in the majority** of PIQRAY-induced hyperglycemia, given the short half-life…」 | EMA 4.4：「**Short-term insulin may be used as rescue treatment** for hyperglycaemia. There is limited experience in patients receiving insulin…」 | 兩者皆允許短期 insulin |
| **停藥時的低血糖風險** | 仿單未設獨立警語（`本回顧未取得可驗證來源`） | **EMA 4.4 明文警告**：中斷或停用 Itovebi 時，先前為控糖而使用的 insulin／sulfonylurea 會造成低血糖，須一併考量【L1】[label_inavolisib.md]。INAVO120 protocol 亦載明 insulin／sulphonylurea 須謹慎使用，因中斷 inavolisib 可導致 insulin 快速上升與低血糖【L2】[INAVO120_Safety_Im_2026.md] | ⚠️ |

### C-2b. 臨床可執行要點（依上表推導）

1. 【L1】**FPG 161–250 mg/dL 是兩藥最容易誤用的區間**。開 inavolisib 者請把「FPG > 160 就停藥」寫進病人衛教單與護理指示；開 alpelisib 者不要因為 FPG 180 就擅自停藥（仿單明文不需調整劑量），而應加強降糖治療並啟動 21 天倒數。
2. 【L1】**FPG > 500 mg/dL 時，alpelisib 的門檻是「確認即永久停藥」**。因此在通報 >500 之前務必確認為**空腹**值、排除檢體或監測誤差；一旦確認，臨床上該病人的 alpelisib 治療即告終止（EMA 版要求 24 小時後複驗）。
3. 【L1】**Inavolisib 的恢復速度決定劑量**：FPG > 250–500 者若 7 天內回到 ≤160 可維持 9 mg；因此**前 7 天的積極降糖介入具有保留劑量強度的直接價值**。這與 INAVO120 protocol「for hyperglycaemia, time was allowed (up to 7 days) for resolution after interruptions … to avoid premature dose reduction or discontinuation」一致【L2】[INAVO120_Safety_Im_2026.md]。
4. 【L1】**停藥／中斷時必須同步下修 insulin 與 sulfonylurea**（EMA 對 inavolisib 有明文警告；alpelisib 仿單雖無獨立警語，但同樣有短半衰期、停藥後血糖回復之特性——FDA 表註 ³ 明載 96%（52/54）停 PIQRAY 後 FPG 回到基線）【L1】[label_alpelisib.md][label_inavolisib.md]。
5. 【L1】**不可因為顧慮 hyperinsulinemia 而延誤急症治療**。兩份仿單在 FPG > 250 mg/dL 之處置中皆明文要求評估／處理 **ketoacidosis 與 hyperosmolar disturbances**（alpelisib：intervention for electrolyte/ketoacidosis/hyperosmolar disturbances；inavolisib：assess for volume depletion and ketosis）。已發生 DKA／HHS 者，補液與 insulin 為標準處置，**「PI3Ki 誘發之高血糖多可自行回復」這句話不適用於急症情境**【L1】[label_alpelisib.md][label_inavolisib.md]。
6. 【L1】**癌症病人的腹瀉／脫水會經腎功能反噬 inavolisib 劑量**：eGFR 掉入 30–<60 時 AUC 上升 73%，仿單要求降至 6 mg QD；而 inavolisib 組腹瀉 48%、體重下降 17%、食慾下降 24%。故高血糖處置（尤其滲透性利尿）與腹瀉、補水、腎功能需**同一張表一起追蹤**【L1】[label_inavolisib.md]。alpelisib 則相反：CLcr 30–<90 不需調整、CLcr <30 影響未知（等於**沒有可依循的劑量**）【L1】[label_alpelisib.md]。
7. 【L4】**體重下降與食慾不佳者慎用 GLP-1 RA**：專家意見指出 BMI > 30 者可考慮 GLP-1 RA，但**須考量惡病質與營養不良風險**【L3】[ToxMgmt_Jhaveri_2026.md]。同來源亦建議 **PI3Ki 誘發之高血糖一般應避免 sulfonylurea，因有 rebound hypoglycemia 風險**【L3】[ToxMgmt_Jhaveri_2026.md]。

---

## C-3. Q4：SOLAR-1 與 INAVO120 為何**不能**直接 cross-trial compare

**結論先行**：把「alpelisib 63.7%（181/284）／Grade 3 32.7% + Grade 4 3.9%」與「inavolisib 58.6%（95/162）／Grade 3 or 4 5.6%（9/162）」並排相減，**在方法學上是不合法的**。兩篇主要文獻的作者**都親自寫下了這個警告**：

> "Cross-trial comparisons should be made with caution owing to **differences in trial design, patient populations, and analysis and reporting methods.**"
> — INAVO120 主論文 DISCUSSION（p.1593）【L2】[INAVO120_Turner_2024.md]

> 「Hyperglycaemia … has been reported with alpelisib; however, **cross-trial comparisons should be made with caution due to differences in trial design, patient populations, analysis, NCI-CTCAE versions used (4.0 in SOLAR-1 and 5.0 in INAVO120) and reporting.**」【L2】[INAVO120_Safety_Im_2026.md]

⚠️ 附帶提醒：INAVO120 的 discussion 亦轉引「alpelisib 併用療法因 AE 停藥 **25.0%**、everolimus 併用 **19%**、capivasertib–fulvestrant **13.0%**，而 inavolisib 組為 **6.8%**」【L2】[INAVO120_Turner_2024.md]——這些是 **INAVO120 作者轉引他文**的數字，引用時須標明為「INAVO120 discussion 內轉引」，不可直接視為各原始試驗之第一手數據。

以下拆解**六個獨立的偏差來源**，其中 (2) 為本節新增之**逐條並列**。

### (1) 族群不同：治療線數、內分泌治療史、年齡

| | SOLAR-1【L2】[SOLAR1_AE_Rugo_2020.md] | INAVO120【L2】[INAVO120_Turner_2024.md] |
|---|---|---|
| 疾病階段 | **晚期後線**：progressed or recurred **on or after an aromatase inhibitor**, with or without a CDK4/6 inhibitor【L1-adjacent】[FDA_Alpelisib_Narayan_2021.md] | **第一線晚期**（first-line）：逐字為「had had **relapse during or within 12 months after the completion of adjuvant endocrine therapy**」；**de novo 轉移病人被排除** |
| 內分泌抗性 | 約 **86%** 有 endocrine resistance（per protocol definition） | 依 protocol 定義分層：**primary resistance 111 (34.2%)**（adjuvant ET 前 2 年內復發）、**secondary resistance 213 (65.5%)**（第 2 年後或完成後 12 個月內復發） |
| 先前 CDK4/6i | 約 **6%** 曾接受 CDK4/6 inhibitor | **98.8% 未曾接受 CDK4/6 inhibitor**（曾用 neoadjuvant/adjuvant CDK4/6i 者僅 **4/325 = 1.2%**）；作者自列為限制：「few patients had previously received adjuvant CDK4/6 inhibitors, given that recruitment primarily occurred before adjuvant CDK4/6 inhibitors were available」 |
| 中位年齡 | alpelisib 組 **62 歲**、placebo 組 **64 歲**；仿單另載 284 人中 **117 人 ≥65 歲、34 人 ≥75 歲**【L1】[label_alpelisib.md] | **54.0 歲**（range 27–79）；<65 歲之 PFS 次族群 n = 136 vs 130（即絕大多數 <65 歲） |
| 停經狀態 | **premenopausal 病人不符資格、未收錄**【L1-adjacent】[FDA_Alpelisib_Narayan_2021.md] | postmenopausal **60.0%**、premenopausal **38.2%**；收錄 pre-／peri-／postmenopausal 女性及男性（女性佔 98.2%） |
| 體位 | 僅可得 BMI 分組人數（alpelisib 組 normal 110／overweight 84／obese 74，未給 kg/m² cut-off） | **中位體重 63.0 kg**（38–124）；BMI **<18.5 佔 5.5%**、18.5–<25.0 佔 **47.1%**、≥30.0 僅 **17.5%** |
| 腫瘤負荷 | **49%** 有肺或肝轉移 | **≥3 器官轉移 51.4%、內臟轉移 80.0%、肝轉移 51.7%**（作者自述族群「enriched for patients with poor prognostic factors」） |
| 種族 | 原文未於本擷取範圍報告 | 亞洲人 **38.2%**、白人 58.8%；作者明載 Black or African American patients **underrepresented**（2/325 = 0.6%） |

**這一點單獨就足以否定跨試驗比較。** alpelisib 仿單記載：≥75 歲者 Grade 3–4 高血糖 **56% vs <75 歲 36%**；≥65 歲者 44% vs <65 歲 32%【L1】[label_alpelisib.md]；SOLAR-1 原文逐字為 **19/34 (55.9%) vs 89/250 (35.6%)**【L2】[SOLAR1_AE_Rugo_2020.md]。INAVO120 族群中位年齡小了 8–10 歲、中位體重僅 63 kg、近一半 BMI 落在正常範圍、甚至 5.5% 過輕——**僅此年齡與體位結構差異即可造成數個百分點以上的 Grade 3–4 高血糖差距，與藥物本身的致高血糖強度無關**。

> ⚠️ **需修正的常見誤解（本版以 NEJM 全文再確認）**：INAVO120 **並非**「CDK4/6i 治療中或治療後短期內進展」的族群。NEJM 原文的 enrichment 條件是**內分泌治療抗性**（adjuvant ET 期間或完成後 12 個月內復發），且 **98.8% 為 CDK4/6i-naive**，屬**一線**治療設定【L2】[INAVO120_Turner_2024.md]。任何把 INAVO120 描述成「CDK4/6i 後線」的敘述與原文不符。**「CDK4/6i 之後」的 alpelisib 族群是 BYLieve**，但 BYLieve 於本地僅有 abstract（📌），本節不對其內文細節作斷言。

### (2) 基線代謝納入條件不同 —— **INAVO120 幾乎排除了所有高血糖風險族群**

#### (2a) ★ 基線糖代謝納入／排除條件 —— 逐條並列（全文可 grep）★

| # | 條件 | **SOLAR-1**（alpelisib + fulvestrant） | **INAVO120**（inavolisib + palbo + fulv） | 門檻落差 |
|---|---|---|---|---|
| 1 | **HbA1c 上限（最終版）** | **< 6.5%**（原逐字：「At the start of the study, the **HbA1c criterion for inclusion was < 8%**, which was then modified to **< 6.5%**, excluding patients with uncontrolled diabetes」）【L2】[SOLAR1_AE_Rugo_2020.md] | **< 6.0%**（NEJM 逐字：「a **glycated hemoglobin level of less than 6.0%**」）【L2】[INAVO120_Turner_2024.md]（原 protocol < 5.7%，後修訂為 < 6.0%【L2】[INAVO120_Safety_Im_2026.md]） | **INAVO120 嚴格 0.5 個百分點**；且 SOLAR-1 的門檻在收案中途才收緊 |
| 2 | **HbA1c 上限（收案初期）** | **< 8%** —— 亦即 SOLAR-1 **前段收的病人可以是 HbA1c 6.5–7.9% 的明確糖尿病族群**【L2】[SOLAR1_AE_Rugo_2020.md] | 全程 < 6.0%（或更嚴的 < 5.7%）【L2】[INAVO120_Turner_2024.md] | **落差最大達 2 個百分點的 HbA1c**；SOLAR-1 前段族群完全不可能出現在 INAVO120 |
| 3 | **FPG 上限** | **≤ 140 mg/dL**（修訂後）【L3】[Multidisc_Rugo_2022.md]（另一來源表述為「排除 FPG > 140 mg/dL 或 HbA1c > 6.4%」【L3】[Delphi_Gallagher_2024.md]）；⚠️ SOLAR-1 AE 全文中**未逐字載明 FPG 納入門檻** → 此列僅有【L3】層級來源 | **< 126 mg/dL**（NEJM 逐字：「a **fasting glucose level of less than 126 mg per deciliter**」）【L2】[INAVO120_Turner_2024.md] | **14 mg/dL 的門檻差**；且證據等級不對等（L3 vs L2） |
| 4 | **既有糖尿病之處置** | 逐字：「Patients with a history of **well-controlled type 2 diabetes were eligible to enroll**; however, patients with **type 1 and uncontrolled type 2 diabetes were excluded**」【L2】[SOLAR1_AE_Rugo_2020.md] | 逐字：「patients with **type 1 or type 2 diabetes that required ongoing treatment were excluded**」【L2】[INAVO120_Turner_2024.md] | ⚠️⚠️ **關鍵**：SOLAR-1 允許**已用藥且控制良好**的 T2DM；INAVO120 **只要在服降糖藥就不能入組**。這是兩試驗最根本的族群切割 |
| 5 | **實際 diabetic 佔比** | **12 人（4%）**（依 ADA 定義以隨機化前數值判定：FPG ≥ 7.0 mmol/L 或 HbA1c ≥ 6.5%）【L2】[SOLAR1_AE_Rugo_2020.md]；EMA 記載 12 名 diabetic 中 **10 人（83.3%）發生 Grade 3–4 高血糖**【L1】[label_alpelisib.md] | ITOVEBI arm **僅 1 名 T2DM 病人**【L1】[label_inavolisib.md]；⚠️ **NEJM Table 1 未列基線糖尿病比例**【L2】[INAVO120_Turner_2024.md] | 4% vs ~0.6%（且 INAVO120 之數字僅有仿單層級） |
| 6 | **實際 pre-diabetic 佔比** | **159 人（56%）**（ADA 定義：FPG 5.6–<7.0 mmol/L 且 HbA1c 5.7–<6.5%）【L2】[SOLAR1_AE_Rugo_2020.md] | HbA1c ≥5.7% 者僅 **9.9%（16/162）**【L2】[INAVO120_Safety_Im_2026.md]；⚠️ **NEJM 未報告 prediabetes 比例**【L2】[INAVO120_Turner_2024.md] | **56% vs 9.9%，相差 5.7 倍** |
| 7 | **基線 normal glycemia 佔比** | **113 人（40%）**【L2】[SOLAR1_AE_Rugo_2020.md] | 未直接報告 | 分布完全反向 |
| 8 | **基線 HbA1c／FPG 之實際數值分佈** | 有（依 ADA 三分類完整報告）【L2】[SOLAR1_AE_Rugo_2020.md] | **NEJM 未報告 mean/median HbA1c 或 FPG，僅有納入門檻**【L2】[INAVO120_Turner_2024.md] | ⚠️ 連「能不能比」的原始資料都缺一半 |
| 9 | **肥胖／BMI 分層** | alpelisib 組逐字分母為 normal **110**、overweight **84**、obese **74**（⚠️ 原文**未給** BMI 分組之 kg/m² cut-off，亦未給佔全體 284 之百分比）【L2】[SOLAR1_AE_Rugo_2020.md] | **BMI ≥30.0 佔 17.5%**、25.0–<30.0 佔 28.9%、18.5–<25.0 佔 **47.1%**、**<18.5 佔 5.5%**（分母 = FAS 325）【L2】[INAVO120_Turner_2024.md]；ITOVEBI arm BMI ≥30 為 17.9%（29/162）【L2】[INAVO120_Safety_Im_2026.md] | INAVO120 明顯較瘦（中位體重 63.0 kg），且**有 5.5% 過輕**；SOLAR-1 之 BMI 分層甚至無法對齊定義 |
| 10 | **既有降糖藥使用者** | 允許（well-controlled T2DM 可入組，故基線即可能在服 metformin）【L2】[SOLAR1_AE_Rugo_2020.md] | **等同排除**（需 ongoing treatment 者不得入組）【L2】[INAVO120_Turner_2024.md] | 影響「新發高血糖」之基準線判讀 |
| 11 | **高血糖風險因子（≥1 項）之盛行率** | 仿單記載風險因子（baseline diabetic/pre-diabetic、BMI ≥30、≥75 歲）存在於**任何等級高血糖者的 74.9%、Grade 3–4 者的 84.7%**（⚠️ 此為**在高血糖病人中**的盛行率，非分層發生率）【L1】[label_alpelisib.md] | **約 40%（69/162）** 有 ≥1 項風險因子【L2】[INAVO120_Safety_Im_2026.md] | 兩者**統計軸不同**，不可直接相比 |

**這是最致命的一項**。SOLAR-1 有 **56% pre-diabetic + 4% diabetic**（且前 56.6% 收案者的 HbA1c 上限竟是 **< 8%**）；INAVO120 只有 **9.9%** 達 ADA prediabetes、全臂只有 **1 名**糖尿病病人，且**凡是在吃降糖藥的人一律不得入組**。而 SOLAR-1 原文自己就證明基線狀態決定一切：**prediabetic 者任何等級高血糖 74%（G3 43.4%、G4 5.0%）vs normal 者 52%（G3 16.8%、G4 1.8%）**【L2】[SOLAR1_AE_Rugo_2020.md]；INAVO120 亦顯示風險因子數目與高血糖率成正比（0 項：52.7%／Grade 3–4 2.2%；1 項：68.0%／8.0%；2 項：62.5%／12.5%；3 項：66.7%／33.3%）【L2】[INAVO120_Safety_Im_2026.md]。**兩個試驗的基線代謝風險分布根本不在同一個分母上**，任何未經 risk-factor 校正的比較都會把「族群篩選」誤讀成「藥物差異」。

#### (2b) 同一個藥、換一組納入條件，發生率就跳動 —— 兩個直接證據

1. **同藥不同納入條件（inavolisib）**：納入條件放寬為 **HbA1c < 7%、fasting glucose < 140 mg/dL** 的 **GO39374**，在有高血糖風險因子的次族群中高血糖率高達 **81%**【L2】[INAVO120_Safety_Im_2026.md]——相對 INAVO120 的 58.6%。
2. **同藥、同機構、只差「試驗 vs 常規診療」（alpelisib）**：MSKCC 真實世界世代（n = 247，2013-01-01 至 2021-10-15）中，**standard care 組（n = 147）any-grade 高血糖 80.3%、Grade 3–4 40.2%**，而**同一機構的 clinical trial 組（n = 100）僅 34.0% 與 13.0%（p < .001）**；Grade 4 更是 standard care 16 人（10.9%）vs trial 組 **0 人**【L4】[MSKCC_RealWorld_Shen_2023.md]。
   - 該差異在**排除發生 DKA 者與血糖最高 5%** 之敏感度分析後**仍顯著（p < .001）**；即使只比較 trial 組中接受**標準 300 mg/day** 的次族群（n = 33），仍為 **80% vs 52%（p < .001）**【L4】[MSKCC_RealWorld_Shen_2023.md]。
   - 作者自列三項解釋：(i) standard care 世代已知糖尿病比例較高，而試驗以 uncontrolled/insulin-dependent diabetes 及 fasting glucose／HbA1c cutoff 為排除條件；(ii) phase 1/2 試驗使用低於 300 mg 之劑量（中位 RDI **277 mg/day** vs **246 mg/day**，p < .001）；(iii) 試驗中血糖監測與處置較結構化、密集【L4】[MSKCC_RealWorld_Shen_2023.md]。
   - 客觀基線落差佐證：standard care 組 HbA1c ≥5.7% 者 **30.6% vs trial 組 15.0%（p = .041）**【L4】[MSKCC_RealWorld_Shen_2023.md]。

> **這兩個證據合起來說明：納入條件＋監測強度所造成的效應（34.0% → 80.3%，或 58.6% → 81%），其量級遠大於 alpelisib 與 inavolisib 之間的名目差距（63.7% vs 58.6%）。** 因此把兩個試驗的百分比相減，量到的主要是**篩選門檻**，不是**藥物本身**。
> ⚠️ MSKCC 為【L4】單中心回溯世代，兩組基線不可比（年齡、HbA1c 分布、HER2 狀態、併用內分泌治療、alpelisib 劑量皆不同），**組間差異不可解讀為因果**；此處僅用以示範「同藥不同族群即可有 2 倍以上落差」【L4】[MSKCC_RealWorld_Shen_2023.md]。

### (3) 高血糖定義、分級標準與端點種類不同

- **CTCAE 版本不同**：SOLAR-1 之 protocol 高血糖處置表（Table 1）與 AE 分級明載 **CTCAE v4.03**【L2】[SOLAR1_AE_Rugo_2020.md]；INAVO120 用 **v5.0**【L2】[INAVO120_Safety_Im_2026.md]【L3】[ToxMgmt_Jhaveri_2026.md]。專家回顧明言：「guidance on management of hyperglycemia by severity is complicated by the fact that **hyperglycemia grade no longer corresponds to specific glucose ranges in CTCAE v5**」【L3】[ToxMgmt_Jhaveri_2026.md]。**v4.03 的 Grade 3 = FPG > 250–500 mg/dL、Grade 4 = FPG > 500 mg/dL 有明確血糖界值（見 SOLAR-1 Table 1 逐字）；v5 沒有。** 因此「Grade 3 32.7% + Grade 4 3.9% vs Grade 3 or 4 5.6%」這組數字，**分子的定義本身就不同**。
- **preferred term vs grouped term**：SOLAR-1 同一篇文章內，**preferred term「hyperglycemia」為 181/284 = 63.7%（G3 32.7%、G4 3.9%）**，而 **AESI grouped term 為 187/284 = 65.8%（grade ≥3 = 38.0%）**；原文表註明文提醒兩者不可混用【L2】[SOLAR1_AE_Rugo_2020.md]。INAVO120 Table 2 之 hyperglycemia **亦為 grouped term**（表註逐字：「hyperglycemia … were assessed as **grouped terms**」）【L2】[INAVO120_Turner_2024.md]。**若拿 SOLAR-1 的 preferred term（63.7%）比 INAVO120 的 grouped term（58.6%），連端點種類都對不上**；改用同為 grouped term 者，應為 **65.8% vs 58.6%**（但族群仍不可比）。
- **grade 拆分粒度不同**：SOLAR-1 逐字給出 Grade 1/2/3/4 四層【L2】[SOLAR1_AE_Rugo_2020.md]；**INAVO120 主論文只給「Grade 3 or 4」合併值 5.6%，未拆分**【L2】[INAVO120_Turner_2024.md]。因此「alpelisib Grade 4 3.9% vs inavolisib Grade 4 0%」這種對比，**在 NEJM 全文層級沒有可驗證的分母**（EMA「無 Grade 4」屬仿單層級【L1】[label_inavolisib.md]）。
- **實驗室值 vs 臨床 AE term**：同一份 inavolisib 仿單裡，FDA 依實驗室 fasting glucose increased 報 **85%／Grade 3–4 12%**，EMA 依臨床 AE term hyperglycaemia 報 **59.9%／Grade 3 5.6%**；仿單擷取稿明文標註「**FDA（85%）與 EMA（59.9%）分母與定義不同，兩者不可互相取代或相加**」【L1】[label_inavolisib.md]。alpelisib 亦同：FDA 5.3 的 hyperglycemia 65% vs 實驗室 glucose increased 79%【L1】[label_alpelisib.md]。**跨試驗比較前，必須先確認比較的是同一種端點。**
- **grouped term 組成不同**：EMA 對 inavolisib 的 hyperglycaemia 定義納入 hyperglycaemia、blood glucose increased、hyperglycaemic crisis、glycated serum protein increased、glucose tolerance impaired、diabetes mellitus、T2DM、HbA1c increased【L1】[label_inavolisib.md]；SOLAR-1 之 AESI grouped term 組成列於 Supplementary Table 1，**本地無補充附錄，無法逐項核對**【L2】[SOLAR1_AE_Rugo_2020.md]。
- **真實世界又是第三套定義**：MSKCC 世代以 **glucose ≥140 mg/dL** 為高血糖門檻、取治療期間**最高血糖值**依 **CTCAE v4.0** 給級，且 time to onset 定義為「起始日至首次 glucose ≥140 mg/dL 之天數」【L4】[MSKCC_RealWorld_Shen_2023.md]——與兩個試驗皆不同，其 61.5%／29.2% 不可與試驗數字並列相減。

### (4) 監測密度不同 —— 監測愈密，偵測到的事件愈多

| | SOLAR-1／alpelisib | INAVO120／inavolisib |
|---|---|---|
| **試驗 protocol 逐字（血液生化）** | 「assessed at screening, **every 2 weeks for the first 8 weeks**, and then **every 4 weeks**」【L2】[SOLAR1_AE_Rugo_2020.md] | protocol 規定 C1 於 **D1、4、8、15、22** 驗 FBG；C2–C3 於 D1、D15；其後每 cycle D1【L3】[ToxMgmt_Jhaveri_2026.md] |
| **FPG 額外加測** | 「Fasting plasma glucose (FPG) was **also assessed on days 8 and 15 in the first 4 weeks**」【L2】[SOLAR1_AE_Rugo_2020.md] | — |
| **首月抽血次數（依可 grep 之排程）** | 第 1–4 週：screening + D8 + D15 + 每 2 週例行 | 第 1 個 cycle：**D1、4、8、15、22 共 5 次**【L3】[ToxMgmt_Jhaveri_2026.md] |
| **Protocol 修訂之影響** | 於 **317/約 560 人（56.6%）** 隨機後修訂：HbA1c 門檻 < 8% → < 6.5%、對 FPG ≥ 100 mg/dL 和／或 HbA1c ≥ 5.7% 者於 screening 衛教生活型態並轉介專科、**新增 day 8 門診**、rash 發生前先用口服抗組織胺【L2】[SOLAR1_AE_Rugo_2020.md] | protocol 修訂為 HbA1c 納入門檻 < 5.7% → < 6.0%【L2】[INAVO120_Safety_Im_2026.md] |
| **HbA1c／insulin 追蹤** | HbA1c 有縱貫追蹤（原文：「a gradual increase in HbA1c was observed with alpelisib, **irrespective of baseline glycemic status**, and remained slightly elevated throughout study treatment」）【L2】[SOLAR1_AE_Rugo_2020.md] | **HbA1c 每 3 個 cycle、空腹 insulin 每個 cycle**【L3】[ToxMgmt_Jhaveri_2026.md] |
| **仿單規定（上市後）** | 前 2 週每週 ≥1 次 → 其後每 4 週 ≥1 次【L1】[label_alpelisib.md] | **D1–7 每 3 天** → D8–28 每週 → 接下來 8 週每 2 週 → 其後每 4 週【L1】[label_inavolisib.md] |

**兩層問題疊在一起**：

1. **試驗間**：INAVO120 第一個 cycle 的抽血次數多於 SOLAR-1 的例行排程。**在偵測率上，這會使 INAVO120 的低度（Grade 1–2）事件被更完整捕捉、高度事件被更早攔截**——兩者對「any-grade 率」與「Grade 3–4 率」的影響方向相反，無法用單一方向的校正抵銷。
2. **試驗內**：**SOLAR-1 自己的前後半段就不可比**。前 50% vs 後 50% 隨機者：any-grade 高血糖 **63.9% vs 63.6%（幾乎不變）**，但 **Grade 3/4 由 40.3% 降至 32.9%**、**因高血糖停藥由 9.0% 降至 3.6%**、因任何級 AE 停藥由 29.2% 降至 20.7%、**因 grade ≥3 AE 停藥由 18.1% 降至 7.9%**【L2】[SOLAR1_AE_Rugo_2020.md]。
   > ⚠️ **詮釋界線**：作者自述此改善「may be attributed to the protocol amendment, **as well as other factors**, such as earlier identification and appropriate management of AESIs」——**非隨機比較，僅為時序性關聯**；且原文亦載明兩段之中位暴露期間與因 AE 減量／中斷頻率「generally consistent」【L2】[SOLAR1_AE_Rugo_2020.md]。
   > **臨床啟示（這一點比跨試驗比較有用得多）**：在**同一個藥、同一個試驗**內，僅僅收緊納入門檻 + 加開 day 8 門診 + 標準化處置指引，就把 Grade 3/4 高血糖從 40.3% 拉到 32.9%、把因高血糖停藥砍掉超過一半。**監測與處置的品質，本身就是可改變的變因。**

### (5) 併用藥不同 —— palbociclib 的間接效應

- SOLAR-1：alpelisib **300 mg/day with food**（可階梯減量至 250、200 mg/day）+ **fulvestrant**【L1】[label_alpelisib.md]【L2】[SOLAR1_AE_Rugo_2020.md]。
- INAVO120：inavolisib **9 mg PO QD（D1–28）** + **palbociclib 125 mg PO QD（D1–21）** + **fulvestrant 500 mg IM（C1 D1、D15，其後約每 28 天）**【L1】[label_inavolisib.md]【L2】[INAVO120_Turner_2024.md]。
- **暴露時間本身就差了近一倍**：alpelisib 中位暴露 **5.5 個月**（range 0–30.8）【L2】[SOLAR1_AE_Rugo_2020.md] vs inavolisib **9.2 個月**（中位相對劑量強度 95.8%）【L2】[INAVO120_Turner_2024.md]。**暴露愈久，累積事件愈多**；把兩組的 crude「曾發生率」相減，等於忽略了分母時間。
- **劑量調整壓力也不同**：SOLAR-1 中 alpelisib **dose reduction 59.2%、dose interruption 72.2%**（因 AE 者 57.7% / 66.5%）【L2】[SOLAR1_AE_Rugo_2020.md]；INAVO120 中任何 AE 導致 inavolisib 減量僅 **14.2%**（placebo 3.1%）【L2】[INAVO120_Turner_2024.md]。減量頻率差約 4 倍，等於兩組實際承受的 PI3Kα 抑制強度分布完全不同。
- **⚠️ 但不可把 palbociclib 減量歸因於高血糖**：INAVO120 原文**未報告**任何 palbociclib 劑量調整與 hyperglycemia 之交互分析；可 grep 者僅為 palbociclib 中位相對劑量強度 **87.3%（inavolisib 組）vs 88.4%（placebo 組）**——兩組接近，且其主要驅動因子 neutropenia 在兩組發生率相近（grade 3/4 **80.2% vs 78.4%**）【L2】[INAVO120_Turner_2024.md]。

**palbociclib 本身不是致高血糖藥物**——INAVO120 的 placebo arm（palbociclib + fulvestrant）any-grade hyperglycaemia 僅 **7.4%（12/162）**、Grade 3–4 **0%**，實驗室 fasting glucose increased 43%／Grade 3–4 0%【L1】[label_inavolisib.md]【L2】[INAVO120_Safety_Im_2026.md]。但 palbociclib **會經由劑量強度與 AE 負荷影響整體暴露**：INAVO120 中 **71.0%（115/162）** 病人曾因 AE 中斷 palbociclib、**37.7%（61/162）** 曾減量 palbociclib（主因為 neutropenia：any grade 54.3%、Grade 3–4 47.5%）【L2】[INAVO120_Safety_Im_2026.md]。三合一方案的中斷與減量事件，會改變病人實際承受的 PI3Kα 抑制暴露分布，使「每人年高血糖風險」不可直接對應到單一藥物。

### (6) 額外：預防性 metformin 的使用率不同

- SOLAR-1：**163 名接受降糖藥者**中 **87.1%** 用過 metformin（單用或併用），但那是**治療性**用藥；且 **41.1%（67/163）僅需 1 種藥、28.8%（47/163）需 ≥3 種藥**【L2】[SOLAR1_AE_Rugo_2020.md]（仿單則以 187 名高血糖者為分母記為 76%，142/187【L1】[label_alpelisib.md]——**兩者分母不同，不可混用**）。SOLAR-1 protocol Table 1 之處置階梯為「FPG < 140 → consider metformin；FPG 140–160 → start or intensify metformin；grade 2 → start oral antidiabetic；超過 metformin MTD → 加 insulin sensitizer（如 pioglitazone）」【L2】[SOLAR1_AE_Rugo_2020.md]。
  - ⚠️ **metformin 之具體 titration schedule（起始 mg、加量間隔、目標劑量）在 SOLAR-1 AE 全文中未報告**（已 grep "metformin"、"titrat"、"500 mg"、"1000 mg" 確認）；仿單所載之 500 mg QD → 500 mg BID → 早 500／晚 1,000 → 1,000 mg BID 為【L1】[label_alpelisib.md] 層級。
- INAVO120：NEJM 原文逐字「**The protocol allowed prophylactic use of metformin in patients with a high risk of hyperglycemia**」——但**未報告使用率、未定義「高風險」、未隨機化、未報告其對高血糖發生率之影響**【L2】[INAVO120_Turner_2024.md]。使用率 **7.4%（12/162）** 僅見於安全性專文【L2】[INAVO120_Safety_Im_2026.md]。
- 真實世界（alpelisib）：MSKCC 世代**無預防性 metformin 政策**，任何降糖藥使用率僅 **66%（101/152）**，低於 SOLAR-1 的 87%；需 ≥3 種藥者與需 insulin 者亦較少【L4】[MSKCC_RealWorld_Shen_2023.md]。

**兩試驗的預防性介入政策不同本身即為一個 confounder**：INAVO120 有一小部分病人（7.4%）在 C1D1 就已在服 metformin，而 SOLAR-1 的 metformin 幾乎都是**事件發生後**才給。這使 INAVO120 的「首次高血糖事件」計數本身被部分抑制，方向與藥物差異同向，**無法從已發表數據中分離**。

> ⚠️ **附帶警告（回應常見過度解讀）**：METALLICA 是 **multicentre, open-label, SINGLE-ARM, phase 2, n = 68** 的研究【L2】[METALLICA_LlombartCussac_2024.md]【L1】[label_alpelisib.md]，**沒有隨機對照組**。它的 Cohort B（prediabetes）在預防性 metformin 之下，高血糖仍發生於 **70%（14/20）**、Grade 3–4 **15%（3/20）**【L1】[label_alpelisib.md]。FDA 仿單的措辭是「**Consider** premedication」，並明載**會增加噁心／嘔吐／腹瀉的發生率與嚴重度**，METALLICA 中 diarrhea 68%、nausea 68%、vomiting 34%、Grade 3–4 diarrhea 13%，因 AE 永久停藥率 19%【L1】[label_alpelisib.md]。**「METALLICA 已證明所有病人都該先吃 metformin」是錯誤結論**；在本來就有腹瀉、體重下降、食慾不佳的癌症病人身上，預防性 metformin 可能是淨損害。

### Q4 綜合建議

**六項偏差來源總表（每一項都足以獨立否定跨試驗相減）**：

| # | 偏差來源 | SOLAR-1 | INAVO120 | 對「誰的高血糖率較高」的影響方向 |
|---|---|---|---|---|
| 1 | 族群與治療線 | 後線、中位 62/64 歲、僅收 postmenopausal、約 6% 曾用 CDK4/6i | 一線、中位 54.0 歲、38.2% premenopausal、**98.8% CDK4/6i-naive** | 偏向 SOLAR-1 較高 |
| 2 | 基線糖代謝門檻 | HbA1c **< 8% → < 6.5%**；**well-controlled T2DM 可入組**；56% prediabetic、4% diabetic | HbA1c **< 6.0%**、FPG **< 126 mg/dL**；**需持續降糖治療者一律排除**；HbA1c ≥5.7% 僅 9.9% | **偏向 SOLAR-1 極度較高** |
| 3 | 高血糖定義與分級 | CTCAE **v4.03**（有明確血糖界值）；preferred term 與 AESI 兩套 | CTCAE **v5.0**（無血糖界值）；**只給 grade 3 or 4 合併值** | 方向不定、無法校正 |
| 4 | 監測密度 | 例行 q2wk×8wk + FPG D8/D15；修訂後才加 day 8 門診 | C1 D1/4/8/15/22 | any-grade 偏向 INAVO120 較高、G3–4 偏低 |
| 5 | 併用藥與暴露 | alpelisib + fulvestrant；中位暴露 **5.5 個月**；減量 59.2% | 三合一（+palbociclib）；中位暴露 **9.2 個月**、RDI 95.8%；減量 14.2% | 方向不定 |
| 6 | 預防性 metformin | 幾無（事件後治療為主） | protocol **允許**，實際 7.4% | 偏向 INAVO120 較低 |

**【L3】臨床上該怎麼做**：
1. **不要**在衛教或跨科溝通中並列「Grade 3–4 36.6% vs 5.6%」作為選藥依據。若一定要引用數字，**必須同時說出六項偏差中至少第 1、2 項**。
2. 若必須比較，**只能在同一風險層內比**：例如以「無風險因子者」對照 —— INAVO120 中 0 項風險因子者 Grade 3–4 高血糖 **2.2%（2/93）**【L2】[INAVO120_Safety_Im_2026.md]；alpelisib 之對應層級**本回顧未取得可直接對照之數字**——SOLAR-1 全文可得者為依基線血糖狀態之分層（normal 者 G3 16.8%、G4 1.8%）與依 BMI 之分層（normal BMI 者 G3 24.5%、G4 2.7%）【L2】[SOLAR1_AE_Rugo_2020.md]，但**其分層軸（ADA 血糖三分類、BMI 三分類）與 INAVO120 的「風險因子項數」不同軸**，兩者之交叉表原文皆未提供 → **無法構成合法的同層對照**。
3. 兩藥的**適應症位置本來就不重疊**（inavolisib 為 adjuvant ET 後復發之一線三合一；alpelisib 為 AI 後進展之二線以後併 fulvestrant），臨床上多數情境**不需要**做這個比較。
4. **真正可以拿來用的比較，是「同藥、不同照護品質」**：SOLAR-1 內部前後半段（Grade 3/4 **40.3% → 32.9%**、因高血糖停藥 **9.0% → 3.6%**）【L2】[SOLAR1_AE_Rugo_2020.md] 與 MSKCC 的 trial vs standard care（**34.0% vs 80.3%**）【L4】[MSKCC_RealWorld_Shen_2023.md]。這兩組數字告訴臨床醫師的是**可以改變的事**（基線篩檢、監測密度、標準化處置流程），而非**不能改變的事**（病人分到哪個試驗、吃哪一顆藥）。

---

## C-4. Q3 直答：發生率、中位發生時間、Grade 3–4 風險

| 問項 | Alpelisib | Inavolisib |
|---|---|---|
| **Any-grade 高血糖** | 65%（FDA 5.3）／67.3%（EMA）；**SOLAR-1 原文 preferred term 181/284 = 63.7%、AESI grouped term 187/284 = 65.8%**【L2】[SOLAR1_AE_Rugo_2020.md]；實驗室 glucose increased 79%【L1】[label_alpelisib.md]。真實世界 **61.5%（152/247）**【L4】[MSKCC_RealWorld_Shen_2023.md] | 59.9%（EMA）；**INAVO120 原文 grouped term 95/162 = 58.6%**（placebo 14/162 = 8.6%）【L2】[INAVO120_Turner_2024.md]；實驗室 fasting glucose increased 85%【L1】[label_inavolisib.md] |
| **Grade 3–4** | **Grade 3 33% + Grade 4 3.9%**（FDA）；實驗室 Grade 3–4 39%【L1】[label_alpelisib.md]；**SOLAR-1 原文 Grade 3 93/284 = 32.7%、Grade 4 11/284 = 3.9%**（AESI grade ≥3 為 108/284 = 38.0%）【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界 Grade 3 22.7% + Grade 4 6.5%，合計 **29.2%（72/247）**【L4】[MSKCC_RealWorld_Shen_2023.md] | **Grade 3 12% + Grade 4 0.6%**（FDA 5.1）；實驗室 Grade 3–4 12%；EMA Grade 3 **5.6%**、**無 Grade 4**【L1】[label_inavolisib.md]；**INAVO120 原文僅給合併值 Grade 3 or 4 = 9/162 = 5.6%**（placebo 0%），⚠️ **未拆分 3 與 4**【L2】[INAVO120_Turner_2024.md] |
| **中位發生時間** | **15 天**（Grade ≥2，range 5–517 天，FDA）【L1】[label_alpelisib.md]；**SOLAR-1 原文：grade ≥3 事件中位 15 天（range 5–395 天，依 FPG 判定）**【L2】[SOLAR1_AE_Rugo_2020.md]；真實世界中位 **16 天**（至首次 glucose ≥140 mg/dL）【L4】[MSKCC_RealWorld_Shen_2023.md] —— **三個獨立來源皆落在 15–16 天** | **7 天**（range 2–955 天）【L1】[label_inavolisib.md]【L2】[INAVO120_Safety_Im_2026.md]。⚠️ **NEJM 主論文未報告 time to onset**【L2】[INAVO120_Turner_2024.md] |
| **中位改善／緩解時間** | 改善 ≥1 grade：仿單 8 天（range 2–65，n = 153）【L1】[label_alpelisib.md]；**SOLAR-1 原文 grade ≥3 事件改善 ≥1 grade 中位 6 天（range 4–7）**【L2】[SOLAR1_AE_Rugo_2020.md]。真實世界緩解（至 glucose <140 mg/dL）：**metformin 單方中位 16 天（IQR 7–26）**；需在 metformin 之外加藥者 **26 天（IQR 14–64）**，顯著較長（p = .024）【L4】[MSKCC_RealWorld_Shen_2023.md] | 改善 ≥1 grade 中位 8 天（range 2–43）【L1】[label_inavolisib.md]；resolution 中位 16 天（IQR 5–50）【L2】[INAVO120_Safety_Im_2026.md] |
| **時間分布** | **平均 FPG 於治療前 2 週達峰**，其後在降糖藥支持下回落趨近基線；**HbA1c 則緩升並維持輕度上升**【L2】[SOLAR1_AE_Rugo_2020.md]；EMA 建議前 4 週、尤其前 2 週密集自我監測【L1】[label_alpelisib.md] | 多發生於**前三個 treatment cycle**【L2】[INAVO120_Safety_Im_2026.md]；EMA：新發率於**前兩個月**最高【L1】[label_inavolisib.md] |
| **可逆性** | **所有發生高血糖者，停用 alpelisib 後均回到 grade 0 或 1**【L2】[SOLAR1_AE_Rugo_2020.md]（⚠️ 回復所需之中位天數原文未報告） | FPG > 160 mg/dL 者 96%（52/54）改善 ≥1 grade【L1】[label_inavolisib.md] |

**【L1】臨床操作結論（不做跨試驗因果推論，只陳述各自仿單事實）**：
- **inavolisib 的第一次抽血必須非常早**。中位 7 天、範圍最短 2 天，而仿單規定 D1–7 每 3 天驗一次 —— 意即 **D4 這次抽血不能省**。
- **alpelisib 的中位 15 天落在「前 2 週每週一次」的規定內**，但 range 上限達 517 天（EMA 1,458 天；SOLAR-1 原文 grade ≥3 事件 range 為 5–395 天【L2】[SOLAR1_AE_Rugo_2020.md]），代表**遲發性高血糖確實存在**，不可在第 3 個月後就放鬆監測。SOLAR-1 全文亦顯示**平均 FPG 峰值就在前 2 週**【L2】[SOLAR1_AE_Rugo_2020.md]——仿單（15 天）、SOLAR-1 全文（15 天）、MSKCC 真實世界（16 天）三個獨立來源訊號一致，**第一次抽血若排在第 2 週才做，已經太晚**。
- **HbA1c 不能拿來當早期偵測工具**：SOLAR-1 顯示 HbA1c 是**緩升**且**不論基線血糖狀態皆然**【L2】[SOLAR1_AE_Rugo_2020.md]；急性期判讀請一律用 **FPG**（兩份仿單的劑量決策也都只認 FPG）【L1】[label_alpelisib.md][label_inavolisib.md]。HbA1c 的角色在**治療前風險分層**——MSKCC 顯示基線 HbA1c 是與高血糖發生（p < .001）及 alpelisib 減量／停藥（p = .015）皆相關的因子，且與 BMI 同入模型時**只有基線 HbA1c 仍顯著（p < .001）**；作者因此強力主張**常規於 PI3Ki 開始前測 baseline HbA1c**（該世代即使在 standard care 組也僅 72% 有基線 HbA1c）【L4】[MSKCC_RealWorld_Shen_2023.md]。⚠️ 該研究統計法為 Pearson's χ²、非多變項迴歸，無 OR/95% CI，**不可解讀為因果或用於個體風險預測**。
- 兩藥的**中位改善時間都是 8 天**【L1】[label_alpelisib.md][label_inavolisib.md]（SOLAR-1 全文對 grade ≥3 事件另報 6 天，range 4–7 天【L2】[SOLAR1_AE_Rugo_2020.md]），故發生高血糖後給予約一週的積極內科處置再論減量／停藥，符合兩份仿單的時間框架。
- ⚠️ **【L2】不可因為顧慮 hyperinsulinemia 而迴避急症所需的 insulin**。SOLAR-1 AE 專文的作者在同一段裡先說「insulin sensitizers（如 metformin）可能優於 insulin secretagogues」，隨即明文寫下：
  > "**However, short-term insulin is clearly effective for managing acute cases as well as more severe hyperglycemia associated with alpelisib and not controlled by oral antihyperglycemic medications alone.**"【L2】[SOLAR1_AE_Rugo_2020.md]

  SOLAR-1 實際有 **52 人**用過 insulin（**33 人為長期使用 >2 天、19 人為 rescue 用藥**）【L2】[SOLAR1_AE_Rugo_2020.md]；MSKCC 真實世界亦有 **16/101（15.8%）** 用 insulin，且該文作者明載「**insulin is still indicated for the management of severe hyperglycemia and/or ketoacidosis**」【L4】[MSKCC_RealWorld_Shen_2023.md]。**已發生 DKA／HHS 或口服藥無法控制之嚴重高血糖時，補液與 insulin 為標準處置；「避免 hyperinsulinemia 以免再活化 PI3K 訊息」屬機轉層級考量【L5】，不得凌駕於急症處置之上。**
- **【L2】metformin 的地位有證據支持，但不等於「人人先吃」**：SOLAR-1 中 163 名用藥者有 **87.1%** 用 metformin【L2】[SOLAR1_AE_Rugo_2020.md]、MSKCC 中 101 名用藥者有 **89.1%** 用 metformin【L4】[MSKCC_RealWorld_Shen_2023.md]——但這兩者**都是事件發生後的治療性用藥**，**不是預防性投予有效的證據**。MSKCC 作者另指出 metformin 的機轉限制（其主要作用 AMPK 活化「is abolished by PI3K inhibition」）與**腸胃道副作用與 alpelisib 重疊**，可能限制其使用與加量【L4】[MSKCC_RealWorld_Shen_2023.md]。
- **【L4】內分泌照會與 SGLT2i 的關聯須小心解讀**：MSKCC 中內分泌轉介率 **49/247 = 19.8%**（standard care 30.0% vs trial 6.0%，p < .001），且與 SGLT2i 處方（p = .007）及 alpelisib 減量／停藥（p < .001）相關——但作者自述兩者皆為**針對持續性、較高等級高血糖的晚期介入**，屬 **confounding by indication**，**不可解讀為「照會內分泌科或加 SGLT2i 會造成減量」**【L4】[MSKCC_RealWorld_Shen_2023.md]。該研究中 SGLT2i **單方僅 3 人**，與 metformin 單方相比緩解時間無顯著差異（p = .5），**無法支持 SGLT2i 優於 metformin 之臨床結論**【L4】[MSKCC_RealWorld_Shen_2023.md]。
- **【L4】高血糖與 PFS 無關（真實世界）**：MSKCC 中位追蹤 13.7 個月、全世代中位 PFS 6.1 個月（95% CI 4.8–7.3），高血糖狀態（time-dependent covariate）與 PFS **無關（HR 0.98；95% CI 0.72–1.33）**；依高血糖分級、BMI ≥25、HbA1c ≥5.7%、是否因高血糖減量／停藥分層，PFS 亦無顯著差異【L4】[MSKCC_RealWorld_Shen_2023.md]。SOLAR-1 亦顯示 PFS 獲益不因基線血糖狀態而異（prediabetes/diabetes 11.0 vs 5.6 個月，HR 0.66 [0.47–0.92]；normal 10.9 vs 6.5 個月，HR 0.65 [0.42–1.02]）【L2】[SOLAR1_AE_Rugo_2020.md]。**臨床意義：積極治療高血糖不會犧牲抗癌療效，糖尿病／糖尿病前期本身也不是排除 PI3Kα 抑制劑的理由。**
- **警訊症狀衛教一致**：excessive thirst、urinating more often、blurred vision、confusion、difficulty breathing、increased appetite with weight loss【L1】[label_inavolisib.md]（alpelisib EMA 版列：excessive thirst、排尿次數／量增加、增加食慾伴體重下降【L1】[label_alpelisib.md]）。癌症病人本身即常有體重下降與食慾改變，**不可將這些症狀一律歸因於腫瘤惡病質而忽略高血糖**。

---

## C-5. 本節查無可驗證來源、留白之項目

> **本版異動**：原第 1、3、5 項因 `SOLAR1_AE_Rugo_2020.md`📄 落地而**部分或全部解除留白**；第 4 項因 `INAVO120_Turner_2024.md`📄 落地而**改寫其留白理由**；新增 5b。

1. **SOLAR-1 之血糖納入條件** → **已部分解除**。`SOLAR1_AE_Rugo_2020.md`📄 Methods 逐字載有糖尿病資格條件（「well-controlled type 2 diabetes were eligible … type 1 and uncontrolled type 2 diabetes were excluded」）與 **HbA1c 門檻由 < 8% 修訂為 < 6.5%**【L2】。**仍留白者：FPG 納入門檻之逐字條文**——該文未載，本節所引「FPG ≤ 140 mg/dL」仍僅有 `Multidisc_Rugo_2022.md`📄【L3】與 `Delphi_Gallagher_2024.md`📄【L3】，**兩份來源表述略有出入（HbA1c ≤6.5% vs >6.4%）**，本回顧照錄不作調和。SOLAR-1 主論文 `SOLAR1_Andre_2019.md` 仍為 **abstract-only（📌）**，其 protocol／supplementary 本地亦無（SOLAR-1 AE 專文之 Supplementary Table 1–7 本地亦不含）。
2. **INAVO120 OS 論文（`INAVO120_OS_Jhaveri_2025.md`）之內文細節**：本地仍僅 abstract（📌），故不作具體斷言。INAVO120 主論文（NEJM，`INAVO120_Turner_2024.md`）**已落地全文（📄）**，本節已據其正文、Table 1 與 Table 2 重寫安全性與族群數字。
3. **「因高血糖」單獨導致之 alpelisib dose interruption／reduction 率** → **仍留白（試驗層級）**。`SOLAR1_AE_Rugo_2020.md`📄 只給**整體** alpelisib dose interruption **72.2%**、dose reduction **59.2%**（因 AE 者 66.5% / 57.7%），**未拆分高血糖**【L2】；`ToxMgmt_Jhaveri_2026.md` 標為 NR。可用之替代僅為【L4】真實世界：MSKCC 因高血糖暫停 **26.7%（66/247）**、減量 **17%（42/247）**、停藥 **4.5%（11/247）**【L4】[MSKCC_RealWorld_Shen_2023.md]——**證據等級不同，不可與仿單數字並列**。
4. **可與 INAVO120「風險因子項數」直接對照之 alpelisib 分層 Grade 3–4 發生率** → **仍留白，但留白理由已更精確**。SOLAR-1 全文提供的是**兩套不同軸**的分層：依 ADA 基線血糖狀態（prediabetic 74%／G3 43.4%／G4 5.0% vs normal 52%／G3 16.8%／G4 1.8%）與依 BMI（normal 57.3%、overweight 73.8%、obese 67.6%）【L2】[SOLAR1_AE_Rugo_2020.md]，**兩軸之交叉表原文未提供**，diabetic 組（n = 12）之分級發生率亦**未分項報告**；INAVO120 則是「風險因子項數 0/1/2/3」軸【L2】[INAVO120_Safety_Im_2026.md]。**軸不同 → 無法構成合法的同層對照表。** 另 SOLAR-1 全文亦**未報告**高血糖風險因子之多變量分析（無 OR/HR/p 值，僅描述性 trend）【L2】。
5. **Alpelisib 之中位治療暴露時間** → **已解除**。`SOLAR1_AE_Rugo_2020.md`📄 逐字：alpelisib 中位暴露 **5.5 個月（range 0–30.8）**，同組 fulvestrant 8.2 個月，placebo 組 fulvestrant 5.6 個月【L2】。
5b. **INAVO120 主論文層級之高血糖時序與處置細節** → **本版新增之留白**。NEJM 全文**未報告**：hyperglycemia 之 median time to onset／resolution、grade 3 與 grade 4 之拆分、因高血糖之 dose interruption 與永久停藥率、實際 metformin 或任何降糖藥使用率、「高風險」之操作型定義、基線糖尿病／prediabetes 比例、基線 HbA1c／FPG 之實際分佈、治療中 FPG／HbA1c 之縱貫變化、DKA／HHS 事件數、BMI 分層下之 grade 3/4 率、血糖監測抽血排程、insulin／C-peptide 藥效動力學、高血糖之 protocol 具體 dose-modification 演算法【L2】[INAVO120_Turner_2024.md]。**本地全文不含 Supplementary Appendix（Table S1–S3、Fig S1–S2），故 Table S3（AE 導致停藥明細）與 Table S2（serious AE 明細）無法 grep 驗證。**
5c. **MSKCC 真實世界世代之未報告項目** → 該文**未報告** DKA 之實際人數／比率（僅於敏感度分析提及排除 DKA 病人）、HHS、類固醇使用、既有糖尿病之量化統計、多變項迴歸 OR/95% CI、高血糖發生時間之 IQR／range、依 BMI 或 HbA1c 分層之實際發生率百分比（僅報 p 值），以及腹瀉／噁心／脫水／eGFR 等其他 AE（僅有 BMI 變化 −1.30 kg/m²）【L4】[MSKCC_RealWorld_Shen_2023.md]。該研究**完全不涵蓋 inavolisib**（收案至 2021 年，僅 alpelisib/BYL-719），**其數字不得外推至 inavolisib**。
6. **兩藥之 head-to-head 隨機比較**：不存在；仿單擷取稿亦明載「inavolisib 與 alpelisib 的頭對頭比較：無此類 label 資料，本回顧未取得可驗證來源」【L1】[label_inavolisib.md]。
7. **TFDA 之 inavolisib 中文仿單、台灣核准與給付狀態**：**本回顧未取得可驗證來源**【L1】[label_inavolisib.md]。台灣 alpelisib 中文仿單版本為 2022-09-22，**早於 FDA 01/2024 改版，故不含 metformin premedication／METALLICA 段落**【L1】[label_alpelisib.md]。
8. **SGLT2i 併用 PI3Kα inhibitor 之 euglycemic DKA 風險**：兩份仿單皆未針對此交互作用出具警語 → **label 層級為空白**【L1】[label_inavolisib.md]。
9. **BYLieve（post-CDK4/6i 之 alpelisib 族群）之內文細節**：本地三個 BYLieve 檔案皆為 abstract（📌），且其中一篇為 Expression of concern（`BYLieve_EoC_2024.md`）→ 本節不對其內文作具體斷言。
10. **EMA SmPC（兩藥）之確切 revision date**：PDF 欄位空白 → **本回顧未取得可驗證來源**【L1】[label_alpelisib.md][label_inavolisib.md]。
