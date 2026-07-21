# D. 基線風險分層表

**回答 Q5：治療前應如何依 HbA1c、FPG、BMI、年齡、既有糖尿病、steroid use、eGFR 及營養狀態進行風險分層？**

---

## D-0. 先決前提：本節分層適用於哪些藥？

本節的分層**僅適用於 PI3Kα-selective inhibitor（alpelisib、inavolisib）與 AKT inhibitor（capivasertib）**，且三者**不可互相套用**。

- ADA SOC—2026 全篇使用的類別詞是 **PI3Kα inhibitor**，並在 Rec 9.35a 明白寫成「PI3K inhibitors **that affect the α isoform**（e.g., alpelisib and inavolisib）」；ADA **並未**把 idelalisib／duvelisib／copanlisib 納入這些建議【L3】[guideline_ada_comparators.md]
- 回溯性資料亦支持此區分：MSKCC 491 例中，所有**因高血糖導致的治療中斷／減量／住院**皆發生在 AKT（5%）、α（13%）或 pan-PI3K（5%）inhibitor 使用者，**接受 β-／γ-／δ-specific PI3K inhibitor 者無任何此類事件**【L4】[RealWorld_Liu_2022.md]
  - ⚠️ **限縮**：該文逐字為「All such hyperglycemia-associated **treatment disruptions** occurred in patients exposed to AKT (5%), α (13%), or pan-PI3K inhibitors (5%), with **none** in patients exposed to PI3K inhibitors specific for isoforms other than α」——**其分母是「治療中斷事件」而非「高血糖發生率」；該文並未報告 β/γ/δ 組的高血糖發生率為零**。本回顧不作「β/γ/δ 不致高血糖」之推論[RealWorld_Liu_2022.md]

**alpelisib 與 inavolisib 的關鍵差異（影響分層後的監測密度，不影響分層本身）**：

| 項目 | alpelisib | inavolisib |
|---|---|---|
| 高血糖中位發生時間 | Grade ≥2 為 **15 天**（range 5–517）【L1】[label_alpelisib.md] | **7.0 天**（range 2.0–955.0）【L2】[INAVO120_Safety_Im_2026.md] |
| 仿單監測起始頻率 | 前 2 週**至少每週 1 次**，之後至少每 4 週【L1】[label_alpelisib.md] | 第 1 週（D1–7）**每 3 天 1 次**，D8–28 每週，之後每 2 週 ×8 週，再每 4 週【L1】[label_inavolisib.md] |
| 仿單列舉之風險因子 | obesity (BMI ≥ 30)、elevated FPG、HbA1c at ULN or above、**use of concomitant systemic corticosteroids**、age ≥ 75【L1】[label_alpelisib.md] | (pre)diabetes、HbA1C ≥ 5.7%、BMI ≥ 30 kg/m²、**≥ 45 years of age**、history of gestational diabetes、**family history of diabetes mellitus**（EMA SmPC 逐字）【L1】[label_inavolisib.md] |

> **臨床意涵**：inavolisib 的 EMA 仿單年齡門檻是 **≥45 歲**，遠低於 alpelisib FDA 仿單的 **≥75 歲**。兩者不是同一個切點，**不可混用**。下方主表對年齡採「分別標註」處理。

---

## D-1. 分層所依據的四套已發表風險因子清單

分層前先攤開四套來源，讓讀者知道每個門檻的出處與強度。

| 來源 | 性質 | 列出的風險因子與門檻 |
|---|---|---|
| FDA PIQRAY 仿單 §5.3【L1】[label_alpelisib.md] | 法規文件 | BMI ≥ 30；elevated FPG；HbA1c 在正常值上限或以上；併用 systemic corticosteroids；年齡 ≥ 75 |
| EMA Itovebi SmPC Table 5【L1】[label_inavolisib.md] | 法規文件 | (pre)diabetes；HbA1C ≥ 5.7%；BMI ≥ 30；年齡 ≥ 45；gestational diabetes 病史；**糖尿病家族史**。另註明併用 corticosteroids／intercurrent infections 者須**更頻繁驗 fasting glucose，並加驗 HbA1C 與 ketones（以血酮為佳）** |
| ADA SOC—2026 Section 3 敘述段【L3】[guideline_ada_comparators.md] | 學會指引 | 「highest risk」= 年齡 **≥70**、BMI **≥30**、**concurrently treated with glucocorticoids**、基線 A1C **≥5.7%** 或 FPG **≥100 mg/dL** |
| Rodón 隨機森林模型（X2101 + SOLAR-1 pooled，n=505；BYLieve n=340 外部驗證）【L2】[RiskModel_Rodon_2024.md] | 試驗 pooled + ML | 5 個最具影響力的基線變項：**FPG、BMI、HbA1c、monocytes、age** |
| Delphi 專家共識（modified Delphi）【L3】[Delphi_Gallagher_2024.md] | 專家共識 | 「highest risk」定義為 **年齡 ≥70 歲 + BMI ≥30 + HbA1c 5.7–6.4%** 三者並存 |

**量化的風險梯度（可直接引用的數字）**：

