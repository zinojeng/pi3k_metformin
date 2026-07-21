# 全文事實擷取：MSKCC 真實世界世代（Shen S, et al. Cancer 2023;129:3854-3861）

- 來源檔：`原始PDF/MSKCC_RealWorld_Shen_2023.md` 📄（全文可 grep）
- PMID 37743730｜DOI 10.1002/cncr.34928（見檔頭 metadata 行與 "How to cite this article" 段）
- 藥物：**alpelisib**（PI3Kα inhibitor）單一藥物之真實世界資料；**不涵蓋 inavolisib**
- 證據等級：【L4】回溯性單中心世代研究
- 擷取日期：2026-07-21

> **標記說明**：以下每一項「事實」後方的 blockquote 為原文逐字英文句子，供稽核 grep 回原檔。

---

## 1. 世代描述

**事實**
- 研究型態：retrospective cohort，**單中心**（Memorial Sloan Kettering Cancer Center, MSKCC）
- 收案期間：**2013 年 1 月 1 日至 2021 年 10 月 15 日**
- 納入人數：**n = 247**（metastatic breast cancer，實際接受 alpelisib）
- 分組：standard care **147 人（59.5%）**；clinical trial **100 人（40.5%）**
- 基線 BMI 中位數：**25.4 kg/m²**（IQR 22.6–29.0）；standard care 25.9 vs clinical trial 24.7（p = .08，Table 1）
- 基線 HbA1c 中位數：**5.5%**（IQR 5.1–5.9）；standard care 5.5 vs clinical trial 5.3（p = .007，Table 1）
- 資料可得率：BMI **235 人（95.1%）**、HbA1c **僅 164 人（66.4%）**（→ HbA1c 分析分母非全 247 人）
- 治療中 BMI 變化中位數 **−1.30 kg/m²（−5.5% of initial BMI）**（IQR −0.33 至 −3.0），兩組無差異（p = .2）
- Alpelisib 中位治療天數 113 天（range 11–1142）
- Alpelisib 中位 RDI：standard care **277 mg/day（92% of intended dose）** vs clinical trial **246 mg/day（99% of intended dose）**（p < .001）

**原文佐證**（Materials and Methods / Results，p.3855–3856；Table 1，p.3857）

> This is a retrospective cohort study of adult patients with metastatic breast cancer who received alpelisib (BYL-719) from January 1, 2013 to October 15, 2021 at MSKCC.

> A total of 247 patients were included in this study, 147 (59.5%) of whom were treated with alpelisib as standard care and 100 (40.5%) of whom were treated on a clinical trial.

> Among 247 patients, baseline median body mass index was 25.4 kg/m<sup>2</sup> and median hemoglobin A1c (HbA1c) was 5.5%.

> Baseline BMI and HbA1c data were available for 235 (95.1%) and 164 (66.4%) patients, respectively.

> Among all patients treated with alpelisib, median BMI change was $-1.30\text{ kg/m}^2$ ($-5.5\%$ of initial BMI) (interquartile range, $-0.33$ to $-3.0$); BMI change was not significantly different between the standard care and clinical trial cohorts ($p = .2$).

> Alpelisib median RDI was 277 mg daily (92% of intended dose) in the standard care cohort versus 246 mg daily (99% of intended dose) in the clinical trial cohort ($p < .001$ for both comparisons).

Table 1（p.3857）逐字欄位：
> | Baseline BMI (kg/m²) | | | | .08 |
> | Median (IQR) | 25.4 (22.6, 29.0) | 25.9 (22.8, 29.8) | 24.7 (22.3, 27.7) | |
> | HbA1c (%) | | | | .007 |
> | Median (IQR) | 5.5 (5.1, 5.9) | 5.5 (5.2, 6.0) | 5.3 (5.0, 5.7) | |
> | Median duration of alpelisib, days (range) | 113 (11–1142) | 135 (11–583) | 91 (11–1142) | .09 |

