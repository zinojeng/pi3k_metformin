# ClinicalTrials.gov 擷取稿：PI3Kα inhibitor 高血糖預防／處置相關試驗

- **擷取日期**：2026-07-21
- **擷取工具**：ClinicalTrials.gov REST API v2（`https://clinicaltrials.gov/api/v2/studies/{NCTId}?format=json`）
- **證據等級**：本檔全部內容為**試驗登錄資料（registry record）**。除非另註「已公布結果（results posted）」，否則登錄內容僅代表「計畫書所述設計」，**不等於已驗證之療效／安全性結論**。
  - 已公布結果者標【L2】📄（ClinicalTrials.gov Results Section 可 grep）
  - 僅有登錄計畫、無結果者標【L2-登錄】📌（**禁止對其結果作任何具體斷言**）
- **全文標記**：📄 = 本檔內含可 grep 之原文；📌 = 僅登錄摘要／無結果

> 稽核提示：本檔所有 `>` blockquote 段落均為 ClinicalTrials.gov 英文原文逐字引用，未經改寫。

---

## 0. 本次檢索策略與涵蓋範圍

檢索詞（`query.term`）：
`alpelisib AND hyperglycemia`、`alpelisib metformin`、`inavolisib`、`ketogenic diet PI3K inhibitor`、`PI3K inhibitor insulin feedback`、`SGLT2 inhibitor PI3K`、`capivasertib hyperglycemia`、`inavolisib hyperglycemia metformin`

**重要提醒（避免藥物混為一談）**：本檔明確區分
- **alpelisib（BYL719）**：非選擇性突變型 PI3Kα 抑制劑，300 mg QD
- **inavolisib（GDC-0077）**：PI3Kα 抑制劑併具突變型 p110α 降解作用，9 mg QD
- **capivasertib**：AKT 抑制劑（非 PI3Kα），僅在 NCT05455619 併列
- **copanlisib**：PI3Kα/δ 泛型抑制劑（IV），非 alpelisib 類
- **serabelisib、tersolisib(STX-478)**：研究中之 PI3Kα 抑制劑
上述藥物之高血糖發生率、機轉細節與處置策略**不可互相外推**。

---

# 第一部分：核心預防性研究

## 1. NCT04300790 — METALLICA【L2-登錄】📌（無 results posted）

**URL**：https://clinicaltrials.gov/study/NCT04300790
**API**：https://clinicaltrials.gov/api/v2/studies/NCT04300790?format=json

| 欄位 | 內容 |
|---|---|
| NCT | NCT04300790 |
| Acronym | METALLICA |
| Phase | Phase 2 |
| Study type | Interventional |
| Sponsor | MedSIR（collaborator: Novartis） |
| Status | **COMPLETED**（last update posted 2025-07-29） |
| Start | 2020-10-23；Primary completion 2022-06-15；Study completion 2025-03-16 |
| Enrollment | **69（actual）** |
| Results posted | **否（hasResults = False）** |

**官方標題（逐字）**：
> Study to Evaluate the Effect of Metformin in the Prevention of Hyperglycemia in HR[+]/HER2[-] PIK3CA-mutation Advanced Breast Cancer Patients Treated With Alpelisib Plus Endocrine Therapy. Study Metallica

### 1.1 Design（**非隨機對照；為三世代單組 Simon two-stage 設計**）

API `designInfo` 欄位：`allocation = RANDOMIZED`、`interventionModel = SINGLE_GROUP`、`masking = NONE`、`primaryPurpose = TREATMENT`。
**注意**：登錄檔中 allocation 欄位標記為 RANDOMIZED，但 `interventionModelDescription` 明確為 **single-group、three-cohort、Simon's two-stage**，且三個 cohort 全部為 `EXPERIMENTAL` arm、**無 control arm**。故本試驗**不可被描述為隨機對照試驗**，亦**不足以證明「所有病人都應預防性使用 metformin」**。

> This is a multicenter, open-label, three-cohort, Simon's two stage design, phase II clinical trial.
>
> Cohort A: Normal fasting glycemia \< 100 mg/dL and HbA1c \< 5,7: 48 patients (20 stage 1 + 28 stage 2). Patients in cohort A will receive.
>
> Cohort B: fasting glycemia 100 mg/dL (5.6 mmol/L) to 140mg/dL (7.8 mmol/L). 20 patients (7 stage 1 + 13 stage 2).
>
> Cohort C: T2DM diagnosed clinically ≥ 90 days prior to screening, HbA1c \< 7,5 %, insulin naïve (5 during stage I + 15 during stage II).

### 1.2 Cohort A/B/C 之基線血糖定義（收案條件原文）

> 13. For Cohort A and B only; Fasting plasma glucose (FPG) and glycosylated hemoglobin (HbA1c):
>
>     Cohort A: FPG ≤100 mg/dL (5.6 mmol/L) and HbA1c \< 5,7
>
>     Cohort B: FPG 100-140 mg/dL (5,6-7,8 mmol/L) (impaired fasting glucose values) or HbA1c 5,7-6,4%.
> 14. For Cohort C only:
>
>     * T2DM subjects diagnosed clinically ≥ 90 days prior to screening,
>     * HbA1c \< 7,5%.
>     * Stable diabetes treatment for 90 days prior to screening

另有全體共通之代謝門檻：
> * Fasting serum amylase ≤ 2 × ULN and fasting serum lipase below or equal to ULN.
> * FPG ≤ 140 mg/dL (7,7 mmol/L) and HbA1c ≤ 6,4% (both criteria must be met for Cohorts A and B only).

腎功能門檻：
> * Renal:
>   * Creatinine clearance ≥ 35 mL/min using Cockcroft-Gault formula.

### 1.3 Metformin 給法（**逐字，含完整 titration 步驟**）

> Metformin 500 mg BID with breakfast and dinner. After 3 days, if no GI intolerance, increase to 1000 mg BID with breakfast and dinner. If not tolerated, reduce to prior tolerated dose. Titrate to 1000mg BID over a period of at least 4 additional days.

Metformin titration 表（依上文拆解，逐列不省略）：

| 步驟 | 劑量 | 時機／條件 |
|---|---|---|
| 1 | Metformin 500 mg **BID**（早餐、晚餐時） | 起始 |
| 2 | 3 天後若**無 GI 不耐受** → 增至 1000 mg BID（早餐、晚餐時） | After 3 days |
| 3 | 若無法耐受 → **降回前一個可耐受劑量** | If not tolerated |
| 4 | 於**至少額外 4 天**期間逐步 titrate 至 1000 mg BID | over a period of at least 4 additional days |

**Lead-in（提前起始）時序 — 三個 cohort 不同**：

| Cohort | Lead-in 規定（原文） |
|---|---|
| A（normoglycemic） | > During the first cycle, patients will receive Endocrine Therapy and metformin **at least one-week prior alpelisib administration (D8)**. |
| B（pre-diabetic） | > During the first cycle, patients will receive Endocrine Therapy and metformin **at least one-week prior alpelisib administration (D8)**. |
| C（insulin-naïve T2DM） | > During the first cycle, patients will receive Endocrine Therapy, metformin and vildagliptin **at least two-weeks prior alpelisib administration (D15)**. |

另於 fulvestrant intervention 欄位補述：
> Patients should be started on metformin and fulvestrant within 7 to 14 days prior to start on alpelisib (D1C1)

### 1.4 各 Cohort 完整介入內容

**Cohort A（Normoglycemic patients）**
> Alpelisib (BYL719) 300 mg PO (two tablets of 150 mg once a day) on a continuous dosing schedule starting on Cycle 1.
> Metformin 500 mg BID ...（同上 titration）
> Endocrine Therapy: Fulvestrant 500 mg (intramuscular injection) on days 1 and 15 of cycle 1 (28 days); then every 4 weeks as per SoC- (day 1 of subsequent 28-days cycles) or Letrozole 2,5 mg, once daily, orally or Exemestane 25 mg once daily, orally.

**Cohort B（Pre-diabetic patients）**：藥物內容與 Cohort A 完全相同（alpelisib 300 mg QD + metformin titration + fulvestrant/letrozole/exemestane）。

**Cohort C（Insulin-naïve type 2 diabetes mellitus patients）**：在 A/B 基礎上**加上 vildagliptin**，且 endocrine therapy 多一個 tamoxifen 選項。
> Vildagliptin 50 mg tablets, twice daily, orally with breakfast and dinner
> ... or Tamoxifen 20 mg once daily, orally.

Cohort C 之抗糖尿病藥組合表：

| 藥物 | 劑量 | 給法 |
|---|---|---|
| Metformin | 500 mg BID → 1000 mg BID | 早、晚餐；titration 同 1.3 |
| Vildagliptin | 50 mg BID | 早、晚餐 |
| Alpelisib | 300 mg QD（150 mg × 2 錠） | 連續，28 天為一 cycle；D15 才開始 |

### 1.5 Primary endpoints（逐字）

