# I. 目前證據爭議與 knowledge gaps

## I-0. 證據等級判讀規則（本節適用）

| 標記 | 定義 | 本回顧中的代表來源 |
|---|---|---|
| 【L1】 | FDA／EMA／TFDA 正式仿單逐字條文 | `label_alpelisib.md`、`label_inavolisib.md` |
| 【L2】 | 前瞻性臨床試驗（含 phase 2 單臂、phase 3 RCT、pooled trial analysis） | SOLAR-1、BYLieve、METALLICA、INAVO120、CAPItello-291 |
| 【L3】 | 專家共識／Delphi／學會指引 | ADA SOC-2026、Delphi Gallagher 2024、Tankova 2022 |
| 【L4】 | 回溯性研究／real-world／claims／case series／case report | Shen 2023、Liu 2022、Ismail 2026、各 DKA case report |
| 【L5】 | 前臨床或純機轉推論 | Hopkins 2018 (Nature)、Fruman 2017 (Cell) |
| 📄／📌 | 本地有全文可 grep／僅有 abstract（**不得對其內文細節作具體斷言**） | 見 `inventory.md` |

> **本節的核心命題**：本報告中「監測頻率」與「劑量調整門檻」幾乎全部有【L1】依據；但「用哪一種降糖藥」「要不要預防性給藥」「要不要為了 hyperinsulinemia 而改變用藥」則幾乎全部落在【L3】—【L5】。這兩件事在臨床上被混為一談，是目前最大的認知風險。

> **本版全文落地更新（2026-07-21）**：以下三篇已由 📌（僅 abstract）升級為 📄（本地全文可 grep），本節相關條目已改以**原始論文數字**重寫，不再以「未取得全文故無法斷言」迴避：
> - `原始PDF/SOLAR1_AE_Rugo_2020.md`（Ann Oncol 2020，PMID 32416251）—— SOLAR-1 AE 時序與處置專文【L2】
> - `原始PDF/INAVO120_Turner_2024.md`（N Engl J Med 2024;391:1584-96，PMID 39476340）—— INAVO120 主論文【L2】
> - `原始PDF/MSKCC_RealWorld_Shen_2023.md`（Cancer 2023;129:3854-3861，PMID 37743730）—— MSKCC 真實世界世代 n=247【L4】
>
> **但仍為 📌 者**：SOLAR-1 **主論文**（André 2019，`SOLAR1_Andre_2019.md`，本地僅 abstract）與 **BYLieve**（Rugo 2021／2024，本地僅 abstract）。因此凡涉及 SOLAR-1 主論文之 subgroup／supplementary table 或 BYLieve 內文細節者，**仍不得引用**。

---

## I-1. 【Q17】證據層級總覽表：本報告每一條核心建議的來源分類

### 表 I-1A：治療前評估與族群篩選

| # | 建議 | 證據等級 | 來源與可 grep 之依據 |
|---|---|---|---|
| 1 | 開始 alpelisib 前必須檢驗 FPG **與** HbA1c，並先 optimize 血糖 | 【L1】📄 | FDA PIQRAY §2.3／§5.3「Before initiating treatment with PIQRAY, test fasting plasma glucose (FPG), HbA1c, and optimize blood glucose.」[label_alpelisib.md] |
| 2 | 開始 inavolisib 前必須檢驗 FPG/FBG **與** HbA1C，並先 optimize | 【L1】📄 | FDA ITOVEBI §2.2；EMA 4.4「Treatment with Itovebi should not be initiated until fasting glucose levels are optimised.」[label_inavolisib.md] |
| 3 | 治療前抽 fasting **或 random** plasma glucose + A1C（學會層級） | 【L3】📄 | ADA SOC-2026 Rec 2.21（證據等級 **C**；A1C 部分為 **E**）[guideline_ada_comparators.md] |
| 4 | 風險分層因子：diabetes／prediabetes／BMI ≥30／age ≥75 | 【L1】📄＋**【L2】原始數據現已可 grep 📄** | EMA Piqray SmPC §4.2「Baseline diabetic and pre-diabetic status, baseline BMI ≥30 and baseline age ≥75 years have been found to be risk factors」；該三項出現於 74.9% 任何級別、84.7% grade 3–4 高血糖病人 [label_alpelisib.md]。**SOLAR-1 之原始分層數據（Rugo 2020 全文）**：基線 prediabetic 者 **74%** 發生高血糖（G3 43.4%、G4 5.0%）vs normal **52%**（G3 16.8%、G4 1.8%）；基線分布 normal 113（40%）／prediabetic 159（56%）／diabetic 12（4%）；BMI 分層 overweight 62/84（**73.8%**）、obese 50/74（**67.6%**）、normal BMI 63/110（**57.3%**），grade 4 分別 3.6%／**9.5%**／2.7%；≥75 歲 grade 3/4 高血糖 **19/34（55.9%）vs 89/250（35.6%）**。**原文未報告 BMI 分組之 kg/m² cut-off，亦無任何 OR/HR/p 值（僅描述性 trend）** [SOLAR1_AE_Rugo_2020.md] |
| 5 | inavolisib 之風險因子清單較寬：(pre)diabetes、HbA1C ≥5.7%、BMI ≥30、**年齡 ≥45 歲**、gestational diabetes 病史、DM 家族史 | 【L1】📄；**其 BMI 依據在 INAVO120 全文中僅為微弱差異 📄** | EMA Itovebi Table 5 逐字 [label_inavolisib.md]。**INAVO120 主論文逐字**：inavolisib 組 BMI ≥30.0 者高血糖 **65.5%**、BMI <30.0 者 **56.8%**，作者自述為「**slightly higher**」；**未報告 BMI 分層下的 grade 3/4 率**。該試驗 BMI ≥30 者僅 57/325（17.5%）、BMI 18.5–<25.0 達 47.1%、BMI <18.5 者 5.5%，中位體重 63.0 kg [INAVO120_Turner_2024.md] |
| 6 | 以 5 項基線變數（FPG、BMI、HbA1c、monocytes、age）之 random forest 模型作風險分層 | 【L2/L4】📄 | Rodon 2024：pooled X2101+SOLAR-1（n=505）建模，BYLieve（n=340）外部驗證；training set 高風險組 2 個月內 grade 3/4 風險 86.2%，test set 57.6% [RiskModel_Rodon_2024.md] |
| 7 | HbA1c 6.5%–<8% 者，**在治療前有內分泌科會診的前提下**可開始 alpelisib | 【L3】📄 | Delphi Gallagher 2024（modified Delphi，1–9 分制）[Delphi_Gallagher_2024.md] |
| 8 | HbA1c ≥8.0% 者之 alpelisib 適用性 | **無建議** | Delphi 專家組明文將此情境之建議「excluded」，理由為「they agreed more evidence is needed」；僅共識「未經治療前內分泌會診即治療這些病人是不適當的」[Delphi_Gallagher_2024.md] |
| 9 | EMA 明文規定糖尿病病人**一定要**照會（should always take place）；prediabetic／FG >250／BMI ≥30／age ≥75 則為 recommended | 【L1】📄 | EMA Piqray §4.2；**FDA 與 TFDA 仿單無對應獨立條文** [label_alpelisib.md §9] |

### 表 I-1B：治療中監測

| # | 建議 | 證據等級 | 來源 |
|---|---|---|---|
| 10 | **alpelisib**：前 2 週至少每週驗 FPG，之後至少每 4 週；HbA1c 每 3 個月 | 【L1】📄 | FDA PIQRAY §2.3；TFDA 中文仿單同 [label_alpelisib.md]。**注意：仿單頻率比 SOLAR-1 試驗實際排程更密。** SOLAR-1 之逐字排程為「screening、前 8 週每 2 週、之後每 4 週」，另於前 4 週加驗 **day 8 與 day 15**；而 day 8 門診是**收案約 56.6% 後才由 protocol amendment 加入**的 [SOLAR1_AE_Rugo_2020.md] |
| 11 | **alpelisib（EMA 版）**：week 1、2、4、6、8 後每月；高風險族群（DM／prediabetes／BMI ≥30／≥75 歲）**前 2 週每日自我監測** | 【L1】📄 | EMA Piqray Table 6（FDA 無對應表）[label_alpelisib.md] |
| 12 | **inavolisib**：Day 1–7 每 3 天 → Day 8–28 每週 → 後 8 週每 2 週 → 之後每 4 週；HbA1C 每 3 個月 | 【L1】📄 | FDA ITOVEBI §5.1；EMA Table 5 [label_inavolisib.md] |
| 13 | 發生高血糖後：至少每週 2 次驗到正常；降糖治療期間每週一次 ×8 週，之後每 2 週 | 【L1】📄 | FDA PIQRAY §5.3；EMA Piqray Table 6；EMA Itovebi Table 5 同義 [label_alpelisib.md][label_inavolisib.md] |
| 14 | 學會版排程：random plasma glucose 前 2 週每週、之後每 4 週；A1C 每 3 個月「可考慮」 | 【L3】📄 | ADA Rec 2.21（C／E）。ADA 明言「A1C alone may not capture the early peak of hyperglycemia noted with PI3Kα inhibitors」[guideline_ada_comparators.md] |
| 15 | 依風險分層調整驗糖頻率：一般每週、中風險每週 2 次、最高風險每日 | 【L3】📄 | Delphi Gallagher 2024（point-of-care／居家血糖機）[Delphi_Gallagher_2024.md] |
| 16 | 併用 corticosteroid、感染或其他 intercurrent illness 時，加驗 HbA1C **與血中 ketone** | 【L1】📄 | EMA Itovebi Table 5 逐字：「Monitoring of HbA1C and ketones (preferably in blood) ... is recommended in these patients.」[label_inavolisib.md] |
| 17 | 常規使用 CGM／FGM | **【L4】📄 僅 case-level；無 RCT** | Pla-Peris 2022（FGM case report）、Blow 2021（case series n=3）、Carrillo 2021（CGM tracing, case report）；Tankova 共識僅寫「If available, self-monitoring and continuous glucose monitoring devices should be prescribed or recommended」【L3】[FGM_PlaPeris_2022.md][VLCD_SGLT2i_Blow_2021.md][DKA_Carrillo_2021.md][Consensus_Tankova_2022.md] |

### 表 I-1C：預防性（prophylactic）降糖治療

| # | 建議 | 證據等級 | 來源 |
|---|---|---|---|
| 18 | **「Consider」預防性 metformin**（依風險因子、GI 耐受度與臨床情境） | 【L1】📄 | FDA PIQRAY §2.3／§5.3 逐字「**Consider** premedication with metformin ... based on patient risk factors for hyperglycemia, gastrointestinal tolerability, and clinical situation」；同段明載「**increases the incidence and severity of nausea, vomiting, and diarrhea adverse reactions**」[label_alpelisib.md] |
| 19 | inavolisib：「metformin premedication **can be considered** in patients with **risk factors** for hyperglycaemia」 | 【L1】📄；**其【L2】基礎現已可查證，且為「protocol 允許」而非「已證實有效」** | **僅 EMA SmPC 4.4**。FDA ITOVEBI 全文 **未出現 "metformin" 字樣**（已 grep 確認）[label_inavolisib.md §14.3]。**INAVO120 主論文逐字**：「**The protocol allowed prophylactic use of metformin in patients with a high risk of hyperglycemia**」——但原文**未報告實際 metformin 使用率、未定義「high risk」之操作型定義、未做任何隨機化、亦未報告其對高血糖發生率之影響**；其他降糖藥（SGLT2i／insulin／SU／DPP-4i）之使用亦完全未報告 [INAVO120_Turner_2024.md] |
| 20 | 學會版：「**Consider** using metformin to prevent hyperglycemia in **high-risk** individuals treated with a PI3Kα inhibitor」 | 【L3】📄 | ADA SOC-2026 Rec 3.8，證據等級標示為 **B**（ADA 內部分級）[guideline_ada_comparators.md] |
| 21 | Delphi 版：**baseline HbA1c 5.7–6.4% 者全部建議**預防性 metformin；HbA1c <5.7% 者「may be appropriate」 | 【L3】📄 | Delphi Gallagher 2024。同文亦載：最高風險族群「是否加預防性 metformin 併第二種降糖藥」**專家未達成共識（disagreement）** [Delphi_Gallagher_2024.md] |
| 22 | METALLICA 之實際給法：metformin 500 mg BID 起始，3 天後若無 GI 不耐受增至 1000 mg BID；**alpelisib 前 7 天開始** | 【L2】📄 | METALLICA 論文＋ClinicalTrials.gov NCT04300790 逐字 [METALLICA_LlombartCussac_2024.md][trials_ongoing.md] |
| 23 | 治療前建議低碳水飲食（60–130 g/日）＋必要時營養師 | 【L3】📄 | Delphi Gallagher 2024 [Delphi_Gallagher_2024.md] |
| 24 | Ketogenic diet（<50 g/日）／治療前空腹 >12 小時 | 【L3】📄 **且共識之間互相矛盾** | Delphi 2024：「may also be appropriate」；Tankova 2022 共識**明確不建議**：「we do not recommend very-low-carbohydrate diets, but rather moderate carbohydrate restriction」[Delphi_Gallagher_2024.md][Consensus_Tankova_2022.md] |

### 表 I-1D：高血糖發生後的藥物選擇