**單位注意**：血糖以 **mg/dL** 表示（hyperglycemia 定義門檻 glucose ≥140 mg/dL）；原文未使用 mmol/L。

---

## 2. 高血糖發生率與發生時間（全世代 n = 247，分母為納入之整體世代）

**事實**
- Any-grade hyperglycemia：**152 人（61.5%）**
- Grade 3–4：**72 人（29.2%）**（grade 3 **56 人 22.7%**、grade 4 **16 人 6.5%**）
- **中位發生時間：16 天**（time to onset 定義 = alpelisib 起始日至首次 glucose ≥140 mg/dL 之天數）
- 結論段另以「14–16 天內」描述高血糖發生之快速性

**原文佐證**（Abstract；Results p.3856；Clinical end points p.3855；Conclusion p.3860）

> A total of 152 patients (61.5%) developed any-grade hyperglycemia and 72 patients (29.2%) developed grade 3-4 hyperglycemia; median time to onset was 16 days.

> In the overall population, hyperglycemia of any grade occurred in 152 patients (61.5%); 56 patients (22.7%) developed grade 3 and 16 patients (6.5%) developed grade 4 hyperglycemia. The median time to onset of hyperglycemia was 16 days.

> Time to onset of hyperglycemia was defined as the number of days between alpelisib start date and first instance of glucose ≥140 mg/dL.

> ...given the rapidity of hyperglycemia onset within 14–16 days of alpelisib initiation during which time this risk factor is no longer meaningfully actionable.

分級依據：
> The highest glucose value and date following initiation of alpelisib that occurred during the treatment period was recorded and assigned hyperglycemia grade according to the Common Terminology Criteria for Adverse Events version 4.0.

---

## 3. 【核心】臨床試驗 vs 標準治療的發生率對比

**事實**

| 指標 | Standard care (n = 147) | Clinical trial (n = 100) | p |
|---|---|---|---|
| Any-grade hyperglycemia | **80.3%** | **34.0%** | **< .001** |
| Grade 3–4 hyperglycemia | **40.2%** | **13.0%** | **< .001** |
| Grade 1 | 15 人（10.2%） | 5 人（5.0%） | |
| Grade 2 | 45 人（30.6%） | 16 人（16.0%） | |
| Grade 3 | 43 人（29.3%） | 13 人（13.0%） | |
| Grade 4 | 16 人（10.9%） | **0 人** | |

- 敏感度分析（排除發生 DKA 之 standard care 病人與血糖最高 5%）後差異**仍顯著（p < .001）**
- 進一步敏感度分析：只比較 clinical trial 中接受**標準 300 mg/day** 之次族群（**n = 33**），差異仍顯著：**80% vs 52%，p < .001**
- 作者提出的差異解釋：(1) standard care 世代已知糖尿病比例較高，而試驗以 uncontrolled/insulin-dependent diabetes、fasting glucose/HbA1c cutoff 為排除條件；(2) phase 1/2 試驗使用低於 300 mg 之劑量（RDI 277 vs 246 mg/day）；(3) 試驗中血糖監測與處置較結構化、密集

**原文佐證**（Abstract；Results p.3856；Discussion p.3859；Figure 1 p.3858）

> A total of 100 patients (40.5%) received alpelisib on a clinical trial; rates of hyperglycemia were significantly higher in patients treated as standard care versus on a clinical trial (any-grade hyperglycemia 80.3% vs. 34.0%, grade 3-4 hyperglycemia 40.2% vs. 13.0%, $p < .001$).

> In the standard care cohort, the rate of any-grade hyperglycemia was 80.3%; 15 patients developed grade 1 hyperglycemia (10.2%), 45 developed grade 2 (30.6%), 43 developed grade 3 (29.3%), and 16 developed grade 4 (10.9%) (Figure 1). In the clinical trial cohort, the rate of any-grade hyperglycemia was 34.0%; 5 patients developed grade 1 (5.0%), 16 developed grade 2 (16.0%), 13 developed grade 3 (13.0%), and 0 developed grade 4 hyperglycemia.