| 風險因子 | 效果量 | 來源 |
|---|---|---|
| BMI ≥ 25 kg/m² | 單變項 OR **5.4（95% CI 2.3–16.0）**；多變項 OR **4.0（95% CI 1.3–17.8）, p=0.03** | n=491 回溯【L4】[RealWorld_Liu_2022.md] |
| HbA1c ≥ 5.7% | 單變項 OR **4.7（95% CI 2.1–11.0）**；多變項 OR **3.4（95% CI 1.2–9.4）, p=0.02** | n=491 回溯【L4】[RealWorld_Liu_2022.md] |
| 基線糖尿病（HbA1c ≥6.5% 或使用降糖藥） | 最高絕對事件率 **8/23（34.7%）** | n=491 回溯【L4】[RealWorld_Liu_2022.md] |
| 基線 HbA1c（連續變項） | 與高血糖發生 **p<0.001** 顯著相關（同一模型中 baseline BMI **p=0.029**、baseline glucose **p<0.001**）；BMI 與 HbA1c 有交互作用（**p=0.005**），同時放入模型時**僅 HbA1c 維持顯著（p<0.001）**。排除 DKA 病人與血糖最高 5% 之敏感度分析後，HbA1c 與高血糖之關聯**仍顯著（p=0.001）** | MSKCC n=247 回溯【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| 基線 HbA1c ≥ 5.7%（類別變項） | 與 **any-grade**（p<0.001）與 **grade 3–4**（p<0.001）高血糖皆顯著相關；與 alpelisib **減量／停藥 p=0.015** | MSKCC n=247 回溯【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| 基線 BMI ≥ 25 kg/m²（類別變項） | 與 **any-grade**（p=0.036）與 **grade 3–4**（p<0.001）高血糖相關；與 alpelisib **減量／停藥 p<0.001** | MSKCC n=247 回溯【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| 年齡 ≥ 75（alpelisib） | Grade 3-4 高血糖 **19/34（55.9%）vs 89/250（35.6%）**（SOLAR-1 AE 專文全文逐字；同族群 all-grade GI toxicity 85.3% vs 74.0%）<br>⚠ FDA 仿單 §8.5 將同一組數字記為 **56% vs 36%**、Tankova 記為 **55% vs 36%**——三者為同一資料之不同進位，本回顧以**全文之 55.9% vs 35.6%** 為準並並陳 | SOLAR-1【L2】📄[SOLAR1_AE_Rugo_2020.md]；仿單【L1】[label_alpelisib.md]；共識【L3】[Consensus_Tankova_2022.md] |
| 年齡 ≥ 65（alpelisib） | Grade 3-4 高血糖 **44% vs 32%**（vs <65 歲） | SOLAR-1，FDA 仿單 §8.5【L1】[label_alpelisib.md] |
| BMI（alpelisib） | 任何級別高血糖：normal BMI **63/110（57.3%）**、overweight **62/84（73.8%）**、obese **50/74（67.6%）**；Grade 3 **24.5% / 35.7% / 39.2%**；Grade 4 **2.7% / 3.6% / 9.5%**<br>⚠ SOLAR-1 全文**未提供 BMI 分組之 kg/m² 切點**，亦未提供 OR/HR | SOLAR-1【L2】📄[SOLAR1_AE_Rugo_2020.md] |
| 基線 prediabetes（alpelisib） | 基線分布：normal **113（40%）**、prediabetic **159（56%）**、diabetic **12（4%）**。任何級別高血糖 prediabetic **74%**（G3 43.4%、G4 5.0%）vs normal **52%**（G3 16.8%、G4 1.8%）；diabetic (n=12) 之分級發生率**原文未分項報告** | SOLAR-1【L2】📄[SOLAR1_AE_Rugo_2020.md] |
| BMI ≥ 30（inavolisib，INAVO120 主論文） | 任何級別高血糖 **65.5%** vs BMI <30 的 **56.8%**（作者形容為 "slightly higher"）；⚠ 主論文**未報 BMI 分層之 grade 3/4 率** | INAVO120【L2】📄[INAVO120_Turner_2024.md] |
| 風險因子個數（inavolisib） | 0 個：any-grade 52.7%、G3-4 **2.2%**；1 個：68.0%／8.0%；2 個：62.5%／12.5%；3 個：66.7%／**33.3%** | INAVO120【L2】[INAVO120_Safety_Im_2026.md] |
| BMI ≥ 30（inavolisib） | G3-4 高血糖 **17.2%（5/29）** vs BMI <30 的 **3.0%（4/132）** | INAVO120【L2】[INAVO120_Safety_Im_2026.md] |
| FBG ≥ 100 mg/dL（inavolisib） | any-grade **73.9%**、G3-4 **10.9%** vs FBG <100 的 52.7%／3.6% | INAVO120【L2】[INAVO120_Safety_Im_2026.md] |
| 內分泌科轉介（作為「已發生麻煩」的代理指標） | 與 alpelisib **減量／停藥 p<0.001**；與 **SGLT2i 使用 p=0.007**。⚠ 作者明言會診與加用 SGLT2i 屬**晚期介入**（針對持續性、較高等級高血糖），此關聯為 **confounding by indication**，**不可**解讀為「轉介或 SGLT2i 造成減量」 | MSKCC n=247 回溯【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| Rodón 模型高風險組 | 訓練集 2 個月內 G3/4 機率 **86.2%**（低風險組 30 個月 <5%）；測試集 **57.6%**（低風險組 <20%）。SOLAR-1 中高風險組 G3/4 **90.6%（96/106）** vs 低風險組 **6.7%（12/178）**；**在已停藥者中**因高血糖停藥者 **15/90（16.7%）vs 4/154（2.6%）**（⚠ 分母為「已停藥病人」而非全體；以全體為分母則為 15/106＝14.2% vs 4/178＝2.2%） | 【L2】[RiskModel_Rodon_2024.md] |

### D-1-1. 現實世界的錨點：你的病人相對於 MSKCC 世代落在哪裡

分層門檻若沒有母群分布作對照，容易高估或低估自己的病人。以下為目前本地唯一一個**未經試驗排除條件篩選**的 alpelisib 世代（MSKCC，2013-01-01 至 2021-10-15，n=247 metastatic breast cancer，standard care 147 人／clinical trial 100 人）【L4】📄[MSKCC_RealWorld_Shen_2023.md]：

| 基線變項 | MSKCC 全世代中位數（IQR） | 分層意涵 |
|---|---|---|
| **BMI** | **25.4 kg/m²（22.6–29.0）** | 中位數**剛好落在本表 25 的中風險切點上**——意即真實門診中「約一半的病人在起始日即已達中風險」。分層 <25 者為 105 人（44.7%）、25–29.9 者 82 人（34.9%）、≥30 者 48 人（20.4%）、未知 12 人（5.1%） |
| **HbA1c** | **5.5%（5.1–5.9）** | 中位數在正常範圍，但 **IQR 上緣 5.9% 已進入 prediabetes**。分層 <5.7% 者 104 人（42.1%）、5.7–6.4% 者 38 人（15.4%）、≥6.5% 者 22 人（8.9%）、**未知 83 人（33.6%）** |
| **年齡** | **62 歲（54–68）** | 中位數低於 ADA／Delphi 的 ≥70 門檻，但**高於 EMA inavolisib 的 ≥45 門檻**——後者在真實世界幾乎等於「絕大多數病人都算有此風險因子」 |
| **既往治療線數** | 3 線（range 0–15） | 屬多線治療後族群 |
| **治療中 BMI 變化** | **−1.30 kg/m²（−5.5% of initial BMI；IQR −0.33 至 −3.0）** | 見 D-5-1 |

⚠ **兩個必須同時交代的限制**：
1. **資料可得率不等於 100%**：基線 BMI 有 235 人（95.1%），但**基線 HbA1c 僅 164 人（66.4%）**——因此上表 HbA1c 之分母並非全世代，且所有 HbA1c 相關的 p 值皆建立在此子集上【L4】📄[MSKCC_RealWorld_Shen_2023.md]。
2. **統計方法為 Pearson's χ²，非多變項 logistic regression**；原文**未提供任何 OR 與 95% CI**。因此本節引用 MSKCC 之 p 值時，僅能表述為「有統計上的關聯」，**不可**轉譯為效果量或風險倍數【L4】📄[MSKCC_RealWorld_Shen_2023.md]。

**兩組基線並不可比**（這正是下一節「試驗 vs 真實世界」落差的部分成因）：standard care 組基線 HbA1c 中位 5.5% vs clinical trial 組 5.3%（**p=0.007**）；HbA1c 落在 ≥5.7% 的 prediabetes／diabetes 範圍者 **30.6% vs 15.0%（p=0.041）**；曾測基線 HbA1c 者 **72.1% vs 58.0%（p=0.021）**；overweight/obese BMI 者 **55.7% vs 48.0%（p=0.09；同文 Table 1 對應欄位記為 0.08，原文兩處不一致，本回顧逐字並陳）**【L4】📄[MSKCC_RealWorld_Shen_2023.md]。

---

