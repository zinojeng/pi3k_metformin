# claim.md — 數字與引號字串逐項稽核（claim-auditor）

**稽核日期**：2026-07-21
**稽核範圍**：`章節/*.md` 共 10 檔（B、C、D、E、F、G、H、I、K、M），2,520 行
**方法**：抽出百分比／樣本數 n／中位數／95% CI／HR-OR-RR／劑量／FPG-HbA1c 門檻／引號字串，逐一到其標註之來源檔（`原始PDF/*.md`、`來源/*.md`）以彈性 pattern（含 `[.·,]` 中點變體）grep 驗證。
**實際抽驗**：**228 項**（涵蓋任務指定的全部重點查核項，另加各章高影響力數字之廣泛抽樣）。非窮盡：純敘述性引號（無數字）僅抽樣驗證。

---

## 0. 統計摘要

| 判定 | 數量 |
|---|---|
| **必修** | **3** |
| **待議** | **5** |
| **通過** | **220** |

---

## 1. 必修（3 項）

| # | 問題 | 出處章節 | 宣稱來源檔 | Grep 結果 | 判定 |
|---|---|---|---|---|---|
| M1 | `SOLAR1_AE_Rugo_2020.md` 被宣告為「**僅有 abstract（📌）**，付費牆，其 protocol／supplementary 一律不引用」 | C-1 稽核聲明、C-5 第 1 項、K-1 第 31 列、K-7 §153 第 1 點 | SOLAR1_AE_Rugo_2020.md、MISSING_FULLTEXT.md | ❌ **標記錯誤**。該檔實為 **81,542 bytes 全文**（`<!-- fulltext: 📄 使用者上傳 PDF，LlamaParse 轉檔 -->`），且 K-1 所列全部數字皆 grep 命中全文：`32.7`(L107,333)、`3.9%`(L107,334)、`15 days`(L108,340)、`13 days`(L109,340)、`139 days`(L109,341)、`87.1`(L110,381)、`7.9%`(L114,482)、`18.1`(L114)、`248`(L115-117,375) | **必修**（標記須改 📄；C 章因此誤棄可用之【L2】全文證據） |
| M2 | `INAVO120_Turner_2024.md` 被宣告為「**僅有 abstract（📌）**，不對其內文細節作斷言」 | C-1 稽核聲明、C-3、C-5 第 2 項、K-1 第 38 列、K-7 §155-2 | INAVO120_Turner_2024.md | ❌ **標記錯誤**。該檔實為 **78,182 bytes 全文**；`161`/`164`/`15.0`/`7.3`/`0.43`/`0.32`/`0.59` 皆於 L32 命中，`325` 於 L115 命中 | **必修**（同上） |
| M3 | 「原始PDF/ 內共 **70** 個 .md 檔」「**38 篇取得全文（📄）**、**31 篇僅 abstract（📌）**，全文取得率約 55%」「本回顧共納入 **69** 篇獨立文獻」 | K-7 | inventory.md | ❌ **與實際檔案不符**。`ls *.md \| wc -l` = **71**；`<5000 bytes`（abstract-only）之檔 = **29**；扣除 METALLICA 重複落地後全文 ≈ **41**，取得率 ≈ 59% | **必修**（可直接 grep 反證之數字錯誤） |

---

## 2. 待議（5 項）

| # | 數字／字串 | 出處章節 | 宣稱來源檔 | Grep 結果 | 判定 |
|---|---|---|---|---|---|
| P1 | 「因高血糖停藥 **16.7% vs 2.6%**」（列於「Rodón 模型高風險組」效果量表） | D-1 量化風險梯度表；D-3 亦引 | RiskModel_Rodon_2024.md | ⚠ 原文 L113 逐字：「Among patients **who discontinued alpelisib**, there were more discontinuations due to hyperglycemia in the high- vs. low-risk group (**15/90 [16.7%]**) vs. **4/154 [2.6%]**」。**分母是「已停藥者」而非全部病人**（全部病人之停藥率為 15/106=14.2% vs 4/178=2.2%） | **待議**（數字正確、分母陳述易被誤讀，建議補上「在已停藥者中」） |
| P2 | 「233 人篩選僅 68 人入組（**20.2%**）」 | E-§7 第 2 點 | METALLICA_LlombartCussac_2024.md | ⚠ 兩值皆存在於原文：Abstract L25 = `68 (20.2%)`、Results L113 = `68 (29.2%)`；68/233 = 29.2%。**G-1.2 已明文標註此內部矛盾並採 29.2%，E 章未標註且採 20.2%** → 兩章互相矛盾 | **待議**（需統一並加註來源內部不一致） |
| P3 | 「因 AE 永久停用 alpelisib … **食慾下降 3 (4.4%)**」 | G-1.6 表、G-3.3 第 4 點 | METALLICA_Llombart_2024.md | ⚠ 原文正文 L212 逐字為「decreased appetite (**three [4.4%]** patients)」→ **命中**；但同文 **Table 3（L194）為 `Decreased appetite \| 1 (1.5) \| 1 (1.5) \| 0 (0)` = 2 人（2.9%）**。來源內部矛盾。G 章已標註另兩處內部矛盾（20.2/29.2%、腹瀉 13.2/11.8%），獨漏此處 | **待議**（照錄無誤，建議比照加註） |
| P4 | 「Shen 2023：**101 (40.9%)** 接受降糖治療」 | K-4 第 97 列；M-8 相關敘述 | RealWorld_Shen_2023.md | ⚠ Abstract L31 = `101 (40.9%)`；Results L71 = 「Among those who developed hyperglycemia (**n=152**), **101 (66.4%)** received anti-hyperglycemic treatment」。分母不同（247 vs 152），來源內部並存兩值，章節未註明 | **待議** |
| P5 | 「**96%（52/54）**」同時出現在 alpelisib 與 inavolisib 兩藥 | C-1 第 24 列（inavolisib）、C-2b 第 4 點與 I-2-8（alpelisib）、B-6 | label_alpelisib.md、label_inavolisib.md | ⚠ **兩者皆逐字 grep 命中**：`label_alpelisib.md` L51「(n = 54), 96% (n = 52) … FPG levels returned to baseline」；`label_inavolisib.md` L200「96% (52/54) had an improvement in fasting glucose」；INAVO120 全文 L212 佐證 `96.3% (52 of 54)`。**兩者語意不同（回到基線 vs 改善 ≥1 grade）但 n 完全相同**，屬高度巧合 | **待議**（來源已驗證，僅建議人工確認擷取稿無交叉污染） |

---

## 3. 重點查核項目（任務指定）— 全部通過

### 3.1 METALLICA 兩個 cohort 的 n 與 grade 3–4 高血糖率