> In a sensitivity analysis excluding patients who developed diabetic ketoacidosis and/or in the top 5% of blood glucose levels, the difference in hyperglycemia rate between standard care and clinical trial patients remained significant ($p < .001$), as did the association between baseline hemoglobin A1c and development of hyperglycemia ($p = .001$).

> To assess whether these differences in prescribed alpelisib dose contributed to the disparate hyperglycemia rates between cohorts, we performed a sensitivity analysis to compare hyperglycemia rates between the standard care cohort and the subgroup of patients in the clinical trial cohort that received the standard 300 mg daily dose ($n = 33$). The difference in hyperglycemia rates between cohorts remained significant (80% vs. 52%, $p < .001$).

> First, the proportion of patients with known diabetes was greater in our standard care cohort, whereas in our clinical trial cohort and in the SOLAR-1 population, uncontrolled or insulin-dependent diabetes and additional fasting glucose/HbA1c cutoffs were often used as exclusion criteria for study entry (Table 2).

> Finally, hyperglycemia monitoring and management were more structured and intensive in some clinical trial protocols versus clinical practice.

Figure 1 數據（p.3858，四捨五入版）：
> | Hyperglycemia grade | SOC | Protocol |
> | 1 | 10 | 5 |
> | 2 | 30.5 | 16 |
> | 3 | 29 | 13 |
> | 4 | 11 | 0 |

**基線異質性佐證**（可解釋兩組落差）：
> A greater proportion of patients in the standard care cohort had HbA1c measured at baseline (72.1% vs. 58.0%, $p = .021$) and a greater proportion had HbA1c in the prediabetes/diabetes range of $\ge 5.7\%$ (30.6% vs. 15.0%, $p = .041$) compared to the clinical trial cohort.

> Compared to the clinical trial cohort, a greater proportion of patients in the standard care cohort had overweight/obese range BMI (55.7% vs. 48.0%, $p = .09$).

（註：本段文字寫 BMI p = .09，Table 1 對應欄位寫 .08；原文兩處數值不一致，此處逐字保留兩者。）

---

## 4. 基線 HbA1c／BMI／glucose 與高血糖、與 alpelisib 減量／停藥的關聯

**事實 — 與高血糖發生之關聯（連續變項）**
- Baseline **BMI** p = **.029**
- Baseline **HbA1c** p **< .001**
- Baseline **glucose** p **< .001**

**類別變項**
- BMI ≥25 kg/m²：與 any-grade（p = **.036**）與 grade 3–4（p **< .001**）高血糖相關
- HbA1c ≥5.7%（prediabetes/diabetes 範圍）：與 any-grade（p **< .001**）與 grade 3–4（p **< .001**）高血糖相關
- **BMI 與 HbA1c 有顯著交互作用（p = .005）；兩者同入模型時，只有 baseline HbA1c 仍顯著（p < .001）** → HbA1c 為獨立預測因子

**事實 — 與 alpelisib 減量／停藥之關聯**
- BMI ≥25 kg/m²：p **< .001**
- HbA1c ≥5.7%：p = **.015**
- 內分泌科轉介：p **< .001**
- SGLT2 inhibitor 處方：p = **.007**

**原文佐證**（Results p.3856）

> Baseline BMI, baseline HbA1c, and baseline glucose levels were all significantly associated with development of hyperglycemia ($p = .029$, $p < .001$, and $p < .001$, respectively).

> When analyzed as categorical variables, baseline BMI $\ge 25\text{ kg/m}^2$ was associated with development of any-grade hyperglycemia and grade 3–4 hyperglycemia ($p = .036$ and $p < .001$, respectively), and baseline HbA1c $\ge 5.7\%$ was associated with development of any-grade hyperglycemia and grade 3–4 hyperglycemia ($p < .001$ and $p < .001$, respectively).