> * Assess the rate of patients with G3-4 hyperglycemia (HG) by CTCAE v4.03 over the first 2 cycles of treatment with alpelisib (BYL719) (Cohorts A and B)
>   The primary objective is to assess the rate of patients with G3-4 (CTCAE v4.03) hyperglycemia (HG) over the first 2 cycles of treatment with alpelisib (BYL719) (300 mg/QD) plus endocrine therapy and metformin, in patients with normal fasting glycemia and HbA1c (cohort A), and in patients with high-risk criteria (cohort B).
>   Time frame: Baseline up tp 15 months

> * Assess the rate of patients with permanent discontinuation of alpelisib due to related AEs after 8 weeks of treatment with alpelisib plus endocrine therapy and antidiabetic treatment (Cohort C).
>   Time frame: Baseline up tp 15 months

### 1.6 Secondary endpoints（完整列出，含代謝相關者）

> * Clinical efficacy of alpelisib plus endocrine therapy, and antidiabetic treatment will be exploratory evaluated based on CTCAE V4.03 guidelines
> * Progression free survival [PFS]
> * Overall response rate [ORR]
> * Time to response [TTR]
> * Duration of the response [DoR]
> * Time to progression [TTP]
> * Clinical benefit rate [CBR]
> * Rate of any grade and grade 3-4 HG by CTCAE v.4.03 in Cohorts A, B, and C
> * Rate of patients with permanent treatment discontinuation at 8 weeks
> * Rate of patients with permanent treatment discontinuation in all cohorts
> * Rate of patients with permanent treatment discontinuation antidiabetic treatment), due to related AEs in all patients and all study cohorts
> * Rate of patients with grade 3-4 HG as per CTCAE v.4.03 over the first 8 weeks of treatment with alpelisib plus endocrine therapy and antidiabetic treatment and during the whole study
> * Rate of patients that requires insulin to control HG during the first 8 weeks and throughout study
> * Type of HG in patients with grade 3-4 HG as per CTCAE v.4.03 and 5.0
> * The rate of any grade and grade 3-4 diarrhea by CTCAE v.4.03
> * Safety and tolerability of the combination of alpelisib with endocrine therapy, and antidiabetic treatment
> * AEs according to the different endocrine agent received as per CTCAE v.4.03

（所有 secondary outcome 之 time frame 皆為 "Baseline up to 15 months"）

### 1.7 與臨床安全直接相關之排除條件（原文）

全體排除：
> 3. Patients treated with insulin.
> 4. Cohort A and B; Established diagnosis of type 1 or 2 diabetes mellitus (DM) requiring anti-diabetic drugs. Patients with an impaired FPG or HbA1c as per inclusion criterion #14 are eligible to enter the cohort B if no anti-diabetic drug were received in the last 14 days prior to the start of study treatment.

Cohort C 專屬排除（**代謝科醫師須特別注意：此為本試驗結論不可外推之族群**）：
> 5. Cohort C;
>    * Type 1 diabetes patients.
>    * Renal impairment defined as eGFR \< 25 mL/min/1.73 m2 as per CKD-EPI.
>    * History of proliferative retinopathy or maculopathy requiring acute treatment.
>    * History of pancreatitis (acute or chronic).
>    * Severe neuropathy, in particular autonomic neuropathy, i.e. gastroparesis, as judged by the investigator.
>    * History of ketoacidosis or hyperosmolar state episodes.
>    * History of intolerance to antidiabetic drugs except metformin.

其他與腸胃／脫水相關之排除：
> 9. Impaired gastrointestinal (GI) function or GI disease that may affect the absorption of study drugs (e.g., ulcerative diseases, uncontrolled nausea, vomiting, diarrhea, malabsorption syndrome or small bowel resection) based on investigator's discretion.

> 12. Patients with renal failure

### 1.8 METALLICA 判讀限制（本檔明列，供後續章節引用）

1. 三個 cohort **皆無對照組**（全為 EXPERIMENTAL arm），為 Simon two-stage 單臂設計 → **只能提供單臂事件率，不能提供「metformin 相對於不用 metformin」之效果量**。
2. n = 69（actual），遠小於 SOLAR-1（n = 572）。
3. **無 results posted**；ClinicalTrials.gov 上查不到任何數值型結果 → 本檔**不對 METALLICA 之高血糖發生率作任何數字斷言**。
4. 已排除 insulin-treated、T1DM、eGFR < 25、有 DKA/HHS 病史、有胰臟炎病史、有嚴重自律神經病變（gastroparesis）者 → 這些族群**不在本試驗結論適用範圍內**。
5. Cohort C 之 vildagliptin 在台灣屬 DPP-4 inhibitor，須注意本試驗 Cohort C **僅收 insulin-naïve、HbA1c < 7.5%、治療穩定 ≥ 90 天者**。

---

## 2. NCT05090358 — TIFA（Targeting Insulin Feedback to Enhance Alpelisib）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT05090358

| 欄位 | 內容 |
|---|---|
| NCT | NCT05090358 |
| 官方標題 | Targeting Insulin Feedback to Enhance Alpelisib (TIFA): A Phase 2 Randomized Control Trial in Metastatic PIK3CA-mutant Hormone-Receptor Positive Breast Cancer |
| Phase | Phase 2 |
| Design | **Randomized, Parallel, Open-label（3 arms）** |
| Sponsor | Memorial Sloan Kettering Cancer Center |
| Status | **ACTIVE_NOT_RECRUITING**（last update 2025-10-27） |
| Start | 2021-10-08；Primary completion（預估）2026-10-08 |
| Enrollment | **15（actual）** ← 遠低於一般 phase 2 規模 |
| Results posted | 否 |

**三個介入 arm（原文）**：
> The purpose of this study to find out whether a very low carbohydrate diet (ketogenic diet), a low carbohydrate diet, or the study drug canagliflozin can prevent high blood sugar and may improve the effectiveness of cancer therapy in people who are receiving standard treatment with alpelisib and fulvestrant for their metastatic PIK3CA-mutant breast cancer.

| Arm | 介入內容（原文） |
|---|---|
| Ketogenic Diet | > Properly formulated meals will be provided to both diet groups for the first 12 weeks to facilitate compliance in women with metastatic breast cancer prescribed alpelisib. After 12 weeks, subjects on the two dietary arms will be given the option to cross-over to the other diet arm and continue the prescribed dietary formulation. The decision to cross over will be per patient preference. |
| Low Carbohydrate Diet | 同上（同一段 crossover 規定） |
| SGLT2i Therapy | > Canagliflozin is an inhibitor of SGLT2, the transporter responsible for reabsorbing the majority of glucose filtered by the kidney. **For the first week of canagliflozin dosing, the dose will be 100 mg. Starting week 2 and onward the dose will be 300 mg** and supplied by the site. |

背景治療：
> Alpelisib: The recommended dose of PIQRAY is 300 mg (two 150 mg film-coated tablets) taken orally, once daily, with food.
> Fulvestrant: The recommended dose is 500 mg ... on days 1, 15, 29 and once monthly thereafter.

**Primary endpoint（原文）**：
> Hyperglycemia-free rate for participants — To determine the grade 3/4 hyperglycemia-free rate at 12 weeks, as assessed by the NCI CTCAE v5.0 — Time frame: 12 weeks

**Secondary outcomes**：登錄檔中為空（無列出）。

**基線血糖條件**：登錄之 inclusion criteria **未設定血糖／HbA1c 門檻**（僅有 HR+/HER2-、PIK3CA mutation、ECOG 0-1、器官功能等）。本檔擷取範圍內未見血糖收案門檻。

**臨床判讀限制**：canagliflozin 為 SGLT2i，**具 euglycemic DKA 風險**；於癌症病人合併腹瀉、食慾不佳、脫水時風險更高。此點在本登錄檔中**未有對應之風險說明**，屬「本回顧未取得可驗證來源」。

---

## 3. NCT04899349 — EPIK-B4（dapagliflozin + metformin XR vs metformin XR）【L2】📄（**已公布結果**）

**URL**：https://clinicaltrials.gov/study/NCT04899349

| 欄位 | 內容 |
|---|---|
| NCT | NCT04899349 |
| Acronym | EPIK-B4 |
| Phase | Phase 2 |
| Design | **Randomized, Parallel, Open-label, Active-controlled；`primaryPurpose = PREVENTION`** ← 本檔中唯一登錄為「預防」目的之隨機試驗 |
| Sponsor | Novartis Pharmaceuticals |
| Status | **TERMINATED**（last update 2024-10-09） |
| Start | 2022-04-06；Primary completion / completion 2023-05-10 |
| Enrollment | 計畫約 66 人／組；**actual = 2** |
| Results posted | **是（hasResults = True）** |

**官方標題**：
> EPIK-B4: A Phase II, Multicenter, Randomized, Open-label, Active-controlled Study to Assess the Safety and Efficacy of Dapagliflozin + Metformin XR Versus Metformin XR During Treatment With Alpelisib (BYL719) in Combination With Fulvestrant in Participants With HR+, HER2-, Advanced Breast Cancer With a PIK3CA Mutation Following Progression on/After Endocrine-based Therapy