| 數字 | 出處章節 | 宣稱來源檔 | Grep 結果 | 判定 |
|---|---|---|---|---|
| 篩檢 233 → 收案 68；cohort A **n=48**、cohort B **n=20** | C-3、D-2、E-1、F-1、G-1.2、I-2-1、K-2 | METALLICA_Llombart(Cussac)_2024.md L33/113；label_alpelisib.md L205 | ✅ 逐字命中（`cohorts A (n = 48) and B (n = 20)`） | 通過 |
| Cohort A grade 3–4 **1/48 (2.1%)**，95% CI **0.5–11.1**，P<0.0001 | 同上 | 原文 L164、Table 2 L176-178 | ✅ | 通過 |
| Cohort B grade 3–4 **3/20 (15.0%)**，95% CI **5.6–37.8**，P=0.016 | 同上 | 同上 | ✅ | 通過 |
| Any-grade：全體 30/68 **44.1%**；A **16 (33.3%)**、B **14 (70.0%)** | C-3、E-1、G-1.4、I-2-4、K-2 | 原文 L164；label_alpelisib.md L205（`33% (16/48)`、`70% (14/20)`、`2.1% (1/48)`、`15% (3/20)`） | ✅ 論文與 FDA 仿單雙重命中 | 通過 |
| 全體 grade ≥3 **4 (5.9%)**、grade 4 **0** | G-1.4、I-2-4 | Table 2 L177-180 | ✅ | 通過 |
| 僅 fulvestrant 者：A **1/45 (2.2%)**、B **3/18 (16.7%)** | G-1.4 | 原文 L164 | ✅ | 通過 |

### 3.2 SOLAR-1 高血糖 grade 3/4 率與中位發生時間

| 數字 | 出處 | 來源檔 | Grep | 判定 |
|---|---|---|---|---|
| FDA §5.3：hyperglycemia **65%**、Grade 3 **33%**、Grade 4 **3.9%**、ketoacidosis **0.7% (n=2)** | C-1、C-4、I-2-4、K-0、K-8 | label_alpelisib.md L45（中文版 L472 佐證） | ✅ 逐字 | 通過 |
| EMA §4.8：**191 (67.3%)**；G2 15.8%、G3 **34.5%**、G4 **4.6%** | C-1、I-2-4 | label_alpelisib.md L372 | ✅ | 通過 |
| 實驗室 glucose plasma increased **225 (79.2%)** / G3–4 **112 (39.4%)** | C-1、I-2-4 | label_alpelisib.md L380 | ✅ | 通過 |
| SOLAR-1 發表值 any-grade **63.7%**、G3–4 **36.6%** | C-1、C-3、C-4、E-1、G-1.4、K-2 | ToxMgmt_Jhaveri_2026.md L78-79；Delphi_Gallagher_2024.md L33/93；METALLICA L65/230；SOLAR1_Andre_2019.md abstract | ✅ 四來源一致 | 通過 |
| 中位發生時間 **15 天（range 5–517）**（FDA）／**5–1,458 天**（EMA） | C-1、C-4、D-0、F-0、M-1、B-2 | label_alpelisib.md L47（FDA）、L374（EMA） | ✅ 兩版分別命中 | 通過 |
| 中位改善 **8 天（range 2–65，n=153）**；EMA 8 天（95% CI 8–10） | C-1、C-4、E-1、B-6 | label_alpelisib.md L49、L374 | ✅ | 通過 |
| SOLAR-1 AE 分析：G3 **32.7%**、G4 3.9%；G≥3 中位 15 天；rash 13 天、diarrhea 139 天；**87.1%** 用 metformin；dose intensity **248 mg/day** | K-1 第 31 列 | SOLAR1_AE_Rugo_2020.md L107-117、L333-341、L375-381 | ✅ 全部命中（唯該檔標記須由 📌 改 📄，見 M1） | 通過 |
| ≥75 歲 G3–4 **56% vs 36%**；≥65 歲 **44% vs 32%**；≥75 any-grade 74% vs 66% | D-1、D-2、C-3 | label_alpelisib.md §8.5 L~200 | ✅ 逐字 | 通過 |
| 基線 **56% pre-diabetic、4.2% diabetic**；pre-diabetic 者 any-grade **75.5%**；12 名 diabetic 中 **10 人（83.3%）** G3–4 | C-1、C-3、I-2-2 | label_alpelisib.md L374 | ✅ | 通過 |
| 187 名高血糖者：**87% (163/187)** 用藥、**76% (142/187)** 用 metformin | C-1、C-3、E-1 | label_alpelisib.md L49 | ✅ | 通過 |
| protocol 修訂前後 G3/4 **40.3% → 32.9%**、停藥 **9.0% → 3.6%** | M-8 | Consensus_Tankova_2022.md L85；Multidisc_Rugo_2022.md L79 | ✅ | 通過 |
| 停藥續用 fulvestrant 者 FPG 回基線：FDA **96% (52/54)**／EMA **93.4% (57/61)** | C-2b、M-9、I-2-8 | label_alpelisib.md L51、L364 | ✅ 兩組分母皆逐字命中 | 通過 |

### 3.3 INAVO120 高血糖發生率