> There was a significant interaction between baseline BMI and HbA1c ($p = .005$); when both variables were included in the model for association with development of hyperglycemia, only baseline HbA1c remained significant ($p < .001$).

> BMI $\ge 25\text{ kg/m}^2$, HbA1c $\ge 5.7\%$, or referral to an endocrinologist were associated with alpelisib dose reduction/discontinuation ($p < .001$, $p = .015$, $p < .001$, respectively). Prescription of an SGLT2 inhibitor was also associated with alpelisib dose reduction/discontinuation ($p = .007$).

**統計方法（避免過度詮釋）**：主要為 **Pearson's χ² test**，非多變項 logistic regression；「交互作用」與「同入模型」之模型型態原文未進一步指明。
> Pearson's $\chi^2$ tests were used to investigate whether baseline characteristics were associated with development of hyperglycemia.

**HbA1c 定義門檻**：
> HbA1c was categorized per American Diabetes Association definitions: normal <5.7%, prediabetes 5.7%–6.4%, and diabetes ≥6.5%.

---

## 5. 降糖治療：接受比率、用藥組合、緩解時間

**事實**
- 分母 = 發生高血糖者 **n = 152**；接受降糖治療者 **101 人（66.4%）**
  - ⚠️ **原文內部不一致**：Abstract 寫「101 (40.9%)」（分母為 247），Results 寫「101 (66.4%)」（分母為 152）。兩者為同一 101 人，僅分母不同；引用時務必註明分母。
- 兩組使用降糖藥比率相近：standard care **68.6%** vs clinical trial **61.8%**（原文未報 p 值）
- 藥物數目（分母 101）：1 種 **69 人（68.3%）**；2 種 **23 人（22.8%）**；≥3 種 **9 人（8.9%）**
- 藥物種類（分母 101，接受降糖治療者）：
  - **Metformin 90 人（89.1%）**（單用或合併）— 最常用
  - SGLT2 inhibitor **20 人（19.8%）**
  - **Insulin 16 人（15.8%）**
  - DPP4 inhibitor **12 人（11.9%）**
  - Thiazolidinedione **8 人（7.9%）**
  - Sulfonylurea **6 人（5.9%）**
- 緩解時間（time to resolution 定義 = 首劑降糖藥至首次 glucose <140 mg/dL 之天數）
  - Metformin 單方：中位 **16 天**（IQR 7–26）
  - SGLT2i 單方僅 **3 人**，與 metformin 單方相比無顯著差異（p = .5）→ 本研究**無法**支持 SGLT2i 單方優於 metformin 之臨床結論
  - 首次介入用 metformin vs 其他藥物：無顯著差異（p = .7）
  - 需在 metformin 之外加藥者：中位 **26 天**（IQR 14–64），顯著長於 metformin 單方（p = **.024**）
- 與 SOLAR-1 比較：本世代任何降糖藥使用率 **66%**，低於 SOLAR-1 的 **87%**；需 ≥3 種藥與需 insulin 者亦較少

**原文佐證**（Results p.3856；Discussion p.3859）

> Among those who developed hyperglycemia ($n = 152$), 101 (66.4%) received anti-hyperglycemic treatment. Rate of anti-hyperglycemic agent use was similar between the standard care and clinical trial cohorts (68.6% vs. 61.8%).

> Overall, 69 patients (68.3%) required one anti-hyperglycemic agent, 23 (22.8%) required two anti-hyperglycemic agents, and nine (8.9%) required three or more anti-hyperglycemic agents.

> Among those who received hyperglycemia treatment, 90 (89.1%) patients received metformin either alone or in combination, 20 (19.8%) received a sodium glucose cotransporter 2 (SGLT2) inhibitor, 16 (15.8%) received insulin, 12 (11.9%) received a dipeptidyl-peptidase 4 (DPP4) inhibitor, eight (7.9%) received a thiazolidinedione, and six (5.9%) received a sulfonylurea.