## D-2. 主表：三層基線風險分層

> **使用方式**：由上而下逐列評估。**任一列落入「高風險」欄，即整體判為高風險**（不採計分制——本回顧未取得任何經驗證的加權計分表，Rodón 模型雖可產生個人分數，但其 nomogram 位於 Additional file，本地未落地）。中風險則需 ≥1 列落在中風險欄且無任何高風險項。

| 評估項目 | 🟢 低風險 | 🟡 中風險 | 🔴 高風險 | 證據 |
|---|---|---|---|---|
| **HbA1c** | **< 5.7%** | **5.7–6.4%**（ADA prediabetes） | **≥ 6.5%**（糖尿病範圍）；**≥ 8.0% 視為不建議起始**（Delphi 專家組將 HbA1c ≥8.0% 的建議整組排除，並認為「未經治療前內分泌科會診即使用 alpelisib 為 inappropriate」） | 門檻【L1】[label_inavolisib.md]／【L3】[guideline_ada_comparators.md]；≥8.0% 之處理【L3】[Delphi_Gallagher_2024.md] |
| **FPG／FBG** | **< 100 mg/dL（< 5.6 mmol/L）** | **100–125 mg/dL（5.6–6.9 mmol/L）** | **≥ 126 mg/dL（≥ 7.0 mmol/L）**；alpelisib 於 SOLAR-1 修正後排除 FPG > 140 mg/dL 者 | ADA 切點【L3】[Multidisc_Rugo_2022.md]；ADA high-risk 定義 FPG ≥100【L3】[guideline_ada_comparators.md]；SOLAR-1 修正【L3】[Multidisc_Rugo_2022.md] |
| **BMI** | **< 25 kg/m²** | **25–29.9 kg/m²**（此區間已達 OR 4.0–5.4 之統計門檻，勿低估；MSKCC 世代 BMI 中位數 25.4 即落在此區間） | **≥ 30 kg/m²** | 25 之切點【L4】[RealWorld_Liu_2022.md]／📄[MSKCC_RealWorld_Shen_2023.md]（BMI ≥25 與 any-grade p=0.036、G3-4 p<0.001、減量／停藥 p<0.001）；30 之切點【L1】[label_alpelisib.md][label_inavolisib.md] |
| **年齡（alpelisib）** | < 65 歲 | **65–74 歲**（G3-4 44% vs 32%） | **≥ 75 歲**（G3-4 56% vs 36%） | 【L1】[label_alpelisib.md] |
| **年齡（inavolisib）** | < 45 歲 | **≥ 45 歲**（EMA 明列之風險因子門檻） | 與其他高風險項並存時升階 | 【L1】[label_inavolisib.md] |
| **年齡（共識用之綜合門檻）** | < 70 歲 | — | **≥ 70 歲**（ADA SOC-2026 與 Delphi 皆用 ≥70） | 【L3】[guideline_ada_comparators.md][Delphi_Gallagher_2024.md] |
| **糖尿病家族史／既往 GDM** | 皆無 | **一等親糖尿病家族史**（EMA 明列） | **既往 gestational diabetes**（EMA 明列；共識認為「implies a baseline propensity to insulin resistance」）；合併其他中風險項時直接升為高風險 | 家族史與 GDM 皆為 EMA 逐字列舉【L1】[label_inavolisib.md]；GDM 之理由【L3】[Consensus_Tankova_2022.md]；ADA 併列 PCOS、HDL <35 mg/dL、TG >250 mg/dL 為糖尿病風險因子【L3】[Mgmt_Goncalves_2022.md] |
| **巨嬰產史** | — | — | — | ⚠ **本回顧未取得可驗證來源**（本地檔案無任何「macrosomia／巨嬰」與 PI3Ki 高血糖風險相關之敘述）。臨床上若欲納入，應以「既往 GDM」項目代理 |
| **既有糖尿病與控制狀態** | 無糖尿病 | 無糖尿病但已達 prediabetes（見上兩列） | **已知 T2DM**。可起始之上限：仿單／共識認為 **HbA1c ≤ 7%（已用藥且控制良好的 T2DM）可起始；HbA1c ≥ 6.5% 者在血糖控制達標前不應起始**。**T1DM 與未控制之 T2DM 為安全性未建立族群**（SOLAR-1、BYLieve、METALLICA、INAVO120 皆排除） | 起始門檻【L3】[Multidisc_Rugo_2022.md]；安全性未建立【L1】[label_alpelisib.md]；INAVO120 排除 T1/T2DM requiring ongoing treatment【L2】[INAVO120_Safety_Im_2026.md]；METALLICA 排除「diagnosis of type I or II diabetes mellitus requiring antidiabetic drugs」【L2】[METALLICA_LlombartCussac_2024.md] |
| **併用 corticosteroid**（含止吐前置用藥、rash 處置用之 prednisone、dexamethasone mouthwash） | 無任何全身性類固醇 | 短期、低劑量或局部（含 dexamethasone mouthwash、topical triamcinolone 0.1%／fluocinonide 0.05%）——**局部類固醇仍「may rarely lead to hyperglycemia」** | **併用 systemic corticosteroids**（FDA 仿單直接列為風險因子）。rash grade 3 時之 **prednisone 0.5–1 mg/kg/day × 7–10 天**屬此類，仿單與共識均警示「take caution with use of systemic steroids as these may worsen hyperglycemia」 | 仿單風險因子【L1】[label_alpelisib.md]；ADA high-risk 第 3 項【L3】[guideline_ada_comparators.md]；EMA 要求併用類固醇者加驗 HbA1C 與 ketones【L1】[label_inavolisib.md]；局部類固醇之高血糖警語與 prednisone 劑量【L3】[Multidisc_Rugo_2022.md]；capivasertib 專家意見同列 systemic corticosteroids 為風險因子【L3】[Capivasertib_Mgmt_Iyengar_2025.md] |
| **eGFR**（**注意：這是「降糖藥可用性」與「脫水風險」的分層，不是 PI3Ki 高血糖本身的風險因子**） | **≥ 60 mL/min/1.73 m²**：metformin 可用，腎功能每年追蹤 | **45–59**：metformin 可用，腎功能每 3–6 個月追蹤。Delphi 之 metformin 上限用藥條件為 **GFR > 45** | **30–44**：**不得新起始 metformin**；已在用者停用或減量 50%，每 3 個月追腎功能。**< 30：metformin 禁忌**。alpelisib 於 CLcr < 30 之藥動學未知；CLcr 30–<90 無需調整劑量 | metformin eGFR 階梯【L3】[Multidisc_Rugo_2022.md]；GFR >45【L3】[Delphi_Gallagher_2024.md]；alpelisib 腎功能【L1】[label_alpelisib.md] |
| **營養狀態**（見 D-5 詳述） | 體重穩定、食慾正常、無腹瀉 | 治療前 3 個月內非蓄意體重下降；食慾下降；基線已有腹瀉病史或併用 GLP-1 RA／metformin／緩瀉劑 | 明顯體重下降＋食慾不佳＋腹瀉／脫水徵象並存；正在脫水或有 AKI 病史 | 需篩檢腹瀉病史、併用藥（含 GLP-1 RA、metformin、瀉劑、鎂補充劑）及合併症，並「assess renal function and electrolytes at baseline and identify patients who may be at higher risk of developing dehydration」【L3】[Capivasertib_Mgmt_Iyengar_2025.md]；GLP-1 RA 用於 BMI >30 者時「the risk of cachexia and malnutrition should be considered」【L3】[ToxMgmt_Jhaveri_2026.md] |
| **先前是否用過 PI3Ki／AKTi** | 未曾使用 | — | **曾因高血糖／DKA 停用 PI3Ki 者再挑戰（rechallenge）**：已報告在**首次劑量後 24 小時內**即出現嚴重高血糖或 DKA；建議在住院或同等監測環境下進行、搭配 CGM、並事先由內分泌科／糖尿病專科介入 | 【L4】[DKA_Rechallenge_Leung_2022.md]。⚠ 注意：METALLICA 與 GO39374 均**排除**曾用過 PI3K／AKT／mTOR inhibitor 者，故**前瞻性試驗中無此族群的風險數據**【L2】[METALLICA_LlombartCussac_2024.md][GO39374_Gambardella_2025.md] |
| **Monocytes（絕對值）** | — | — | — | Rodón 模型中 monocytes 為 5 個最具影響力變項之一【L2】[RiskModel_Rodon_2024.md]，但 ⚠ **本回顧未取得其數值切點**（原文僅稱「Monocytes may be elevated in patients who are obese」並稱「warrants further investigation」）。**不建議在本表中使用 monocytes 作為分層依據** |