### 3.1 高風險族群定義（本檔中最完整的「alpelisib 嚴重高血糖風險因子」登錄定義）

> This was a multicenter, randomized, open-label, active-controlled trial, stratified by diabetic status at baseline (i.e., normal vs prediabetic/diabetic based on fasting plasma glucose (FPG) and/or Hemoglobin A1c (HbA1c) laboratory values). The study included only participants with **at least one baseline risk factor for the development of severe hyperglycemia** which were **diabetes (FPG ≥ 126 milligram (mg)/deciliter (dL) or ≥ 7.0 millimole (mmol)/liter (L) and/or HbA1c ≥ 6.5%), prediabetes (FPG ≥ 100 mg/dL to \< 126 mg/dL or 5.6 to \< 7.0 mmol/L and/or HbA1c 5.7 to \< 6.5%), obesity (body mass index [BMI] ≥ 30) and age (≥ 75 years)**.

風險因子表（逐列）：

| 風險因子 | 登錄定義 |
|---|---|
| Diabetes | FPG ≥ 126 mg/dL（≥ 7.0 mmol/L）**和／或** HbA1c ≥ 6.5% |
| Prediabetes | FPG ≥ 100 至 < 126 mg/dL（5.6 至 < 7.0 mmol/L）**和／或** HbA1c 5.7 至 < 6.5% |
| Obesity | BMI ≥ 30 |
| Age | ≥ 75 歲 |

### 3.2 兩組介入與劑量調整（逐列完整）

| Arm | 劑量（原文） |
|---|---|
| Alpelisib + Fulvestrant + **Dapagliflozin + Metformin XR** | > Participants also received a combination treatment of dapagliflozin+metformin XR (as a single tablet or as two separate tablets, at the discretion of the investigator) at a **starting dose of 5 mg dapagliflozin + 500 mg metformin XR orally once daily** which could be **titrated to a maximum dose of 10 mg dapagliflozin + 2000 mg metformin XR once daily**. |
| Alpelisib + Fulvestrant + **Metformin XR**（active comparator） | > Participants also received **metformin XR 500 mg orally once daily** which could be **titrated to a maximum dose of 2000 mg once daily**. |

Alpelisib 起始時序（**metformin 提前 7 天 lead-in**）：
> Alpelisib (tablets) administered at 300 mg orally once daily on a continuous dosing schedule **starting on Cycle 1 Day 8** in a 28 days cycle.
> Metformin XR (tablets) administered at a starting dose of 500 mg orally once daily on a continuous dosing schedule **starting on Cycle 1 Day 1** in a 28 days cycle. Dose titration from 500 mg once a day to 2000 mg once a day.

治療期長度：
> The planned duration of treatment with alpelisib and fulvestrant was 12 cycles (28 days in each cycle) or until disease progression, unacceptable toxicity, or discontinuation from study treatment for any other reason, whichever came first.

### 3.3 Primary endpoint（原文，含 grade ≥3 高血糖之數值定義）

> Number of Participants With Hyperglycemia Grade ≥ 3 Over the First Eight Weeks of Alpelisib Plus Fulvestrant Treatment — Number of participants with severe hyperglycemia over the first eight weeks of alpelisib plus fulvestrant treatment. **Severe hyperglycemia (Grade ≥ 3) is defined as any glucose laboratory values \> 250 milligram (mg)/ deciliter (dL) (\> 13.9 millimole (mmol)/ liter (L))** — Time frame: From Cycle 1 Day 8 to Cycle 3 Day 8 (first eight weeks of treatment with alpelisib). Cycle = 28 days.

Secondary：PFS（up to 7.4 months）、ORR（RECIST 1.1）、CBR、Number of Participants With Dose Modifications。

### 3.4 已公布結果（Results Section，逐字／數值）

- Outcome group OG000 = Alpelisib + Fulvestrant + Dapagliflozin + Metformin XR；OG001 = Alpelisib + Fulvestrant + Metformin XR
- Primary outcome「Number of Participants With Hyperglycemia Grade ≥ 3」：**僅 OG000 有數值 = 1**（OG001 無收案病人，無數值）
- Secondary PFS：OG000 = NA

**終止原因（whyStopped，逐字 — 對本回顧極重要）**：
> Study was early terminated due to slow recruitment and emerging data showing that **prophylactic use of metformin may prevent or reduce the incidence of all-grades alpelisib-related hyperglycemia**. The decision was not driven by safety concerns

**判讀限制**：n = 2（1 人可評估），**此試驗無法提供任何有效力的療效比較**。上述「終止原因」僅為 sponsor 於登錄檔中的敘述性理由，**不構成 metformin 預防效果之證據**。

---

## 4. NCT05025735 — Alpelisib + Fulvestrant + Dapagliflozin（單臂 pilot）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT05025735

| 欄位 | 內容 |
|---|---|
| Phase | Phase 2 |
| Design | **Single group, open-label pilot（無對照）** |
| Sponsor | Saint Luke's Health System |
| Status | **UNKNOWN**（last update 2021-10-19；預計 primary completion 2022-12） |
| Enrollment | 25（estimated；**無 actual**） |
| Results posted | 否 |

介入時序（**dapagliflozin 於 C1D3 才加入**）：
> Fulvestrant 500 mg intramuscular, Cycle 1, Day 1 and Day 15; Cycle 2 and beyond 500 mg Intramuscular Day 1.
> Alpelisib 300 mg by mouth, daily, continuously beginning on Cycle 1, Day 1.
> **Dapagliflozin 10 mg by mouth, daily, continuously beginning Cycle 1, Day 3.**

**Primary endpoint**：
> Incidence of all grade hyperglycemia as assessed by CTCAE v5.0 — Time frame: Through study completion, an average of 1 year.

**Secondary**：Grade 3/4 高血糖發生率（CTCAE v5.0）、ORR（RECIST 1.1）、PFS。

**基線條件**：ECOG 0-2；`Creatinine Clearance ≥ 35 mL/min`；未設血糖／HbA1c 門檻（於本次擷取之 inclusion criteria 節錄中未見）。

**登錄檔內之機轉敘述（原文；屬【L5】前臨床推論，非人體證據）**：
> Cantley and colleagues have shown in animal models that treatment with BYL-719(alpelisib) results in rapid increase in plasma glucose level and a compensatory increase in insulin.
> They went on to show that this rebound hyperinsulinemia was able to rescue KPC tumor allografts from BYL-719 inhibition as evidenced by increasing phosphorylation of downstream effectors in the PI3K pathway, pAKT and PS6. **Pretreatment of the mice with an SGLT-2 inhibitor decreased the hyperglycemia and hyperinsulinemia following treatment with BYL-719.** Importantly, the response of the KPC tumor allografts to treatment was concordant with reduction in insulin levels.3

同一登錄檔亦引用 SOLAR-1 數據（**此為該登錄檔作者之敘述，非 SOLAR-1 原始出版品**）：
> The SOLAR-1 study randomized patients with MBC progressing after aromatase inhibitor therapy patients had a PFS of 11 months with fulvestrant plus alpelisib versus 5.7 months with fulvestrant alone. Alpelisib was associated with a 65% incidence of hyperglycemia, including 37% Grade 3 or 4 hyperglycemia.

> ⚠️ 稽核註記：上列 11 / 5.7 個月與 65% / 37% 之數字**來自 NCT05025735 登錄檔的 detailed description 欄位**，非 SOLAR-1 之 results section。若正文要引用 SOLAR-1 之高血糖率，應以 SOLAR-1 自身之 results（見第 10 節）或原始論文為準。

---

## 5. NCT05753657 — Pioglitazone 治療 hyperinsulinemia／hyperglycemia（單臂 pilot）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT05753657

| 欄位 | 內容 |
|---|---|
| Phase | **Early Phase 1** |
| Design | Single group, open-label |
| Sponsor | Rambam Health Care Campus |
| Status | **RECRUITING**（last update 2023-03-03） |
| Start | 2022-12-25；Primary completion（預估）2026-12-31；Completion 2027-12-31 |
| Enrollment | 30（estimated） |
| Results posted | 否 |

> The goal of this study is to test whether monitoring insulin levels and using pioglitazone to treat hyperglycemia and hyperinsulinemia in patients treated with Alpelisib for metastatic breast cancer is feasible and safe, and to assess the rates of glycemic control, dose reductions and treatment discontinuation and the progression free survival of patients treated with this regimen.

研究目標（逐條原文）：
> 1. To assess the feasibility and safety of monitoring insulin levels alongside glucose levels and of directing antidiabetic treatment according to insulin and fasting glucose levels in patients treated with Alpelisib for metastatic breast cancer.
> 2. To assess the feasibility and safety of treatment with pioglitazone in these patients.
> 3. To assess the rate of severe (grade 3-4) hyperglycemia in patients treated according to this protocol.
> 4. To assess the rates of dose reductions and treatment discontinuation due to hyperglycemia in patients treated according to this protocol.
> 5. To assess the median progression free survival of patients treated according to this protocol