| # | 建議 | 證據等級 | 來源 |
|---|---|---|---|
| 25 | 可用藥物類別：metformin、SGLT2i、insulin sensitizers（TZD／DPP-4i） | 【L1】📄 | FDA PIQRAY Table 3 註²；EMA Piqray Table 2 註²（**兩者皆未提供任何頭對頭比較數據**）[label_alpelisib.md] |
| 26 | metformin 為 INAVO120 之「preferred initial agent」 | 【L1】📄 | **僅 EMA Itovebi Table 2 註 b**；FDA ITOVEBI 未指定藥物 [label_inavolisib.md] |
| 27 | SOLAR-1 之 metformin titration：500 mg QD → 500 mg BID → 早 500／晚 1000 → 1000 mg BID | 【L1】📄 | FDA PIQRAY Table 3 註²（逐字）[label_alpelisib.md]。**⚠ 此 titration 僅見於仿單**：SOLAR-1 AE 專文全文中 protocol Table 1 只寫「consider metformin」「start or intensify metformin」「beyond MTD of metformin」，**全文無任何 mg 劑量或加量時程**（已 grep "metformin"／"titrat"／"500 mg"／"1000 mg" 確認）[SOLAR1_AE_Rugo_2020.md] |
| 28 | metformin 為第一線；SGLT2i 或 TZD 為第二／三線或 metformin 不耐受時之第一線；GLP-1 RA 可考慮；**insulin／SU／DPP-4i 一般不適合作第一或第二線** | 【L3】📄 | Delphi Gallagher 2024 [Delphi_Gallagher_2024.md] |
| 29 | 學會版：metformin 為 PI3Kα inhibitor 高血糖之第一線 | 【L3】📄 | ADA Rec 9.35a，證據等級 **E（expert consensus）** [guideline_ada_comparators.md] |
| 30 | **insulin 應保留給 severe hyperglycemia 與 hyperglycemic crises** | 【L3】📄（其理由屬【L5】） | ADA Rec 9.35b，等級 **E**；其理由「due to its potential impact on the efficacy of PI3K inhibitors」為機轉推論 [guideline_ada_comparators.md] |
| 31 | 仿單版 insulin 定位：「insulin may be used for **1-2 days** until hyperglycemia resolves」 | 【L1】📄；**但 SOLAR-1 之實際使用型態與此不符（【L2】📄）** | FDA PIQRAY Table 3 註³；EMA Piqray Table 2 註³。EMA Itovebi 4.4：「**Short-term insulin may be used as rescue treatment**」 [label_alpelisib.md][label_inavolisib.md]。**SOLAR-1 實際數據**：共 **52 人**用過 insulin，其中 **33 人為長期使用（>2 天）**、僅 19 人為 rescue；依基線血糖狀態：diabetic **5/12**、prediabetic **34/159**、normal **13/113**。作者於 Discussion 逐字寫道：「**short-term insulin is clearly effective for managing acute cases as well as more severe hyperglycemia associated with alpelisib and not controlled by oral antihyperglycemic medications alone**」[SOLAR1_AE_Rugo_2020.md]。**「insulin 只用 1–2 天」是仿單的建議措辭，不是試驗中的實際情形；不得據此在嚴重高血糖時延遲或限縮 insulin。** |
| 32 | 停用／中斷 PI3Kα inhibitor 時，須同步下修 insulin／SU 以免低血糖 | 【L1】📄 | EMA Itovebi 4.4 逐字 [label_inavolisib.md] |
| 33 | SU 應避免（rebound hypoglycemia 風險） | 【L3】📄 | Jhaveri 2026 pooled safety review [ToxMgmt_Jhaveri_2026.md] |
| 34 | metformin 起始 500 mg QD（早期嚴重高血糖者 1000 mg），每 3–4 週加 500 mg 至最大 2000 mg；優先 extended-release | 【L3】📄 | Jhaveri 2026 [ToxMgmt_Jhaveri_2026.md] |
| 35 | SGLT2i 可較 metformin 更快降低血糖 | 【L4】📄 | Liu 2022 校正後分析：SGLT2i −48 mg/dL（95% CI −75 至 −21）vs metformin −28 mg/dL（−41 至 −16）[RealWorld_Liu_2022.md] |
| 36 | SGLT2i 併用可降低 grade ≥3 高血糖 | 【L2/L5】📄 **但為 propensity-matched，非隨機** | Borrego 2024：SGLT2i cohort n=19 vs matched control n=74；grade ≥3 高血糖事件率 0.00461 vs 0.02272（4.9 倍差）；time-to-first-event HR 0.294 [SGLT2i_Borrego_2024.md] |

### 表 I-1E：劑量調整（全部為【L1】，但兩藥門檻不同）

| # | 建議 | 證據等級 | 來源 |
|---|---|---|---|
| 37 | **alpelisib** 減量階梯 300 → 250 → 200 mg → 停藥 | 【L1】📄 | FDA/EMA/TFDA Table 1 三地一致 [label_alpelisib.md] |
| 38 | **inavolisib** 減量階梯 9 → 6 → 3 mg → 停藥；**EMA 另允許臨床評估後回調至 9 mg（FDA 無此條文）** | 【L1】📄 | FDA ITOVEBI Table 1；EMA SmPC 4.2 [label_inavolisib.md] |
| 39 | alpelisib：FPG >160–250（G2）**不需調整劑量**，21 天內未降至 ≤160 才降一階 | 【L1】📄 | FDA PIQRAY Table 3 [label_alpelisib.md] |
| 40 | inavolisib：FPG >160–250 即 **withhold** 直到 ≤160，再以**原劑量** resume | 【L1】📄 | FDA ITOVEBI Table 2 [label_inavolisib.md] |
| 41 | 兩藥的 Grade 3／4 均要求 IV hydration 並處理 electrolyte／ketoacidosis／hyperosmolar disturbance | 【L1】📄 | FDA PIQRAY Table 3 Grade 3、Grade 4；FDA ITOVEBI Table 2 第 4 列「Assess for volume depletion and ketosis」[label_alpelisib.md][label_inavolisib.md] |
| 42 | inavolisib 腎功能減量：eGFR 30–<60 → 6 mg；eGFR <30 → 3 mg | 【L1】📄 | FDA ITOVEBI §2.5（04/2026 RECENT MAJOR CHANGE）；EMA 5.2 藥動依據：moderate RI 之 AUC 高 73%、severe RI 高 123% [label_inavolisib.md] |
| 43 | alpelisib 腎功能減量 | **無條文** | FDA PIQRAY §8.6：mild–moderate（CLcr 30–<90）不需調整；severe（<30）之影響「unknown」[label_alpelisib.md] |

### 表 I-1F：機轉性論述（**全部為【L5】，不可當臨床建議陳述**）

| # | 論述 | 證據等級 | 來源 |
|---|---|---|---|
| 44 | PI3Kα 抑制阻斷肌肉／脂肪之葡萄糖攝取並活化肝醣分解 → 為 on-target、off-tumor 效應 | 【L5】📄 | Hopkins 2018；Fruman 2017；Huang 2018 [InsulinFeedback_Hopkins_2018.md][Mech_Fruman_Cell_2017.md][Mech_Huang_ObesityT2D_2018.md] |
| 45 | Insulin feedback 可在 PI3K inhibitor 存在下重新活化 PI3K 訊息，削弱抗腫瘤療效 | 【L5】📄 **小鼠模型** | Hopkins 2018 (Nature)：「we show **in several model tumors**, that systemic glucose-insulin feedback ... is sufficient to activate PI3K signaling, even in the presence of PI3K inhibitors」[InsulinFeedback_Hopkins_2018.md] |
| 46 | 抑制 insulin feedback（飲食或藥物）可提升 efficacy/toxicity 比 | 【L5】📄 **小鼠模型** | Hopkins 2018 [InsulinFeedback_Hopkins_2018.md] |
| 47 | SGLT2i 前處理可降低 alpelisib 誘發之高血糖與高胰島素血症 | 【L5】📄 | Borrego 2024 之動物模型部分（BN／ZDF／tumor-bearing nude rats）[SGLT2i_Borrego_2024.md] |
| 48 | 高血糖與 PFS 較差有關（**buparlisib／glioblastoma**） | 【L5/L4】📌 **僅 abstract** | Noch 2023，Neuro-oncology。**不同藥物（buparlisib，pan-PI3K）、不同腫瘤（GBM）；不得外推至 alpelisib／inavolisib 之乳癌族群** [InsulinFeedback_Noch_2023.md] |

---

## I-2. 爭議與缺口逐項展開

### I-2-1. 預防性 metformin：缺乏隨機對照試驗，METALLICA 無法回答「不給會怎樣」

**現況**

METALLICA 是本領域**唯一一個以「預防」為主要目的、且有正式發表的前瞻性試驗**（作者自述：「METALLICA is the first prospective study to evaluate prevention of a key toxicity related to alpelisib」）[METALLICA_LlombartCussac_2024.md]。其設計為 multicentre, open-label, **single-arm**, Simon's two-stage, phase 2，西班牙 18 個中心 [METALLICA_LlombartCussac_2024.md]。ClinicalTrials.gov 登錄檔中 allocation 欄雖標為 RANDOMIZED，但 `interventionModelDescription` 明確為 single-group、three-cohort，且三個 cohort **全部為 EXPERIMENTAL arm、無 control arm** [trials_ongoing.md]。

結果：233 人篩檢，68 人入組（cohort A n=48 血糖正常、cohort B n=20 prediabetes）。前 8 週 grade 3–4 高血糖：cohort A **1/48（2.1%，95% CI 0.5–11.1；P<0.0001）**、cohort B **3/20（15.0%，95% CI 5.6–37.8；P=0.016）** [METALLICA_LlombartCussac_2024.md]。

**爭議點**

1. **P 值不是與對照組比較出來的。** 兩個 cohort 的 P 值來自 Koyama-Chen 方法，檢定的是「真實率 ≥25%（cohort A）／≥40%（cohort B）」之虛無假設；而這兩個門檻是「based on the hyperglycaemia rates observed in SOLAR-1 and BYLieve」[METALLICA_LlombartCussac_2024.md]。也就是說，**對照組是歷史文獻，不是同期隨機分配的病人**。作者自己在 Discussion 首句列為限制：「One limitation of this study is the **non-randomised single-arm design**; data from SOLAR-1 and BYLieve were used to benchmark」[METALLICA_LlombartCussac_2024.md]。
   - **歷史 benchmark 現在可以直接查核了**：SOLAR-1 全文顯示，其 grade 3 高血糖 32.7%、grade 4 3.9%（preferred term，n=284），若以 AESI grouped term 計算則 grade ≥3 為 **108/284（38.0%）**；而 **basline normal 者 grade 3 僅 16.8%、grade 4 1.8%；prediabetic 者 grade 3 43.4%、grade 4 5.0%** [SOLAR1_AE_Rugo_2020.md]。**METALLICA cohort A（血糖正常）之 25% 虛無假設門檻，明顯高於 SOLAR-1 對應之 normal 次族群實際的 grade 3+4 約 18.6%（16.8%+1.8%）**；cohort B（prediabetes）之 40% 門檻則接近 SOLAR-1 prediabetic 次族群的 48.4%（43.4%+5.0%）。也就是說，**兩個 cohort 的檢定門檻並非取自對應的基線血糖次族群，而是取自試驗整體率**，這會使 cohort A 的 P<0.0001 看起來比實際更具說服力。此為本回顧依兩篇全文所作之**數字對照**，非任一原文之結論。
2. **歷史對照的族群與監測強度都不同。** METALLICA 病人「are more pre-treated and have worse diagnosis compared to SOLAR-1」；且高血糖偵測是「a more robust schedule than that used in SOLAR-1 and BYLieve」[METALLICA_LlombartCussac_2024.md]。更密集的監測理論上會**增加**偵測到的事件，卻仍得到較低的事件率——這一點支持 metformin 有效，但**不能量化其效果量**。
   - **SOLAR-1 自身的 protocol amendment 提供了「監測強度可獨立改變事件率」的直接證據**：在約 560 名計畫收案數中已隨機 **317 人（56.6%）**時，protocol 將 HbA1c 收案門檻由 **<8% 改為 <6.5%**、新增 **day 8 門診**、並對 FPG ≥100 mg/dL 和／或 HbA1c ≥5.7% 者建議篩選期即衛教與轉介。前 50% vs 後 50% 隨機者：any-grade 高血糖幾乎不變（**63.9% vs 63.6%**），但 **grade 3/4 由 40.3% 降至 32.9%**、**因高血糖停藥由 9.0% 降至 3.6%**、因 grade ≥3 AE 停藥由 **18.1% 降至 7.9%** [SOLAR1_AE_Rugo_2020.md]。作者自述此改善「**may be attributed to the protocol amendment, as well as other factors**」，**非隨機比較，僅為時序性關聯**。**這代表 METALLICA 相對於 SOLAR-1 的差距中，有多少來自 metformin、有多少來自收案篩選與監測強化，目前無法拆解。**
3. **代價是明確的、且被寫進仿單。** FDA PIQRAY §5.3 逐字：metformin 前給藥「decreases the incidence and severity of hyperglycemia, but **increases the incidence and severity of nausea, vomiting, and diarrhea adverse reactions**」[label_alpelisib.md]。METALLICA 中：nausea 47/68（69.1%）、diarrhoea 46/68（67.6%，其中 9 人 [13.2%] grade ≥3）、rash 28/68（41.2%，11 人 [16.2%] grade ≥3）[METALLICA_LlombartCussac_2024.md]。仿單另載 METALLICA 之永久停藥率 19%、劑量調整或中斷 56% [label_alpelisib.md §5.4]。**有 10/68（14.7%）病人在 alpelisib 尚未開始的第一週就出現腹瀉**——這是純粹的 metformin 歸因 [METALLICA_LlombartCussac_2024.md]。
4. **唯一登錄為「PREVENTION」目的的隨機試驗失敗了。** EPIK-B4（NCT04899349，dapagliflozin + metformin XR vs metformin XR）為 randomized, active-controlled，但**因收案緩慢而終止，actual enrollment = 2**（primary outcome 只有一組有數值 = 1）[trials_ongoing.md]。其登錄之終止理由逐字為：「Study was early terminated due to slow recruitment and emerging data showing that prophylactic use of metformin **may** prevent or reduce the incidence of all-grades alpelisib-related hyperglycemia」[trials_ongoing.md] — 這是 sponsor 的敘述性理由，**本身不構成 metformin 預防效果之證據**。
5. **T2DM cohort 從未發表。** 登錄檔中 METALLICA 原設 cohort C（臨床診斷 ≥90 天之 T2DM、HbA1c <7.5%、insulin-naïve，加 vildagliptin 50 mg BID，且 lead-in 為 **2 週**而非 1 週）[trials_ongoing.md]，但已發表之 primary analysis **僅報告 cohort A 與 B**（該論文標題與摘要皆寫 "2-cohort"）[METALLICA_LlombartCussac_2024.md]。**cohort C 的結果本回顧未取得可驗證來源**。作者結語僅寫「exploring the role of prophylactic metformin in diabetic patients **is warranted**」[METALLICA_LlombartCussac_2024.md]。
6. **仿單與指引的措辭都是「考慮」，不是「應該」。** FDA「**Consider** premedication」【L1】；ADA Rec 3.8「**Consider** using metformin ... in **high-risk** individuals」【L3, B】；EMA Itovebi「**can be considered** in patients **with risk factors**」【L1】[label_alpelisib.md][guideline_ada_comparators.md][label_inavolisib.md]。**把 METALLICA 讀成「所有病人都該預防性用 metformin」是對三份文件的共同誤讀。**

**需要什麼研究才能回答**