> The median time to resolution of hyperglycemia with metformin monotherapy was 16 days (interquartile range, 7–26). Only three patients received SGLT2 inhibitor monotherapy, and there was no significant difference in time to resolution of hyperglycemia compared to metformin monotherapy ($p = .5$).

> For patients with persistent hyperglycemia, the median time to resolution of hyperglycemia if additional agents were combined with metformin was 26 days (interquartile range, 14–64), which was significantly longer compared to metformin monotherapy ($p = .024$).

> The use of any anti-hyperglycemic medication was less frequent in our cohort (66%) than in the SOLAR-1 trial (87%). Consistent with the alpelisib label, metformin was the most common intervention in our cohort and in SOLAR-1, although fewer patients in our cohort required 3 or more anti-hyperglycemic agents and fewer received insulin.

> Time to resolution of hyperglycemia was defined as the number of days between first anti-hyperglycemic agent start date and first instance of glucose <140 mg/dL.

---

## 6. 內分泌科轉介比率與 SGLT2i 之關聯

**事實**
- 全世代轉介內分泌科：**49 人（19.8%）**（分母 247）
- 依組別：standard care **30.0%** vs clinical trial **6.0%**，**p < .001**
- **內分泌科會診與 SGLT2 inhibitor 使用顯著相關（p = .007）**
- 內分泌科轉介亦與 alpelisib 減量／停藥相關（p < .001）
- 作者詮釋：內分泌會診與 metformin 之外加上 SGLT2i 屬**晚期介入**（針對持續性、較高等級高血糖），故與減量／停藥、較長緩解時間呈相關 → **屬時序性偏誤（confounding by indication），不可解讀為 SGLT2i 或會診「造成」減量**

**原文佐證**（Results p.3856；Discussion p.3859）

> In total, 49 patients (19.8%) were referred to an endocrinologist for further management, which varied by cohort (30.0% in the standard care cohort vs. 6.0% in the clinical trial cohort, $p < .001$). Endocrinology consultation was associated with use of an SGLT2 inhibitor ($p = .007$).

> Consultation with an endocrinologist and addition of an SGLT2 inhibitor to metformin were late interventions for persistent and higher-grade hyperglycemia, which likely accounts for the association of these management strategies with alpelisib dose reduction and/or discontinuation and longer time to resolution of hyperglycemia.

⚠️ **原文內部不一致**：Discussion 寫「nearly one-third of patients in our cohort consulted with an endocrinologist」，與 Results 的 19.8%（全世代）不符；19.8% 較接近 standard care 世代的 30.0%。引用時應採 Results 的 **49 人（19.8%）** 與分組 30.0% / 6.0%。
> Additionally, nearly one-third of patients in our cohort consulted with an endocrinologist, which was associated with use of an SGLT2 inhibitor.

---

## 7. Alpelisib 劑量調整（因高血糖）

**事實**
- 暫停用藥至高血糖緩解：**66 人（26.7%）**
- 減量：**42 人（17%）**
- 因高血糖停藥：**11 人（4.5%）**
- 分組：減量／停藥 standard care **43 人（29.3%）** vs clinical trial **10 人（10.0%）**，**p = .3**（原文所載 p 值；與百分比落差大，逐字保留，引用時宜註明）
- 對照：SOLAR-1 因高血糖停藥率 6.3%（原文引用文獻 6）

**原文佐證**（Results p.3856；Introduction p.3855）

> In 66 patients (26.7%), alpelisib was held until resolution of hyperglycemia; 42 patients (17%) required dose reductions, and 11 (4.5%) discontinued alpelisib due to hyperglycemia. Dose reduction/discontinuation due to hyperglycemia occurred in 43 patients (29.3%) in the standard care cohort versus 10 patients (10.0%) in the clinical trial cohort ($p = .3$).