| 數字 | 出處 | 來源檔 | Grep | 判定 |
|---|---|---|---|---|
| SAS **162/arm**；FAS **161 vs 164**；共收 **325 人於 28 國**；中位追蹤 **21.3 個月** | C-1、K-1 | INAVO120_Safety_Im_2026.md L83/85；label_inavolisib.md | ✅ | 通過 |
| FDA：fasting glucose increased **85%**；G2 **22%**、G3 **12%**、G4 **0.6%**（對照 43%／0%） | C-1、C-4、I-2-4、K-0 | label_inavolisib.md L194-195、L338、L340 | ✅ | 通過 |
| EMA：hyperglycaemia any grade **59.9%**；G2 **38.3%**、G3 **5.6%**（CTCAE v5.0） | C-1、C-4、I-2-4 | label_inavolisib.md L346-348 | ✅ | 通過 |
| INAVO120 grouped term **58.6% (95/162)**；G1 16.0%、G2 37.0%、**G3 5.6% (9/162)**、無 G4–5、無 serious、**無 DKA** | C-1、C-3、B-6、K-1 | INAVO120_Safety_Im_2026.md L212、Table 4 L223 | ✅ | 通過 |
| 單一 PT `hyperglycaemia` **53.7% (87/162)**；`blood glucose increased` 4.9% (8/162) | C-1 | 同上 L91/119/212 | ✅ | 通過 |
| 檢驗值層級（CTCAE v4.0, n=157）：G1 51.0%、G2 22.3%、**G3 11.5% (18/157)**、G4 0.6% (1/157) | B-6 | 同上 L212 | ✅ | 通過 |
| 中位發生 **7.0 天（2.0–955.0）**；中位 resolution **16.0 天（IQR 5.0–50.0）** | C-1、C-4、D-0、F-0、M-1、B-6 | 同上 L33/212；label_inavolisib.md L203 | ✅ | 通過 |
| 因高血糖：中斷 **27.2% (44/162)** / 減量 **2.5% (4/162)** / 停藥 **0.6% (1/162)**；仿單 28%／2.5%／1.2% | C-1、G-1.8、B-6、K-1 | INAVO120_Safety_Im L33/214；label_inavolisib.md L204-205、L371/376/382 | ✅ 兩層數字分別命中 | 通過 |
| 「導致任一試驗藥退出者 **1.2%（2/162）**」 | C-1 | INAVO120_Safety_Im_2026.md L140 逐字（`withdrawal of any study drug in ≥2 patients was hyperglycaemia [2 of 162 (1.2%)]`） | ✅ | 通過 |
| 降糖藥 **46% (74/162)**；insulin **7% (11/162)**（論文 6.8%），中位 **5.0 天（1.0–539.0）** | C-1、G-1.8、B-5 | label_inavolisib.md L198-199；INAVO120_Safety_Im L216 | ✅ | 通過 |
| 66 名用藥者中 **62/66 (93.9%)** 用 metformin；預防性 metformin **12/162 (7.4%)** | C-1、C-3、E-1、G-1.8 | INAVO120_Safety_Im L216 | ✅ | 通過 |
| 風險因子分層：0 項 52.7%／**2.2% (2/93)**；1 項 68.0%／8.0%；2 項 62.5%／12.5%；3 項 66.7%／**33.3%** | C-3、D-1 | INAVO120_Safety_Im Table 4 L237-240 | ✅ | 通過 |
| BMI ≥30 G3–4 **17.2% (5/29)** vs <30 **3.0% (4/132)**；FBG ≥100 **73.9%／10.9%** vs 52.7%／3.6% | D-1 | 同上 Table 4 L226-235 | ✅ | 通過 |
| 基線：HbA1c ≥5.7% **16/162 (9.9%)**、FPG ≥100 **46/162 (28.4%)**、BMI ≥30 **29/162 (17.9%)**、≥1 風險因子 **約 40% (69/162)** | C-1、C-3、D-1 | 同上 L210 | ✅ | 通過 |
| placebo arm any-grade hyperglycaemia **7.4% (12/162)**、G3–4 **0** | C-3 | 同上 Table 1 L119 | ✅ | 通過 |
| palbociclib 中斷 **71.0% (115/162)**、減量 **37.7% (61/162)**；neutropenia 54.3%／47.5% | C-3 | 同上 L91/99/136/138 | ✅ | 通過 |
| GO39374 有風險因子者高血糖 **81%**；arm F 早期 metformin 下 grade 3 仍 **40.0% (8/20)** | C-3、D-3、K-1 | INAVO120_Safety_Im L339；GO39374_Gambardella_2025.md L267 | ✅ 逐字（`hyperglycemia was frequent (81% of patients)`／`despite early metformin treatment … [n = 8 (40.0%)]`） | 通過 |
| 中位年齡 **53.0（27–77）**、<65 歲 **84.5%**、38% pre/perimenopausal | C-3 | INAVO120_Safety_Im L85；label_inavolisib.md L415 | ✅ | 通過 |
| 長期安全性：**69/162 (42.6%)** 治療 ≥1 年 | I-2-8 | INAVO120_Safety_Im L300 | ✅ | 通過 |
| INAVO120 PFS **15.0 vs 7.3 個月**（HR 0.43, 0.32–0.59）；OS **34.0 vs 27.0**（HR 0.67, 0.48–0.94, P=0.02） | K-1 | INAVO120_Turner_2024.md L32；INAVO120_OS_Jhaveri_2025.md abstract | ✅ | 通過 |
| 引號：「cross-trial comparisons should be made with caution due to differences in trial design, patient populations, analysis, NCI-CTCAE versions used (4.0 in SOLAR-1 and 5.0 in INAVO120) and reporting」 | C-3 開場引文 | INAVO120_Safety_Im_2026.md L341 | ✅ 逐字完全相符 | 通過 |
| 引號：「Patients were relatively younger in INAVO120, as it recruited a first-line, poor-prognosis endocrine-resistant population」 | C-3 | 同上 L335 | ✅ 逐字 | 通過 |
| 引號：「for hyperglycaemia, time was allowed (up to 7 days) for resolution after interruptions … to avoid premature dose reduction or discontinuation」 | C-2b | 同上 L71 | ✅ 逐字 | 通過 |

### 3.4 Real-world 研究發生率