### 分層的外部參照（讓臨床醫師知道自己的病人相當於哪一群）

- 若病人符合 **METALLICA cohort A**（FPG < 100 mg/dL **且** HbA1c < 5.7%）→ 對應本表低風險【L2】[METALLICA_LlombartCussac_2024.md]
- 若符合 **METALLICA cohort B**（FPG 100–140 mg/dL **和／或** HbA1c 5.7–6.4%）→ 對應本表中風險【L2】[METALLICA_LlombartCussac_2024.md]
- **INAVO120 收案門檻**：主論文逐字為 **fasting glucose < 126 mg/dL 且 glycated hemoglobin < 6.0%**（原訂 <5.7%，後修正）→ 高於此門檻者**無 phase 3 前瞻資料**【L2】📄[INAVO120_Turner_2024.md][INAVO120_Safety_Im_2026.md]
  - ⚠ **INAVO120 的體型分布與一般門診族群不同，直接套用其低事件率會低估風險**：full analysis population（N=325）中位體重僅 **63.0 kg**、BMI ≥30.0 者 **57 人（17.5%）**、BMI 18.5–<25.0 達 **153 人（47.1%）**、BMI <18.5 者 **18 人（5.5%）**、亞洲人 **38.2%**、中位年齡 **54.0 歲（range 27–79）**【L2】📄[INAVO120_Turner_2024.md]。其 hyperglycemia（grouped term，safety population 兩組各 N=162）any-grade **58.6% vs placebo 8.6%**、grade 3–4 **5.6% vs 0%**，是在此「已被篩過的低風險體型與血糖族群」中產生的數字【L2】📄[INAVO120_Turner_2024.md]
  - ⚠ INAVO120 主論文**未報告**基線既有糖尿病比例、基線 HbA1c／FPG 之實際數值、基線 prediabetes 比例，以及基線降糖藥使用率；亦**未報告**高血糖之 median time to onset【L2】📄[INAVO120_Turner_2024.md]
- **SOLAR-1 收案門檻**：允許 well-controlled T2DM，**排除 T1DM 與 uncontrolled T2DM**；HbA1c 收案上限於試驗中途（已隨機 317/約 560 人，56.6%）由 **<8% 修訂為 <6.5%**【L2】📄[SOLAR1_AE_Rugo_2020.md]
- **GO39374 收案門檻**：HbA1c < 7% 且 fasting glucose < 140 mg/dL【L2】[INAVO120_Safety_Im_2026.md]

---

## D-3. 各風險層的行動建議

| 行動項目 | 🟢 低風險 | 🟡 中風險 | 🔴 高風險 |
|---|---|---|---|
| **是否需先延後起始、優化血糖** | 否，可直接起始 | 否，但應在起始前完成飲食衛教與居家血糖機教學 | **是**。HbA1c ≥ 6.5% 者「should not initiate alpelisib until good glycemic control is achieved」；HbA1c ≤ 7% 且已用藥控制良好之 T2DM 可起始【L3】[Multidisc_Rugo_2022.md]。HbA1c ≥ 8.0% 者**在無治療前內分泌科會診下起始為 inappropriate**【L3】[Delphi_Gallagher_2024.md] |
| **是否轉介內分泌科** | 一般不需要。Delphi：最低風險者（無肥胖、HbA1c < 5.7%）「generally unnecessary to refer」【L3】[Delphi_Gallagher_2024.md] | 視情況。⚠ Delphi 對「BMI < 30 但 HbA1c 5.7–6.4%」及「BMI ≥ 30 但 HbA1c < 5.7%」是否需治療前會診**未達共識（disagreement）**【L3】[Delphi_Gallagher_2024.md] | **是，且應在起始前完成**。Delphi：年齡 ≥70 + BMI ≥30 + HbA1c 5.7–6.4% 者建議治療前內分泌科評估；**所有 T2DM 和／或 HbA1c 6.5–<8.0% 者，未經治療前內分泌科會診即使用 alpelisib 為 inappropriate**【L3】[Delphi_Gallagher_2024.md]。共識亦建議高風險者（prediabetes／diabetes，尤其 BMI ≥30 或年齡 ≥75）由含內分泌科之多專科團隊管理；若無法及時轉介，應與病人共同討論風險效益後決定【L3】[Consensus_Tankova_2022.md] |
| **血糖監測頻率（起始後）** | 仿單基準即可：alpelisib 前 2 週每週 ≥1 次，之後 ≥每 4 週；HbA1c 每 3 個月【L1】[label_alpelisib.md]。inavolisib 依 D-0 表之較密集排程【L1】[label_inavolisib.md]。Delphi：多數病人**每週一次 FBG**【L3】[Delphi_Gallagher_2024.md] | Delphi：中風險（肥胖 + HbA1c 5.7–6.4%）**每週兩次 FBG**【L3】[Delphi_Gallagher_2024.md]。共識建議高風險者於**起始前 1 週**即開始居家 FSBG，FSBG 持續 >160 mg/dL 應通報【L3】[Multidisc_Rugo_2022.md] | Delphi：**每日 FBG**【L3】[Delphi_Gallagher_2024.md]。共識：起始前 1 週開始每日 FSBG 或居家連續血糖監測【L3】[Multidisc_Rugo_2022.md]。EMA：併用類固醇／有 intercurrent infection 者，除 fasting glucose 外**加驗 HbA1C 與 ketones（以血酮為佳）**【L1】[label_inavolisib.md]。可考慮 CGM，目標為血糖維持在 70–250 mg/dL 之間 >90% 的時間【L3】[ToxMgmt_Jhaveri_2026.md] |
| **是否用預防性 metformin** | **不必常規使用**。Delphi 僅稱 HbA1c < 5.7% 者「**may** be appropriate」【L3】[Delphi_Gallagher_2024.md]。ADA Rec 3.8 為「**Consider** ... in **high-risk** individuals」，evidence grade **B**【L3】[guideline_ada_comparators.md] | **建議使用**。Delphi：baseline HbA1c 5.7–6.4% 者**建議預防性 metformin**（短效或緩釋）【L3】[Delphi_Gallagher_2024.md]。METALLICA 給法：alpelisib 起始前 **7 天**開始，D1–D3 metformin 500 mg BID，之後視耐受度增至 1000 mg BID【L1】[label_alpelisib.md] | **建議使用，但單靠 metformin 可能不足**。Delphi：高風險者在等待內分泌科評估期間可先起始 metformin（GFR > 45 時可加至 2000 或 2500 mg/day），必要時加第二線 SGLT2i 或 TZD；但對「高風險者是否應直接雙藥預防」**專家組未達共識**【L3】[Delphi_Gallagher_2024.md] |
| **飲食** | 建議低碳水化合物飲食 60–130 g/day，必要時營養師會診【L3】[Delphi_Gallagher_2024.md] | 同左，並強化衛教 | 同左；可考慮 ketogenic diet（總碳水 <50 g/day）及每日給藥前 >12 小時禁食，惟兩者於 Delphi 僅屬「may also be appropriate」【L3】[Delphi_Gallagher_2024.md]。⚠ ketogenic diet 與 GI 症狀、體重下降、排便習慣改變相關【L3】[Multidisc_Rugo_2022.md] |
| **治療中血糖目標** | 預後佳者：餐前 90–130 mg/dL、睡前 90–150 mg/dL 或 HbA1c < 7.5%【L3】[Multidisc_Rugo_2022.md] | 同左，依個別化調整 | **frail 或預後較差者應放寬**：餐前 100–180 mg/dL、睡前 110–200 mg/dL 或 HbA1c < 8.5%，因過嚴的控制需要過量降糖藥或胰島素【L3】[Multidisc_Rugo_2022.md] |