> In the SOLAR-1 trial, 63.7% of alpelisib-treated patients experienced hyperglycemia of any grade and 36.6% experienced grade 3–4 hyperglycemia; the alpelisib discontinuation rate due to hyperglycemia was 6.3%.

---

## 8. 高血糖與療效（PFS）

**事實**
- 中位追蹤 **13.7 個月**；全世代中位 PFS **6.1 個月**（95% CI 4.8–7.3）
- 高血糖狀態（time-dependent covariate）與 PFS **無關**：HR **0.98**（95% CI 0.72–1.33）
- Standard care 中位 PFS 6.8 個月（95% CI 5.6–8.2）vs clinical trial 4.1 個月（95% CI 3.6–6.9），p = .06
- 以高血糖分級、BMI ≥25、HbA1c ≥5.7%、治療情境、是否因高血糖減量／停藥分層，PFS 均無顯著差異

**原文佐證**（Results p.3856–3857）

> At a median follow-up of 13.7 months, median PFS among all alpelisib-treated patients was 6.1 months (95% confidence interval [CI], 4.8–7.3) and did not differ significantly by hyperglycemia status (hazard ratio, 0.98; 95% CI, 0.72–1.33). Median PFS was 6.8 months (95% CI, 5.6–8.2) in the standard care cohort and 4.1 months (95% CI, 3.6–6.9) in the clinical trial cohort (*p* = .06).

> There were no significant differences in PFS by grade of hyperglycemia, nor by hyperglycemia status when stratified by BMI ≥25 kg/m<sup>2</sup> versus <25 kg/m<sup>2</sup>, HbA1c ≥5.7% versus <5.7%, treatment as standard care versus on trial, or alpelisib dose reduction/discontinuation due to hyperglycemia yes versus no.

---

## 9. 其他基線變項（Table 1，p.3857）

- 中位年齡 **62 歲**（IQR 54–68）；standard care 63 vs clinical trial 60，**p = .013**（此為**兩組基線差異**之 p 值，**非**年齡與高血糖之關聯）
- 女性 245 人（99.1%）
- 種族：White 198（80.1%）、Black 11（4.5%）、Asian 22（8.9%）、Other 16（6.5%），p = .2
- 基線 HbA1c 分層：<5.7% 104 人（42.1%）、5.7–6.4% 38 人（15.4%）、≥6.5% 22 人（8.9%）、Unknown 83 人（33.6%）
- 基線 BMI 分層：<25 105 人（44.7%）、25–29.9 82 人（34.9%）、≥30 48 人（20.4%）、Unknown 12 人（5.1%）
- 併用內分泌治療：fulvestrant 138（55.9%）、exemestane 41（16.6%）、letrozole 29（11.7%）、oral SERD 7（2.8%）、tamoxifen 3（1.2%）、無 26（10.5%）
- 中位既往治療線數 3 線（range 0–15）
- HER2-negative 214（86.6%）、HER2-positive 33（13.4%）

（表格逐字內容見第 1 節所引 Table 1 欄位；完整表格位於原檔 Table 1。）

---

## 10. 作者提出的臨床建議（原文結論，非本回顧推論）

- 主張**常規於 alpelisib 開始前測量 baseline HbA1c**，並在轉移性疾病診斷或第一線治療時即早測量，以爭取生活型態介入或早期內分泌科諮詢的時間窗
- 即使在 standard care 世代，也**僅 72% 有基線 HbA1c**
- 指出 metformin 的機轉限制（AMPK 活化被 PI3K 抑制所抵銷）與腸胃道副作用重疊，可能限制其使用與加量
- **insulin 仍為嚴重高血糖／酮酸中毒之適應症**，但在可能時應避免，因 hyperinsulinemia 可重新活化 PI3K 訊息
- 提及 TIFA 試驗（NCT05090358，ketogenic diet vs low-carbohydrate diet vs canagliflozin）與其他 4 項進行中試驗（Table 3：NCT04300790 metformin、NCT05025735 dapagliflozin、NCT05090358、NCT04330625 REMD-477）