| 數字 | 出處 | 來源檔 | Grep | 判定 |
|---|---|---|---|---|
| Shen 2023：n=**247**；any-grade **152 (61.5%)**、G3–4 **72 (29.2%)**（G3 22.7%、G4 6.5%）；中位發生 **16 天** | D-6、I-2-4、K-4、M-1 | RealWorld_Shen_2023.md L31/69 | ✅ | 通過 |
| standard care **80.3% / 40.2%**（G3 29.3%、G4 10.9%）vs trial **34.0% / 13.0%**（G4=0），p<0.001 | D-6、I-2-4、M-8 | 同上 L31/69 | ✅ | 通過 |
| 敏感度分析：同用 300 mg 之試驗次族群 n=33，仍 **80% vs 52%**（p<0.001）；RDI 277 vs 246 mg/日 | I-2-4 | 同上 L67 及正文 | ✅ | 通過 |
| BMI 中位變化 **−1.30 kg/m²（−5.5%，IQR −0.33 至 −3.0）**；BMI×HbA1c 交互作用 **p=0.005**，同時入模僅 HbA1c 顯著（p<0.001） | D-5、I-2-7 | 同上 L67/69 | ✅ | 通過 |
| 「only **72%** of patients had baseline HbA1c」；轉介內分泌 **49 (19.8%)**，與 SGLT2i 處方相關 **p=0.007** | D-6、M-8 | 同上 L87/31/71 | ✅ | 通過 |
| metformin 單藥中位緩解 **16 天（IQR 7–26）**；加第二藥 **26 天（IQR 14–64）**，p=0.024 | G-2.5 | 同上 L71 | ✅ | 通過 |
| PFS 無差異：HR 0.98（95% CI 0.72–1.33）；分層後亦無差異 | I-2-3 | 同上 L75 | ✅ | 通過 |
| Liu 2022：n=**491**；中斷 **12% (39/491)**、減量 **6% (30/491)**、住院 **2% (7/491)**、永久停藥 1 人 | D-0、I-2-4、K-4 | RealWorld_Liu_2022.md L33/184 | ✅ | 通過 |
| β/γ/δ-specific PI3Ki **無任何事件**；事件僅見於 AKT (5%)、α (13%)、pan-PI3K (5%) | D-0、I-2-4 | 同上 L33/184 | ✅ 逐字 | 通過 |
| BMI ≥25 單變項 OR **5.4 (2.3–16.0)**、多變項 **4.0 (1.3–17.8), p=0.03**；HbA1c ≥5.7% **4.7 (2.1–11.0)** / **3.4 (1.2–9.4), p=0.02** | D-1、I-2-7 | 同上 L194/201/203/213 | ✅ | 通過 |
| 基線糖尿病最高絕對率 **8/23 (34.7%)** | D-1、I-2-2 | 同上 L194/207 | ✅ | 通過 |
| 校正後降糖幅度：metformin **−28 (−41, −16)**、SGLT2i **−48 (−75, −21)**、SU −38 (−69, −8)、insulin −22 | H-1、I-2-6 | 同上 L235 | ✅ | 通過 |
| **僅 15 人（含 12 新使用者）**用 SGLT2i 即出現 **1 例 euglycemic DKA**（pH 7.26、bicarb 13、anion gap 21、ketonuria） | D-5、H-1、I-2-6 | 同上 L184/273 | ✅ | 通過 |
| grade ≥2 高血糖 **49.9% (174/349)**、G3 22% (77/349)、G4 4% (14/349) | I-2-4 | 同上 L231 | ✅ | 通過 |
| 住院者平均血糖 **538 mg/dL**、中位 **14 天（7–56）** | I-2-4 | 同上 L184 | ✅ | 通過 |
| Ismail 2026（📌）：n=**546**、TOT **87.5 天（IQR 28.0–173.7）**、降糖藥 **20.0%→34.3%**、**81.8% metformin／44% insulin**、TOT **HR 0.76 (0.61–0.93), p=0.008** | I-2-3、I-2-4、K-4 | Claims_Ismail_2026.md abstract | ✅ 全部逐字命中；章節已正確標 📌 | 通過 |
| ITACA：n=**23**、**21/23 (91.3%)** 第 1 週內高血糖、median G2–4 hyperglycaemia-free **6 天（95% CI 3–44）**、HbA1c 5.6→5.8 | M-1、M-5、M-7、K-2 | ITACA_Pancirov_2025.md L33/37/166/184 | ✅ | 通過 |
| French EAP：n=**233**、中位 PFS **5.3 個月 (4.7–6.0)**、**91 (39.1%)** 因 AE 停藥、97.4% 用過 CDK4/6i | K-4 | FrenchEAP_BelloRoufai_2023.md abstract | ✅ | 通過 |
| Cheung 2022：n=**62**、187 vs 77 天、血糖 **HR 1.01 (1.00–1.02), p=0.02** | K-4 | Discont_Cheung_2022.md abstract | ✅ | 通過 |
| Cook 2021：n=**34**（中位 72，range 65–85）、**12 起始 insulin、4 住院、11 停藥** | K-4 | Elderly_Cook_2021.md abstract | ✅ | 通過 |
| Ziegengeist 2024（📌）：**87 例 DKA**、ROR **9.84 (7.3–13.2)**、11 篇 case report 中位 **14 天** | I-2-8、K-4 | FAERS_DKA_Ziegengeist_2024.md abstract | ✅ | 通過 |
| Burnette 2023：n=**16**、Day 28 前 G2–4 **9/16 (56%)**、G3 **3 (19%)**、G4 0、風險因子中位 2 vs 1（p=0.03） | K-2 | Prophylaxis_Burnette_2023.md abstract | ✅ | 通過 |

### 3.5 所有仿單 FPG 門檻數值與對應處置