### ⚠ 關於預防性 metformin 的四項必要限縮

1. **METALLICA 是 single-arm, open-label, phase 2**（n=68，Simon two-stage，西班牙 18 中心），對照組是 SOLAR-1／BYLieve 的歷史數據，**不是隨機對照**【L2】[METALLICA_LlombartCussac_2024.md]。ADA 亦僅描述其為 "a phase 2 trial"，Rec 3.8 evidence grade 為 **B**，且限於 high-risk【L3】[guideline_ada_comparators.md]。**不得推論成「所有病人都該用預防性 metformin」。**
2. **仿單措辭是「Consider」而非「should」**：「Consider premedication with metformin prior to the initiation of PIQRAY ... based on patient risk factors for hyperglycemia, **gastrointestinal tolerability**, and clinical situation」【L1】[label_alpelisib.md]
3. **代價明確**：仿單逐字寫明 metformin 前給藥「**increases the incidence and severity of nausea, vomiting, and diarrhea adverse reactions**」。METALLICA 中 diarrhea 68%、nausea 68%、Grade 3-4 diarrhea 13%、rash 16%，且**因不良反應永久停用 alpelisib 者達 19%**【L1】[label_alpelisib.md]。ADA 亦提醒 metformin 的腹瀉「is also a frequent adverse effect of PI3Kα therapy」【L3】[guideline_ada_comparators.md]
4. **對 inavolisib 的預防效果未經證實，且有相反訊號**：GO39374 arm F（inavolisib + palbociclib + fulvestrant + 早期 metformin，D1–D15）中，**具 ≥1 項風險因子者仍有 40.0%（8/20）發生 grade 3 高血糖**；作者明言「Hyperglycemia remained frequent in patients with risk factors, **despite early metformin treatment**」【L2】[GO39374_Gambardella_2025.md][INAVO120_Safety_Im_2026.md]。INAVO120 中僅 7.4%（12/162）接受預防性 metformin【L2】[INAVO120_Safety_Im_2026.md]。**METALLICA 的結論不可外推至 inavolisib。**

---

## D-4. 治療前必做檢查清單

### 必做（所有病人，不分風險層）

| # | 項目 | 依據 |
|---|---|---|
| 1 | **FPG 或 FBG** | 仿單：「Before initiating treatment with PIQRAY, test fasting plasma glucose (FPG), HbA1c, and **optimize blood glucose**」【L1】[label_alpelisib.md]；inavolisib：「Evaluate fasting plasma glucose (FPG)/blood glucose (FBG) and hemoglobin A1C (HbA1C) and optimize blood glucose」【L1】[label_inavolisib.md] |
| 2 | **HbA1c** | 同上【L1】。⚠ ADA 明白指出「**A1C alone may not capture the early peak of hyperglycemia noted with PI3Kα inhibitors**」——因此不可只追 HbA1c，必須併驗 plasma glucose【L3】[guideline_ada_comparators.md] |
| 3 | **eGFR／血清 creatinine** | metformin 起始前必須評估 eGFR【L3】[Multidisc_Rugo_2022.md]；capivasertib 專家意見要求「assess renal function and electrolytes at baseline」【L3】[Capivasertib_Mgmt_Iyengar_2025.md] |
| 4 | **電解質（含 Na、K）** | 同上【L3】[Capivasertib_Mgmt_Iyengar_2025.md]。SOLAR-1 實驗室異常：Creatinine increased 67%（G3-4 2.8%）、corrected calcium decreased 27%（2.1%）、**potassium decreased 14%（G3-4 6%）**【L1】[label_alpelisib.md] |
| 5 | **BMI（身高、體重）＋近 3 個月體重變化** | BMI 為仿單與所有模型共同列舉之風險因子【L1】[label_alpelisib.md][label_inavolisib.md]【L2】[RiskModel_Rodon_2024.md] |
| 6 | **病史問診**：既往／現有糖尿病與用藥、**gestational diabetes 病史**、**糖尿病家族史**、PCOS、高血壓、久坐、既往 PI3Ki／AKTi 暴露 | EMA 逐字列舉 GDM 與家族史【L1】[label_inavolisib.md]；PCOS／HDL <35 mg/dL／TG >250 mg/dL 等 ADA 風險因子【L3】[Mgmt_Goncalves_2022.md] |
| 7 | **用藥檢視**：是否併用 systemic corticosteroid（含化療前置止吐之類固醇）、SGLT2i、瀉劑、鎂補充劑、GLP-1 RA | 類固醇為仿單風險因子【L1】[label_alpelisib.md]；併用藥篩檢清單【L3】[Capivasertib_Mgmt_Iyengar_2025.md] |
| 8 | **衛教**：高血糖症狀（excessive thirst、urinating more often、increased appetite **with weight loss**）與就醫時機 | 仿單逐字要求【L1】[label_alpelisib.md]；FSBG 持續 >160 mg/dL 應通報【L3】[Multidisc_Rugo_2022.md]；FG ≥160 mg/dL 應通報【L3】[Capivasertib_Mgmt_Iyengar_2025.md] |