- 一個 **randomized, double-blind, placebo-controlled** 的預防性 metformin 試驗，主要終點為前 8–12 週之 grade 3–4 高血糖，**共同主要終點須包含 grade ≥3 腹瀉與 alpelisib 相對劑量強度（RDI）**——因為爭點不是「metformin 能不能降血糖」，而是「淨效益是否為正」。METALLICA 之 median RDI 為 95.1%（僅單臂數值，無對照）[METALLICA_LlombartCussac_2024.md]。
- 分層設計須依 baseline HbA1c（<5.7% vs 5.7–6.4% vs ≥6.5%）分層，因為 Delphi 專家組僅對 HbA1c 5.7–6.4% 達成共識，對 <5.7% 與最高風險族群**均未達成共識** [Delphi_Gallagher_2024.md]。
- 必須有 **inavolisib 版本的同類試驗**：目前 FDA ITOVEBI 全文無 metformin 字樣，EMA 僅寫「can be considered」[label_inavolisib.md §14.4]。**INAVO120 主論文全文已落地，可直接查證：protocol 僅「allowed prophylactic use of metformin in patients with a high risk of hyperglycemia」，並未隨機分配，且全文未報告任何 metformin 使用百分比、亦未定義「high risk」** [INAVO120_Turner_2024.md]。因此**「inavolisib 之預防性 metformin 有效」在 INAVO120 中沒有任何可驗證來源**——這不再是「未取得全文」的問題，而是原文確實沒有這項資料。

---

### I-2-2. 已知糖尿病病人：最需要指引的族群，證據卻最少

**現況（此為本節最嚴重的缺口）**

| 試驗／藥物 | 糖尿病族群的納入情形 | 來源 |
|---|---|---|
| SOLAR-1 / alpelisib（仿單版） | 「The safety of PIQRAY in patients with **Type 1 and uncontrolled Type 2 diabetes has not been established as these patients were excluded**」；僅納入 controlled T2DM | 【L1】[label_alpelisib.md] |
| **SOLAR-1（Rugo 2020 全文逐字 📄）** | 「Patients with a history of **well-controlled type 2 diabetes were eligible** to enroll; however, patients with **type 1 and uncontrolled type 2 diabetes were excluded**」。**更關鍵的是：收案途中 protocol amendment 將 HbA1c 門檻由 <8% 收緊為 <6.5%**（在已隨機 317/約560 人＝56.6% 時），逐字理由為「**excluding patients with uncontrolled diabetes**」——**即後半段收案實際上比前半段更嚴格排除糖尿病** | 【L2】📄 [SOLAR1_AE_Rugo_2020.md] |
| SOLAR-1（EMA 數字） | 基線僅 **4.2%** 為 diabetic（FPG ≥126 和／或 HbA1c ≥6.5%）；即 n=12。這 12 人中 **10 人（83.3%）**發生 grade 3–4 高血糖，0 人僅 grade 1–2 | 【L1】[label_alpelisib.md §6.4] |
| **SOLAR-1（全文之基線血糖分布 📄）** | 依 ADA 定義以隨機化前數值判定（不論病史）：normal **113（40%）**、prediabetic **159（56%）**、**diabetic 僅 12（4%）**。**⚠ 這 12 人的分級高血糖發生率，Rugo 2020 全文並未分項報告**（僅 EMA 仿單有 83.3% 之數字）——兩者來源不同，不可交叉宣稱為同一分析 | 【L2】📄 [SOLAR1_AE_Rugo_2020.md] |
| INAVO120 / inavolisib（仿單版） | 收案要求 **HbA1C < 6% 且 FBG < 126 mg/dL**；排除 T1DM 與需持續降糖治療之 T2DM | 【L1】[label_inavolisib.md §9] |
| **INAVO120（Turner 2024 全文逐字 📄）** | 納入門檻：「**a fasting glucose level of less than 126 mg per deciliter, a glycated hemoglobin level of less than 6.0%**」。排除範圍逐字：「**patients with type 1 or type 2 diabetes that required ongoing treatment were excluded**」——**注意措辭是「需要持續治療的糖尿病」，原文並未說明未用藥之 diet-controlled DM 是否可入組；本回顧不對此作斷言**。作者將此列為試驗第三項限制，並自述「**future studies that evaluate the benefit–risk profile in this population will be useful**」 | 【L2】📄 [INAVO120_Turner_2024.md] |
| **INAVO120（基線代謝資料之空白 📄）** | Table 1 **無 diabetes 一列**；**基線既有糖尿病比例、prediabetes 比例、基線 HbA1c／FPG 之實際分佈值、基線降糖藥使用率——原文全部未報告**，僅有納入門檻。因此「INAVO120 族群的基線血糖狀態」在主論文層級**不可量化** | 【L2】📄 [INAVO120_Turner_2024.md] |
| INAVO120（EMA 數字） | 「**Only 1 patient with Type 2 diabetes was included in the Itovebi arm**」 | 【L1】[label_inavolisib.md §9] |
| METALLICA | 全體排除「Patients treated with insulin」；cohort A/B 排除已需降糖藥之 T1DM/T2DM。cohort C 另排除 eGFR <25、**有 ketoacidosis 或 hyperosmolar state 病史者**、胰臟炎病史、嚴重自律神經病變（gastroparesis） | 【L2】[trials_ongoing.md] |
| GO39374 / inavolisib phase I/Ib | 收案較寬（HbA1c <7%、fasting glucose <140 mg/dL）；具風險因子者高血糖率 **81%** | 【L2】[INAVO120_Safety_Im_2026.md] |
| Amelia-1（NCT05455619） | **alpelisib 組 HbA1c ≤6.4%；capivasertib 組 HbA1c <8%** — 同一試驗內兩藥門檻不同 | 【L2-登錄】📌 [trials_ongoing.md] |

也就是說：**仿單要求臨床醫師「密切監測糖尿病病人」，但產生該仿單的試驗幾乎沒有糖尿病病人。** alpelisib 全球 phase 3 只有 12 位糖尿病病人（12/284，4%）[SOLAR1_AE_Rugo_2020.md]，inavolisib 全球 phase 3 只有 1 位 [label_inavolisib.md §9]。

**兩藥的排除方式並不相同，臨床外推風險也不同**（此為五項禁忌中「兩藥必須分開陳述」之直接體現）：

- **alpelisib（SOLAR-1）**排除的是 **T1DM 與「uncontrolled」T2DM**，且中途才把 HbA1c 門檻由 <8% 收緊到 <6.5%；換言之，**收案前半段實際上納入了 HbA1c 6.5–8% 的病人**，只是原文未報告這群人的獨立結果 [SOLAR1_AE_Rugo_2020.md]。這也是 Delphi 共識敢把可治療範圍推到 HbA1c 6.5%–<8% 的間接背景 [Delphi_Gallagher_2024.md]——但**Delphi 並未引用 SOLAR-1 前半段族群作為依據，兩者不可等同**。
- **inavolisib（INAVO120）**排除的是 **「需要持續治療」的 T1DM 與 T2DM**，且門檻更緊（HbA1c <6.0%、FPG <126 mg/dL）[INAVO120_Turner_2024.md]。**任何已在服用降糖藥的病人，在 INAVO120 中沒有對應資料。** 因此把 inavolisib 用於已知糖尿病病人，是**完全的外推**，比 alpelisib 的外推幅度更大。

**這個空白是由誰填補的？——【L3】與【L4】**

- Delphi 專家共識把可治療範圍推到 HbA1c 6.5%–<8%（前提為治療前內分泌會診），並**明確拒絕**對 HbA1c ≥8.0% 給建議 [Delphi_Gallagher_2024.md]。
- real-world 資料顯示臨床實務早已超出試驗範圍：Shen 2023 之 standard care cohort 中 prediabetes/diabetes 範圍（HbA1c ≥5.7%）者佔 **30.6%**，顯著高於 clinical trial cohort 的 **15.0%（p=.041）**；全世代基線 HbA1c 分層為 <5.7% 104 人（42.1%）、5.7–6.4% 38 人（15.4%）、**≥6.5% 22 人（8.9%）**、unknown 83 人（33.6%）[MSKCC_RealWorld_Shen_2023.md]。**即真實臨床中約每 11 人就有 1 人是 HbA1c ≥6.5% 的糖尿病病人——這個比例是 SOLAR-1（4%）的兩倍以上、是 INAVO120（1 人）的數十倍。**
  - ⚠ **界線**：Shen 2023 全文**未提供「已知糖尿病」之人數、百分比或 p 值**，僅在 Discussion 敘述性寫「the proportion of patients with known diabetes was greater in our standard care cohort」；量化資料**只有** HbA1c ≥6.5% 分層之 22 人（8.9%），且 HbA1c 僅 164/247（66.4%）有值 [MSKCC_RealWorld_Shen_2023.md]。因此「真實世界糖尿病病人比例」在本回顧中**只能以 HbA1c 分層近似，不可宣稱為既有糖尿病盛行率**。原稿所引之作者敘述「clinicians may be more willing to consider alpelisib use even in patients with an established diabetes with the aid of endocrinology consultation」保留 [RealWorld_Shen_2023.md]。
  - 支持「臨床實務確實在處理糖尿病病人」的另一項全文數據：該世代 **49 人（19.8%）**轉介內分泌科，standard care **30.0%** vs clinical trial **6.0%（p<.001）**[MSKCC_RealWorld_Shen_2023.md]。（原文 Discussion 另寫「nearly one-third」，與 Results 之 19.8% 不一致；本回顧採 Results 數字。）
- Liu 2022 中，基線糖尿病者的高血糖事件絕對率最高：**8/23（34.7%）** [RealWorld_Liu_2022.md]。
- 最嚴重的後果只有 case report 等級的描述：Leung 2022 記錄一位長期 T2DM 病人 rechallenge alpelisib 後「**within 24 hours of the first dose**」再度嚴重高血糖／DKA [DKA_Rechallenge_Leung_2022.md]；Li 2026 記錄 inavolisib 誘發之 fulminant-like diabetes 併 HHS [Inavolisib_HHS_Li_2026.md]。

**需要什麼研究才能回答**

- 一個**專為已知 T2DM 設計的前瞻性單臂或隨機試驗**，收案門檻放寬至 HbA1c 7.5–9.0%，主要終點為 grade 3–4 高血糖、DKA/HHS 發生率與 alpelisib/inavolisib RDI；須事先規定 insulin 使用的觸發條件與內分泌科共管路徑。METALLICA cohort C 是唯一嘗試（insulin-naïve、HbA1c <7.5%），但**結果未發表**。
- 一個**多中心 real-world registry**，前瞻收錄所有起始 PI3Kα inhibitor 的病人（不排除糖尿病），紀錄基線 HbA1c、降糖處方、DKA/HHS 事件與 time-on-therapy。
- 必須把「insulin-treated T2DM」與「T1DM」分開研究：兩者在 insulin feedback 的機轉推論上處境完全不同，而目前**所有**關鍵試驗都把兩者一起排除。

> ⚠ **臨床安全提醒（跨越所有證據層級）**：ADA Rec 9.35b 雖建議 insulin 保留給嚴重高血糖，但同一條文本身即載明其適用情境為「severe hyperglycemia **and hyperglycemic crises**」[guideline_ada_comparators.md]；FDA PIQRAY Table 3 之 Grade 3／4 兩列均明文要求「Administer intravenous hydration and consider appropriate treatment (e.g., intervention for electrolyte/**ketoacidosis**/**hyperosmolar** disturbances)」[label_alpelisib.md]。**不得以「避免 hyperinsulinemia」為由，延誤 DKA／HHS 所需的 insulin 與輸液。**
>
> **此立場現已有【L2】試驗層級的直接支持（先前僅有【L1】仿單與【L3】指引）**：SOLAR-1 AE 專文於 Discussion 逐字寫道「**However, short-term insulin is clearly effective for managing acute cases as well as more severe hyperglycemia associated with alpelisib and not controlled by oral antihyperglycemic medications alone.**」；且該試驗中實際有 **52 人使用 insulin，其中 33 人為長期使用（>2 天）**，並非全部符合仿單「1–2 天」的敘述 [SOLAR1_AE_Rugo_2020.md]。SOLAR-1 之 protocol Table 1 亦在 grade 3 明列「**Insulin may be used as rescue medication for 1 to 2 days**」，在 grade 3／4 均要求「**Consider/Consult with endocrinologist**」[SOLAR1_AE_Rugo_2020.md]。Shen 2023 同樣保留適應症：「although **insulin is still indicated for the management of severe hyperglycemia and/or ketoacidosis**」[MSKCC_RealWorld_Shen_2023.md]。

---

### I-2-3. Hyperinsulinemia 削弱抗腫瘤療效：前臨床明確，人體證據薄弱

**前臨床端（【L5】，證據強度高）**

Hopkins 2018（Nature）在**小鼠模型**中證明：systemic glucose-insulin feedback 足以在 PI3K inhibitor 存在下重新活化 PI3K 訊息；以飲食或藥物阻斷 insulin feedback 可大幅提升 efficacy/toxicity 比 [InsulinFeedback_Hopkins_2018.md]。Borrego 2024 之動物部分於 BN／ZDF／tumor-bearing nude rats 顯示 dapagliflozin 可改善 alpelisib 誘發之血糖與胰島素控制 [SGLT2i_Borrego_2024.md]。

**人體端（薄弱，且方向不一致）**