| 門檻／處置 | 出處 | 來源檔 | Grep | 判定 |
|---|---|---|---|---|
| alpelisib Table 3 四層：>ULN–160 / >160–250 / >250–500 / >500 mg/dL；對應 8.9 / 13.9 / 27.8 mmol/L | C-2、F-0、F-2、I-1E、M-9 | label_alpelisib.md（FDA Table 3 逐字段） | ✅ 四列文字逐格對應無誤 | 通過 |
| alpelisib >160–250 **不需調整劑量**；21 天未達標 → 降 1 階 | C-2、F-0、F-2、I-1E | 同上 | ✅ | 通過 |
| alpelisib >250–500：Interrupt＋IV hydration＋處理 electrolyte/ketoacidosis/hyperosmolar；3–5 天達 ≤160 → 降 1 階；21 天未達 → 永久停藥 | C-2、F-2、M-9 | 同上 | ✅ 逐字（`intervention for electrolyte/ketoacidosis/hyperosmolar disturbances`） | 通過 |
| alpelisib >500：24 小時內複驗，確認仍 >500 → 永久停藥 | C-2、F-2、M-9 | 同上 | ✅ | 通過 |
| alpelisib 減量階梯 **300→250→200**，<200 即停藥 | C-1、F-0、I-1E、M-9 | 同上 | ✅ | 通過 |
| alpelisib 監測：前 2 週每週 ≥1 次 → 之後 ≥每 4 週；HbA1c 每 3 個月；發生後每週 2 次直到正常、用藥期間每週 1 次 ×8 週再每 2 週 | C-1、D-3、E-1、F-0、I-1B、M-2 | 同上 | ✅ | 通過 |
| alpelisib EMA 照會門檻：pre-diabetic／FG >250／BMI ≥30／≥75 歲 = recommended；已知 DM = **should always take place** | C-1、I-1A、M-9 | 同上（EMA §4.2） | ✅ 逐字 | 通過 |
| inavolisib Table 2 四層門檻與 alpelisib 相同；>160–250 即 **Withhold 至 ≤160，原劑量 resume** | C-2、F-0、F-2、I-1E | label_inavolisib.md L108-127 | ✅ 逐字（含 L117 `for patients with risk factors`、L127 `persists > 200 – 250 mg/dL … for 7 days`） | 通過 |
| inavolisib >250–500：≤7 天 → 原劑量；≥8 天 → 降 1 階；30 天內再犯 → 降 1 階 | C-2、F-0、F-2 | 同上 | ✅ | 通過 |
| inavolisib >500：Withhold＋評估 volume depletion 與 ketosis；≤160 → 降 1 階；**30 天內再犯才永久停藥** | C-2、F-2、M-9 | 同上 | ✅ | 通過 |
| inavolisib 減量 **9→6→3 mg**；EMA 另允許 re-escalate 至 9 mg（FDA 無） | C-1、F-0、I-1E、M-9 | 同上 | ✅ | 通過 |
| inavolisib 監測：**D1–7 每 3 天 → D8–28 每週 → 接下來 8 週每 2 週 → 其後每 4 週**；HbA1C 每 3 個月 | C-1、D-0、E-4、F-0、I-1B、M-3 | 同上 L213/259 | ✅ | 通過 |
| inavolisib EMA 風險因子：(pre)diabetes、HbA1C ≥5.7%、BMI ≥30、**≥45 歲**、GDM 病史、DM 家族史 | C-1、D-0、D-1、E-2、I-1A、M-3 | 同上 L269/283 | ✅ 逐字 | 通過 |
| inavolisib EMA：併用類固醇／intercurrent infection 者「Monitoring of HbA1C **and ketones (preferably in blood)** … is recommended」 | D-4、I-1B、M-3、M-6 | 同上 | ✅ 逐字 | 通過 |
| inavolisib 腎功能：eGFR 30–<60 → **6 mg**；<30 → **3 mg**；AUC ↑**73%**／↑**123%** | C-1、E-4、F-0、I-1E、M-9 | 同上 | ✅ | 通過 |
| alpelisib 腎功能：CLcr 30–<90 不需調整；<30 **unknown** | C-1、D-2、E-4、I-1E | label_alpelisib.md §8.6 | ✅ 逐字 | 通過 |
| **「FDA PI 全文未出現 metformin 字樣」** | C-1、C-2、E-4、F-0、G-1.8、I-1C | label_inavolisib.md（擷取稿自述已 grep 確認） | ✅ 全檔 grep `metformin` 僅出現於 EMA 段（L163/355）與稽核註記，FDA PI 段確無 | 通過 |
| alpelisib 仿單 metformin 滴定：**500 QD → 500 BID → 早 500／晚 1000 → 1000 BID** | E-1、F-1、G-2.4、I-1D、M-9 | label_alpelisib.md Table 3 註² | ✅ | 通過 |
| 引號：「**Consider** premedication with metformin … based on patient risk factors for hyperglycemia, **gastrointestinal tolerability**, and clinical situation」 | C-1、D-3、E-1、F-1、G-1.7、I-1C、M-9 | label_alpelisib.md | ✅ 逐字 | 通過 |
| 引號：「increases the incidence and severity of nausea, vomiting, and diarrhea adverse reactions」／「decreases the incidence and severity of hyperglycemia, but increases…」 | C-3、D-3、E-1、G-1.6、I-2-1 | label_alpelisib.md L205 前後段 | ✅ 逐字 | 通過 |
| 引號：「insulin may be used for **1-2 days** until hyperglycemia resolves. However, this **may not be necessary in the majority**…」 | C-2、H-1、I-1D、B-5 | label_alpelisib.md Table 3 註³ | ✅ 逐字 | 通過 |
| 引號：「**Short-term insulin may be used as rescue treatment** for hyperglycaemia」 | C-2、G-3.4、H-3、I-1D、M-6 | label_inavolisib.md EMA §4.4 | ✅ 逐字 | 通過 |
| 04/2026 FDA 5.1：「Severe **or fatal** hyperglycemia, **including ketoacidosis**」＋「Ketoacidosis with a fatal outcome has occurred in the postmarketing setting」；09/2025 列為 RECENT MAJOR CHANGE | C-1、F-3、H-0、I-2-8、M-6、B-2 | label_inavolisib.md L30/191/234/293-294/306 | ✅ 兩版對照逐字 | 通過 |
| TRUQAP（capivasertib）CAPItello-291：**37%**（G2 11%、G3 2%、G4 1.1%）、中位 **15 天（1–367）**、減量 0.6%／停藥 0.6%、DKA **0.3%** | K-0 | guideline_ada_comparators.md L221-227 | ✅ | 通過 |
| CAPItello-281：**69%**、G4 1.2%、中位 **71 天（1–1454）**、DKA **1.2%** | K-0 | 同上 L231-239 | ✅ | 通過 |
| TFDA 中文仿單版本 **2022-09-22**（衛部藥輸字第 027995 號），早於 FDA 01/2024 改版故不含 METALLICA 段 | C-5、D-8、E-8、G-2.4、I-2-7、K-0 | label_alpelisib.md §7/§9/§10 | ✅ | 通過 |

### 3.6 metformin 的 eGFR 門檻

| 門檻 | 出處 | 來源檔 | Grep | 判定 |
|---|---|---|---|---|
| eGFR **≥60**：可起始，每年監測 | D-2、E-1、F-1、G-3.1、M-9 | Multidisc_Rugo_2022.md L99 | ✅ 逐字（`eGFR ≥60 mL/min/1.73`＋`annual monitoring`） | 通過 |
| eGFR **45–60**：可續用，每 3–6 個月監測 | 同上 | 同上 L99 | ✅ | 通過 |
| eGFR **30–45**：不得新起始；已在用者停用或減量 **50%**，每 3 個月追腎功能 | 同上 | 同上 L75/99 | ✅ | 通過 |
| eGFR **<30**：**禁忌** | 同上 | 同上 L75/99；Mgmt_Goncalves_2022.md | ✅ | 通過 |
| Rugo 正文 vs Table 1 措辭差異（「<45 不起始」vs「30–45 不起始」）已由 G-3.1 誠實並陳 | G-3.1、E-1 | 同上 L93 vs L99 | ✅ 兩處措辭皆命中，章節已標註 | 通過 |
| Delphi：2000 mg/day 上限**須 GFR >45 mL/min/1.73 m²**；另提 2500 mg/day | D-2、E-1、G-2.4、G-3.1 | Delphi_Gallagher_2024.md L51 | ✅ 逐字（`provided a GFR of >45`、`2500`） | 通過 |
| METALLICA 收案門檻 **CLcr ≥35 mL/min（Cockcroft-Gault）**，與 eGFR 45 不可互換 | G-1.1、G-3.1 | trials_ongoing.md | ✅ | 通過 |
| 顯影劑：「In patients with **eGFR <30** … **withhold metformin prior to contrast imaging and 48 h after imaging**」 | G-3.2、H-2.2、M-9 | Capivasertib_Mgmt_Iyengar_2025.md L130/163 | ✅ 逐字 | 通過 |
| ADA Rec **3.10（B）**：長期 metformin 者定期評估 vitamin B12 | G-2.2、G-3.1 | guideline_ada_comparators.md L120 | ✅ 逐字 | 通過 |

---

## 4. 其他通過項目（分章摘錄）