### 選做（依風險層加做）

| # | 項目 | 適用對象與依據 |
|---|---|---|
| 9 | **OGTT（75 g，2-h PG）** | 僅在 FPG／HbA1c 結果不一致、需確立 ADA 診斷分類時使用。ADA 診斷門檻：2-h PG ≥ 200 mg/dL（11.1 mmol/L）為糖尿病、140–199 mg/dL（7.8–11.0 mmol/L）為 prediabetes【L3】[Multidisc_Rugo_2022.md]。⚠ **本回顧未取得任何來源建議在 PI3Ki 治療前常規執行 OGTT**；腫瘤病人若有腹瀉、噁心或食慾不佳，OGTT 的可行性與可解釋性均受限 |
| 10 | **Fructosamine／glycated albumin** | 高風險（基線 prediabetes 或 diabetes）者可於基線及每 2 週監測，通常由內分泌科執行。切點：**fructosamine > 230 μM**、**glycated albumin > 13.35%**【L3】[Mgmt_Goncalves_2022.md][Multidisc_Rugo_2022.md]。特別適用於**貧血、近期輸血、腎功能異常導致 HbA1c 失真**的腫瘤病人 |
| 11 | **血酮（β-hydroxybutyrate）基線值** | 併用 corticosteroids、有 intercurrent infection、或將使用 SGLT2i 者。EMA 建議「Monitoring of HbA1C and **ketones (preferably in blood)**」【L1】[label_inavolisib.md]；SGLT2i 使用者每次回診評估 anion gap 與血／尿酮【L3】[Multidisc_Rugo_2022.md] |
| 12 | **居家血糖機／CGM 配發與教學** | 高風險者應於**起始前 1 週**完成【L3】[Multidisc_Rugo_2022.md] |

---

## D-5. 特別處理：癌症病人的營養狀態波動如何改變風險評估

這一段是本節最需要臨床判斷、也最容易被一般糖尿病分層邏輯誤導的部分。

### D-5-1. BMI 是一個會動的數字，不是固定的分層依據

- MSKCC 247 例接受 alpelisib 的病人中，**BMI 中位變化為 −1.30 kg/m²（相當於起始體重的 −5.5%，IQR −0.33 至 −3.0）**，且此變化在 standard care 與 clinical trial 兩組間**無顯著差異（p=0.2）**——意即體重下降不是「試驗族群特有」的現象，門診族群同樣會發生【L4】📄[MSKCC_RealWorld_Shen_2023.md]
  - ⚠ MSKCC 全文**僅**報告 BMI 變化，**未報告**腹瀉、噁心、脫水、eGFR／腎功能資料，亦未報告 SGLT2i 使用者之 DKA 或泌尿生殖道感染率；本節關於脫水與腎功能的論述須另引其他來源，不可掛在此文名下【L4】📄[MSKCC_RealWorld_Shen_2023.md]
- 體重下降在各藥皆常見：alpelisib（SOLAR-1）任何級別 **26.8%**、grade 3 **3.9%**；inavolisib（INAVO120）**17.0%**／**3.7%**；everolimus（BOLERO-2）19%／1%。**三個試驗的仿單皆未提供體重下降的處置指引**【L3】[ToxMgmt_Jhaveri_2026.md]。FDA 仿單 SOLAR-1 數據亦列 Weight decreased 27%（G3-4 3.9%）、Decreased appetite 36%【L1】[label_alpelisib.md]

**臨床操作結論**：
1. 基線 BMI 應取「最接近但早於用藥起始日」的數值【L4】📄[MSKCC_RealWorld_Shen_2023.md]，並**同時記錄近 3 個月體重軌跡**，不要只記一個橫斷面數字。
2. 治療中若 BMI 因體重下降而跨過 25 或 30 的切點，**不代表風險已下降**——所有 BMI 相關的風險數據皆來自**基線** BMI【L1】[label_alpelisib.md]【L2】📄[SOLAR1_AE_Rugo_2020.md][INAVO120_Turner_2024.md]【L4】[RealWorld_Liu_2022.md]。監測頻率不應因體重下降而放寬。
3. ⚠ **「sarcopenic obesity 會被 BMI 低估」這項推論，本回顧未取得可驗證的本地來源**（本地 38 篇全文中無 sarcopenia／body composition 與 PI3Ki 高血糖之分析）。臨床上可將其視為**降低 BMI 這一列權重、提高 HbA1c 與 FPG 權重**的理由——這與 MSKCC 全文一致：兩者有顯著交互作用（**p=0.005**），同時放入模型時**僅 baseline HbA1c 維持顯著（p<0.001）**【L4】📄[MSKCC_RealWorld_Shen_2023.md]。**當 BMI 與 HbA1c 給出不同分層時，以 HbA1c 為準。**（惟須留意：此結論來自 HbA1c 僅 66.4% 可得的子集，且統計法為 χ²，非多變項迴歸）

### D-5-2. 脫水會放大 metformin 與 SGLT2i 的風險

- alpelisib 仿單 §5.5：「**Severe diarrhea, including dehydration and acute kidney injury**, has occurred」；SOLAR-1 中 diarrhea 58%（G3-4 7%）、**acute kidney injury 為 serious adverse reaction，發生率 2.5%**【L1】[label_alpelisib.md]
- 這代表**基線 eGFR 只是一個起點**：腹瀉→脫水→AKI 會使病人在數天內從「metformin 可用」掉到「metformin 禁忌（eGFR <30）」【L3】[Multidisc_Rugo_2022.md]
- SGLT2i：「**Hold SGLT2 inhibitor if with poor hydration and/or concurrent illness**」、手術或大腸鏡前 5 天停用；並監測 anion gap 與血酮（β-hydroxybutyrate 目標 0.6–3.0 mmol/L）【L3】[Multidisc_Rugo_2022.md]
- 真實世界已有 euglycemic DKA 案例：MSKCC 491 例中，**僅 15 人（含 12 名新使用者）在 PI3K／AKT inhibitor 期間使用 SGLT2i，即出現 1 例 euglycemic DKA**（pH 7.26、bicarbonate 13、anion gap 21、ketonuria）【L4】[RealWorld_Liu_2022.md]

**臨床操作結論**：對已有腹瀉、食慾不佳或脫水風險者，
- 起始前即建立 **eGFR 與電解質的重複測量計畫**，不能只驗一次【L3】[Capivasertib_Mgmt_Iyengar_2025.md]
- 預防性 metformin 的效益／風險天平在此族群**明顯往風險端傾斜**（仿單已明載 metformin 前給藥會增加噁心、嘔吐、腹瀉的發生率與嚴重度）【L1】[label_alpelisib.md]
- 若仍決定使用，**優先選 XR（緩釋）劑型**——XR 較 immediate-release 的 GI 副作用少，有助於降低與 alpelisib 重疊的腹瀉與噁心【L3】[Consensus_Tankova_2022.md]；並可考慮 METALLICA 的作法，即**先給 metformin 加內分泌治療 1 週再加 alpelisib**，讓病人先適應 metformin【L2】[METALLICA_LlombartCussac_2024.md]