| 觀察 | 方向 | 來源 |
|---|---|---|
| **Shen 2023（全文 📄）：以高血糖狀態為 time-dependent covariate，PFS 之 HR = 0.98（95% CI 0.72–1.33）**；全世代中位追蹤 13.7 個月、中位 PFS 6.1 個月（95% CI 4.8–7.3）。依高血糖**分級**、BMI ≥25 vs <25、HbA1c ≥5.7% vs <5.7%、standard care vs trial、**是否因高血糖減量／停藥**分層，PFS 均無顯著差異 | ✗ 不支持 | 【L4】📄 [MSKCC_RealWorld_Shen_2023.md] |
| Rodon 2024：SOLAR-1 中 PIK3CA-mutant 病人，高風險 vs 低風險組之 median PFS **相近（11.0 vs 10.9 個月）** | ✗ 不支持 | 【L2/L4】📄 [RiskModel_Rodon_2024.md] |
| **SOLAR-1 原始數據（Rugo 2020 全文 📄，不再需要轉引）**：PIK3CA-mutant 者之 PFS 優勢在 **prediabetes/diabetes 族群 11.0 vs 5.6 個月，HR 0.66（95% CI 0.47–0.92）**；**normal 族群 10.9 vs 6.5 個月，HR 0.65（95% CI 0.42–1.02）**——兩者幾乎重疊 | ✗ 不支持 | **【L2】📄（本條原為「僅 abstract 📌 故只能轉引 Shen 2023」，現已直接自 SOLAR-1 全文取得）** [SOLAR1_AE_Rugo_2020.md] |
| **SOLAR-1 dose intensity 與 PFS（📄）**：PIK3CA-mutant 者中位 dose intensity 248 mg/日；**≥248 mg/日組中位 PFS 12.5 個月、<248 mg/日組 9.6 個月、placebo 5.8 個月** | ⚠ 不可用於本命題 | 【L2】📄 **原文未報告 HR／95% CI／p 值**，且為事後 landmark 式分組，存在 **guarantee-time／反向因果**（早進展者暴露短）偏誤；**不可解讀為「維持高劑量可因果改善 PFS」，更不可反推「降糖策略經由保住劑量而改善療效」** [SOLAR1_AE_Rugo_2020.md] |
| **INAVO120（Turner 2024 全文 📄）**：主論文**完全未報告**依高血糖狀態、依 metformin 使用、或依基線代謝狀態分層之 PFS；亦未報告任何 insulin／C-peptide／HOMA-IR 藥效動力學數據 | — 無資料 | 【L2】📄 **本回顧未取得可驗證來源**（不得以 SOLAR-1 之結果代替）[INAVO120_Turner_2024.md] |
| Noch 2023：GBM 病人中高血糖為 PFS 較差之獨立因子 | ✓ 支持 | 【L5/L4】📌 **僅 abstract；藥物為 buparlisib（pan-PI3K）、腫瘤為 GBM，不可外推** [InsulinFeedback_Noch_2023.md] |
| METALLICA：加 metformin 後 median PFS 7.3 個月，與 BYLieve cohort A（7.3 個月）相似 → 作者結論僅為「improves safety **without compromising** efficacy」 | 中性 | 【L2】📄 [METALLICA_LlombartCussac_2024.md] |
| INAVO120（EMA 4.8）：blood insulin increased 為 **Common，6.2%（all grades），Grade 3-4 為 0** | 描述性 | 【L1】📄 [label_inavolisib.md] |

**爭議點**

- 「應為了避免 hyperinsulinemia 而選 SGLT2i／避開 insulin」這一整條推理鏈，目前在人體端**只有機轉合理性與替代終點（血糖）證據，沒有以 PFS/OS 為終點的前瞻性驗證**。ADA 自己把 Rec 9.35b 標為 **E（expert consensus）**，且用詞為「**potential** impact on the efficacy」[guideline_ada_comparators.md]。
- **兩篇新落地的全文，其作者立場並不一致，且雙方都把急症治療排在機轉考量之前**：
  - SOLAR-1 AE 專文（Rugo 2020，【L2】📄）先寫「insulin sensitizers (e.g., metformin) **may be preferable to** insulin secretagogues (e.g., sulfonylurea, meglitinides) ... due to the insulin spikes and relative resistance noted with PI3K inhibitors」，並明言「Beyond metformin, **there is no second agent widely accepted as a standard**」、SGLT2i「**more data is needed to support their use**」；隨即以獨立段落強調「**However, short-term insulin is clearly effective for managing acute cases as well as more severe hyperglycemia associated with alpelisib and not controlled by oral antihyperglycemic medications alone.**」[SOLAR1_AE_Rugo_2020.md]
  - Shen 2023（【L4】📄）則寫「although **insulin is still indicated for the management of severe hyperglycemia and/or ketoacidosis**, it should be avoided when possible, as hyperinsulinemia can reactivate PI3K signaling despite use of a PI3K inhibitor」——同一句話中同時保留了適應症與避免原則 [MSKCC_RealWorld_Shen_2023.md]。
  - **⚠ 這兩段是本節最重要的臨床邊界：所有「避免 insulin」的論述都附帶「嚴重高血糖／酮酸中毒除外」的但書。把但書拿掉、變成一律避免 insulin，是對兩篇原文的誤讀。**
- **Shen 2023 對 metformin 本身的機轉質疑（【L4】📄，作者論述）**：「The primary mechanism of metformin action is activation of AMP-activated protein kinase, **which is abolished by PI3K inhibition**, although there may be some clinical efficacy at high doses. Additionally, **overlapping gastrointestinal adverse effects may limit metformin use and dose escalation** with alpelisib」[MSKCC_RealWorld_Shen_2023.md]。**這與 METALLICA 的立場形成張力，且與癌症病人的腹瀉／食慾不佳處境直接相關。**
- 反方向的實用性資料同樣不可忽視：Ismail 2026（📌 abstract）之全國 claims 分析顯示，**alpelisib 開始後才使用降糖藥的病人，time-on-therapy 反而較長（HR = 0.76, 95% CI 0.61–0.93, p = 0.008）** [Claims_Ismail_2026.md]。
  - ⚠️ **此處必須嚴格限縮讀法**：原文結論用的是「**associated with**」。「起始降糖藥」是**時間相依暴露**，這類 claims 分析天生存在 **immortal-time bias**（活得久、用藥久的人才有機會被開立降糖藥）與 **confounding by indication**。因此本結果**僅為關聯性觀察，不足以支持任何因果推論，亦不足以支持「積極控糖優先於機轉考量」之優先順序主張**。本回顧僅將其視為「真實世界中積極控糖與較長藥物暴露並存」的描述性訊號。
- 唯一直接檢驗此假說的人體試驗 TIFA（NCT05090358，randomized 3-arm：ketogenic diet vs low-carb diet vs canagliflozin）之 **actual enrollment 僅 15 人**，狀態 ACTIVE_NOT_RECRUITING，預估 primary completion 2026-10-08，**無結果公布**；且其主要終點是 12 週的 grade 3/4 hyperglycemia-free rate，**不是** PFS [trials_ongoing.md]。以 n=15 之規模，即使有結果也無法回答療效問題。
- 另一個直接檢驗 insulin 假說的試驗 NCT05753657（pioglitazone，監測 insulin 濃度導向治療）為 **Early Phase 1、單臂、n=30 estimated**，且登錄檔**未載 pioglitazone 劑量**（本回顧未取得可驗證來源）[trials_ongoing.md]。

**需要什麼研究才能回答**

- 一個以 **PFS 或 OS 為主要終點**的隨機試驗，將接受 alpelisib／inavolisib 的病人隨機分配至「insulin-sparing 降糖策略（metformin ± SGLT2i ± TZD）」vs「標準降糖策略（含必要時 insulin）」，並**預先設定 DKA/HHS 之安全停止規則**。
- 需要在人體中量測**腫瘤內 pAKT／pS6 之藥效動力學終點**（paired biopsy），以驗證 insulin feedback 是否真的在人體腫瘤內重新活化路徑——目前所有這類資料都來自小鼠 [InsulinFeedback_Hopkins_2018.md]。
- 需要以 C-peptide／fasting insulin／HOMA-IR 作為分層變數。Amelia-1 是本地檔案中唯一把 **HOMA-IR** 寫進收案風險定義的試驗，但為 pilot 且無結果 [trials_ongoing.md]。

---

### I-2-4. Real-world 高血糖率遠高於臨床試驗

**具體數字對比（全部可 grep）**

| 資料來源 | 族群 | Any-grade 高血糖 | Grade 3–4 | 註 |
|---|---|---|---|---|
| **FDA PIQRAY 仿單（SOLAR-1, n=284）**【L1】📄 | 排除 T1DM 與 uncontrolled T2DM | **65%** | G3 33%、G4 3.9% | ketoacidosis 0.7%（n=2）[label_alpelisib.md] |
| **EMA Piqray SmPC（同族群）**【L1】📄 | 同上 | **67.3%（191 人）** | G3 34.5%、G4 4.6% | 實驗室 glucose plasma increased 為 79.2%／39.4% [label_alpelisib.md] |
| **SOLAR-1 原始論文（Rugo 2020, n=284）— preferred term**【L2】📄 | 同上 | **63.7%（181 人）**（G1 11.3%、G2 15.8%） | **G3 32.7%（93 人）、G4 3.9%（11 人）** | placebo 組 9.8%（28 人）；**此為 preferred term** [SOLAR1_AE_Rugo_2020.md] |
| **SOLAR-1 原始論文 — AESI grouped term**【L2】📄 | 同上 | **65.8%（187 人）** | **grade ≥3 38.0%（108 人）** | placebo 10.5%（30 人）、grade ≥3 0.7%（2 人）。**⚠ 63.7%/32.7%/3.9% 與 65.8%/38.0% 為兩套定義，不可混用** [SOLAR1_AE_Rugo_2020.md] |
| **Shen 2023（MSKCC, n=247）**【L4】📄 | 未排除糖尿病 | **61.5%（152 人）** | **29.2%（72 人）**（G3 22.7%／56 人、G4 6.5%／16 人） | median time to onset **16 天**（定義：起始日至首次 glucose ≥140 mg/dL）；**原文未報告 IQR 或 range**；分級依 CTCAE v4.0 [MSKCC_RealWorld_Shen_2023.md] |
| **Shen 2023 — standard care 次族群（n=147）**【L4】📄 | 真實臨床 | **80.3%**（G1 10.2%、G2 30.6%） | **40.2%**（G3 29.3%／43 人、G4 10.9%／16 人） | **p<.001** vs 試驗族群 [MSKCC_RealWorld_Shen_2023.md] |
| **Shen 2023 — clinical trial 次族群（n=100）**【L4】📄 | 試驗內 | **34.0%**（G1 5.0%、G2 16.0%） | **13.0%**（G3 13 人、**G4 = 0 人**） | [MSKCC_RealWorld_Shen_2023.md] |
| **METALLICA（預防性 metformin, n=68）**【L2】📄 | 排除已用降糖藥者 | **44.1%（30 人）** | **5.9%（4 人）** | cohort A 33.3%／cohort B 70.0% [METALLICA_LlombartCussac_2024.md] |
| **FDA ITOVEBI 仿單（INAVO120, n=162）**【L1】📄 | HbA1C <6%、FBG <126 | **fasting glucose increased 85%** | **12%**（G3 12%、G4 0.6%） | 對照組 43%／0% [label_inavolisib.md] |
| **EMA Itovebi SmPC（同試驗，臨床 AE term）**【L1】📄 | 同上 | **59.9%** | G3 5.6%（G2 38.3%） | **與 FDA 之 85% 分母與定義不同，不可互換或相加** [label_inavolisib.md] |
| **INAVO120 原始論文（Turner 2024, n=162）— grouped term**【L2】📄 | 同上 | **58.6%（95 人）** | **grade 3 or 4 合併 5.6%（9 人）** | placebo 組 **8.6%（14 人）／grade 3-4 = 0**。**⚠ 原文只報合併值，未拆分 grade 3 與 grade 4；任何「inavolisib grade 4 = X%」之陳述在主論文中無可驗證來源** [INAVO120_Turner_2024.md] |

**⚠ 三個數字、三種定義，必須分開理解**：同一個 INAVO120 試驗現在有 **85%**（FDA，實驗室 fasting glucose increased）、**59.9%**（EMA，臨床 AE term）與 **58.6%**（NEJM 主論文，grouped term）三個 any-grade 數字；同一個 SOLAR-1 也有 **65%／67.3%／63.7%／65.8%** 四個。**跨試驗比較高血糖率之前，必須先確認是同一種 term 與同一個分母。**

**80.3% vs 34.0%（p<.001）這個 2.4 倍落差是本節最重要的臨床數字**，其 grade 3–4 對應落差為 **40.2% vs 13.0%（p<.001）**，且 **grade 4 為 10.9% vs 0 人** [MSKCC_RealWorld_Shen_2023.md]。Shen 2023 全文提出三個原因，並以敏感度分析逐一排除替代解釋：

1. **族群篩選**：standard care 組有更高比例 HbA1c ≥5.7%（**30.6% vs 15.0%, p=.041**），且更高比例在基線就測了 HbA1c（**72.1% vs 58.0%, p=.021**）；overweight/obese BMI 比例亦較高（**55.7% vs 48.0%, p=.09**）。試驗組多以 uncontrolled/insulin-dependent diabetes 或 FPG/HbA1c 門檻排除，該文 Table 2 逐一列出 6 個 MSKCC 試驗的排除條件（從「fasting glucose ≥140 mg/dL」到「HbA1c >5.9%」到「Diabetes 全排除」）[MSKCC_RealWorld_Shen_2023.md]。
2. **劑量差異**：standard care median RDI **277 mg/日（92% of intended dose）** vs trial **246 mg/日（99% of intended dose）**（**p<.001**）。作者的敏感度分析——**只比較試驗組中同樣用標準 300 mg/日的 n=33 次族群，差距依然顯著：80% vs 52%（p<.001）** [MSKCC_RealWorld_Shen_2023.md]。**劑量無法解釋全部落差。**
3. **監測與處置強度**：「hyperglycemia monitoring and management were more structured and intensive in some clinical trial protocols versus clinical practice」[MSKCC_RealWorld_Shen_2023.md]。**此假說現在有 SOLAR-1 全文的內部證據支持**：SOLAR-1 grade ≥3 高血糖之 **median time to onset 為 15 天（range 5–395 天，依 FPG 判定）**，而其原始排程為「screening、前 8 週每 2 週、之後每 4 週，另於前 4 週加驗 day 8 與 day 15」；**day 8 門診是收案 56.6% 後才由 protocol amendment 加入**。amendment 前後（前 50% vs 後 50% 隨機者）：any-grade **63.9% → 63.6%（幾乎不變）**、**grade 3/4 40.3% → 32.9%**、**因高血糖停藥 9.0% → 3.6%**、因 grade ≥3 AE 停藥 **18.1% → 7.9%** [SOLAR1_AE_Rugo_2020.md]。**即：監測與管理強度改變的是「嚴重度與停藥率」，而非「有沒有發生」——這正好解釋了為什麼 real-world 的落差在 grade 3–4（40.2% vs 13.0%）比在 any-grade（80.3% vs 34.0%）更具臨床意義。**
   - ⚠ **詮釋界線**：SOLAR-1 amendment 之前後比較**非隨機**，作者自述改善「may be attributed to the protocol amendment, **as well as other factors**」，且 amendment 同時收緊了 HbA1c 收案門檻（<8% → <6.5%），**族群改變與監測改變無法拆解** [SOLAR1_AE_Rugo_2020.md]。