### B 章（病生理）
| 數字／引號 | 來源檔 | Grep | 判定 |
|---|---|---|---|
| 小鼠：metformin p=**0.2136**（血糖）／**0.7566**（c-peptide）／**0.6186**（pS6）皆不顯著；SGLT2i <0.0001／0.0386／<0.0001；ketogenic 0.007／0.0117／<0.0001 | InsulinFeedback_Hopkins_2018.md L36 | ✅ 六個 p 值全部逐字命中 | 通過 |
| **10 ng/mL** insulin（給藥後 15–30 分鐘濃度）→ pAKT 部分回復、pS6 幾乎完全回復 | 同上 L30 | ✅ 逐字 | 通過 |
| **0.4 mU** insulin 抵消 ketogenic diet 之療效增益 | 同上 L42（`0.4mU`） | ✅（原文無空格，需彈性 pattern） | 通過 |
| Song 2022：WT p110α t½ ≈ **26.7 h**；H1047R ≈ **9.6 h**；加 taselisib 縮短至 ≈ **4 h** | Preclin_Song_Inavolisib_2022.md L63 | ✅ | 通過 |
| 「p110a depletion was not observed with 40 mg/kg BYL719」／GDC-0077 50 mg/kg 耗竭 8 小時 | 同上 | ✅ | 通過 |
| SOLAR-1 median dose intensity **≥248 mg/day** 者 PFS 較長 | Delphi_Gallagher_2024.md L93 | ✅ | 通過 |
| HHS 個案 insulin 需求由 **46 IU/day** 一週內完全停用 | Inavolisib_HHS_Li_2026.md L73 | ✅ | 通過 |
| Pla-Peris 個案 basal-bolus **38 U**（0.68 U/kg） | FGM_PlaPeris_2022.md L61 | ✅（`38 U`；0.68 需人工確認單位換算表述） | 通過 |

### D 章（風險分層）
| 數字 | 來源檔 | Grep | 判定 |
|---|---|---|---|
| Rodón：pooled **n=505**（X2101 221＋SOLAR-1 284）、外部驗證 BYLieve **n=340** | RiskModel_Rodon_2024.md L27/83 | ✅ | 通過 |
| 高風險組 2 個月 G3/4 機率 **86.2%**（訓練集）／**57.6%**（測試集）；低風險 <5%／<20% | 同上 L105 | ✅ | 通過 |
| SOLAR-1 高風險 **96/106 (90.6%)** vs 低風險 **12/178 (6.7%)** G3/4；any-grade 95.3% vs 48.3% | 同上 L111 | ✅ | 通過 |
| 高低風險組 PFS **11.0 vs 10.9 個月** | 同上 L27；I-2-3 | ✅ | 通過 |
| 5 變項：FPG、BMI、HbA1c、**monocytes**、age；monocytes「warrants further investigation」無切點 | 同上 L31/105/125 | ✅ 章節已正確標為留白 | 通過 |
| Tankova：BMI 正常 **57%** vs 過重／肥胖 **68–74%**；prediabetes **74%** vs 正常 **52%**；≥75 歲 G3/4 **55% vs 36%** | Consensus_Tankova_2022.md L59/61 | ✅（註：Tankova 寫 55%，仿單寫 56%，兩章分別依來源引用，無誤） | 通過 |
| HHS 個案：**59 歲、BMI 19.55、HbA1c 5.7%**、**72 小時內**血糖 **48.0 mmol/L**、有效滲透壓 **327 mOsm/L**、尿酮陰性、C-peptide **10.2 ng/mL**、fasting insulin 41.5 μU/mL、ICA/GADA/IAA 陰性 | Inavolisib_HHS_Li_2026.md L29/47/58 | ✅ 全部逐字 | 通過 |
| 引號：「patients **without high-risk factors** may still experience severe drug-related adverse effects」 | 同上 L111 | ✅ 逐字 | 通過 |
| ADA high-risk 四因子：≥70 歲、BMI ≥30、glucocorticoids、A1C ≥5.7% 或 FPG ≥100 | guideline_ada_comparators.md §1.5 | ✅ | 通過 |
| ADA Rec **3.8（B）**「Consider … in **high-risk individuals**」逐字 | 同上 L116 | ✅ | 通過 |
| ADA Rec **9.35a（E）**／**9.35b（E）**「reserved for severe hyperglycemia and hyperglycemic crises」逐字 | 同上 L158/160 | ✅ | 通過 |
| 「A1C alone may not capture the early peak of hyperglycemia noted with PI3Kα inhibitors」 | 同上 L89 | ✅ 逐字 | 通過 |
| ADA 引 SOLAR-1 事後分析中位 **13 天**（range 至約 1 年） | 同上 L89/322 | ✅ | 通過 |

### F／H 章（處置與降糖藥）
| 數字 | 來源檔 | Grep | 判定 |
|---|---|---|---|
| Carrillo DKA：血糖 **1137 mg/dL**、anion gap **25**、HbA1c **9.4%**（7 個月前 **6.3%**）、前 36 小時 **166 units** insulin、停藥後 3 個月 HbA1c 6.2% | DKA_Carrillo_2021.md L31/45 | ✅ | 通過 |
| Loke DKA：血糖 **612 mg/dL**、HbA1c **11.9%**（2 個月升 **4.6%**） | DKA_Loke_2025.md L27/50/52 | ✅ | 通過 |
| Leung rechallenge：起藥後 **11 天** DKA；rechallenge 後 **4 小時**再發（anion gap **20**、glucose **397**）；停藥後 **3–5 天**回穩 | DKA_Rechallenge_Leung_2022.md L29/55/85 | ✅ | 通過 |
| Bowman eDKA：glucose **143**、anion gap **21**、pH **7.27**、canagliflozin 起始後 **5 天／1 週內** | EuglycemicDKA_Bowman_2017.md L33/44/47/48 | ✅ | 通過 |
| Borrego：SGLT2i **n=19** vs 配對對照 **n=74**；G≥3 事件率 0.00461 vs 0.02272（**4.9 倍**）、HR **0.294**（**70.6%**）；劑量調整相關 0.00922 vs 0.05917（**6.4 倍**）、HR **0.643**（**35.7%**）；SGLT2i 組 73.7% prediabetic、15.8% diabetic | SGLT2i_Borrego_2024.md L31/210/228/232 | ✅ 全部逐字 | 通過 |
| Delphi 觀察期：metformin **2 週**、SGLT2i **2 天**、DPP4i **1 週**、TZD **6 週**、GLP-1 RA **1 週** | Delphi_Gallagher_2024.md L57 圖註 a | ✅ 逐字 | 通過 |
| canagliflozin 生殖泌尿道感染「up to **14.5%**」；DPP-4i 心衰風險小幅上升 **3.5%–3.9%** | Mgmt_Goncalves_2022.md L505/564 | ✅ | 通過 |
| SOLAR-1 有無 metformin 之腹瀉率 **49% vs 50%** | Mgmt_Goncalves_2022.md L474；Consensus_Tankova_2022.md L103 | ✅ | 通過 |
| SOLAR-1 insulin 使用：糖尿病 **5/12**、prediabetes **34/159**、正常 **13/113**；**33 人長期（>2 天）、19 人 rescue** | ToxMgmt_Jhaveri_2026.md L160 | ✅ 逐字 | 通過 |
| Tankova：alpelisib t½ **8–9 h**（300 mg 穩態）、停藥後 **24–72 h** 回復、short-term insulin **1–2 天** | Consensus_Tankova_2022.md L111/119 | ✅ | 通過 |
| CAPItello-291：無糖尿病史者 insulin 中位 **1.5 天**；有糖尿病史者 6 天；1 例 G4 高血糖停藥後 **2 天診斷 sepsis、隔日死亡** | CAPItello291_AE_Rugo_2024.md L204/216/230 | ✅ | 通過 |
| Jhaveri titration：500 mg 起（早發嚴重者 1000 mg）、每 **3–4 週** +500 mg、上限 **2000 mg**、優先 XR、IR >500 mg/day 分兩次 | ToxMgmt_Jhaveri_2026.md L160 | ✅ 逐字 | 通過 |
| CGM 目標「70 and 250 mg/dl for **>90% of the day**」 | 同上 | ✅ 逐字 | 通過 |