**Primary outcomes**：
> * Rate of severe (grade 3 and 4) hyperglycemia in patients enrolled in the study and in patients treated per protocol
> * Rate of all grade hyperglycemia in patients enrolled in the study and in patients treated per protocol
> * Progression free survival in patients enrolled in the study and in patients treated per protocol
（time frame 皆為 "through study completion, an average of 1 year"）

**基線血糖條件（原文）**：
> Exclusion Criteria:
> * Uncontrolled diabetes mellitus, **defined as HbA1c above 8%**
> * **Diabetes mellitus controlled by insulin**
> * Known allergy to pioglitazone

**注意**：本試驗**未列 pioglitazone 之具體劑量**於登錄檔 intervention 欄位（僅寫 `Pioglitazone: hyperinsulinemia and hyperglycemia`）→ 劑量資訊「本回顧未取得可驗證來源」。

---

## 6. NCT04330625 — GRIP-IT PILOT（glucagon receptor 抗體 REMD-477 / volagidemab）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT04330625

| 欄位 | 內容 |
|---|---|
| Phase | Phase 1 |
| Design | Single group, open-label |
| Sponsor | Duke University |
| Status | **TERMINATED**（last update 2022-11-08） |
| Start | 2020-11-13；completion 2021-05-05 |
| Enrollment | **1（actual）** |
| Results posted | 否 |

> REMD-477 (Volagidemab) is a human anti-glucagon receptor antibody. Its proposed mechanism of action in controlling hyperglycemia is by blocking glucagon receptor (GCGR) signaling. In this way, it increases hepatic glucose uptake, decreases hepatic glycogenolysis and gluconeogenesis, increases glycogen synthesis, and ultimately decreases blood glucose levels. This protocol will test the hypotheses that REMD-477 is safe and tolerable in patients with severe hyperglycemia on apelisib and prevent hyperglycemia associated with alpelisib in patients with advanced breast cancer who discontinue alpelisib due to severe hyperglycemia despite appropriate medical management.

介入：
> REMD-477 (human IgG2 anti-glucagon receptor antibody Volagidemab) will be administered as a **subcutaneous injection for four weekly doses**

**族群條件（本檔中唯一針對「已因高血糖停用 alpelisib」之族群）**：
> * Participant has experienced **grade 3 or 4 hyperglycemia during treatment with alpelisib (any cycle) despite standard of care measures (e.g metformin) leading to discontinuation of alpelisib.**
> * Established diagnosis of diabetes mellitus type 1 or uncontrolled type 2 diabetes (fasting plasma glucose level, \>140 mg per decilite[r]) — （排除條件）

**Primary endpoints**：Adverse Events、Serious Adverse Events（皆 28 days）。

**判讀限制**：n = 1、已終止、無結果公布 → **不可作任何療效或安全性斷言**。

---

## 7. NCT04073680 — Serabelisib + Canagliflozin（PI3Kα inhibitor + SGLT2i）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT04073680

| 欄位 | 內容 |
|---|---|
| Phase | Phase 1b/2 |
| Design | Single group（Part 1 dose escalation、Part 2 expansion cohorts） |
| Sponsor | Petra Pharma |
| Status | **UNKNOWN**（last update 2020-05-21） |
| Enrollment | 60（estimated） |
| Results posted | 否 |

> This study aims to test the hypothesis that **controlling the glucose/insulin feedback will enhance the efficacy of PI3K inhibition** in treating solid tumors. The treatment consists of serabelisib, a PI3K alpha isoform (PI3Kα) inhibitor, combined with the sodium-glucose cotransporter-2 (SGLT2) inhibitor canagliflozin.

劑量（逐列）：

| 項目 | 內容（原文） |
|---|---|
| Serabelisib Part 1 | > Cohort 1 = 600 mg; Cohort 2 = 900 mg; Cohort 3 = 1200 mg |
| Serabelisib 給法 | > Subjects will be dosed with Serabelisib on **3 consecutive days a week in a 28 day cycle** until tumor progression |
| Canagliflozin | > All subjects will be dosed with **300 mg canagliflozin** in combination with serabelisib |
| Part 2 cohorts | > Cohort 4 = PIK3CA-mutated breast cancer; Cohort 5 = PIK3CA-mutated Non breast cancer; Cohort 6 = KRAS mutated |

**基線血糖條件（排除條件原文）**：
> 4. Have diabetes mellitus requiring insulin therapy
> 5. Have diabetes mellitus requiring insulin secretagogue therapy
> 6. Have poorly controlled diabetes mellitus defined as glycosylated hemoglobin A1c (HbA1c) \>7.5%

**Primary outcomes**：Rate of Adverse Events、Rate of Laboratory Abnormalities、Dose confirmation、Tumor Assessments by RECIST。

---

## 8. NCT05455619 — Amelia-1（Evexomostat / SDX-7320 + alpelisib **或** capivasertib）【L2-登錄】📌（**進行中，RECRUITING**）

**URL**：https://clinicaltrials.gov/study/NCT05455619

| 欄位 | 內容 |
|---|---|
| Acronym | Amelia-1 |
| Phase | Phase 1b/2 |
| Design | Open-label, **parallel-arms pilot**（登錄之 interventionModel 為 SINGLE_GROUP、allocation = NA） |
| Sponsor | SynDevRx, Inc. |
| Status | **RECRUITING**（last update 2026-04-22） |
| Start | 2022-08-26；Primary completion（預估）2026-12；Completion 2027-03 |
| Enrollment | 52（estimated；「up to 52 patients **for each combination arm**」） |
| Results posted | 否 |

> This is a Phase 1b/2, open-label, parallel-arms pilot study in men and post-menopausal women with hormone receptor positive (HR+), HER2- advanced or metastatic breast cancer with an alteration in the PI3K pathway, including a mutation of the PIK3CA gene, PTEN loss, or AKT1 mutation, designed to determine the safety of evexomostat (SDX-7320) plus standard of care treatment alpelisib (BYL-719) or capivasertib and fulvestrant (each combined, the 'triplet therapy'), to measure the severity and number of hyperglycemic events, and to assess clinical, anti-tumor benefit of the triplet therapy.