4. **另一項先前無法查證、現在確定的落差：降糖藥使用率。** Shen 2023 全世代發生高血糖者 n=152 中，僅 **101 人（66.4%）**接受降糖治療；而 SOLAR-1 為 **163/187（87.2%）**接受降糖藥物。（**注意分母**：SOLAR-1 之「metformin 87.1%」其分母是 **163 名接受降糖藥者**，不是 187、更不是 284；此 87.1% 與上述 87.2% 為兩個不同的比率，數值接近純屬巧合，不可混用。）Shen 2023 逐字：「The use of any anti-hyperglycemic medication was **less frequent in our cohort (66%) than in the SOLAR-1 trial (87%)** ... **fewer patients in our cohort required 3 or more anti-hyperglycemic agents and fewer received insulin**」[MSKCC_RealWorld_Shen_2023.md][SOLAR1_AE_Rugo_2020.md]。
   - **這是一個弔詭且重要的訊號**：真實世界的高血糖**更嚴重**（G3–4 40.2% vs 13.0%），但**接受降糖治療的比例反而更低**（66% vs 87%）。**落差的一部分可能不是「病人更容易高血糖」，而是「處置不足」。**
   - 對應的處置強度數字：SOLAR-1 中 **67/163（41.1%）**只需一種降糖藥、**47/163（28.8%）**需要三種以上 [SOLAR1_AE_Rugo_2020.md]；Shen 2023 中 **69/101（68.3%）**只需一種、**9/101（8.9%）**需三種以上 [MSKCC_RealWorld_Shen_2023.md]。
   - Shen 2023 之降糖藥種類（分母 101）：metformin **90 人（89.1%）**、SGLT2i **20 人（19.8%）**、insulin **16 人（15.8%）**、DPP-4i **12 人（11.9%）**、TZD **8 人（7.9%）**、SU **6 人（5.9%）** [MSKCC_RealWorld_Shen_2023.md]。
   - 緩解時間：metformin 單方中位 **16 天（IQR 7–26）**；需在 metformin 之外加藥者中位 **26 天（IQR 14–64）**，顯著較長（**p=.024**）；首次介入用 metformin vs 其他藥物無顯著差異（p=.7）[MSKCC_RealWorld_Shen_2023.md]。
5. **因高血糖之劑量調整（Shen 2023 全文）**：暫停用藥至高血糖緩解 **66 人（26.7%）**、減量 **42 人（17%）**、**因高血糖停藥 11 人（4.5%）**；分組為 standard care 43 人（29.3%）vs clinical trial 10 人（10.0%），**原文所載 p=.3**（與百分比落差看似矛盾，逐字保留）[MSKCC_RealWorld_Shen_2023.md]。對照 SOLAR-1：alpelisib **dose reduction 59.2%、dose interruption 72.2%**（其中因 AE 者 57.7%／66.5%），但**原文未拆分「因高血糖」單獨導致之比率** [SOLAR1_AE_Rugo_2020.md]。

**另外兩組 real-world 數字**

- Liu 2022（n=491，10 種癌別，涵蓋 PI3K 與 AKT inhibitors）：12%（39/491）需中斷、6%（30/491）需減量、**2%（7/491）因高血糖住院**，僅 1 人永久停藥。住院者入院時平均血糖 **538 mg/dL**，median time from starting treatment to admission **14 天**（range 7–56）。在 AKT／α／pan-PI3K 使用者中，grade ≥2 高血糖為 **49.9%（174/349）**，G3 22%、G4 4% [RealWorld_Liu_2022.md]。**接受 β-／γ-／δ- 專一性 PI3K inhibitor 者無任何事件**——這是「不可把所有 PI3K inhibitors 當同一類」的直接數據支持。
- Ismail 2026（📌 abstract，全國 claims，n=546）：median time on therapy 僅 **87.5 天（IQR 28.0–173.7）**；降糖藥使用率由 alpelisib 前的 20.0% 上升至後的 34.3%；**新開始降糖藥者中 81.8% 用 metformin、44% 用 insulin** [Claims_Ismail_2026.md]。**44% 這個 insulin 使用比例，遠高於 INAVO120 仿單記載的 7%（11/162）** [label_inavolisib.md] 與 Delphi 共識「insulin 一般不適合作第一或第二線」的立場 [Delphi_Gallagher_2024.md]。真實世界的實際做法與共識建議之間存在明顯落差。

**需要什麼研究才能回答**

- 需要**前瞻性、非選擇性的 registry**（不設 HbA1c 上限），以標準化的驗糖排程（依仿單頻率）收案，才能得到「無篩選族群 + 標準監測」下的真實發生率。目前 80.3% 這個數字是回溯性、且血糖值「did not differentiate fasting versus non-fasting status」[RealWorld_Shen_2023.md]，可能高估；同時該世代 HbA1c 僅 164/247（66.4%）有值、BMI 235/247（95.1%）有值，基線代謝資料本身即不完整 [MSKCC_RealWorld_Shen_2023.md]。
- 需要一個**監測強度的隨機比較**（例如仿單頻率 vs CGM／每日 SMBG），主要終點為 grade 3–4 高血糖與住院率，以檢驗「落差是否由監測造成」。這是目前完全空白的問題。**SOLAR-1 的 amendment 前後比較（grade 3/4 40.3%→32.9%、因高血糖停藥 9.0%→3.6%，any-grade 幾乎不變）提供了此假說最強的人體訊號，但它是非隨機、且與收案門檻變更共線** [SOLAR1_AE_Rugo_2020.md]。
- 需要一個**「處置不足」的介入研究**：既然真實世界的高血糖更嚴重但降糖藥使用率反而更低（66% vs 87%）[MSKCC_RealWorld_Shen_2023.md][SOLAR1_AE_Rugo_2020.md]，應檢驗「結構化降糖處置路徑（含內分泌共管）」能否縮小 grade 3–4 落差——主要終點為 grade 3–4 高血糖與 alpelisib RDI，次要終點為住院與 DKA/HHS。
- 需要台灣／亞洲的 claims 或健保資料庫分析，以取得本地的 time-on-therapy 與降糖藥使用型態（見 I-2-7）。

---

### I-2-5. alpelisib 與 inavolisib 的仿單門檻不同，卻無頭對頭比較

**兩藥的【L1】條文差異（逐項對照）**

| 項目 | alpelisib (PIQRAY) | inavolisib (ITOVEBI) | 差異的臨床意義 |
|---|---|---|---|
| 起始劑量 | 300 mg QD **with food** | 9 mg QD，可與食物併服 | — |
| 減量階梯 | 300 → 250 → 200 → 停藥 | 9 → 6 → 3 → 停藥 | — |
| Re-escalation | 無條文 | **EMA 允許**回調至 9 mg；FDA 無條文 | 兩地做法不同 |
| **FPG >160–250 (G2)** | **不需調整劑量**；21 天未達標才降一階 | **Withhold 至 ≤160**，再以原劑量 resume | **inavolisib 在較低血糖即要求停藥** |
| **FPG >250–500 (G3)** | Interrupt；3–5 天內降至 ≤160 → 降一階 resume；21 天未達標 → **永久停藥** | Withhold；**≤7 天達標 → 原劑量**；**≥8 天達標 → 降一階**；30 天內再犯 → 降一階 | 恢復規則邏輯完全不同 |
| **FPG >500 (G4)** | 確認 >500 → **永久停藥** | 降至 ≤160 → 降一階 resume；**30 天內再犯**才永久停藥 | **alpelisib 的永久停藥門檻明顯較嚴** |
| 監測頻率 | 前 2 週每週 → 每 4 週 | q3d ×1 週 → q1w ×3 週 → q2w ×8 週 → q4w | inavolisib 早期監測密集得多 |
| CTCAE 版本 | v4.03 | FDA 表註 b 寫 **v5.0**、Table 4 表註 c 寫 **v4.03**；EMA 表註 a 寫 **v4.03**，4.8 節數字用 **v5.0** | 同一份 label 內版本標示不一致；**本回顧不對其原因作推論** [label_inavolisib.md §4] |
| metformin | FDA 明文列出並給 titration | **FDA 全文無 "metformin" 字樣**（已 grep 確認）；僅 EMA 寫「preferred initial agent」 | 兩地監管立場不同 |
| 腎功能減量 | 無（severe RI 影響 unknown） | **eGFR 30–<60 → 6 mg；<30 → 3 mg** | 對脫水／腹瀉病人影響重大 |
| 試驗血糖收案門檻 | controlled T2DM 可入組（基線 4.2% diabetic；全文版：diabetic 12/284＝4%）[SOLAR1_AE_Rugo_2020.md] | **HbA1C <6.0%、FPG <126 mg/dL；排除「需要持續治療」之 T1DM/T2DM；EMA 載僅 1 位 T2DM** [INAVO120_Turner_2024.md] | 外推風險 inavolisib 遠高於 alpelisib |

（劑量／監測／減量條文全部來自 [label_alpelisib.md] 與 [label_inavolisib.md]；收案門檻與族群數字另標示原始論文來源）

**兩試驗的族群差異，現在可以逐項量化（這是「不可把兩藥當同一類」的實證基礎）**

| 基線特徵 | SOLAR-1（alpelisib 組 n=284）📄 | INAVO120（全體 n=325）📄 |
|---|---|---|
| 中位年齡 | **62 歲**（placebo 組 64） | **54.0 歲**（range 27–79） |
| 中位體重 | 原文未報告 | **63.0 kg**（range 38–124） |
| BMI ≥30 | 74/284 有 BMI 分組資料（obese 74 人），**原文未給 kg/m² cut-off** | **57/325（17.5%）**；BMI 18.5–<25.0 **47.1%**；**BMI <18.5 5.5%** |
| 曾用 CDK4/6 inhibitor | **約 6%** | **僅 4/325（1.2%）；98.8% 為 CDK4/6i-naive** |
| 治療線別定位 | endocrine resistance 約 86%，屬後線 | **輔助內分泌治療期間或完成後 12 個月內復發之一線設定；de novo 轉移被排除** |
| 腫瘤負荷 | 肺／肝轉移 49% | **≥3 器官轉移 51.4%、內臟轉移 80.0%、肝轉移 51.7%** |
| 亞洲人比例 | 原始論文未於本地全文報告（見 I-2-7） | **124/325（38.2%）** |

（[SOLAR1_AE_Rugo_2020.md]／[INAVO120_Turner_2024.md]）

> ⚠️ **稽核提醒**：INAVO120 **不是** CDK4/6i 治療中或治療後進展的族群。其 enrichment 條件是**內分泌治療抗性**（primary resistance 111/325＝34.2%、secondary 213/325＝65.5%），且 98.8% 未曾用過 CDK4/6i，原文自述「recruitment primarily occurred before adjuvant CDK4/6 inhibitors were available」[INAVO120_Turner_2024.md]。任何相反敘述與原文不符。

**爭議點**

1. 這些門檻差異**不是**基於兩藥的比較性資料，而是兩個獨立開發計畫各自的試驗設計結果。`label_inavolisib.md` §14.5 明白列為缺口：「**inavolisib 與 alpelisib 的頭對頭比較：無此類 label 資料，本回顧未取得可驗證來源。**」
2. 兩藥的高血糖率**在數學上不可比較**：alpelisib 65%（FDA, AE-based）／79%（實驗室 glucose increased）／**63.7%（原始論文 preferred term）／65.8%（原始論文 AESI grouped term）** vs inavolisib 85%（實驗室 fasting glucose increased）／59.9%（EMA, AE term）／**58.6%（原始論文 grouped term）**。連同一個藥的 FDA 與 EMA 數字都因分母與定義不同而不可互換 [label_inavolisib.md §8.2 明文警告][SOLAR1_AE_Rugo_2020.md][INAVO120_Turner_2024.md]。加上兩者的基線族群完全不同（inavolisib 只收 HbA1C <6.0%、中位年齡小 8 歲、中位體重 63 kg），**任何「哪一個比較不會高血糖」的陳述在目前都沒有可驗證來源。**
   - **INAVO120 作者自己就下了這個警語**（逐字）：「**Cross-trial comparisons should be made with caution owing to differences in trial design, patient populations, and analysis and reporting methods.**」[INAVO120_Turner_2024.md]
   - 該段落中出現的 alpelisib 停藥率 **25.0%**、everolimus **19%**、capivasertib **13.0%**（相對於 inavolisib 的 **6.8%**）是 **INAVO120 作者轉引他文**的數字，**引用時必須標示為「INAVO120 discussion 內轉引」**，不得直接當成 SOLAR-1／CAPItello-291 之原始數據 [INAVO120_Turner_2024.md]。（SOLAR-1 AE 專文本身亦記載其 AE 導致停藥率 alpelisib 25.0%、placebo 4.2%，引自主論文 [SOLAR1_AE_Rugo_2020.md]。）
3. 併用藥也不同：inavolisib 為三合一（+ palbociclib + fulvestrant），alpelisib 為 + fulvestrant [label_inavolisib.md][label_alpelisib.md]。palbociclib 的血液毒性與 28 天 21/7 週期會影響 dose interruption 的判讀，使兩者的「因高血糖中斷率」（inavolisib 28% vs alpelisib 之 dose reduction 29%）無法直接對照。
   - **可查證的劑量強度對照**：INAVO120 中位 RDI 為 inavolisib **95.8%**、palbociclib **87.3%**、fulvestrant **100.0%**（placebo 組 palbociclib 88.4%），中位服藥時間 inavolisib **9.2 個月**；**因高血糖導致 inavolisib 減量者僅 2.5%，且是唯一達 ≥2% 的減量原因** [INAVO120_Turner_2024.md]。對照 SOLAR-1：alpelisib 中位暴露僅 **5.5 個月（range 0–30.8）**，dose reduction **59.2%**、dose interruption **72.2%** [SOLAR1_AE_Rugo_2020.md]。
   - ⚠ **但這組對照不能解讀為「inavolisib 比較好耐受」**：兩試驗的族群（年齡、線別、體位、血糖收案門檻）與 AE 分級／報告方式皆不同，且 **INAVO120 原文未報告「因高血糖而 dose interruption」與「因高血糖而永久停藥」的比率**（相關細節在 Table S3 補充附錄，本地全文檔不含補充附錄）[INAVO120_Turner_2024.md]；SOLAR-1 亦未拆分「因高血糖」單獨導致之減量／中斷比率 [SOLAR1_AE_Rugo_2020.md]。**兩邊的關鍵分母都缺，比較無法成立。**
4. **時序資料只有 alpelisib 有，inavolisib 完全沒有。** SOLAR-1 全文報告 grade ≥3 高血糖 **median time to onset 15 天（range 5–395）**、改善 ≥1 grade 之中位 **6 天（range 4–7）**，且平均 FPG「**peaked within the first 2 weeks**」後在降糖藥支持下回落趨近基線，HbA1c 則「gradual increase ... remained slightly elevated throughout」[SOLAR1_AE_Rugo_2020.md]。**INAVO120 主論文全文完全未報告 hyperglycemia 的 median time to onset、time to resolution 或首次發生之週期分佈**（已 grep "time to onset" 確認）[INAVO120_Turner_2024.md]。**因此 inavolisib 的「前 1–2 週是高峰」之說法，在本回顧中沒有可驗證來源，不得由 alpelisib 移植。**
5. 唯一在同一個 protocol 內併列兩類藥的是 Amelia-1（evexomostat + alpelisib **或** capivasertib），但它是 pilot、無結果，且**兩組的收案 HbA1c 門檻本來就不同**（≤6.4% vs <8%）[trials_ongoing.md]。這反而證明了「不同藥物需要不同血糖門檻」是設計者的共識，而非可互換。