### D-5-3. 降糖藥選擇必須避開「加重體重下降」

- **GLP-1 RA**：可用於 BMI > 30 者，但「**the risk of cachexia and malnutrition should be considered**」【L3】[ToxMgmt_Jhaveri_2026.md]。此類藥物「增加飽足感，常導致顯著體重下降」【L3】[Mgmt_Goncalves_2022.md]
- **SGLT2i、metformin**：兩者皆列為「Weight loss: Yes」【L3】[Multidisc_Rugo_2022.md]
- **飲食**：低碳水／生酮飲食雖有機轉與臨床理由，但共識同時提醒「Decreased appetite and weight were observed in clinical trials of alpelisib; hence, **patients should be encouraged to maintain similar level of caloric intake**」，並建議轉介熟悉低碳水膳食規劃的營養師【L3】[Multidisc_Rugo_2022.md][Mgmt_Goncalves_2022.md]

### D-5-4. Albumin 作為分層指標

⚠ **本回顧未取得可驗證來源。** 本地 38 篇全文中，albumin 僅以 **glycated albumin（血糖監測替代指標，切點 >13.35%）**【L3】[Mgmt_Goncalves_2022.md] 及 **corrected calcium 之校正用途**【L1】[label_alpelisib.md] 出現，**沒有任何來源將血清 albumin 作為 PI3Ki 高血糖的風險因子或營養分層依據**。本表因此**不納入 albumin 作為分層門檻**，僅建議作為整體營養評估的一部分留待臨床判斷。

---

## D-6. 分層的四個重要限制（必須向臨床醫師交代）

1. **低風險不等於零風險。** 已報告一名 **BMI 19.55 kg/m²、HbA1c 5.7%、無糖尿病個人史與家族史、無類固醇暴露**的 59 歲女性，在起始 inavolisib **72 小時內**發展為 HHS（血糖 48.0 mmol/L、有效血漿滲透壓 327 mOsm/L、尿酮陰性、糖尿病自體抗體皆陰性、C-peptide 10.2 ng/mL 顯示為嚴重胰島素阻抗而非 β 細胞衰竭）。作者結論：「patients **without high-risk factors** may still experience severe drug-related adverse effects」【L4】[Inavolisib_HHS_Li_2026.md]。**分層決定監測密度，不決定是否監測。**

2. **真實世界的發生率遠高於試驗——這是本節最重要的一個數字。**

   MSKCC 全世代（n=247，alpelisib）any-grade hyperglycemia **152 人（61.5%）**、grade 3–4 **72 人（29.2%）**（grade 3 **56 人 22.7%**、grade 4 **16 人 6.5%**）【L4】📄[MSKCC_RealWorld_Shen_2023.md]。但一旦拆開治療情境，落差極大：

   | | Standard care (n=147) | Clinical trial (n=100) | p |
   |---|---|---|---|
   | Any-grade hyperglycemia | **80.3%** | **34.0%** | **< 0.001** |
   | Grade 3–4 | **40.2%** | **13.0%** | **< 0.001** |
   | Grade 4 | **16 人（10.9%）** | **0 人** | — |

   【L4】📄[MSKCC_RealWorld_Shen_2023.md]

   **這個落差不是統計雜訊，作者做了兩層敏感度分析都撐得住**：
   - 排除發生 DKA 之 standard care 病人與血糖最高 5% 後，兩組差異**仍顯著（p<0.001）**，基線 HbA1c 與高血糖之關聯亦**仍顯著（p=0.001）**
   - 只拿 clinical trial 中接受**標準 300 mg/day** 之次族群（**n=33**）來比，差異**仍顯著：80% vs 52%，p<0.001**——意即落差**不能全部歸因於試驗用了較低劑量**

   **但也必須公允地說明落差的三個來源**（作者自述）：(1) standard care 世代已知糖尿病比例較高，而試驗以 uncontrolled／insulin-dependent diabetes 及 fasting glucose／HbA1c cutoff 為排除條件；(2) phase 1/2 試驗使用低於 300 mg 之劑量（中位 RDI：standard care **277 mg/day＝92% of intended dose** vs clinical trial **246 mg/day＝99% of intended dose**，p<0.001）；(3) 試驗中血糖監測與處置**更結構化、更密集**【L4】📄[MSKCC_RealWorld_Shen_2023.md]。

   第 (3) 點有 SOLAR-1 全文的獨立佐證：SOLAR-1 於試驗中途修訂 protocol（加驗 day 8 門診、收緊 HbA1c 收案門檻、對 FPG ≥100 mg/dL 或 HbA1c ≥5.7% 者於 screening 即衛教與轉介）後，比較前 50% 與後 50% 隨機者——**any-grade 高血糖幾乎不變（63.9% → 63.6%），但 grade 3/4 由 40.3% 降至 32.9%、因高血糖停藥由 9.0% 降至 3.6%、因 grade ≥3 AE 停藥由 18.1% 降至 7.9%**【L2】📄[SOLAR1_AE_Rugo_2020.md]。⚠ 作者自陳此改善「may be attributed to the protocol amendment, **as well as other factors**」，屬**非隨機的時序性關聯**，不可視為因果。

   **對風險分層的三個操作結論**：
   - 所有以試驗數據為基礎的分層與衛教，在門診真實族群中應**視為低估**；用 SOLAR-1／INAVO120 的發生率向病人說明時，須明言「這是被篩選過的族群」。
   - 反過來說，**落差中至少有一部分是可被醫療系統改善的**（監測密度、處置結構化、事前分層轉介）——這正是本節存在的理由。
   - **Grade 4 在 standard care 出現 10.9%、在試驗組為 0%**：真實世界的分層必須把「最壞情況」納入衛教與回診安排，不能以試驗的 grade 4 罕見度安慰病人。

3. **分層應該提早做。** MSKCC 全世代高血糖之**中位發生時間僅 16 天**（定義為 alpelisib 起始日至首次 glucose ≥140 mg/dL 之天數；⚠ 原文**未報 IQR 或全距**）；作者據此明言高血糖在起始後 **14–16 天內**發生，屆時基線風險因子「is no longer meaningfully actionable」，因此應在**轉移性疾病診斷時或第一線治療期間**即測 HbA1c，爭取生活型態介入或早期內分泌科諮詢的時間窗【L4】📄[MSKCC_RealWorld_Shen_2023.md]。此與 alpelisib 仿單之 grade ≥2 中位 15 天、SOLAR-1 全文之 **grade ≥3 中位 15 天（range 5–395）**互相吻合【L1】[label_alpelisib.md]【L2】📄[SOLAR1_AE_Rugo_2020.md]。

   **而基線 HbA1c 的實際檢驗率遠低於應然**：全世代僅 **164/247（66.4%）**有基線 HbA1c；即使在 standard care 組也**只有 72.1%**（clinical trial 組 58.0%，p=0.021）。MSKCC 作者因此「strongly advocate for incorporation of baseline HbA1c measurement into routine clinical practice for patients who are candidates for PI3K inhibitor treatment」【L4】📄[MSKCC_RealWorld_Shen_2023.md]。