**原文佐證**（Discussion p.3859）

> However, even among standard care patients, only 72% of patients had baseline HbA1c levels available. Based on our findings, we strongly advocate for incorporation of baseline HbA1c measurement into routine clinical practice for patients who are candidates for PI3K inhibitor treatment.

> The primary mechanism of metformin action is activation of AMP-activated protein kinase, which is abolished by PI3K inhibition, although there may be some clinical efficacy at high doses. Additionally, overlapping gastrointestinal adverse effects may limit metformin use and dose escalation with alpelisib.

> Finally, although insulin is still indicated for the management of severe hyperglycemia and/or ketoacidosis, it should be avoided when possible, as hyperinsulinemia can reactivate PI3K signaling despite use of a PI3K inhibitor.

---

## 11. 原文未報告 / 無法引用之項目

以下項目在本全文中**未報告**，不得以先驗知識補述：

1. **DKA 的實際發生人數與比率** — 原文僅提及敏感度分析「排除發生 DKA 的 standard care 病人」，**未給出 DKA 人數或百分比**。
   > A sensitivity analysis was performed by excluding standard care patients who developed diabetic ketoacidosis and the highest 5% of glucose levels.
2. **HHS（hyperosmolar hyperglycemic state）** — 全文未提及。
3. **類固醇（steroid / glucocorticoid）使用** — 全文未記錄、未分析其與高血糖之關聯。
4. **既有糖尿病（pre-existing diabetes）作為風險因子的正式統計分析** — 原文僅在 Discussion 敘述性提及 standard care 世代已知糖尿病比例較高（"the proportion of patients with known diabetes was greater in our standard care cohort"），**未提供人數、百分比或 p 值**；量化資料僅有 HbA1c ≥6.5% 之分層（22 人，8.9%）。
5. **年齡與高血糖發生之關聯分析** — 未報告；Table 1 的 p = .013 僅為兩組基線年齡差異。
6. **多變項迴歸（multivariable logistic regression）之 OR 與 95% CI** — 未報告，統計法為 Pearson's χ²。
7. **高血糖發生時間之 IQR 或範圍** — 僅報中位 16 天，未給離散度。
8. **各降糖藥（metformin 以外）之劑量、療程** — 未報告。
9. **腹瀉、體重下降、食慾不佳、脫水、腎功能變化等其他不良事件** — 全文**僅**報告 BMI 變化中位數 −1.30 kg/m²（−5.5%），**未報告**腹瀉、噁心、脫水、eGFR/腎功能資料；SGLT2i 使用者的 DKA 或泌尿生殖道感染風險亦未報告。
10. **血糖以 mmol/L 表示之數值** — 原文一律 mg/dL。
11. **依 BMI 或 HbA1c 分層之高血糖發生率（實際百分比）** — 僅報 p 值，未報各層發生率。
12. **inavolisib 相關資料** — 本研究完全不涵蓋 inavolisib（收案至 2021 年，僅 alpelisib/BYL-719）。

---

## 12. 引用注意事項（供撰稿者）

- 本研究為【L4】回溯性、單中心、非隨機；**standard care 與 clinical trial 兩組基線不可比**（年齡、HbA1c 分布、HER2 狀態、併用內分泌治療、alpelisib 劑量皆不同），組間差異**不可解讀為因果**。
- 「80.3% vs 34.0%」是本文最具政策意涵的數字，但需同時陳述試驗族群有 HbA1c／fasting glucose 排除條件（Table 2）與較低劑量，方屬公允。
- 兩處內部數字不一致已於第 5、6 節標註（101 之分母；endocrinology 轉介 19.8% vs "nearly one-third"）。
- 第 7 節 standard care 29.3% vs clinical trial 10.0% 之 p = .3 為原文所載，與百分比落差看似矛盾，逐字保留。