**需要什麼研究才能回答**

- 嚴格意義上的頭對頭 RCT 在商業上幾乎不可能（兩藥適應症有重疊但不完全相同：inavolisib 限 endocrine-resistant、adjuvant ET 後復發）。務實的替代是：
  - **共用一致定義的 pooled safety analysis**（統一以 CTCAE v5.0 的 AE term、統一以 fasting glucose、統一分母），由監管機關或獨立學術團體主導。
  - **以 propensity score 配對的跨試驗比較**，配對變數至少含 baseline FPG、HbA1c、BMI、age（即 Rodon 2024 之風險模型變數）[RiskModel_Rodon_2024.md]。
  - 一個**前瞻性 CGM 子研究**，同時收兩藥病人，比較血糖曲線的形狀（peak 時間、持續時數）。目前僅有 case-level 描述：alpelisib 之血糖上升在服藥後約 4 小時開始、持續約 22 小時 [DKA_Carrillo_2021.md]；FGM 顯示服藥後 4 小時內有明顯下降段 [FGM_PlaPeris_2022.md]。試驗層級的時序資料亦僅 alpelisib 有（grade ≥3 中位 15 天發生、6 天改善；FPG 於前 2 週達峰）[SOLAR1_AE_Rugo_2020.md]。**inavolisib 之對應時間曲線（無論 CGM 層級或試驗層級）本回顧未取得可驗證來源；INAVO120 主論文全文亦未報告。**

---

### I-2-6. CGM、ketogenic diet、SGLT2i：三者在此適應症皆無 RCT

#### (a) CGM

- **無任何 RCT。** 本地檔案中的 CGM 相關研究：NCT06083038（observational、單中心、**actual enrollment 8 人**、無結果公布）、AAREN NCT05107388（單組、40 人 estimated、狀態 UNKNOWN、無結果）、NCT06354088（Columbia，**健康志願者**、非癌症族群、單劑 alpelisib 之代謝生理學研究）[trials_ongoing.md]。
- 支持 CGM 的只有 case-level 資料：Pla-Peris 2022（FGM）、Carrillo 2021（CGM tracing）、Blow 2021（CGM + insulin pump, n=3）[FGM_PlaPeris_2022.md][DKA_Carrillo_2021.md][VLCD_SGLT2i_Blow_2021.md]。
- 指引立場分歧：Tankova 2022【L3】寫「**If available**, self-monitoring and continuous glucose monitoring devices should be prescribed or recommended」[Consensus_Tankova_2022.md]；Delphi 2024【L3】的監測建議則完全以 **fingerstick FBG／point-of-care／at-home glucose monitor** 表述，未把 CGM 列入建議 [Delphi_Gallagher_2024.md]；ADA Rec 2.21【L3】用的是 **random plasma glucose** [guideline_ada_comparators.md]。
- 另一個實務障礙：NCT06083038 明文排除「high-dose vitamin C（≥1 g/日口服或 IV）」，因其干擾 CGM 讀值 [trials_ongoing.md]——癌症病人使用高劑量維生素 C 並不罕見。
- Leung 2022 在 rechallenge 情境下建議「Continuous glucose monitoring **and hospital admission** are recommended during rechallenge」，但此為【L4】case report 之作者建議 [DKA_Rechallenge_Leung_2022.md]。

**需要什麼研究**：以 CGM 導向處置 vs 仿單排程 SMBG 的**隨機比較**，主要終點為 grade 3–4 高血糖發生率與 time-in-range，次要終點為 alpelisib/inavolisib RDI 與住院率。樣本數須足以偵測 real-world 的高事件率（依 Shen 2023 的 40.2% grade 3–4 估算）。同時須驗證 CGM 在此情境的**準確度**（PI3Kα inhibitor 造成的急遽血糖波動 + 癌症病人常見的水腫／脫水，皆可能影響 interstitial 讀值——本回顧未取得任何驗證 CGM 準確度的來源）。

#### (b) Ketogenic / 極低碳水飲食 —— **兩份【L3】共識直接互相矛盾**

| 立場 | 內容 | 來源 |
|---|---|---|
| 傾向支持 | 「it **may also be appropriate** to recommend a ketogenic diet (total carbohydrate intake of <50 g/day) and/or pre-treatment fasting (e.g., >12 hours)」 | Delphi Gallagher 2024【L3】[Delphi_Gallagher_2024.md] |
| **明確反對** | 「**we do not recommend very-low-carbohydrate diets, but rather moderate carbohydrate restriction**」 | Tankova 2022【L3】[Consensus_Tankova_2022.md] |

Tankova 的反對理由**具體且與癌症病人處境直接相關**，值得完整轉述 [Consensus_Tankova_2022.md]：
1. 「such diets are not usually recommended as they may **not be well tolerated or sustainable**」——對本來就有食慾不佳、體重下降的病人尤其成立（SOLAR-1：decreased appetite 36%、weight decreased 27%（G3-4 3.9%）[label_alpelisib.md]；INAVO120：decreased appetite 24%、decreased weight 17%（G3-4 3.7%）[label_inavolisib.md]）。
2. 「can lead to **positive urine ketones, which may be misinterpreted as alpelisib-induced ketoacidosis**」——這會直接干擾急症判讀，尤其在同時使用 SGLT2i 時。
3. 引述之前臨床研究顯示 ketogenic diet 併 PI3K inhibitor「led to **drastic deterioration in the general health condition** of the experimental animals」，且「The ketogenic diet resulted in the **best therapeutic impact on tumor xenotransplants, but the worst effect on animal well-being**」。
4. 「ketones in the blood are a **strict indication for insulin therapy initiation**」。

**唯二的介入性資料**：TIFA（NCT05090358，ketogenic vs low-carb vs canagliflozin，**actual n=15**、無結果）[trials_ongoing.md]；copanlisib + ketogenic diet（NCT04750941，**TERMINATED，actual n=1**）[trials_ongoing.md]。後者更不可外推——copanlisib 為靜脈注射之 pan-PI3K（α/δ），其高血糖型態與口服每日連續給藥的 alpelisib 不同 [trials_ongoing.md §9]。

**需要什麼研究**：一個以 **grade 3–4 高血糖為主要終點、以體重變化與 PRO 為共同主要終點**的隨機飲食試驗（低碳水 60–130 g/日 vs 標準飲食 vs ketogenic <50 g/日），必須在**接受 PI3Kα inhibitor 的癌症病人**中進行、有營養師介入與依從性客觀量測（血酮），並預先規定「血酮升高時如何與 DKA 鑑別」的流程。TIFA 的 n=15 完全不足。

#### (c) SGLT2i

- **無 RCT。** 最強的人體資料是 Borrego 2024 的 **propensity-score matched 跨試驗次分析**：SOLAR-1 + BYLieve 中使用 SGLT2i 者 **n=19**，配對對照 **n=74**（依 age、BMI、HbA1c、FPG 配對）。結果：grade ≥3 高血糖事件發生率 0.00461 vs 0.02272（**4.9 倍差**）；time to first grade ≥3 event HR **0.294**（相對風險降低 70.6%）；導致劑量調整／中斷／停藥之高血糖事件率 0.00922 vs 0.05917（**6.4 倍差**），HR **0.643** [SGLT2i_Borrego_2024.md]。
  - **限制**：n=19、非隨機、且該 19 人中 73.7% 為 prediabetic、15.8% 為 diabetic——與一般 alpelisib 族群的代謝分布不同 [SGLT2i_Borrego_2024.md]。
- 支持性【L4】：Liu 2022 之校正分析顯示 SGLT2i 降糖幅度最大（−48 mg/dL, 95% CI −75 至 −21）[RealWorld_Liu_2022.md]；Shen 2023 顯示內分泌科會診與 SGLT2i 處方顯著相關（**p=.007**），但同時指出「Consultation with an endocrinologist and addition of an SGLT2 inhibitor to metformin were **late interventions** for persistent and higher-grade hyperglycemia, which likely accounts for the association of these management strategies with alpelisib dose reduction and/or discontinuation and longer time to resolution」——即 SGLT2i 的使用本身可能是嚴重度的標記，存在 confounding by indication [MSKCC_RealWorld_Shen_2023.md]。
- **反向訊號（新落地全文提供，先前無法引用）**：Shen 2023 中接受 **SGLT2i 單方治療者僅 3 人**，其高血糖緩解時間與 metformin 單方**無顯著差異（p=.5）**；SGLT2i 處方在該世代並與 **alpelisib 減量／停藥顯著相關（p=.007）** [MSKCC_RealWorld_Shen_2023.md]。**因此「SGLT2i 比 metformin 更快降糖」這個【L4】論點，在 MSKCC 世代中並未被複製；n=3 不足以下任何結論，但同樣不足以支持相反方向。**
- **SOLAR-1 全文對 SGLT2i 的立場**（【L2】作者論述）：「Beyond metformin, **there is no second agent widely accepted as a standard** to treat hyperglycemia due to PI3K inhibitors. Some consider ... SGLT2 inhibitors to be the best choice, **however, more data is needed to support their use**」；且該試驗**未報告 SGLT2i、DPP-4i、GLP-1 RA、SU 等個別藥物之實際使用人數**（僅 metformin 87.1%、insulin 52 人有數字）[SOLAR1_AE_Rugo_2020.md]。
- **安全性訊號（本回顧認為被低估）**：
  - Liu 2022：僅 15 人（含 12 位新使用者）在 PI3K/AKT inhibitor 期間使用 SGLT2i，其中**就出現 1 例 euglycemic DKA**（VBG 7.26、bicarbonate 13、anion gap 21、ketonuria；當時併用 empagliflozin 10 mg QD + metformin 1000 mg BID）[RealWorld_Liu_2022.md]。
  - Bowman 2017：taselisib 併 canagliflozin 之 ketoacidosis case report [EuglycemicDKA_Bowman_2017.md]。
  - **兩份仿單皆未針對 SGLT2i + PI3Kα inhibitor 之 ketoacidosis 交互風險作特別警語**，儘管 04/2026 FDA ITOVEBI label 已納入 postmarketing fatal ketoacidosis [label_inavolisib.md §14.6]。
  - Delphi 專家組「did not recommend requiring ketone monitoring while on SGLT2i therapy ... but this monitoring can be done per provider discretion」[Delphi_Gallagher_2024.md]——此立場與上述訊號、以及 Danne 2019 之 SGLT inhibitor DKA 風險管理國際共識【L3】[DKA_Danne_Consensus_2019.md] 之間存在張力。
- EPIK-B4（唯一登錄為 PREVENTION 之隨機試驗，dapagliflozin + metformin XR vs metformin XR）**終止於 n=2** [trials_ongoing.md]。

**需要什麼研究**：一個 **metformin vs metformin + SGLT2i** 的隨機試驗，主要終點為 grade ≥3 高血糖，**安全性共同主要終點必須是 ketoacidosis（含 euglycemic DKA）**，並強制血酮監測與病人衛教。此試驗必須明確納入癌症病人特有的 DKA 誘因：腹瀉、嘔吐、食慾不佳、脫水與急性腎損傷（alpelisib serious AKI 2.5%）[label_alpelisib.md][label_inavolisib.md]。**兩篇原始論文的逐字數字（現可 grep）**：SOLAR-1 alpelisib 組 diarrhea **164/284（57.7%，G3 6.7%）**、nausea **44.7%**、decreased appetite **35.6%**、vomiting **27.1%**、decreased weight **26.8%（G3 3.9%）**、stomatitis 24.6% [SOLAR1_AE_Rugo_2020.md]；INAVO120 inavolisib 組 diarrhea **78/162（48.1%，G3-4 3.7%）**、nausea **27.8%**、decreased appetite **23.5%**、stomatitis/mucosal inflammation **51.2%（G3-4 5.6%）**，且該族群中位體重僅 63.0 kg、5.5% 為 BMI <18.5 [INAVO120_Turner_2024.md]。**在一個本就會腹瀉、噁心、食慾差、體重下降的族群中疊加 SGLT2i，euglycemic DKA 不是理論風險。** 兩篇原始論文均**未報告脫水事件率或腎功能軌跡**，此為設計新試驗時必須主動收集的資料。EPIK-B4 的失敗顯示這類試驗**收案極為困難**，可能需要國際多中心與 registry-based randomization 設計。

---

### I-2-7. 亞洲／台灣族群資料缺乏

**現有的亞洲代表性（僅為人口統計數字，非次族群療效／安全性分析）**

| 試驗／研究 | 亞洲人比例 | 來源 |
|---|---|---|
| INAVO120（仿單版） | **38% Asian**（59% White、2.5% unknown、0.6% Black）；median age 54 歲 | 【L1】📄 [label_inavolisib.md §9] |
| **INAVO120（Turner 2024 主論文 Table 1 📄）** | **Asian 124/325（38.2%）**（inavolisib 組 61/161＝37.9%、placebo 組 63/164＝38.4%）；White 191（58.8%）、Black 2（0.6%）；median age **54.0 歲** | 【L2】📄 [INAVO120_Turner_2024.md] |
| SOLAR-1（FDA approval summary） | Asian 74/335（22%） | 【L1-adjacent】📄 [FDA_Alpelisib_Narayan_2021.md] |
| **SOLAR-1 AE 專文（Rugo 2020）** | **原文未報告種族組成**；僅載中位年齡 62／64 歲、endocrine resistance 約 86%、肺／肝轉移 49%、曾用 CDK4/6i 約 6% | 【L2】📄 **本文未取得亞洲人比例**（22% 之數字來自 FDA approval summary，非本文）[SOLAR1_AE_Rugo_2020.md] |
| CAPItello-291（capivasertib，**AKT inhibitor，僅供對照**） | Asian 95/355（26.8%）vs 94/353（26.6%） | 【L2】📄 [CAPItello291_Turner_2023.md] |
| BELLE-2（buparlisib） | Asian 132（23%）／153（27%） | 【L2】📄 [BELLE2_Baselga_2017.md] |
| Shen 2023（MSKCC real-world） | Asian 22/247（**8.9%**）；White 198（80.1%）、Black 11（4.5%）、Other 16（6.5%），組間 p=.2 | 【L4】📄 [MSKCC_RealWorld_Shen_2023.md] |
| Inavolisib phase I/Ib (Jhaveri 2024) | Asian 1（3.0%） | 【L2】📄 [Inavolisib_Jhaveri_JCO_2024.md] |
| GO39374 | Asian 全體 5/193（2.6%） | 【L2】📄 [GO39374_Gambardella_2025.md] |