4. **分層預測的是「高血糖與治療中斷」，不是「療效」。** MSKCC 中位追蹤 13.7 個月，全世代中位 PFS **6.1 個月（95% CI 4.8–7.3）**；以高血糖狀態為 time-dependent covariate，**與 PFS 無關（HR 0.98；95% CI 0.72–1.33）**，且以高血糖分級、BMI ≥25、HbA1c ≥5.7%、治療情境、是否因高血糖減量／停藥分層，PFS 均無顯著差異【L4】📄[MSKCC_RealWorld_Shen_2023.md]。SOLAR-1 亦顯示基線血糖狀態不影響 PFS 獲益：prediabetes/diabetes 11.0 vs 5.6 個月（HR 0.66；95% CI 0.47–0.92）、normal 10.9 vs 6.5 個月（HR 0.65；95% CI 0.42–1.02）【L2】📄[SOLAR1_AE_Rugo_2020.md]。
   → **臨床意涵**：高風險分層**不是拒絕給藥的理由**，而是「要不要先優化血糖、要不要更密集監測、要不要先轉介內分泌」的理由。

---

## D-7. 安全底線：分層不得延誤 insulin

雖然理論上應避免 hyperinsulinemia（insulin feedback 可能部分再活化 PI3K pathway，此為 preclinical 證據【L5】[InsulinFeedback_Hopkins_2018.md]），但**在下列情況下不得因此延誤 insulin**：

- **Ketoacidosis**：共識明載「**insulin is required for ketoacidosis**」；Grade 3/4 高血糖病人應常規驗酮體，若陽性應停用口服降糖藥，並在住院環境給予**積極的 insulin 與靜脈輸液**【L3】[Consensus_Tankova_2022.md]
- **DKA 處置**：以生理食鹽水補液，接續 insulin 治療與補鉀，pH 持續偏低或嚴重磷缺乏者給予 bicarbonate 或 phosphate【L3】[ToxMgmt_Jhaveri_2026.md]
- **ADA Rec 9.35b**：insulin「should be **reserved for severe hyperglycemia and hyperglycemic crises**」——是限縮用於重症，**不是禁用**【L3】[guideline_ada_comparators.md]
- alpelisib 仿單已載**上市後出現致死性 ketoacidosis**【L1】[label_alpelisib.md]；inavolisib 仿單 5.1 於 2025 年 9 月更新為「can cause **severe or fatal** hyperglycemia **including ketoacidosis**」【L1】[label_inavolisib.md]

---

## D-8. 本節查不到可驗證來源而留白的項目

| 項目 | 狀態 |
|---|---|
| **巨嬰產史（macrosomia）**作為風險因子 | 本回顧未取得可驗證來源。本地檔案僅有 gestational diabetes，無 macrosomia |
| **血清 albumin** 作為風險分層門檻 | 本回顧未取得可驗證來源（僅有 glycated albumin 作為血糖監測替代指標） |
| **Sarcopenic obesity／body composition** 與 PI3Ki 高血糖的關聯 | 本回顧未取得可驗證來源 |
| **Monocytes 的數值切點** | 本回顧未取得可驗證來源（Rodón 模型列為第 5 重要變項，但未給切點，原文自陳 "warrants further investigation"）【L2】[RiskModel_Rodon_2024.md] |
| **經驗證的加權風險計分表／nomogram** | 本回顧未取得可驗證來源（Rodón model 7 的個人分數圖位於 Additional file Figure S3，本地未落地）【L2】[RiskModel_Rodon_2024.md] |
| **eGFR 作為 PI3Ki 高血糖本身的獨立風險因子** | 本回顧未取得可驗證來源。本地所有 eGFR 門檻均是 **metformin 的用藥限制**，非高血糖風險預測 |
| **治療前常規 OGTT 的建議** | 本回顧未取得可驗證來源（OGTT 僅出現於 ADA 診斷標準的引述中） |
| **capivasertib 的量化基線風險分層數據** | 部分留白。本地有 Iyengar 專家意見列舉風險因子【L3】[Capivasertib_Mgmt_Iyengar_2025.md]，但 CAPItello-291 之基線分層 subgroup 數據本回顧未取得 |
| **既往 PI3Ki／AKTi 暴露者的前瞻性風險數據** | 本回顧未取得可驗證來源（METALLICA 與 GO39374 均排除此族群），現有證據僅為單一 case report【L4】[DKA_Rechallenge_Leung_2022.md] |
| **SOLAR-1 AE 專文、INAVO120 主論文、MSKCC 真實世界世代** | ✅ **已解除留白**：三篇均已落地為可 grep 之本地全文（📄）——`原始PDF/SOLAR1_AE_Rugo_2020.md`（PMID 32416251）、`原始PDF/INAVO120_Turner_2024.md`（PMID 39476340）、`原始PDF/MSKCC_RealWorld_Shen_2023.md`（PMID 37743730）。本節 D-1、D-1-1、D-2 外部參照、D-5-1、D-6 已改採其全文數字 |
| **上述三篇之 supplementary appendix** | 仍為留白。INAVO120 之 Table S3（因高血糖停藥率）、SOLAR-1 之 Supplementary Table 1/3/4 與 Supplemental Figure 1、Supplemental Table 6/7 之逐格數值，本地全文檔**不含 supplementary appendix**，不得引用 |
| **BYLieve 主論文之 subgroup 與 supplementary table** | 本回顧未取得可驗證來源（本地僅有 abstract 層級，📌）【參見 來源/inventory.md §7】 |
| **MSKCC 世代之 DKA 實際人數與比率** | 本回顧未取得可驗證來源。全文僅提及敏感度分析「排除發生 DKA 的 standard care 病人」，**未給人數或百分比**；HHS 全文未提及【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| **MSKCC 世代之類固醇使用與高血糖之關聯** | 本回顧未取得可驗證來源（全文未記錄、未分析）【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| **MSKCC 世代依 BMI／HbA1c 分層之高血糖「實際發生率百分比」** | 本回顧未取得可驗證來源（原文**僅報 p 值，未報各層發生率**）【L4】📄[MSKCC_RealWorld_Shen_2023.md] |
| **SOLAR-1 之高血糖風險因子多變量分析（OR/HR/p）** | 本回顧未取得可驗證來源（全文僅有描述性 trend，無任何 OR/HR/p）【L2】📄[SOLAR1_AE_Rugo_2020.md] |
| **INAVO120 主論文之基線 HbA1c／FPG 實際數值與 metformin 使用率** | 本回顧未取得可驗證來源（主論文僅給收案門檻；protocol *allowed* prophylactic metformin 但**未報告使用率與「高風險」之操作型定義**）【L2】📄[INAVO120_Turner_2024.md] |
| **TFDA 中文仿單之風險因子條文** | 本回顧未取得可驗證來源（現有台灣仿單版本日期 2022-09-22，早於 FDA 01/2024 改版，**不含** metformin 預防性給藥段落）【L1】[label_alpelisib.md] |