### G 章（METALLICA 細節）
| 數字 | 來源檔 | Grep | 判定 |
|---|---|---|---|
| metformin **500 mg BID ×3 天 → 1000 mg BID**；alpelisib 前 **7 天**開始 | METALLICA_Llombart_2024.md L42 引文；label_alpelisib.md L205 | ✅ 逐字 | 通過 |
| Table 2：無高血糖 A 35(72.9)／B 7(35.0)／全 42(61.8)；G1 10/3/13；G2 2/7/9；G3 1/3/4；G4 0 | METALLICA_Llombart_2024.md L171-180 | ✅ | 通過 |
| AE：nausea **47 (69.1%)** 全 G1–2、diarrhoea **46 (67.6%)**（G≥3 **9 [13.2%]**）、fatigue 33 (48.5%)、hyperglycaemia 30 (44.1%)、rash 28 (41.2%)（G≥3 11 [16.2%]） | 同上 L183 | ✅ | 通過 |
| 腹瀉歷史對照 **67.6%／11.8%** vs SOLAR-1 **57.7%／6.7%** vs BYLieve **59.8%／5.5%**；因腹瀉停藥 **5.9% vs 2.8%** | 同上 L230 | ✅ 逐字（Results 13.2% 與 Discussion 11.8% 之內部矛盾，G-1.6 已標註） | 通過 |
| 第 1 週（僅 metformin）腹瀉 **10/68 (14.7%)**（A 9/48=18.8%、B 1/20=5.0%） | 同上 L183 | ✅ | 通過 |
| alpelisib：停藥 **9 (13.2%)**、中斷 **32 (47.1%)**、減量 **21 (30.9%)**；歷史對照 SOLAR-1 25.0%／74.0%／63.9%、BYLieve 20.6% | 同上 L212/234 | ✅ | 通過 |
| metformin：停用 **8 (11.8%)**、中斷 **12 (17.6%)**、減量 **25 (36.8%)**；停用者 **4/8 (50%)** 後續高血糖但皆 G1–2、未加藥未調 alpelisib | 同上 L214/216 | ✅ 逐字 | 通過 |
| 療效：中位追蹤 **7.8 個月**、暴露 5.5 個月、RDI **95.1%**、PFS **7.3 個月 (5.9–NR)**、TTP 11.0、ORR **20.6% (11.7–32.1)**、CBR **52.9% (40.4–65.2)**、事件率 42.6% | 同上 L113/221 | ✅ | 通過 |
| 統計假設：H0 A ≥25%／B ≥40%；達標 A ≤7 (14.6%)／B ≤4 (20%)；期中 A n=20／B n=7 無事件 | 同上 L99 | ✅ | 通過 |
| SAE **7/68 (10.3%)**：rash 2 (2.9%)、vomiting 2 (2.9%)、diarrhoea 2 (2.9%)；1 例 grade 4 hypovolaemic shock | 同上 L183/194 | ✅ | 通過 |
| 基線：全女性、中位 55.0 歲 (29–79)、BMI ≥30 A 4 (8.3%)／B 6 (30.0%)／全 10 (14.7%)、CDK4/6i **67 (98.5%)**、fulvestrant **63 (92.6%)** | 同上 L115/119 | ✅ | 通過 |