**核心爭議：以 BMI ≥30 作為風險分層門檻，在亞洲族群可能失效**

- EMA Piqray SmPC 與 EMA Itovebi SmPC 皆以 **BMI ≥30 kg/m²** 作為高血糖風險因子與加強監測的觸發條件 [label_alpelisib.md][label_inavolisib.md]；FDA PIQRAY §5.3 亦以「obesity (BMI ≥ 30)」列示 [label_alpelisib.md]；EPIK-B4 登錄之高風險定義同樣用 BMI ≥30 [trials_ongoing.md]。
- 但 real-world 資料顯示，**在 BMI 中位數僅 25.4 kg/m²（IQR 22.6–29.0）的族群中，風險依然顯著**：Shen 2023 全世代 median BMI **25.4 kg/m²**、BMI 分層 <25 為 105 人（44.7%）、25–29.9 為 82 人（34.9%）、**≥30 僅 48 人（20.4%）**；而 **baseline BMI ≥25 kg/m²**（非 ≥30）即與 any-grade（**p=.036**）與 grade 3–4（**p<.001**）高血糖顯著相關，連續變項之 baseline BMI 亦顯著（**p=.029**）[MSKCC_RealWorld_Shen_2023.md]。Liu 2022 同樣以 **BMI >25** 為切點，得到最大的 odds ratio（**OR 5.4, 95% CI 2.3–16.0**）[RealWorld_Liu_2022.md]。
- **這兩篇的切點（≥25）比仿單的 ≥30 低了 5 個單位，而 ≥25 恰好接近亞洲人常用的過重／肥胖切點。** 換言之，**若在台灣直接套用 BMI ≥30 作為「加強監測」的觸發條件，將漏掉大量實際高風險的病人。**
- **兩篇新落地的試驗全文，從不同方向削弱了「BMI ≥30」作為單一觸發條件的鑑別力**：
  - **SOLAR-1（alpelisib）之 any-grade 高血糖對 BMI 並非單調遞增**：normal BMI 63/110（**57.3%**）、overweight 62/84（**73.8%**）、**obese 50/74（67.6%，反而低於 overweight）**；**只有在 grade 3（24.5% → 35.7% → 39.2%）與 grade 4（2.7% → 3.6% → 9.5%）才呈單調遞增** [SOLAR1_AE_Rugo_2020.md]。**即 BMI 預測的是「嚴重度」而非「發生與否」**；且原文**未給 BMI 分組之 kg/m² cut-off、亦無任何 OR/HR/p 值**，不可過度量化。
  - **INAVO120（inavolisib）之 BMI ≥30 vs <30 差距極小**：**65.5% vs 56.8%**，原文自述為「**slightly higher**」，且**未報告 BMI 分層下的 grade 3/4 率**；該試驗 BMI ≥30 者本來就只有 17.5%、BMI 18.5–<25.0 達 47.1%、**BMI <18.5 者 5.5%**，中位體重僅 **63.0 kg**、亞洲人 38.2% [INAVO120_Turner_2024.md]。**這是一個體位偏瘦、亞洲人比例接近四成的族群，其 5.6% 的 grade 3/4 率不可外推至肥胖或糖尿病病人。**
- 不過須注意：Shen 2023 亦指出 **BMI 與 HbA1c 有顯著交互作用（p=.005）**，且同時放入模型時**只有 baseline HbA1c 維持顯著（p<.001）**；baseline glucose 亦顯著（p<.001）[MSKCC_RealWorld_Shen_2023.md]。⚠ 該文統計法為 **Pearson's χ² test，非多變項 logistic regression**，「交互作用」與「同入模型」之模型型態原文未進一步指明，且**未報告任何 OR 與 95% CI**——因此此結論的強度應視為**描述性關聯**。即便如此，它仍支持「**以 HbA1c 而非 BMI 作為主要分層依據**」的務實做法，且 HbA1c 沒有族群切點爭議。
- 亞洲人 vs 非亞洲人的毒性差異，本地檔案中僅有**方向性、未量化**的敘述：Jhaveri 2026 之 pooled safety review 記載 any-grade hyperglycemia「numerically higher in ... **non-Asian patients versus Asian patients**」，而 rash 與 stomatitis 則是 Asian 較高、diarrhea 是 Asian 較低 [ToxMgmt_Jhaveri_2026.md]。INAVO120 safety analysis 則寫「Data were largely **comparable across regions** and ages」[INAVO120_Safety_Im_2026.md]。**兩者未必矛盾（前者為跨試驗 pooled、後者為單一試驗），但都不是預先設定的次族群分析，不足以支持任何族群特異的門檻調整。**

**台灣特有的、可立即執行的落差**

1. **台灣中文仿單版本落後。** 本地落地之 TFDA 愛克利（PIQRAY）中文仿單為**衛部藥輸字第 027995 號、版本日期 2022-09-22**，早於 FDA 的 01/2024 改版，因此**不含 metformin 預防性給藥（METALLICA）段落** [label_alpelisib.md §7、§9]。也就是說，**台灣醫師若僅依中文仿單行事，會看不到 FDA 已納入的 metformin premedication 條文**。是否存在更新版台灣中文仿單，**本回顧未取得可驗證來源**。
2. **TFDA inavolisib 仿單完全未取得。** `label_inavolisib.md` §14.1 明列：「TFDA（台灣食藥署）inavolisib 仿單：本回顧未取得可驗證來源。本檔案不對台灣核准狀態、健保給付或中文仿單內容作任何斷言。」
3. **台灣健保給付規定原文非本次擷取範圍**，本回顧未收錄 [label_alpelisib.md §10.5]。
4. **無任何台灣或亞洲的 real-world 高血糖研究落地。** 本地全文中，real-world 研究全部來自美國單中心（MSKCC，Asian 僅 8.9%）、法國 EAP 或美國 claims [inventory.md][MSKCC_RealWorld_Shen_2023.md]。
5. **INAVO120 雖有 38.2% 亞洲人，卻無任何依種族分層的高血糖分析。** 主論文全文的次族群分析只呈現 PFS（年齡 <65 vs ≥65 等），**未報告依種族分層之 hyperglycemia 發生率** [INAVO120_Turner_2024.md]。**這是最可惜的一項空白：全球 phase 3 中亞洲代表性最高的試驗，卻沒有把這個代表性用在血糖終點上。**

**需要什麼研究才能回答**

- **台灣（或東亞多國）的前瞻性 registry**，收錄所有起始 alpelisib／inavolisib 的病人，主要終點為 grade 3–4 高血糖發生率，並**預先設定以 BMI ≥25 vs ≥30 兩種切點分別分析**，直接檢驗西方仿單的風險分層在本地的鑑別力。
- **對 INAVO120 進行預先未設定但可執行的 post-hoc 種族次族群安全性分析**：該試驗有 124 位亞洲病人，是目前唯一有足夠亞洲樣本數可回答「亞洲人的 PI3Kα inhibitor 高血糖風險是否不同」的 phase 3 資料庫 [INAVO120_Turner_2024.md]。此分析成本近乎為零，卻能直接填補本節最大的缺口。
- **以 HbA1c 為主軸重新建構風險模型並在亞洲族群外部驗證**：Rodon 2024 的 5 變數模型（FPG、BMI、HbA1c、monocytes、age）在 X2101+SOLAR-1 建立、BYLieve 驗證 [RiskModel_Rodon_2024.md]，但**未有亞洲族群的外部驗證**。這是最容易執行、CP 值最高的一項研究。
- **健保資料庫分析**，比對台灣的 time-on-therapy 與降糖藥使用型態，對照 Ismail 2026 的美國數字（median TOT 87.5 天、降糖藥使用 20.0%→34.3%）[Claims_Ismail_2026.md]。
- 若 CAPItello-291 之中國 cohort（`citations_round1.md` 中列為 `CAPItello291_China_Hu_2025`，Nat Commun 2025）能取得全文，可作為 AKT inhibitor 在東亞族群的對照資料 —— **但該篇本回顧未落地全文，且 capivasertib 非 PI3Kα inhibitor，不可直接外推** [citations_round1.md]。

---

### I-2-8. 長期代謝後果：停藥後是否完全回復、心血管風險

**目前僅有的可驗證資料（且範圍極窄）**

| 觀察 | 數字 | 限制 |
|---|---|---|
| FDA PIQRAY：停 alpelisib 後繼續 fulvestrant 且原有 FPG 升高者（n=54），**96%（n=52）FPG 回到基線** | 【L1】📄 [label_alpelisib.md] | 分母僅 54 人；**只看 FPG，未報告 HbA1c**；追蹤期間未載明 |
| EMA Piqray：同類分析 n=61，**93.4%（n=57）**回到基線 | 【L1】📄 [label_alpelisib.md] | 同上；FDA 與 EMA 分母不同 |
| GO39374（inavolisib）：具風險因子者高血糖「**was reversible (86%)**」 | 【L2】📄 [INAVO120_Safety_Im_2026.md] | 「reversible」之操作型定義未於本地檔案中取得 |
| INAVO120 長期安全性：162 人中 **69 人（42.6%）**接受 inavolisib ≥1 年；「No adverse events leading to withdrawal of study treatment occurred in the long-term safety population」 | 【L2】📄 [INAVO120_Safety_Im_2026.md] | 為治療**期間**之安全性，**非停藥後的代謝追蹤** |
| **SOLAR-1（Rugo 2020 全文 📄）：「All patients who developed hyperglycemia had grade 0 or 1 hyperglycemia following discontinuation of alpelisib.」** | 【L2】📄 [SOLAR1_AE_Rugo_2020.md] | **這是本回顧目前最強的可逆性證據，但它只講「停藥後降到 grade 0/1」**：原文**未報告回復所需之中位天數**、未報告停藥後 HbA1c、未報告追蹤時長。可 grep 到的僅有 grade ≥3 事件「改善 ≥1 grade」之中位 **6 天（range 4–7 天）**——**這是治療中的改善，不是停藥後的恢復，兩者不可混用** |
| Carrillo 2021（case report）：停 alpelisib 後 14 天內血糖正常化、不再需要 insulin 或 empagliflozin；HbA1c 由 9.4% 降至 3 個月後的 6.2% | 【L4】📄 [DKA_Carrillo_2021.md] | n=1 |
| **INAVO120（Turner 2024 全文 📄）：停藥後代謝追蹤 — 完全未報告** | 【L2】📄 [INAVO120_Turner_2024.md] | 全文未報告治療期間 FPG／HbA1c 之縱貫變化，亦無停藥後之血糖資料。**inavolisib 之可逆性在主論文層級無可驗證來源** |

**明確的空白**

1. **無任何研究以「停藥後 HbA1c」或「停藥後新診斷 T2DM 累積發生率」為終點。** 仿單只回答了「FPG 有沒有回到基線」，而且只在一個高度選擇的次族群（停 alpelisib 但續用 fulvestrant 者）中回答。**對於「治療期間曾發生 grade 3–4 高血糖的病人，停藥一年後有多少比例成為永久性糖尿病」——本回顧未取得可驗證來源。**
2. **無任何心血管結局資料。** 本地全文中，沒有任何一篇報告 PI3Kα inhibitor 相關高血糖之 MACE、心衰竭或腎臟結局。**本回顧未取得可驗證來源。** 值得註記的是，INAVO120 之 grade 5（致死）AE 在 inavolisib 組為 3.7%，其中包含 **acute coronary syndrome、cerebral hemorrhage、cerebrovascular accident 各 1 例**，但原文明載「**None of the deaths were considered by the investigator to be related to the trial agents**」，且**未做任何與高血糖之關聯分析** [INAVO120_Turner_2024.md]。**不可將此解讀為高血糖相關之心血管訊號。**
2b. **兩篇關鍵試驗全文都「未報告」DKA／HHS，這與「未發生」不同。** SOLAR-1 AE 專文經 grep `ketoacid`／`DKA`／`HHNK`／`hyperosmolar` **均為 0 命中**，且原文亦未聲明無此類事件 [SOLAR1_AE_Rugo_2020.md]；INAVO120 主論文全文同樣未出現 ketoacidosis／DKA／HHS 相關詞彙，致死 AE 清單中不含 hyperglycemia [INAVO120_Turner_2024.md]；Shen 2023 僅在敏感度分析中提及「排除發生 DKA 的 standard care 病人」，**未給出 DKA 人數或百分比**，且全文未提及 HHS [MSKCC_RealWorld_Shen_2023.md]。**因此正確表述為「本文未報告 DKA/HHS 事件」，絕不可寫成「該試驗未發生 DKA」。** 上市後致死性 ketoacidosis 已寫入兩份仿單 [label_alpelisib.md][label_inavolisib.md §7]。
3. **不可逆的極端案例已被記錄，但無分母。** Li 2026 記載 inavolisib 誘發之 **fulminant-like diabetes 併 HHS**（case report）[Inavolisib_HHS_Li_2026.md]；FDA ITOVEBI 04/2026 label 已將「Ketoacidosis with a fatal outcome has occurred in the postmarketing setting」寫入 §5.1，並新增 §6.2 Postmarketing 之 Ketoacidosis 項目 [label_inavolisib.md §7]；FDA PIQRAY 亦載「Fatal cases of ketoacidosis have occurred in the postmarketing setting」與 postmarketing HHNKS [label_alpelisib.md]。**上市後通報無分母，無法估算發生率。** FAERS 之 disproportionality 分析（Ziegengeist 2024）本地**僅有 abstract 📌**，不得對其內文細節作具體斷言 [FAERS_DKA_Ziegengeist_2024.md]。
4. **一個被忽略的臨床風險：停藥時的低血糖。** EMA Itovebi 4.4 明文警告，當 Itovebi 中斷或停用時，先前為控制高血糖而使用的 insulin／sulfonylurea 會產生低血糖風險 [label_inavolisib.md]。**但沒有任何研究量化過這個風險的發生率**——本回顧未取得可驗證來源。這是實務上每次 dose interruption（inavolisib 因高血糖中斷率 28%）都會遇到的情境 [label_inavolisib.md]。

**需要什麼研究才能回答**