目的（逐條）：
> * to characterize the safety of the triplet drug combination consisting of either alpelisib or capivasertib (per the treating oncologist's choice) and fulvestrant plus evexomostat,
> * to test whether evexomostat, when given in combination with either alpelisib or capivasertib and fulvestrant will reduce the number and severity of hyperglycemic events and/or reduce the number or dose of anti-diabetic medications needed to control the hyperglycemia **for metabolically normal patients and those deemed at risk for capivasertib and alpelisib-induced hyperglycemia (insulin resistance, as measured by HOMA-IR, baseline elevated HbA1c or well-controlled type 2 diabetes)**, and
> * to assess preliminary anti-tumor efficacy for each combination and changes in key biomarkers and quality of life in this patient population.

**Lead-in 設計（原文）**：
> The study will consist of a **14-day pre-treatment phase of evexomostat plus fulvestrant starting on C1D1 before adding either alpelisib or capivasertib on C1D15.**

**Evexomostat 劑量遞增表（逐列完整）**：

| 狀況 | 劑量 |
|---|---|
| 起始劑量 | 36 mg/m²（> one dose below the monotherapy MTD of 49 mg/m²） |
| 若前 6 位病人前兩個 cycle 無 ≥ 2 DLT | 可上調至 **49 mg/m²** |
| 若 ≥ 2 DLT | 可降至 **27 mg/m²**，並可調整 alpelisib 或 capivasertib 劑量 |
| Fulvestrant | > The dose of fulvestrant will not be adjusted. |
| 若 49 mg/m² 不可耐受 | > current and future patients for only their respective combination treatment will receive evexomostat at 36 mg/m² |

原文：
> The planned escalation scheme starts at an evexomostat dose of 36 mg/m2 (one dose below the monotherapy MTD of 49 mg/m2) in combination with either alpelisib or capivasertib and fulvestrant given at the marketed doses. Based on aggregate safety data from the first two cycles of the first 6 patients across each triplet combination, and in the absence of ≥ 2 dose-limiting toxicities (DLTs as defined herein), the Safety Review Committee (SRC), in consultation with the Sponsor and the Investigator(s), may increase the evexomostat dose for the next cohort to 49 mg/m2. In the presence of ≥2 DLTs, the SRC may decrease the evexomostat dose to 27 mg/m2 and may adjust the dose of either alpelisib or capivasertib if warranted. The dose of fulvestrant will not be adjusted. If the evexomostat dose of 49 mg/m2 is determined by the SRC not to be tolerable in combination with either alpelisib or capivasertib and fulvestrant, then current and future patients for only their respective combination treatment will receive evexomostat at 36 mg/m2.

**基線血糖收案門檻（原文；alpelisib 與 capivasertib 門檻不同 — 直接證明兩藥不可混為一談）**：
> 7. Patient has a Screening fasting plasma glucose (FPG) level **≤140 mg/dL (7.7 mmol/L)** and an **HbA1c ≤6.4% (47 mmol/mol) for those taking alpelisib**, or an **HbA1c \<8% (64 [mmol/mol]) [for those taking capivasertib]**

**Primary outcomes**：
> * Incidence of Adverse Events — Safety and tolerability profile will be assessed by Common Terminology Criteria for Adverse Events v5.0 ... (up to 48 months)
> * Hyperglycemic Events — Severity, number, and proportion of patients with hyperglycemic events (up to 42 months)

**Secondary outcomes**：Anti-tumor activity（6 months）、Glucose control、Leptin activity、Adiponectin activity、Angiogenic activity (bFGF/FGF2)、Angiogenic activity (VEGFC)、**Insulin resistance**（皆 up to 42 months）。

登錄檔中之機轉背景（原文，含其自引之文獻名）：
> However, hyperglycemia, a toxicity associated with PI3K and/or Akt inhibition, leads to hyperinsulinemia, re-activating the pathway and thereby limiting each drug's clinical efficacy. Management of hyperglycemia is important to ensure patients receive optimal anti-tumor therapy (Rugo 2020). Restoring insulin sensitivity and reducing levels of insulin have been suggested as ways to blunt the hyperglycemia associated with drugs that inhibit this pathway and have been reported to improve their efficacy (Hopkins 2018, Crouthamel 2009).

---

## 9. NCT04750941 — Copanlisib + Ketogenic Diet【L2】📄（**已 results posted**，但 n = 1）

**URL**：https://clinicaltrials.gov/study/NCT04750941

| 欄位 | 內容 |
|---|---|
| Phase | Phase 2（pilot） |
| Design | Non-randomized, parallel（兩個疾病別 cohort） |
| Sponsor | Columbia University |
| Status | **TERMINATED**（last update 2025-03-04） |
| Start | 2022-02-10；completion 2023-06-09 |
| Enrollment | 計畫 FL 23 人 + EC 19 人；**actual = 1** |
| Results posted | 是（hasResults = True） |

> This is a multicenter, open label, pilot phase II study of the PI3K inhibitor copanlisib in combination with a ketogenic diet in the treatment of patients with one of the following malignancies: (a) relapsed or refractory (R/R) follicular lymphoma (FL), (b) R/R endometrial cancer (EC) with a documented activating mutation in PIK3CA or loss of phosphatase and tensin homolog (PTEN).

> As the investigators recently reported ketogenic diet can suppress hyperinsulinemia associated with PI3K inhibitors, leading to potentiation of the anti-tumor effects of PI3K inhibitors.

**Ketogenic diet run-in 設計（原文，含合規性 gate）**：
> In cycle 1, patients will first start ketogenic diet for **7 days (Day -6 to Day 0)**. **Only patients who demonstrate compliance and tolerance with the ketogenic diet for all 7 days, as confirmed by pertinent blood and urine tests, will be allowed to continue the study** and treatment using copanlisib and the ketogenic diet starting on Day 1. In cycle 2 and beyond, patients will start the ketogenic diet and copanlisib on day 1.

Copanlisib 給法：
> Copanlisib will be infused intravenously on **days 1, 8, 15 of each cycle, over 1 hour, of 28-day cycles.**

**Primary endpoint**：ORR（CR + PR）；Secondary：CR rate、PR rate、ORR at Simon Stage I、**Patient Compliance With the Ketogenic Diet**。

**重要區隔**：copanlisib 為**靜脈注射之 PI3Kα/δ 抑制劑**，其高血糖型態（typically 輸注後短暫高血糖）與口服每日連續給藥之 alpelisib **不同**，本試驗結果**不可外推至 alpelisib 或 inavolisib**。且 n = 1，無任何可用結論。

---

## 10. 連續血糖監測（CGM）相關研究

### 10.1 NCT06083038 — CGM characterize/manage hyperglycemia（觀察性）【L4】📌

**URL**：https://clinicaltrials.gov/study/NCT06083038

| 欄位 | 內容 |
|---|---|
| Study type | **OBSERVATIONAL**（cohort、prospective）；無 phase |
| Sponsor | HealthPartners Institute |
| Status | **COMPLETED**（last update 2026-05-06） |
| Start | 2023-10-05；Primary completion 2025-01-13；Completion 2026-04-21 |
| Enrollment | **8（actual）** |
| Results posted | 否 |

> This is a prospective, descriptive, single site, observational study in subjects receiving alpelisib for treatment of metastatic breast cancer. The purpose of the study is to characterize the impact of alpelisib on glucose control in patients with breast cancer using continuous glucose monitoring to measure glucose levels throughout the day and night. **Patients will follow a hyperglycemia prevention and management regimen aimed to diminish hyperglycemia known to occur in most oncology patients starting alpelisib.**
>
> All patients will wear an **Abbott FreeStyle Libre 2** system to obtain continuous glucose monitor (CGM) data (glucose measured every minute for 14 days). **CGM will be placed at least 10 days prior to starting alpelisib and continue for at least 3 months** while taking alpelisib.

**Primary outcome（原文）**：
> Time to peak glucose level following the administration of alpelisib — Time (hr., min.) from taking alpelisib to the peak of the median glucose line of the standardize AGP/CGM report from **day 21-28 after start of alpelisib**. (calculated as- the average time to peak glucose on 7-day AGP profile minus avg time taking alpelisib). Primary outcome is time to peak glucose for all patients on alpelisib combined — Time frame: Up to 28 days after start of alpelisib

**排除條件（與 CGM 判讀直接相關）**：
> 2. Known currently uncontrolled diabetes, defined as the most recent HbA1c over 10% or history of DKA within 6 months prior to enrollment.
> 3. **Concurrent use of high-dose vitamin C, defined as ≥ 1g of oral vitamin C daily, or intravenous Vitamin C infusions.**（此為 CGM 干擾因素）

**注意**：登錄檔未提供該「hyperglycemia prevention and management regimen」之具體內容 → **本回顧未取得可驗證來源**。

### 10.2 NCT05107388 — AAREN（CGM profile under alpelisib）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT05107388

| 欄位 | 內容 |
|---|---|
| Acronym | AAREN |
| Phase | N/A（interventional device study） |
| Design | Single group |
| Sponsor | Centre Hospitalier Universitaire de Besançon |
| Status | **UNKNOWN**（last update 2021-11-04）；預計 primary completion 2024-01 |
| Enrollment | 40（estimated） |
| Results posted | 否 |

> AAREN is a monocentric prospective study monitoring glycemic profile in patients treated with alpelisib plus fulvestrant. Patients will wear a noninvasive glucose monitoring sensor, the **Freestyle Libre Pro for a 14 day period**. Forty patients will be enrolled.

**Primary outcome 之高血糖操作型定義（逐列完整；本檔中最細緻的 CGM 高血糖定義）**：
> Incidence rate of hyperglycemia — In percentage, measured before breakfast and diner (fasting blood glucose).
> Hyperglycemia defined as follows:
> * if diabetes de novo:
>   * capillar or interstitial fasting blood glucose ≥ 1,50 g/L,
>   * OR postprandial interstitial glucose ≥ 2 g/L
>   * OR glucose monitoring indicator ≥ 6,5%
> * if worsening pre-existing diabetes:
>   * increased capillar or interstitial fasting blood glucose ≥ 0,50 g/L compared to average fasting blood glucose at J-3, J-2 and J-1
>   * AND postprandial interstitial glucose ≥ + 1,00 g/L compared to average fasting blood glucose at J-3, J-2 et J-1 OR average blood glucose ≥ +0,50 g/L
> Time frame: Day 14

換算對照（原文為 g/L）：1.50 g/L = 150 mg/dL；2 g/L = 200 mg/dL；0.50 g/L = 50 mg/dL；1.00 g/L = 100 mg/dL。

**收案條件**：僅收停經 ≥ 24 個月之女性；排除男性、孕婦及具生育能力女性。

### 10.3 NCT06354088 — Human Models of Selective Insulin Resistance: Alpelisib, Part I【L2-登錄】📌（**RECRUITING，非癌症族群**）

**URL**：https://clinicaltrials.gov/study/NCT06354088

| 欄位 | 內容 |
|---|---|
| Phase | Phase 1 |
| Design | **Randomized, CROSSOVER, double-masked（participant + investigator）；primaryPurpose = BASIC_SCIENCE** |
| Sponsor | Columbia University |
| Status | **RECRUITING**（last update 2026-04-09） |
| Start | 2024-04-24；Primary completion（預估）2026-12-31 |
| Enrollment | 32（estimated） |
| 族群 | **健康志願者（healthyVolunteers = True）**，非乳癌病人 |
| Results posted | 否 |

> The investigators plan to test whether the multifactorial IR in patients at risk of T2DM/MASLD is selective by determining if inducing a discrete, "pure" form of IR, via pharmacologic inhibition of phosphoinositide-3-kinase (PI3K) with alpelisib, versus placebo, attenuates excessive DNL.

介入：
> All participants will ingest **one dose of alpelisib 300 mg (2 x 150-mg overencapsulated tablets)** on one of two study admissions.
> All participants will ingest one dose of placebo (2 overencapuslated doses of microcrystalline cellulose) on one of two study admissions.
> [1-13C] sodium acetate ... continuous infusions ... for up to 23 hours ... in order to quantify de novo lipogenesis (DNL).
> [6,6-2H2] D-glucose ... continuous infusions ... for up to 15 hours ...
> Nestlé BOOST Plus: standardized mixed meals ... on Study Day 1 and then smaller portions hourly x 8 hours on Study Day 2

**分組之代謝定義（逐列完整）**：

| 組別 | BMI | 代謝定義（原文） |
|---|---|---|
| IS（insulin sensitive） | 18-25 kg/m² | > (1) Fasting serum insulin ≤ 10 µIU/mL, (2) Absence of dysglycemia (fasting plasma glucose \< 100 mg/dL and hemoglobin A1c \< 5.7%), (3) Homeostasis Model Assessment of Insulin Resistance (HOMA-IR) score \< 2.5, and (4) Fibrosis-4 (FIB-4) score \< 1.3 |
| IR（insulin resistant） | 30-45 kg/m² | > fasting serum insulin ≥ 13 µIU/mL plus at least one of the following: (1) Presence of prediabetic state (fasting plasma glucose 100-125 mg/dL and/or hemoglobin A1c 5.7-6.4%), and/or HOMA-IR ≥ 2.5 |

排除：
> * Laboratory evidence of diabetes mellitus: (1) Hemoglobin A1c ≥ 6.5%, and/or (2) Fasting plasma glucose ≥ 126 mg/dL

**Primary outcomes**：Hepatic de novo lipogenesis（絕對值 % 與相對值）、Endogenous glucose production（mg/kg/min 與相對值；> Calculated from D2G tracer enrichment by the Steele equations）。
**Secondary**：Serum insulin、Plasma glucose、Triglycerides、Free fatty acids、Glucose Ra／Rd。

Washout：
> There will be a **2-8-week hiatus for drug washout** between the two inpatient study admissions.

---

# 第二部分：關鍵註冊性試驗登錄資訊

## 11. NCT04191499 — INAVO120（inavolisib）【L2】📄（**已 results posted**）

**URL**：https://clinicaltrials.gov/study/NCT04191499

| 欄位 | 內容 |
|---|---|
| Acronym | INAVO120 |
| Phase | **Phase 2/3**（登錄 phases = PHASE2, PHASE3） |
| Design | **Randomized, Parallel, DOUBLE masking（participant + investigator）, placebo-controlled** |
| Sponsor | Hoffmann-La Roche |
| Status | **ACTIVE_NOT_RECRUITING**（last update 2026-06-15） |
| Start | 2020-01-29；Primary completion 2023-09-29；預計 completion 2027-11-15 |
| Enrollment | **325（actual）** |
| Results posted | **是（hasResults = True）** |

官方標題：
> A Phase III, Randomized, Double-Blind, Placebo-Controlled Study Evaluating the Efficacy and Safety of Inavolisib Plus Palbociclib and Fulvestrant Versus Placebo Plus Palbociclib and Fulvestrant in Patients With PIK3CA-Mutant, Hormone Receptor-Positive, HER2-Negative, Locally Advanced or Metastatic Breast Cancer

介入（**注意：inavolisib 於登錄之 intervention 欄位未載明 mg 數；INAVO120 之劑量數字本檔未取得**）：
> (DRUG) Inavolisib: Participants will receive oral inavolisib on Days 1-28 of each 28-day cycle.
> (DRUG) Palbociclib: Participants will receive oral palbociclib on Days 1-21 of each 28-day cycle.
> (DRUG) Fulvestrant: Participants will receive intramuscular (IM) fulvestrant approximately every 4 weeks.

> ⚠️ 9 mg QD 之 inavolisib 劑量在本檔中係由 **NCT05646862（INAVO121）** 登錄檔取得（見第 13 節），非 INAVO120 登錄檔。

Crossover 設計：
> Participants randomized to the placebo arm who are still deriving benefit from the study treatment will be given an optional opportunity to crossover to the inavolisib arm.

**Primary endpoint（原文，含 PD 定義）**：
> Progression-Free Survival (PFS) — PFS was defined as the time from randomization to the first occurrence of disease progression, as determined by the investigator according to Response Evaluation Criteria in Solid Tumors (RECIST), Version 1.1 or death from any cause (whichever occurs first). Progressive disease (PD) was defined as at least a 20% increase in the sum of diameters of target lesions ... The appearance of one or more new lesions was also considered progression. ... Median PFS was calculated using the Kaplan-Meier methodology. — Time frame: **Up to 3.7 years**

**與糖尿病照護直接相關之收案條件（原文）**：
> * **Type 2 diabetes requiring ongoing systemic treatment at the time of study entry; or any history of Type 1 diabetes**（排除）

→ 臨床意涵：**INAVO120 之族群不含需要藥物治療的 T2DM 病人**，故其高血糖數據**不可外推至已在使用降血糖藥的糖尿病病人**。

### 11.1 已公布結果中之高血糖不良事件（Results Section, Adverse Events Module）

| 事件 | Inavo+Palbo+Fulv（EG000） | Pbo+Palbo+Fulv（EG001） |
|---|---|---|
| Other (non-serious) adverse events — **Hyperglycaemia** | **87 / 162** | **12 / 162** |
| Serious adverse events — Hyperglycaemia | 未於 serious events 清單中列出 | 未列出 |
| Serious — DKA / Ketoacidosis / T2DM | 未於 serious events 清單中列出 | 未列出 |

（安全性分析人數：each group `numAtRisk = 162`）

---

## 12. NCT02437318 — SOLAR-1（alpelisib）【L2】📄（**已 results posted**）

**URL**：https://clinicaltrials.gov/study/NCT02437318

| 欄位 | 內容 |
|---|---|
| Acronym | SOLAR-1 |
| Phase | **Phase 3** |
| Design | **Randomized, Parallel, TRIPLE masking（participant + care provider + investigator）, placebo-controlled** |
| Sponsor | Novartis Pharmaceuticals |
| Status | **COMPLETED**（last update 2025-02-13） |
| Start | 2015-07-23；Primary completion 2018-06-12；Completion 2023-06-09 |
| Enrollment | **572（actual）** |
| Results posted | **是** |

設計原文：
> Subjects were allocated to either the PIK3CA mutant or PIK3CA non-mutant cohort, based on central testing of hotspot-mutations in tumor tissue. Subjects with unknown results were not eligible. Within each cohort, subjects were randomized in a **1:1 ratio** to receive either **alpelisib 300 mg orally once daily (q.d.)**, in combination with **fulvestrant 500 mg intramuscular (i.m.) on Days 1 and 15 of Cycle 1 and Day 1 of a 28-day cycle thereafter**, or placebo daily in combination with fulvestrant 500 mg following the same treatment regimen.

**Primary endpoint**：
> Progression-free Survival (PFS) Per Investigator Assessment in the PIK3CA Mutant Cohort — Time frame: Once approximately 243 PFS events in the PIK3CA mutant cohort had been observed, **up to 33.3 months**

**基線血糖相關之收案／排除（原文）**：
> * Patients had an established diagnosis of **diabetes mellitus type I or uncontrolled type II**（排除）

→ **注意**：SOLAR-1 並**未**排除「controlled type II diabetes」，這與 INAVO120（排除所有需系統性治療之 T2DM）**明顯不同**。兩試驗之高血糖數據因此不可直接互比。

### 12.1 已公布結果中之高血糖不良事件（Results Section, Adverse Events Module）

安全性分析人數：Alpelisib + Fulvestrant（EG000）**n = 284**；Placebo + Fulvestrant（EG001）**n = 287**

| 事件 | Alpelisib + Fulvestrant | Placebo + Fulvestrant |
|---|---|---|
| **Serious** — Hyperglycaemia | **28 / 284** | **0 / 287** |
| **Serious** — Diabetic ketoacidosis | **2 / 284** | **0 / 287** |
| **Serious** — Ketoacidosis | **1 / 284** | **0 / 287** |
| **Serious** — Type 2 diabetes mellitus | **1 / 284** | **0 / 287** |
| **Other (non-serious)** — Hyperglycaemia | **182 / 284** | **27 / 287** |

> ⚠️ 臨床重點：SOLAR-1 之 results section 明確記載 alpelisib 組出現 **DKA 2 例 + ketoacidosis 1 例**（安慰劑組 0 例）。此為「不可為了避免 hyperinsulinemia 而延誤嚴重高血糖／DKA 所需 insulin」之直接登錄證據。

---

## 13. NCT03056755 — BYLieve（alpelisib）【L2】📄（**已 results posted**）

**URL**：https://clinicaltrials.gov/study/NCT03056755

| 欄位 | 內容 |
|---|---|
| Acronym | BYLieve |
| Phase | **Phase 2** |
| Design | **NON_RANDOMIZED、Parallel、Open-label（masking = NONE）、three-cohort、non-comparative** |
| Sponsor | Novartis Pharmaceuticals |
| Status | **COMPLETED**（last update 2026-01-13） |
| Start | 2017-08-29；Primary completion 2021-06-14；Completion 2024-11-12 |
| Enrollment | **383（actual）**；Core Phase 分析 379 人（A 127 / B 126 / C 126）；Extension Phase 11 人（A 1 / C 10） |
| Results posted | **是** |

**Cohort 定義（依前線治療分組，原文）**：
> * **Cohort A**: alpelisib (300 mg oral QD) + fulvestrant (500 mg intramuscular (IM)) to subjects whose last prior treatment was a CDK4/6i plus any AI;
> * **Cohort B**: alpelisib (300 mg oral QD) + letrozole (2.5 mg oral QD) to subjects whose last prior treatment was a CDK4/6i plus fulvestrant;
> * **Cohort C**: alpelisib (300 mg oral QD) + fulvestrant (500 mg IM) to subjects who failed prior AI based therapy and whose last prior treatment was systemic chemotherapy or endocrine therapy (as monotherapy or in combination with targeted treatment except CDK 4/6i + AI).

其他介入：
> Goserelin: 3.6 mg ... subcutaneous implant administered every 28 days. Only for men in Cohort B and premenopausal women.
> Leuprolide: 7.5 mg ... intramuscular depot administered every 28 days. Only for men in cohort B and premenopausal women.

**Primary endpoint（原文）**：
> Core Phase: Percentage of Participants Who Were Alive Without Disease Progression at 6 Months — Percentage of participants who were alive without disease progression at 6-month follow-up based on local investigator assessment per RECIST v1.1 in Cohort A, Cohort B and Cohort C. Participants who progressed, died, or discontinued study before 6 months were counted as a failure. — Time frame: **At 6 months**

**基線血糖排除（原文）**：
> * Subjects with an established diagnosis of **diabetes mellitus type I or uncontrolled type II**.

（與 SOLAR-1 相同；ECOG 允許 ≤ 2，較 SOLAR-1 寬）

### 13.1 已公布結果中之高血糖不良事件

| 事件 | Cohort A (n=127) | Cohort B (n=126) | Cohort C (n=126) | Ext A (n=1) | Ext B (n=0) | Ext C (n=10) |
|---|---|---|---|---|---|---|
| **Serious** — Hyperglycaemia | 7 | 3 | 2 | 0 | 0 | 0 |
| **Other (non-serious)** — Hyperglycaemia | **76** | **81** | **85** | 1 | 0 | 6 |

---

## 14. NCT05646862 — INAVO121（inavolisib **vs** alpelisib，head-to-head）【L2-登錄】📌

**URL**：https://clinicaltrials.gov/study/NCT05646862

| 欄位 | 內容 |
|---|---|
| Acronym | INAVO121 |
| Phase | **Phase 3** |
| Design | **Randomized, Parallel, OPEN-LABEL**（active comparator = alpelisib） |
| Sponsor | Hoffmann-La Roche |
| Status | **ACTIVE_NOT_RECRUITING**（last update 2026-06-24）；> Enrollment for the main study is now complete. |
| Start | 2023-06-07；Primary completion（預估）2026-11-13；Completion（預估）2029-03-30 |
| Enrollment | 420（estimated） |
| Results posted | 否 |

**劑量對照（本檔中唯一同時載明兩藥劑量之來源）**：
> (DRUG) Inavolisib: Participants will be administered a **9 milligram (mg) inavolisib tablet orally once a day (PO QD) on Days 1-28 of each 28-day cycle** of main study and sub-study.
> (DRUG) Alpelisib: Alpelisib will be administered to participants at the approved dose in combination with fulvestrant: **300 mg taken PO QD and on days 1-28 of each 28-day cycle.**
> (DRUG) Fulvestrant: ... 500 mg of fulvestrant on Days 1 and 15 of Cycle 1 and then on Day 1 of each subsequent 28-day cycle ...

**Primary endpoint**：
> Blinded Independent Central Review (BICR)-Assessed Progression Free Survival (PFS) — From randomization until disease progression or death due to any cause (up to approximately 64 months)

**基線血糖相關排除（原文）**：
> * **Type 2 diabetes requiring ongoing systemic treatment at the time of study entry; or any history of Type 1 diabetes**

**臨床意涵**：INAVO121 是目前**唯一直接比較 inavolisib 與 alpelisib** 的 phase 3 試驗（ECOG 允許 0-2）。其安全性比較結果尚未公布 → **目前不可斷言 inavolisib 之高血糖負擔低於 alpelisib**（本回顧未取得可驗證之直接比較數據）。DDI 子研究（midazolam / omeprazole / bupropion）目前仍開放收案。

---

## 15. NCT05768139 — PIKALO-1 / STX-478（tersolisib，突變選擇型 PI3Kα inhibitor）【L2-登錄】📌（**RECRUITING**）

**URL**：https://clinicaltrials.gov/study/NCT05768139

| 欄位 | 內容 |
|---|---|
| Acronym | PIKALO-1 |
| Phase | Phase 1/2（first-in-human） |
| Design | Non-randomized, Sequential, open-label（部分 cohort 為 dose randomization） |
| Sponsor | Eli Lilly and Company |
| Status | **RECRUITING**（last update 2026-07-07） |
| Start | 2023-04-17；Primary completion（預估）2030-07 |
| Enrollment | 880（estimated） |
| Results posted | 否 |

官方標題：
> First-in-Human Study of STX-478, a **Mutant-Selective PI3Kα Inhibitor** as Monotherapy and in Combination With Other Antineoplastic Agents in Participants With Advanced Solid Tumors

**與代謝直接相關之設計（本檔重點）**：登錄檔中有一個**專門的 metformin 藥物交互作用（DDI）arm**：
> [EXPERIMENTAL] Experimental: Drug to Drug Interaction (DDI) **Metformin** STX-478 +/- ET ([AIs or fulvestrant]: CDK4/6 inhibitor therapy in Cohort A8: all solid tumors Cohort B2 and Cohort F: HR+/HER2- or HR+/HER2 low breast cancer expressing PI3Kα mutations
> (DRUG) Metformin: Metformin | arms=['Experimental: Drug to Drug Interaction (DDI) Metformin STX-478 +/- ET ...']

**代謝相關 secondary outcomes（原文）**：
> * Changes in circulating markers of glucose metabolism as assessed by changes in circulating glycosylated hemoglobin (HbA1c) — 12 months
> * Changes in circulating markers of glucose metabolism as assessed by circulating fasting plasma glucose — 12 months
> * Changes in circulating markers of glucose metabolism as assessed by **circulating C-peptide** — 12 months

**臨床意涵**：mutant-selective PI3Kα inhibitor 之設計目標即為降低對 wild-type PI3Kα（胰島素訊號）之抑制。**目前無任何已公布之人體高血糖比較數據** → 本回顧不對其代謝安全性作任何斷言。

---

# 第三部分：檢索到但相關性較低／已終止之研究（列出以供完整性稽核）

| NCT | 標題（節錄） | Status | Phase | n | Results | 備註 |
|---|---|---|---|---|---|---|
| NCT04967248 | A NIS of Alpelisib in Combination With Fulvestrant... | TERMINATED | 觀察性 | 4 | 否 | 非介入性研究，n 極小 |
| NCT05073120 | Survey Among Healthcare Professionals Treating Patients With Metastatic Breast Cancer in Selected European Countries | COMPLETED | 調查 | 103 | 否 | 醫師問卷，非病人試驗 |
| NCT04862143 | Pilot Decentralized Clinical Trial in Men and Pre and Post-menopausal Women With Breast Cancer and a Specific... | TERMINATED | PHASE2 | 2 | 是 | n=2 |
| NCT05660083 | Alpelisib/iNOS Inhibitor/Nab-paclitaxel in Metaplastic Breast Cancer | RECRUITING | PHASE2 | 36 | 否 | 非高血糖主題 |
| NCT01791478 | BYL719 and Letrozole in Post-Menopausal HR+ MBC | ACTIVE_NOT_RECRUITING | PHASE1 | 46 | 否 | 早期試驗 |
| NCT02038010 | BYL719 + T-DM1 in HER2(+) MBC | COMPLETED | PHASE1 | 17 | 是 | 非高血糖主題 |
| NCT05472220 | Alpelisib in Combination With Carboplatin... | WITHDRAWN | PHASE1 | 0 | 否 | 未執行 |
| NCT07426822 | Rash & Diarrhea Prophylaxis With Capivasertib | NOT_YET_RECRUITING | PHASE2 | 108 | 否 | capivasertib（AKT inhibitor）之皮疹／腹瀉預防，非高血糖 |

---

# 第四部分：本次檢索**未能取得**之資訊（明列，禁止以先驗知識補洞）

以下項目在本次 ClinicalTrials.gov 擷取中**查無可驗證來源**，正文若需論述必須另尋 L1 仿單或已發表全文：

1. **METALLICA 之任何結果數值**（grade 3-4 高血糖發生率、停藥率、PFS 等）— 登錄檔 `hasResults = False`，ClinicalTrials.gov 無結果區段。
2. **INAVO120 之 inavolisib 劑量（mg）** — 該登錄檔 intervention 欄位未載明；9 mg QD 之數字係由 INAVO121（NCT05646862）取得。
3. **INAVO120 之 grade 3/4 高血糖分級人數** — Results Section 之 adverse events module 僅提供 all-grade「Other (non-serious) Hyperglycaemia 87/162 vs 12/162」，未於本次擷取中取得分級細目。
4. **任何 FDA / EMA / TFDA 仿單之高血糖劑量調整表（Piqray、Itovebi）** — 不在 ClinicalTrials.gov 範圍內；需另行擷取至 `來源/` 目錄。
5. **NCT05753657（pioglitazone）之 pioglitazone 劑量** — 登錄檔未載明。
6. **NCT06083038 所採用之「hyperglycemia prevention and management regimen」具體內容** — 登錄檔未載明。
7. **NCT05090358（TIFA）之 ketogenic diet 巨量營養素組成（碳水公克數／比例）** — 登錄檔未載明。
8. **inavolisib 與 alpelisib 之高血糖直接比較數據** — INAVO121 尚未公布結果。
9. **任何 PI3Kα inhibitor 相關 DKA / HHS 之處置流程或 insulin 起始準則之試驗方案** — 本次檢索未見以此為 primary endpoint 之登錄試驗。
10. **癌症病人腹瀉／脫水／腎功能波動情境下之抗糖尿病藥（尤其 metformin、SGLT2i）安全性專門試驗** — 本次檢索未見。

---

# 第五部分：供正文引用之關鍵摘要表

| NCT | 簡稱 | Phase | Design | n | 基線血糖條件 | 介入（代謝相關） | Primary endpoint | Status | Results |
|---|---|---|---|---|---|---|---|---|---|
| NCT04300790 | METALLICA | 2 | 三世代**單臂** Simon 2-stage、open-label | 69 (actual) | A: FPG ≤100 & HbA1c <5.7；B: FPG 100-140 或 HbA1c 5.7-6.4%；C: T2DM ≥90 天、HbA1c <7.5%、insulin-naïve | Metformin 500 mg BID → 1000 mg BID（A/B 提前 1 週；C 提前 2 週 + vildagliptin 50 mg BID） | A/B: 前 2 cycles G3-4 高血糖率；C: 8 週後因 AE 永久停用 alpelisib 率 | COMPLETED | **否** |
| NCT04899349 | EPIK-B4 | 2 | **隨機**、open-label、active-controlled、**PREVENTION** | 2 (actual，計畫 132) | 需具 ≥1 風險因子：DM／prediabetes／BMI≥30／年齡≥75 | Dapa 5→10 mg + Met XR 500→2000 mg vs Met XR 500→2000 mg（C1D1 起，alpelisib C1D8 起） | 前 8 週 grade ≥3 高血糖人數（血糖 >250 mg/dL） | TERMINATED | 是（n=1 可評估） |
| NCT05090358 | TIFA | 2 | **隨機** 3-arm、open-label | 15 (actual) | 未設門檻 | 生酮飲食 / 低碳飲食 / canagliflozin 100 mg×1週→300 mg | 12 週 grade 3/4 高血糖-free rate | ACTIVE_NOT_RECRUITING | 否 |
| NCT05025735 | — | 2 | 單臂 pilot | 25 (est.) | 未設門檻；CrCl ≥35 | Dapagliflozin 10 mg QD（C1D3 起） | all-grade 高血糖發生率 | UNKNOWN | 否 |
| NCT05753657 | — | Early 1 | 單臂 | 30 (est.) | 排除 HbA1c >8%、insulin 治療者 | Pioglitazone（劑量未載）＋監測 insulin | G3-4 及 all-grade 高血糖率、PFS | RECRUITING | 否 |
| NCT04330625 | GRIP-IT | 1 | 單臂 | 1 (actual) | 已因 G3-4 高血糖停用 alpelisib 者 | REMD-477（volagidemab）SC ×4 週 | AE / SAE（28 天） | TERMINATED | 否 |
| NCT04073680 | — | 1b/2 | 單臂 | 60 (est.) | 排除需 insulin／secretagogue、HbA1c >7.5% | Serabelisib 600/900/1200 mg（每週 3 天）+ canagliflozin 300 mg | AE 率、lab 異常率、劑量確認、RECIST | UNKNOWN | 否 |
| NCT05455619 | Amelia-1 | 1b/2 | Open-label parallel pilot | 52 (est./arm) | alpelisib arm: FPG ≤140 & HbA1c ≤6.4%；capivasertib arm: HbA1c <8% | Evexomostat 36→49 或 ↓27 mg/m²（14 天 lead-in 後 C1D15 加 PI3Ki/AKTi） | AE 發生率；高血糖事件之嚴重度／次數／比例 | **RECRUITING** | 否 |
| NCT04750941 | — | 2 | 非隨機、2 cohort | 1 (actual) | 未設血糖門檻 | 生酮飲食 7 天 run-in（需通過合規檢驗）+ copanlisib IV D1/8/15 | ORR | TERMINATED | 是（n=1） |
| NCT06083038 | — | 觀察性 | 前瞻 cohort | 8 (actual) | 排除 HbA1c >10%、6 個月內 DKA | FreeStyle Libre 2（alpelisib 前 ≥10 天起、持續 ≥3 個月） | alpelisib 服藥後至血糖峰值之時間 | COMPLETED | 否 |
| NCT05107388 | AAREN | N/A | 單臂 | 40 (est.) | 未設門檻 | FreeStyle Libre Pro 14 天 | 高血糖發生率（定義見 10.2） | UNKNOWN | 否 |
| NCT06354088 | — | 1 | **隨機 crossover、雙盲** | 32 (est.) | IS: insulin ≤10 µIU/mL, FPG <100, HbA1c <5.7, HOMA-IR <2.5, FIB-4 <1.3；IR: insulin ≥13 µIU/mL + prediabetes 或 HOMA-IR ≥2.5 | 單次 alpelisib 300 mg vs placebo（健康志願者） | 肝臟 DNL、EGP | **RECRUITING** | 否 |
| NCT04191499 | INAVO120 | 2/3 | **隨機雙盲安慰劑對照** | 325 (actual) | 排除需系統性治療之 T2DM、任何 T1DM 病史 | Inavolisib + palbociclib + fulvestrant | PFS（up to 3.7 years） | ACTIVE_NOT_RECRUITING | **是** |
| NCT02437318 | SOLAR-1 | 3 | **隨機三盲安慰劑對照** | 572 (actual) | 排除 T1DM 與 **uncontrolled** T2DM | Alpelisib 300 mg QD + fulvestrant 500 mg | PIK3CA-mutant cohort 之 PFS（up to 33.3 months） | COMPLETED | **是** |
| NCT03056755 | BYLieve | 2 | **非隨機**、open-label、3 cohort、non-comparative | 383 (actual) | 排除 T1DM 與 **uncontrolled** T2DM | Alpelisib 300 mg QD + fulvestrant 或 letrozole 2.5 mg | 6 個月無疾病進展存活比例 | COMPLETED | **是** |
| NCT05646862 | INAVO121 | 3 | **隨機 open-label**（inavolisib vs alpelisib） | 420 (est.) | 排除需系統性治療之 T2DM、任何 T1DM 病史 | Inavolisib **9 mg QD** vs Alpelisib **300 mg QD**（皆 + fulvestrant 500 mg） | BICR-assessed PFS | ACTIVE_NOT_RECRUITING | 否 |
| NCT05768139 | PIKALO-1 | 1/2 | 非隨機 sequential | 880 (est.) | 本次擷取未取得 | Tersolisib (STX-478) ± ET/CDK4/6i；**含 metformin DDI arm** | DLT、ORR、TEAE | **RECRUITING** | 否 |

---

## 附錄：本檔資料完整性宣告

- 所有 NCT number、n、劑量、日期、endpoint 文字，皆取自 2026-07-21 當日 ClinicalTrials.gov API v2 之 `protocolSection` 與 `resultsSection`。
- 高血糖 AE 數字（第 11.1、12.1、13.1 節）取自各試驗 `resultsSection.adverseEventsModule`，格式為 `numAffected / numAtRisk`。
- 本檔**未引用**任何未在上述 API 回應中出現之數字。
- 本檔內容為**登錄資料**，非同儕審查論文；引用至正文時應標【L2-登錄】或【L2】，並註記本檔名 `[trials_ongoing.md]`。