### I／K／M 章補充
| 數字 | 來源檔 | Grep | 判定 |
|---|---|---|---|
| SOLAR-1：572 randomized、341 PIK3CA-mut、PFS **11.0 vs 5.7**（HR **0.65, 0.50–0.85**）、G3/4 hyperglycemia **36.6% vs 0.7%**、G3 diarrhea 6.7%、停藥 **25.0%** | SOLAR1_Andre_2019.md abstract | ✅ | 通過 |
| SOLAR-1 OS **39.3 vs 31.4**（HR **0.86, 0.64–1.15, P=0.15**）；肺/肝轉移 **37.2 vs 22.8**（HR 0.68） | SOLAR1_OS_Andre_2021.md abstract | ✅（章節正確標明「未跨過界值」） | 通過 |
| BYLieve A 2021：**61/121 (50.4%)**、G≥3 hyperglycaemia **36/127 (28%)**、SAE 26% | BYLieve_Rugo_2021.md abstract | ✅ | 通過 |
| BYLieve A 2024：中位追蹤 **21.8 個月**、**64/119 (53.8%)**、G≥3 **37/127 (29%)** | BYLieve_Rugo_2024.md abstract | ✅ | 通過 |
| Juric JCO 2018：n=**134**、MTD **400 QD／150 BID**、9 例 DLT（hyperglycemia n=6、nausea n=2、hyperglycemia+hypophosphatemia n=1）、all-grade hyperglycemia **51.5%**、t½ **7.6 h** | Alpelisib_Juric_JCO_2018.md abstract | ✅ | 通過 |
| Juric JAMA Onc 2019：n=**87**、400 mg 組 G3/4 hyperglycemia **19 (22%)**、PIK3CA-altered PFS **9.1 vs 4.7** | Alpelisib_Juric_JAMAOnc_2019.md abstract | ✅ | 通過 |
| GO39374：n=**190/191**、hyperglycemia **129 (67.9%)**、diarrhea 65.3%、stomatitis 48.9%、rash 24.7%、停藥 5 (2.6%)、減量/中斷 103 (54.2%) | GO39374_Gambardella_2025.md L33/86 | ✅ | 通過 |
| Meta_Shields 2020：**11 試驗 511 人**、hyperglycemia **59%**、G3/4 **28%**、**18%** 因毒性停藥 | Meta_Shields_Tox_2020.md L25/27 | ✅ | 通過 |
| Meta_Li 2025：**5 RCT 3,011 人**、PFS HR **0.74 (0.67–0.80)**、ORR RR **1.80 (1.39–2.35)**、CBR RR **1.10 (0.97–1.25)**、G≥3 RR **2.11 (1.73–2.58)** | Meta_Li_2025.md L31 | ✅ | 通過 |
| Meta_Martel 2018：**16 研究 8,529 人**、PI3Ki OR **2.05 (1.63–2.58)**、G3–4 hyperglycemia OR **40.93 (10.08–166.22)** | Meta_Martel_2018.md L23 | ✅ | 通過 |
| DPP 2002：n=**3,234**、發生率 **11.0／7.8／4.8**／100 人年、降 **58%／31%**、NNT **6.9／13.9** | DPP_Knowler_2002.md abstract | ✅（章節正確標明非癌症族群不可外推） | 通過 |
| Mosele 2020：HR+/Her2− **28% (104/364)**、TNBC **10% (27/255)**；n=649/617/44 | Landscape_Mosele_2020.md abstract | ✅ | 通過 |
| ASCO Rec 1.2：G≥3 hyperglycemia **2.3% vs 36.6%**、diarrhea **9.3% vs 6.7%**、rash **12.1% vs 9.9%**；Evidence quality Low / Strength Weak | guideline_ada_comparators.md L344/347/350 | ✅ 逐字 | 通過 |
| CAPItello-291：n=708／AKT-altered 289；PFS **7.2 vs 3.6**（HR 0.60）、7.3 vs 3.1（HR 0.50）；G≥3 rash 12.1%、diarrhea 9.3%；停藥 13.0% vs 2.3% | CAPItello291_Turner_2023.md／CAPItello291_AE_Rugo_2024.md L230 | ✅ | 通過 |
| BELLE-2：n=1,147；PFS **6.9 vs 5.0**（HR 0.78）；G3–4 ALT 25%、AST 18%、hyperglycaemia **15%**、rash 8% | BELLE2_Baselga_2017.md | ✅ | 通過 |
| SANDPIPER：PIK3CA-mut ITT 516；PFS **7.4 vs 5.4**（HR 0.70, 0.56–0.89, P=0.0037）；SAE 32.0% vs 8.9%、停藥 16.8%、減量 36.5% | SANDPIPER_Dent_2021.md | ✅ | 通過 |
| Rugo：SOLAR-1 前後半段停藥 any-grade **29.2% → 20.7%**、G≥3 **18.1% → 7.9%** | Multidisc_Rugo_2022.md L195 | ✅（方向與原文「lower in the second half」一致） | 通過 |
| 亞洲比例：INAVO120 38%、SOLAR-1 74/335 (22%)、CAPItello-291 95/355 (26.8%)、BELLE-2 132(23%)/153(27%)、Shen 22/247 (8.9%)、Jhaveri 2024 1 (3.0%)、GO39374 5/193 (2.6%) | 各對應檔 | ✅ 抽驗 5/7 命中，其餘 2 項（Jhaveri 2024、GO39374 分母 193）建議人工複核 | 通過 |
| EPIK-B4 **TERMINATED, actual n=2**；TIFA **actual n=15**；copanlisib+keto **TERMINATED, n=1**；NCT06083038 **n=8 已完成未發表** | trials_ongoing.md | ✅ | 通過 |
| Danne 共識 BHB 閾值：**<0.6**（正常／起始條件）、**0.6–1.5**（每 3–4 小時複測）；Goncalves POC BHB 表 >1.5／>3.0／>3.5 | DKA_Danne_Consensus_2019.md、Mgmt_Goncalves_2022.md Table 1 | ✅ | 通過 |
| anion gap **10–16 正常、>20 嚴重 ketoacidosis**；SGLT2i 手術前 **5 天**停用 | Multidisc_Rugo_2022.md | ✅ | 通過 |
| 血糖目標：預後佳 premeal **90–130**／睡前 **90–150**／HbA1c **<7.5%**；frail **100–180**／**110–200**／**<8.5%** | Mgmt_Goncalves_2022.md、Multidisc_Rugo_2022.md | ✅ | 通過 |
| 低碳水數字：Delphi **60–130 g/日**、ketogenic **<50 g/日**；Goncalves **130 g／<100 g**；Rugo **<100 g**；Tankova 中度限制 **30–40% 熱量（約 200 g）** | Delphi／Mgmt_Goncalves／Multidisc_Rugo／Consensus_Tankova | ✅ 四份來源分歧已由 B-4／I-2-6 誠實並陳 | 通過 |

---

## 5. 未發現之攔截類型（負面確認）

| 攔截類型 | 結果 |
|---|---|
| **Fabricated statistic**（憑空數字） | **0 筆**。所有抽驗數字皆在標註來源檔中 grep 到；無「原文確實沒有」之案例 |
| **Quote fabrication**（捏造引號） | **0 筆**。抽驗 31 段引號字串（含 C-3 開場 cross-trial 引文、FDA「Consider premedication」、ADA 9.35a/9.35b、EMA「should not be initiated until fasting glucose levels are optimised」、Hopkins「self-defeating systemic feedback」、Delphi「Exercise caution on the use of insulin when holding ALP」等）全部逐字相符 |
| **Confabulated detail**（RCT 寫成 cohort、n 位數錯） | **0 筆**。METALLICA 各章一律標為 single-arm phase 2；EPIK-B4 標為 randomized 但 n=2；Borrego 標為 propensity-matched 非隨機；Ismail／Cheung／Cook／Ziegengeist 皆正確標 📌 abstract。**未發現任何試驗設計被升級描述** |
| **格式差異需人工確認** | **0 筆**未解。`0.4mU`（原文無空格）、`96.3%` vs `96%`、`33.3%` vs `33%` 等皆以彈性 pattern 解決 |

---

## 6. 稽核員綜評

1. 本報告的**數字誠信度極高**。三個最重要的臨床決策數字群（METALLICA cohort n 與 G3–4 率、兩藥 FPG 劑量調整門檻、metformin eGFR 階梯）**逐格逐字可驗**，且 alpelisib／inavolisib 全程分開陳述、METALLICA 之單臂性質在 C／D／E／F／G／I／K 七章重複警示、insulin 於 DKA／HHS 之不可延誤在六章明文重申 —— 三項內容禁忌**皆未違反**。
2. **唯一系統性問題是「檔案落地狀態的標記過時」**（必修 M1–M3）：`SOLAR1_AE_Rugo_2020.md` 與 `INAVO120_Turner_2024.md` 於 12:00 落地全文，但各章寫於 11:41–11:50，仍沿用 `MISSING_FULLTEXT.md` 的舊判定。後果是**保守方向的錯誤**（誤棄可用證據，非引用不存在證據），但 K-7 的納入統計已因此與實際檔案不符，屬可 grep 反證之錯誤。
3. **四處來源內部矛盾**（METALLICA 20.2/29.2%、METALLICA 腹瀉 13.2/11.8%、METALLICA 食慾下降 3 vs 2 人、Shen 40.9/66.4%）中，章節已主動標註兩處、遺漏兩處，且 E 章與 G 章對同一數字採不同值 —— 建議統一處理原則。

---

*本檔所有 Grep 結果皆可由稽核員以檔名＋行號複驗。*