- **停藥後 12–24 個月的前瞻性代謝追蹤 cohort**：終點為 HbA1c、OGTT／FPG、降糖藥持續使用率、新診斷 T2DM 累積發生率，並依「治療期間最高高血糖 grade」分層。這可以直接嫁接在既有試驗的 long-term follow-up 上，成本低。
- **以 registry 或 claims 資料進行的心血管結局分析**：比較曾接受 PI3Kα inhibitor 且發生 grade ≥3 高血糖者 vs 未發生者之 MACE 與腎功能軌跡，並以癌症分期與存活時間校正（competing risk 分析為必要）。
- **dose interruption 期間之低血糖前瞻性量測**（CGM 最適合此問題）：在因高血糖中斷 inavolisib／alpelisib 的病人中，量化 level 1／level 2 低血糖的發生率與時間分布，以產出**明確的降糖藥減量規則**（目前 EMA 只寫「should be considered」，無具體減量幅度）[label_inavolisib.md]。

---

## I-3. 本節「未取得可驗證來源」清單（不以先驗知識補洞）

1. **METALLICA cohort C（T2DM 族群）之結果**：登錄檔有設計，已發表論文僅報告 cohort A/B；ClinicalTrials.gov **無 results posted** [trials_ongoing.md][METALLICA_LlombartCussac_2024.md]。
2. ~~**SOLAR-1／INAVO120／BYLieve 主論文全文**：本地僅有 abstract 📌~~ → **本項已部分解除（2026-07-21）**：
   - ✅ **SOLAR-1 AE 專文（Rugo 2020, Ann Oncol）全文已落地 📄** —— 其 Table 1（protocol 高血糖處置）、Table 2（分級發生率）、time-to-onset、protocol amendment 前後比較、降糖藥使用、基線風險因子分層、dose intensity vs PFS **均可引用**。
   - ✅ **INAVO120 主論文（Turner 2024, NEJM）全文已落地 📄** —— 其 Table 1（基線）、Table 2（AE）、納入／排除條件、RDI、PFS/OS/ORR **均可引用**；但**Supplementary Appendix（Table S1–S3、Fig S1–S2）本地不含，Table S3 之 AE 導致停藥明細仍不得引用**。
   - ✅ **MSKCC 真實世界世代（Shen 2023, Cancer）全文已落地 📄**。
   - ❌ **仍為 📌**：**SOLAR-1 主論文（André 2019）** 與 **BYLieve（Rugo 2021／2024）** 本地僅有 abstract，其 subgroup 與 supplementary table **仍不得引用**。
3. **inavolisib 之血糖時間曲線與時序資料**：alpelisib 有 case-level（CGM/FGM）與試驗層級（median time to onset 15 天）描述 [SOLAR1_AE_Rugo_2020.md]；**inavolisib 則兩個層級皆無 —— INAVO120 主論文全文完全未報告 hyperglycemia 之 median time to onset 與 time to resolution**（已 grep 確認）[INAVO120_Turner_2024.md]。
4. **PI3Kα inhibitor 相關高血糖之心血管結局**：本地 38 篇全文中無任何一篇報告。
5. **停藥後 HbA1c 恢復情形與新診斷 T2DM 累積發生率**：仿單僅報告 FPG，且分母僅 54／61 人。
6. **dose interruption 期間低血糖之發生率與具體降糖藥減量幅度**：EMA 有定性警告，無定量資料。
7. **台灣族群之 real-world 高血糖資料、健保給付規定、TFDA inavolisib 中文仿單**：全部未取得 [label_alpelisib.md §10][label_inavolisib.md §14]。
8. **是否存在 2022-09-22 之後的台灣 alpelisib 中文仿單更新版**：未取得 [label_alpelisib.md §10.1]。
9. **降糖藥物在此適應症之頭對頭比較療效數據**：兩藥仿單皆僅列出可用類別，「未提供任何頭對頭比較數據」[label_alpelisib.md §10.4]。
10. **inavolisib 與 alpelisib 之頭對頭比較**：無 label 資料，無試驗 [label_inavolisib.md §14.5]。
11. **SGLT2i + PI3Kα inhibitor 之 ketoacidosis 交互風險的仿單級警語**：兩份仿單皆無 [label_inavolisib.md §14.6]。
12. **NCT05753657 之 pioglitazone 劑量**：登錄檔未載 [trials_ongoing.md]。
13. **NCT06083038 所稱之「hyperglycemia prevention and management regimen」具體內容**：登錄檔未提供 [trials_ongoing.md]。
14. **NCCN Guidelines（登入牆）與 ESMO 對 PI3Ki 高血糖之專門聲明**：未取得 [guideline_ada_comparators.md §0]。
15. **ADA SOC-2026 Section 3 敘述段中「there is no evidence that concurrent use of these two medica[tions]...」之完整後半句**：擷取中被截斷，**撰寫時不得臆測** [guideline_ada_comparators.md]。
16. **CGM 在 PI3Kα inhibitor 誘發之急遽血糖波動下的準確度驗證**：無任何來源。
17. **CAPItello-291 中國 cohort 全文**（`CAPItello291_China_Hu_2025`）：列於 citations 但未落地 [citations_round1.md]。

**新增（三篇全文落地後才確認為「原文確實沒有」的缺口 —— 這類缺口比「未取得全文」更難補，因為必須重新做研究）**

18. **INAVO120 之 grade 3 與 grade 4 高血糖拆分值**：主論文只報合併 **5.6%（9/162）**，未拆分 [INAVO120_Turner_2024.md]。
19. **INAVO120 之實際 metformin 使用率、「high risk」操作型定義、以及其他降糖藥（SGLT2i／insulin／SU／DPP-4i）之使用**：protocol 僅「allowed」，全文未報告任何百分比 [INAVO120_Turner_2024.md]。
20. **INAVO120 之「因高血糖 dose interruption」與「因高血糖永久停藥」比率**：僅有「因高血糖減量 2.5%」；停藥明細在本地不含之 Table S3 [INAVO120_Turner_2024.md]。
21. **INAVO120 之基線既有糖尿病／prediabetes 比例、基線 HbA1c 與 FPG 實際分佈值、基線降糖藥使用率**：Table 1 無 diabetes 一列，全部未報告 [INAVO120_Turner_2024.md]。
22. **INAVO120 之血糖監測排程（抽血頻率）與 protocol 高血糖 dose-modification 演算法**：正文僅稱「described in the protocol」，本地無 protocol 檔 [INAVO120_Turner_2024.md]。
23. **INAVO120 之依種族分層高血糖分析**：有 38.2% 亞洲人，但無此分析 [INAVO120_Turner_2024.md]。
24. **SOLAR-1 之 metformin 具體 titration schedule（起始 mg、加量間隔、目標劑量）**：全文僅「consider／start or intensify／beyond MTD of metformin」，無任何 mg 或時程（已 grep 確認）；本回顧引用之 titration 僅來自 FDA 仿單 [SOLAR1_AE_Rugo_2020.md][label_alpelisib.md]。
25. **SOLAR-1 之 diabetic 基線族群（n=12）之分級高血糖發生率**：全文未分項報告（EMA 仿單之 83.3% 為另一來源，不可交叉宣稱為同一分析）[SOLAR1_AE_Rugo_2020.md]。
26. **SOLAR-1 停用 alpelisib 後高血糖回復至 grade 0/1 所需之中位天數**、以及該試驗高血糖風險因子之多變量分析（無 OR/HR/p 值）[SOLAR1_AE_Rugo_2020.md]。
27. **SOLAR-1 之腎功能（eGFR／creatinine）變化、脫水事件率，及其與 metformin 使用安全性之分析**：全文未報告 [SOLAR1_AE_Rugo_2020.md]。**對癌症病人（腹瀉 57.7%、嘔吐 27.1%、食慾不佳 35.6%、體重下降 26.8%）而言，這是最直接影響 metformin 安全性的空白。**
28. **Shen 2023 之 DKA 實際人數與比率**（僅提及敏感度分析排除該類病人）、**HHS**（全文未提及）、**類固醇使用與高血糖之關聯**（未記錄）、**依 BMI/HbA1c 分層之高血糖發生率實際百分比**（僅報 p 值）、**腹瀉／脫水／腎功能資料**（僅報 BMI 變化中位 −1.30 kg/m²，−5.5%）[MSKCC_RealWorld_Shen_2023.md]。
29. **Shen 2023 全文之兩處內部數字不一致**（降糖藥 101 人之分母 40.9% vs 66.4%；內分泌轉介 19.8% vs Discussion「nearly one-third」；BMI 組間 p 值內文 .09 vs Table 1 .08）：本回顧一律採 Results 版並標註，**不作調和推論** [MSKCC_RealWorld_Shen_2023.md]。

---

## I-4. 給臨床醫師的可執行結論

1. **把「監測與劑量調整」和「藥物選擇」分開看待。** 前者有【L1】仿單條文，照做即可；後者主要是【L3】共識與【L5】機轉推論，應保留個案化判斷空間，並在病歷中註明依據。
2. **alpelisib 與 inavolisib 的處置流程不可共用一張表。** 最關鍵的差異是 FPG >160–250 這一段：alpelisib 不需停藥、inavolisib 要停藥；以及 FPG >500 的永久停藥門檻（alpelisib 較嚴）[label_alpelisib.md][label_inavolisib.md]。
3. **在台灣，風險分層建議以 baseline HbA1c 為主軸、BMI ≥25 為輔**，而非直接套用仿單的 BMI ≥30 —— 依據是 Shen 2023（BMI ≥25 與 any-grade p=.036、grade 3–4 p<.001；同時放入模型時只有 HbA1c 維持顯著 p<.001）與 Liu 2022（BMI >25，OR 5.4）[MSKCC_RealWorld_Shen_2023.md][RealWorld_Liu_2022.md]。此為【L4】外推，應如此標示。**兩篇試驗全文亦不支持把 BMI ≥30 當成單一觸發條件**：SOLAR-1 的 any-grade 高血糖在 obese（67.6%）反而低於 overweight（73.8%），只有 grade 3／4 隨 BMI 單調上升 [SOLAR1_AE_Rugo_2020.md]；INAVO120 的 BMI ≥30 vs <30 僅 65.5% vs 56.8%（作者自述「slightly higher」）[INAVO120_Turner_2024.md]。
3b. **判讀「試驗數字」時務必先確認 term 與分母。** 同一個 SOLAR-1 有 63.7%（preferred term）與 65.8%（AESI grouped term）、grade 3/4 則有 32.7%+3.9%（preferred term，Rugo 2020）、38.0%（AESI grouped，grade ≥3，Rugo 2020）、以及 **36.6%**（Shen 2023 引述 SOLAR-1 之數字，並載 SOLAR-1 因高血糖停藥率 6.3%）；同一個 INAVO120 有 85%（FDA 實驗室值）／59.9%（EMA AE term）／58.6%（NEJM grouped term）。**在對病人或同儕說明風險時，引用哪一個數字會改變整段對話的基調。** [SOLAR1_AE_Rugo_2020.md][INAVO120_Turner_2024.md][MSKCC_RealWorld_Shen_2023.md][label_alpelisib.md][label_inavolisib.md]
3c. **真實世界的問題可能是「處置不足」而非只是「病人體質」。** MSKCC 世代高血糖更嚴重（grade 3–4 40.2% vs 13.0%），但接受降糖治療者反而較少（66% vs SOLAR-1 的 87%），需 ≥3 種降糖藥者與用 insulin 者亦較少 [MSKCC_RealWorld_Shen_2023.md][SOLAR1_AE_Rugo_2020.md]。**建立院內標準化的驗糖與降糖處置路徑，可能比爭論用哪一種降糖藥更能改變結果。**
4. **預防性 metformin 是「考慮」不是「常規」**，且必須把腹瀉／噁心的代價、以及癌症病人本身的腹瀉率（alpelisib 58%、inavolisib 48%）一併納入決策 [label_alpelisib.md][label_inavolisib.md]。ADA 的措辭是「high-risk individuals」，Delphi 的共識範圍是「baseline HbA1c 5.7–6.4%」[guideline_ada_comparators.md][Delphi_Gallagher_2024.md]。**INAVO120 的 protocol 雖「allowed」預防性 metformin，但全文未報告使用率、未定義高風險、未做隨機化——不可據此宣稱 inavolisib 的預防性 metformin 已被驗證** [INAVO120_Turner_2024.md]。**METALLICA 為單臂 phase 2、以歷史文獻為對照，其結果不可外推為「所有病人都該預防性用 metformin」** [METALLICA_LlombartCussac_2024.md]。
4b. **第一次驗糖不能等到第 3–4 週。** SOLAR-1 之 grade ≥3 高血糖 **median time to onset 15 天（range 5–395）**、MSKCC 世代 **median time to onset 16 天**（首次 glucose ≥140 mg/dL）[SOLAR1_AE_Rugo_2020.md][MSKCC_RealWorld_Shen_2023.md]。**兩個獨立資料集給出幾乎相同的 15–16 天**，而 alpelisib 仿單要求前 2 週至少每週驗、inavolisib 要求 Day 1–7 每 3 天——**仿單頻率的設計邏輯正是要在這個時間點之前抓到病人** [label_alpelisib.md][label_inavolisib.md]。Shen 2023 亦據此指出，超過此時間窗後「this risk factor is no longer meaningfully actionable」，因此**基線 HbA1c 必須在轉移診斷或第一線治療時就先驗**，該世代即使在 standard care 組也只有 72% 有基線 HbA1c [MSKCC_RealWorld_Shen_2023.md]。
4c. **改善通常很快，但不代表可以放鬆。** SOLAR-1 之 grade ≥3 高血糖改善 ≥1 grade 的中位時間為 **6 天（range 4–7）**；MSKCC 世代 metformin 單方之高血糖緩解中位 **16 天（IQR 7–26）**，需加第二種藥者延長至 **26 天（IQR 14–64，p=.024）** [SOLAR1_AE_Rugo_2020.md][MSKCC_RealWorld_Shen_2023.md]。**「需要加第二種藥」本身即是嚴重度與較長病程的標記，應同步啟動內分泌共管。**
5. **不要因為機轉推論而延誤急症治療。** ADA Rec 9.35b 本身即把 hyperglycemic crises 列為 insulin 的適應症，且該條等級僅為 **E**；兩藥仿單的 Grade 3／4 均明文要求處理 ketoacidosis 與 hyperosmolar disturbance [guideline_ada_comparators.md][label_alpelisib.md][label_inavolisib.md]。
6. **若使用 SGLT2i，須把 euglycemic DKA 當成真實風險處理**：在 Liu 2022 中，15 位使用者就出現 1 例 [RealWorld_Liu_2022.md]；癌症病人的腹瀉、嘔吐、食慾不佳與脫水都是誘因。仿單無警語不代表無風險。
7. **停藥（含 dose interruption）時務必同步下修 insulin／SU**，這是【L1】明文條文，卻最容易被忽略 [label_inavolisib.md]。
