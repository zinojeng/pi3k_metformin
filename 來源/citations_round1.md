# PI3Kα inhibitor 相關高血糖 — 第一層文獻搜尋結果（Round 1）

- **擷取日期**：2026-07-21
- **擷取工具**：`mcp__paper-search__search_pubmed`、`mcp__paper-search__search_europepmc`
- **本檔性質**：**搜尋階段的 metadata + abstract 擷取稿**，尚未下載任何全文。
- **全文取得標記**：本檔內**所有**條目一律為 📌（僅有 abstract／metadata）。**在 fetch.py 把 PDF／JATS 落地到 `原始PDF/` 之前，禁止對任何論文的內文細節（劑量調整表、Kaplan–Meier 數字、subgroup、supplementary table）作具體斷言。**
- **重要稽核聲明**：本檔中所有數字與引文，來源皆為 PubMed／Europe PMC 回傳之 **abstract 全文欄位**，非撰寫者記憶。每段 `>` blockquote 均為 abstract 逐字節錄，可用 PMID 回 PubMed 驗證。
- **期刊欄位說明**：paper-search API **未回傳期刊名稱欄位**。表格中標記 `†` 者，為由 DOI 字串本身可辨識之期刊（如 `10.1056/NEJMoa*` → NEJM）；標記「未擷取」者表示本輪未取得可驗證的期刊名，**不以先驗知識補填**。

---

## 0. 本輪未能取得的項目（明白記錄，不用先驗知識補洞）

| 目標主題 | 狀態 |
|---|---|
| FDA / EMA / TFDA **正式仿單**（Piqray、Itovebi、Truqap 原文 label，含 dose modification table） | **本回顧未取得可驗證來源**。PubMed／Europe PMC 不收錄仿單。需另以 DailyMed／EMA EPAR／TFDA 藥品許可證資料庫擷取，屬 Round 2 工作。 |
| 「metformin oncology dosing renal function」專文 | PubMed 檢索 `metformin dosing renal impairment eGFR lactic acidosis guideline` **回傳 0 筆**。本輪僅取得 ADA Standards of Care 2026（PMID 41358891）作為替代來源。 |
| 「ketogenic diet PI3K inhibitor 臨床試驗」獨立論文 | 檢索僅回傳 Noch 2023（PMID 37399061，GBM，臨床前 + 試驗回溯）1 筆。**無獨立的 ketogenic diet + alpelisib 前瞻試驗**被檢出。 |
| CGM（連續血糖監測）於 PI3Ki 病人之專門研究 | 檢索結果過大且雜訊高，本輪未篩出可用條目；僅有 Pla Peris 2022（FGM 個案，PMID 35178031）。 |
| METALLICA（PubMed 檢索） | PubMed 以 `METALLICA metformin prophylaxis alpelisib` 檢索**回傳 0 筆**；改用 **Europe PMC** 才檢出（PMID 38638399）。記錄此檢索行為差異供稽核。 |
| 癌症病人腹瀉／體重下降／脫水／腎功能波動 與 PI3Ki 高血糖交互作用之專文 | **本回顧未取得可驗證來源**。目前僅能從各 AE 管理綜論的 abstract 得知 diarrhea／decreased appetite 為常見 AE，無專門探討脫水—腎功能—metformin／SGLT2i 安全性的論文被檢出。列為 Round 2 補搜重點。 |

---

## 1. 主表：第一層搜尋結果

> `design` 欄位依 abstract 自述之研究型態填寫。證據等級標記見各段落註記。

### 1.1 前瞻性臨床試驗主報告（【L2】）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 31091374 | 2019 | André F | Alpelisib for PIK3CA-Mutated, Hormone Receptor-Positive Advanced Breast Cancer | NEJM † | randomized phase 3 (SOLAR-1) | 10.1056/NEJMoa1813904 | `SOLAR1_Andre_2019` |
| 必拿 | 33246021 | 2021 | André F | Alpelisib plus fulvestrant …: final overall survival results from SOLAR-1 | Ann Oncol † | phase 3 final OS analysis | 10.1016/j.annonc.2020.11.011 | `SOLAR1_OS_Andre_2021` |
| 必拿 | 32416251 | 2020 | Rugo HS | Time course and management of key adverse events during the randomized phase III SOLAR-1 study | Ann Oncol † | phase 3 safety/AE analysis | 10.1016/j.annonc.2020.05.001 | `SOLAR1_AE_Rugo_2020` |
| 必拿 | 33780274 | 2021 | Ciruelos EM | Patient-Reported Outcomes … From SOLAR-1 | J Clin Oncol † | phase 3 PRO analysis | 10.1200/JCO.20.01139 | `SOLAR1_PRO_Ciruelos_2021` |
| 必拿 | 33794206 | 2021 | Rugo HS | Alpelisib plus fulvestrant … after a CDK4/6 inhibitor (BYLieve): cohort A | Lancet Oncol † | phase 2, single-arm, non-comparative | 10.1016/S1470-2045(21)00034-6 | `BYLieve_Rugo_2021` |
| 必拿 | 39637900 | 2024 | Rugo HS | BYLieve cohort A（18 個月追蹤更新版） | Lancet Oncol † | phase 2, single-arm, non-comparative | 10.1016/S1470-2045(24)00673-9 | `BYLieve_Rugo_2024` |
| 必拿 | 38142701 | 2024 | The Editors of The Lancet Oncology | **Expression of concern** — BYLieve | Lancet Oncol † | editorial notice | 10.1016/S1470-2045(23)00673-3 | `BYLieve_EoC_2024` |
| 必拿 | 39476340 | 2024 | Turner NC | Inavolisib-Based Therapy in PIK3CA-Mutated Advanced Breast Cancer | NEJM † | randomized double-blind phase 3 (INAVO120) | 10.1056/NEJMoa2404625 | `INAVO120_Turner_2024` |
| 必拿 | 40454641 | 2025 | Jhaveri KL | Overall Survival with Inavolisib in PIK3CA-Mutated Advanced Breast Cancer | NEJM † | phase 3 final OS analysis | 10.1056/NEJMoa2501796 | `INAVO120_OS_Jhaveri_2025` |
| 必拿 | 42202490 | 2026 | Im SA | Safety analyses of the INAVO120 randomised phase III trial | ESMO Open † | phase 3 safety analysis | 10.1016/j.esmoop.2026.107735 | `INAVO120_Safety_Im_2026` |
| 必拿 | 40513140 | 2025 | Gambardella V | Safety overview and management of inavolisib alone and in combination therapies (GO39374) | ESMO Open † | phase I/Ib dose-escalation/-expansion | 10.1016/j.esmoop.2025.105303 | `GO39374_Gambardella_2025` |
| 必拿 | 38638399 | 2024 | Llombart-Cussac A | **Preventing alpelisib-related hyperglycaemia … using metformin (METALLICA)** | eClinicalMedicine † | **multicentre, open-label, SINGLE-ARM, phase 2** | 10.1016/j.eclinm.2024.102520 | `METALLICA_LlombartCussac_2024` |
| 必拿 | 39177931 | 2024 | Borrego MR | SGLT2 inhibition improves PI3Kα inhibitor-induced hyperglycemia (BYLieve + SOLAR-1) | Breast Cancer Res Treat † | preclinical animal + propensity-matched trial subanalysis | 10.1007/s10549-024-07405-8 | `SGLT2i_Borrego_2024` |
| 必拿 | 40152314 | 2025 | Pancirov M | Dynamics of hyperglycemia of patients treated with alpelisib: exploratory interim analysis of ITACA trial | The Oncologist † | prospective trial, exploratory interim analysis (n=23) | 10.1093/oncolo/oyaf023 | `ITACA_Pancirov_2025` |
| 必拿 | 39241495 | 2024 | Rugo HS | Capivasertib and fulvestrant …: characterization, time course, and management of frequent AEs from CAPItello-291 | ESMO Open † | phase 3 safety analysis | 10.1016/j.esmoop.2024.103697 | `CAPItello291_AE_Rugo_2024` |
| 次要 | 40346047 | 2025 | Hu X | CAPItello-291 extended Chinese cohort | Nat Commun † | phase 3 prespecified exploratory cohort | 10.1038/s41467-025-59210-6 | `CAPItello291_China_Hu_2025` |
| 次要 | 40626336 | 2025 | Fernandez Teruel C | Population PK and Exposure-Response Analyses for Capivasertib | 未擷取 | popPK / exposure-response | 10.1111/cts.70286 | `Capivasertib_PopPK_FernandezTeruel_2025` |
| 次要 | 37634128 | 2023 | Canaud G | Alpelisib for treatment of patients with PROS (EPIK-P1) | Genet Med † | non-interventional retrospective chart review | 10.1016/j.gim.2023.100969 | `EPIKP1_Canaud_2023` |

### 1.2 法規核准摘要（**非仿單本身**；等級介於【L1】與【L2】，須註明係 FDA 審查者撰寫之 approval summary）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 33168657 | 2021 | Narayan P | FDA Approval Summary: Alpelisib Plus Fulvestrant | Clin Cancer Res † | regulatory approval summary | 10.1158/1078-0432.CCR-20-3652 | `FDA_Alpelisib_Narayan_2021` |
| 必拿 | 40845250 | 2025 | Wedam S | US FDA Approval Summary: Inavolisib With Palbociclib and Fulvestrant | J Clin Oncol † | regulatory approval summary | 10.1200/JCO-25-00663 | `FDA_Inavolisib_Wedam_2025` |
| 必拿 | 39159418 | 2024 | Dilawari A | US FDA Approval Summary: Capivasertib With Fulvestrant | J Clin Oncol † | regulatory approval summary | 10.1200/JCO.24.00427 | `FDA_Capivasertib_Dilawari_2024` |

### 1.3 專家共識／Delphi／學會指引／AE 管理綜論（【L3】）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 38297009 | 2024 | Gallagher EJ | Managing hyperglycemia and rash associated with alpelisib: expert consensus using the Delphi technique | npj Breast Cancer † | modified Delphi consensus | 10.1038/s41523-024-00613-x | `Delphi_Gallagher_2024` |
| 必拿 | 35406370 | 2022 | Tankova T | Management Strategies for Hyperglycemia Associated with the α-Selective PI3K Inhibitor Alpelisib | Cancers † | expert consensus (14 oncologists + 7 endocrinologists) | 10.3390/cancers14071598 | `Consensus_Tankova_2022` |
| 必拿 | 35075945 | 2022 | Goncalves MD | Management of Phosphatidylinositol-3-Kinase Inhibitor-Associated Hyperglycemia | Integr Cancer Ther † | narrative review / management guidance | 10.1177/15347354211073163 | `Mgmt_Goncalves_2022` |
| 必拿 | 35016012 | 2022 | Rugo HS | A multidisciplinary approach to optimizing care of patients treated with alpelisib | The Breast † | narrative review / management guidance | 10.1016/j.breast.2021.12.016 | `Multidisc_Rugo_2022` |
| 必拿 | 39462728 | 2025 | Moore HN | Effective Strategies for the Prevention and Mitigation of PI3K Inhibitor-Associated Hyperglycemia | Clin Breast Cancer † | expert review / management guidance | 10.1016/j.clbc.2024.09.017 | `Prevention_Moore_2025` |
| 必拿 | 41604817 | 2026 | Jhaveri KL | Clinical management of common toxicities with inhibitors targeting the PI3K/AKT/mTOR pathway in breast cancer | ESMO Open † | pooled phase III safety review + guidance | 10.1016/j.esmoop.2025.105936 | `ToxMgmt_Jhaveri_2026` |
| 必拿 | 41345397 | 2025 | Iyengar NM | Optimizing clinical monitoring and management guidelines for capivasertib | npj Breast Cancer † | expert opinion | 10.1038/s41523-025-00864-2 | `Capivasertib_Mgmt_Iyengar_2025` |
| 必拿 | 41358891 | 2026 | (ADA Professional Practice Committee) | 3. Prevention or Delay of Diabetes and Associated Comorbidities: Standards of Care in Diabetes-2026 | Diabetes Care † | society clinical practice guideline | 10.2337/dc26-s003 | `ADA_SOC2026_Ch3` |
| 次要 | 39674130 | 2024 | Fanucci K | Practical treatment strategies and novel therapies in the PI3K/AKT/mTOR pathway in HR+/HER2− ABC | ESMO Open † | narrative review | 10.1016/j.esmoop.2024.103997 | `Review_Fanucci_2024` |
| 次要 | 41658572 | 2025 | Alshehri A | Optimizing second-line endocrine-based treatment … GCC Region expert statement | Front Oncol † | regional expert consensus | 10.3389/fonc.2025.1706670 | `Consensus_GCC_Alshehri_2025` |

### 1.4 機轉／insulin feedback（【L5】前臨床或機轉推論）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 30051890 | 2018 | Hopkins BD | **Suppression of insulin feedback enhances the efficacy of PI3K inhibitors** | Nature † | preclinical (mouse tumor models) | 10.1038/s41586-018-0343-4 | `InsulinFeedback_Hopkins_2018` |
| 必拿 | 37399061 | 2023 | Noch EK | Insulin feedback is a targetable resistance mechanism of PI3K inhibition in glioblastoma | Neuro Oncol † | preclinical + retrospective phase 2 trial analysis | 10.1093/neuonc/noad117 | `InsulinFeedback_Noch_2023` |
| 次要 | 38319732 | 2024 | Duchatel RJ | PI3K/mTOR is a therapeutically targetable genetic dependency in DIPG（paxalisib + metformin） | J Clin Invest † | preclinical | 10.1172/JCI170329 | `Paxalisib_Metformin_Duchatel_2024` |
| 次要 | 36490341 | 2022 | Ladraa S | PIK3CA gain-of-function mutation in adipose tissue induces metabolic reprogramming … severe endocrine disruption | Sci Adv † | preclinical + patient samples | 10.1126/sciadv.ade7823 | `Adipose_Ladraa_2022` |
| 次要 | 41347072 | 2025 | Shi Y | Metformin enhances alpelisib sensitivity in HER2+ breast cancer | Front Oncol † | in vitro preclinical | 10.3389/fonc.2025.1631415 | `Preclinical_Shi_2025` |

### 1.5 回溯性／real-world／pharmacovigilance（【L4】）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 37743730 | 2023 | Shen S | Incidence, risk factors, and management of alpelisib-associated hyperglycemia in metastatic breast cancer | Cancer † | single-centre retrospective (n=247, MSKCC) | 10.1002/cncr.34928 | `RealWorld_Shen_2023` |
| 必拿 | 35212193 | 2022 | Liu D | Characterization, management, and risk factors of hyperglycemia during PI3K or AKT inhibitor treatment | Cancer Med † | retrospective (n=491) | 10.1002/cam4.4579 | `RealWorld_Liu_2022` |
| 必拿 | 38439079 | 2024 | Rodón J | A risk analysis of alpelisib-induced hyperglycemia in advanced solid tumors and breast cancer | Breast Cancer Res † | pooled trial data + machine-learning risk model | 10.1186/s13058-024-01773-1 | `RiskModel_Rodon_2024` |
| 必拿 | 36409396 | 2023 | Burnette SE | Evaluation of alpelisib-induced hyperglycemia prophylaxis and associated risk factors | Breast Cancer Res Treat † | single-centre retrospective (n=16) | 10.1007/s10549-022-06798-8 | `Prophylaxis_Burnette_2023` |
| 必拿 | 38245400 | 2024 | Ziegengeist JL | Alpelisib-Induced Diabetic Ketoacidosis: A Pharmacovigilance Analysis of FAERS | Clin Breast Cancer † | disproportionality analysis (FAERS) + literature review | 10.1016/j.clbc.2024.01.004 | `FAERS_DKA_Ziegengeist_2024` |
| 必拿 | 42159385 | 2026 | Ismail M | Assessment of alpelisib-induced hyperglycemia in a real-world setting: nationwide claims data analysis | J Oncol Pharm Pract † | retrospective longitudinal claims (n=546) | 10.1177/10781552261451729 | `Claims_Ismail_2026` |
| 次要 | 38011835 | 2024 | Sarfraz H | A Cohort Study of the Antitumor Efficacy and Toxicity Profile of Alpelisib … Single-Institution | 未擷取 | retrospective cohort (n=76) | 10.1159/000534953 | `RealWorld_Sarfraz_2024` |
| 必拿 | 36611120 | 2023 | Bello Roufai D | Alpelisib and fulvestrant … French early access program | Oncogene † | prospective registry / real-life (n=233) | 10.1038/s41388-022-02585-3 | `FrenchEAP_BelloRoufai_2023` |
| 必拿 | 33752998 | 2021 | Cook K | Alpelisib-induced hyperglycemia in older patients with breast cancer: qualitative findings | J Geriatr Oncol † | qualitative chart review (n=34, age ≥65) | 10.1016/j.jgo.2021.03.007 | `Elderly_Cook_2021` |
| 次要 | 41681940 | 2026 | Loizidis S | Alpelisib + ET vs Everolimus + ET after CDK4/6i progression | Cancers † | single-centre retrospective | 10.3390/cancers18030468 | `RealWorld_Loizidis_2026` |
| 次要 | 33909934 | 2021 | Turner S | Effectiveness of Alpelisib + Fulvestrant Compared with Real-World Standard Treatment | The Oncologist † | matched/weighted trial-vs-real-world comparison | 10.1002/onco.13804 | `BYLieve_RWD_Turner_2021` |
| 次要 | 36321996 | 2023 | Rugo HS | Biology and Targetability of the Extended Spectrum of PIK3CA Mutations | Clin Cancer Res † | genomic + clinico-genomic database analysis | 10.1158/1078-0432.CCR-22-2115 | `PIK3CAm_Rugo_2023` |
| 次要 | 42121892 | 2026 | Pellegrino F | Alpelisib in PROS: A Systematic Review of Real-World Evidence in over 100 Patients | Cells † | systematic review of real-world reports | 10.3390/cells15090788 | `PROS_SR_Pellegrino_2026` |

### 1.6 個案報告／case series — DKA、HHS、飲食與 SGLT2i（【L4】）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 39896940 | 2025 | Loke M | Alpelisib-Induced Diabetic Ketoacidosis and Insulin-Resistant Hyperglycemia | AACE Clin Case Rep † | case report | 10.1016/j.aace.2024.10.002 | `DKA_Loke_2025` |
| 次要 | 34095470 | 2021 | Carrillo M | Alpelisib-Induced Diabetic Ketoacidosis: A Case Report and Review of Literature | AACE Clin Case Rep † | case report + review | 10.1016/j.aace.2020.11.028 | `DKA_Carrillo_2021` |
| 必拿 | 35750516 | 2022 | Chafai K | An atypical alpelisib-induced hyperglycemic hyperosmolar and diabetic ketoacidosis state … critical analysis of management guidelines | Ann Endocrinol † | case report + guideline critique | 10.1016/j.ando.2022.02.004 | `HHS_DKA_Chafai_2022` |
| 必拿 | 42181200 | 2026 | Li H | **Inavolisib-induced fulminant-like diabetes and hyperosmolar hyperglycemic state** | Front Endocrinol † | case report | 10.3389/fendo.2026.1747317 | `Inavolisib_HHS_Li_2026` |
| 必拿 | 36330532 | 2022 | Leung M | Ketoacidosis in a Patient with Type 2 Diabetes Requiring Alpelisib: Learnings … Initiation and Rechallenge | Onco Targets Ther † | case report（含 rechallenge） | 10.2147/ott.s370244 | `DKA_Rechallenge_Leung_2022` |
| 必拿 | 28856166 | 2017 | Bowman C | **Ketoacidosis With Canagliflozin Prescribed for PI3K Inhibitor-Induced Hyperglycemia** | J Investig Med High Impact Case Rep † | case report（taselisib + SGLT2i） | 10.1177/2324709617725351 | `EuglycemicDKA_Bowman_2017` |
| 必拿 | 34259084 | 2021 | Blow T | Treating Alpelisib-Induced Hyperglycemia with Very Low Carbohydrate Diets and SGLT2 Inhibitors: A Case Series | Integr Cancer Ther † | case series (n=3) | 10.1177/15347354211032283 | `VLCD_SGLT2i_Blow_2021` |
| 必拿 | 35178031 | 2022 | Pla Peris B | Alpelisib-Induced Diabetes Mellitus: Case Report, Pharmacodynamics and Management Considerations | Front Endocrinol † | case report + flash glucose monitoring | 10.3389/fendo.2022.802612 | `FGM_PlaPeris_2022` |
| 次要 | 35975254 | 2022 | Ekanayake PS | ALPELISIB-INDUCED HYPERGLYCEMIA | Acta Endocrinol (Buchar) † | case series (n=3) | 10.4183/aeb.2022.115 | `CaseSeries_Ekanayake_2022` |
| 次要 | 35712858 | 2022 | Thomas K | S.U.G.A.R: A Case to Outline Tactics for the Prevention of Alpelisib-Induced Hyperglycemia | J Investig Med High Impact Case Rep † | case report + proposed protocol | 10.1177/23247096221105249 | `SUGAR_Thomas_2022` |
| 次要 | 38524964 | 2024 | Polisetty L | Diabetic Ketoacidosis With the Use of Alpelisib in a Patient … Without Diabetes | JCEM Case Rep † | case report | 10.1210/jcemcr/luae023 | `DKA_Polisetty_2024` |
| 次要 | 35834907 | 2022 | Dao EA | Periorbital edema associated with alpelisib | Cancer Treat Res Commun † | case series | 10.1016/j.ctarc.2022.100596 | `PeriorbitalEdema_Dao_2022` |

### 1.7 系統性回顧／統合分析

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 必拿 | 40535135 | 2025 | Li X | Efficacy and safety of PI3K inhibitors combined with fulvestrant for HR+/HER2− ABC: systematic review and meta-analysis | Front Oncol † | SR + meta-analysis（5 RCT, n=3,011） | 10.3389/fonc.2025.1556978 | `Meta_Li_2025` |
| 必拿 | 29108713 | 2018 | Martel S | Risk of adverse events with the addition of targeted agents to endocrine therapy … SR and meta-analysis | Cancer Treat Rev † | SR + meta-analysis（16 studies, n=8,529） | 10.1016/j.ctrv.2017.09.009 | `Meta_Martel_2018` |

### 1.8 藥物經濟學（背景用，非本回顧核心）

| 優先序 | PMID | 年份 | 第一作者 | 標題 | 期刊 | design | DOI | 建議 slug |
|---|---|---|---|---|---|---|---|---|
| 次要 | 41989051 | 2026 | Zeng H | Economic Evaluation of Inavolisib … in USA | Technol Cancer Res Treat † | Markov cost-effectiveness | 10.1177/15330338261444965 | `CEA_Zeng_2026` |
| 次要 | 41496420 | 2026 | Zhu J | Cost-effectiveness of inavolisib plus palbociclib-fulvestrant | The Breast † | partitioned survival model | 10.1016/j.breast.2026.104693 | `CEA_Zhu_2026` |
| 次要 | 37975961 | 2023 | Wu W | Is Alpelisib Plus Fulvestrant Cost-Effective … in the USA? | Clin Drug Investig † | Markov cost-effectiveness | 10.1007/s40261-023-01325-z | `CEA_Wu_2023` |

---

## 2. 關鍵 abstract 逐字節錄（供稽核 grep）

> **再次提醒**：以下為 **abstract 層級** 引文（📌）。全文中的劑量調整表、CTCAE 分級處置流程、supplementary table 尚未取得，**Round 1 不得對其作斷言**。

### 2.1 SOLAR-1 主報告 — PMID 31091374（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/31091374/

> "In the cohort of patients with PIK3CA-mutated cancer, progression-free survival at a median follow-up of 20 months was 11.0 months (95% confidence interval [CI], 7.5 to 14.5) in the alpelisib-fulvestrant group, as compared with 5.7 months (95% CI, 3.7 to 7.4) in the placebo-fulvestrant group (hazard ratio for progression or death, 0.65; 95% CI, 0.50 to 0.85; P<0.001)"

> "In the overall population, the most frequent adverse events of grade 3 or 4 were hyperglycemia (36.6% in the alpelisib-fulvestrant group vs. 0.7% in the placebo-fulvestrant group) and rash (9.9% vs. 0.3%). Diarrhea of grade 3 occurred in 6.7% of patients in the alpelisib-fulvestrant group, as compared with 0.3% of those in the placebo-fulvestrant group; no diarrhea of grade 4 was reported. The percentages of patients who discontinued alpelisib and placebo owing to adverse events were 25.0% and 4.2%, respectively."

### 2.2 SOLAR-1 AE 時序與管理 — PMID 32416251（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/32416251/

> "Patients were randomly assigned to receive fulvestrant plus alpelisib (n = 284) or placebo (n = 287). The most common grade 3/4 AEs with alpelisib were hyperglycemia (grade 3, 32.7%; grade 4, 3.9%), rash (grade 3, 9.9%), and diarrhea (grade 3, 6.7%). Median time to onset of grade ≥3 toxicity was 15 days (hyperglycemia, based on fasting plasma glucose), 13 days (rash), and 139 days (diarrhea)."

> "Metformin alone or in combination with other antidiabetic agents was used by most patients (87.1%) with hyperglycemia."

> "Discontinuations due to grade ≥3 AEs were lower following more-detailed AE management guidelines (7.9% versus 18.1% previously). Patients with PIK3CA mutations had a median alpelisib dose intensity of 248 mg/day. Median progression-free survival with alpelisib was 12.5 and 9.6 months for alpelisib dose intensities of ≥248 mg/day and <248 mg/day, respectively, compared with 5.8 months with placebo."

### 2.3 SOLAR-1 最終 OS — PMID 33246021（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/33246021/

> "In the PIK3CA-mutated cohort (n = 341), median OS [95% confidence interval (CI)] was 39.3 months (34.1-44.9) for alpelisib-fulvestrant and 31.4 months (26.8-41.3) for placebo-fulvestrant [hazard ratio (HR) = 0.86 (95% CI, 0.64-1.15; P = 0.15)]. OS results did not cross the prespecified efficacy boundary."

### 2.4 BYLieve cohort A（2024 更新） — PMID 39637900（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/39637900/

> "127 patients with at least 18 months' follow-up were enrolled into cohort A. 119 patients had a centrally confirmed PIK3CA mutation. … 64 (53·8%; 95% CI 44·4-63·0) of 119 patients were alive without disease progression at 6 months. The most frequent grade 3 or worse adverse events were hyperglycaemia (37 [29%] of 127 patients), rash (13 [10%]), and rash maculopapular (11 [9%])."

**⚠️ 稽核註記**：BYLieve 有一則 **Lancet Oncology Expression of Concern（PMID 38142701, 2024, DOI 10.1016/S1470-2045(23)00673-3）**。引用 BYLieve 數據時必須一併揭露。

### 2.5 INAVO120 主報告 — PMID 39476340（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/39476340/

> "A total of 161 patients were assigned to the inavolisib group and 164 to the placebo group; the median follow-up was 21.3 months and 21.5 months, respectively. The median progression-free survival was 15.0 months (95% confidence interval [CI], 11.3 to 20.5) in the inavolisib group and 7.3 months (95% CI, 5.6 to 9.3) in the placebo group (hazard ratio for disease progression or death, 0.43; 95% CI, 0.32 to 0.59; P<0.001)."

> "The incidence of grade 3 or 4 neutropenia was 80.2% in the inavolisib group and 78.4% in the placebo group; **grade 3 or 4 hyperglycemia, 5.6% and 0%**, respectively; grade 3 or 4 stomatitis or mucosal inflammation, 5.6% and 0%; and grade 3 or 4 diarrhea, 3.7% and 0%."

**臨床要點（供第二輪查證）**：INAVO120 的 grade 3/4 hyperglycemia 為 **5.6%**，SOLAR-1 alpelisib 臂為 **grade 3 32.7% + grade 4 3.9%**。**alpelisib 與 inavolisib 的高血糖負擔量級不同，禁止混為一談。**

### 2.6 INAVO120 OS — PMID 40454641（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/40454641/

> "After a median follow-up of 34.2 months in the inavolisib group and 32.3 months in the placebo group, the median overall survival was 34.0 months (95% confidence interval [CI], 28.4 to 44.8) with inavolisib and 27.0 months (95% CI, 22.8 to 38.7) with placebo (hazard ratio for death, 0.67; 95% CI, 0.48 to 0.94; P = 0.02 [prespecified boundary for statistical significance, P<0.0469])."

### 2.7 INAVO120 安全性專篇 — PMID 42202490（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/42202490/

> "Inavolisib was given 9 mg orally once daily on days 1-28 of each 28-day cycle; palbociclib, at 125 mg orally once daily on days 1-21; fulvestrant, at 500 mg intramuscularly on days 1 and 15 of cycle 1, and every ∼28 days thereafter."

> "Inavolisib dose interruptions, reductions and discontinuations due to hyperglycaemia were observed in 27.2%, 2.5% and 0.6% of patients, respectively; the median time to first onset was 7.0 days (range 2.0-955.0). Metformin was the most commonly used antihyperglycaemic. **No patients in the prediabetic population discontinued inavolisib due to hyperglycaemia.**"

> "Inavolisib dose interruptions, reductions and discontinuations due to diarrhoea were observed in 6.8%, 1.2% and 0% of patients respectively; the median time to first onset was 13.0 days (range 1.0-610.0). Loperamide was most commonly used."

### 2.8 GO39374 inavolisib 安全性 — PMID 40513140（【L2】📌）
URL: https://europepmc.org/articles/PMC12205636

> "At data cutoff (1 January 2024), 190 patients had been treated… Hyperglycemia, diarrhea, stomatitis (grouped terms), and rash (grouped terms) occurred in 129 (67.9%), 124 (65.3%), 93 (48.9%), and 47 (24.7%) patients, respectively."

> "**Hyperglycemia remained frequent in patients with risk factors, despite early metformin treatment.**"

### 2.9 METALLICA — PMID 38638399（【L2】📌，**單臂 phase 2**）
URL: https://europepmc.org/articles/PMC11024566

> "this 2-cohort, phase 2, multicentre, **single-arm** trial (NCT04300790) enrolled patients with HR+/HER2-/PIK3CA-mutated ABC: **cohort A, normal glycaemia (fasting plasma glucose <100 mg/dL [<5.6 mmol/L] and HbA1c <5.7%), and cohort B, prediabetes (fasting plasma glucose 100-140 mg/dL [5.6-7.8 mmol/L] and/or haemoglobin A1C [HbA1c] 5.7-6.4%)**."

> "233 patients were screened, and 68 (20.2%) patients were enrolled in cohorts A (n = 48) and B (n = 20)… Over the first 8 weeks, **one (2.1%) of 48 patients in cohort A** (95% CI: 0.5-11.1; P < 0.0001), and **three (15.0%) of 20 patients in cohort B** (95% CI: 5.6-37.8; P = 0.016) had grade 3-4 hyperglycaemia."

> "Discontinuation of alpelisib caused by AEs was reported in nine patients (13.2%), **none caused by hyperglycaemia**."

> "In the full analysis set, median PFS was 7.3 months (95% CI: 5.9-not reached), ORR was 20.6% (95% CI: 11.7-32.1%), and CBR was 52.9% (95% CI: 40.4-65.2)."

**⚠️ 撰寫禁忌提醒**：METALLICA 為 **單臂、無對照組、n=68（A 48 / B 20）**，且**排除已知糖尿病族群**（收案條件為正常血糖或 prediabetes）。**不得寫成「已證明所有病人都該用預防性 metformin」。** 其結論僅支持「在 baseline 正常血糖或 prediabetes 的病人，預防性 metformin 下 grade 3-4 高血糖發生率低」。

### 2.10 Delphi 共識 — PMID 38297009（【L3】📌）
URL: https://europepmc.org/articles/PMC10831089

> "Per the hyperglycemia panel, it is appropriate to start alpelisib in patients with **HbA1c 6.5% (diabetes) to <8%, or at highest risk for developing hyperglycemia, if they have a pre-treatment endocrinology consult. Recommend prophylactic metformin in patients with baseline HbA1c 5.7% to 6.4%. Metformin is the preferred first-line anti-hyperglycemic agent.** Per the rash panel, initiate prophylactic nonsedating H1 antihistamines in patients starting alpelisib."

### 2.11 Tankova 共識 — PMID 35406370（【L3】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/35406370/

> "Hyperglycemia is an on-target effect of alpelisib affecting **approximately 60% of treated patients**, and sometimes necessitating dose reductions, treatment interruptions, or discontinuation of alpelisib."

> "Lifestyle modifications, mainly comprising a reduced-carbohydrate diet, and a designated stepwise, personalized antihyperglycemic regimen, **based on metformin, sodium-glucose co-transporter 2 inhibitors, and pioglitazone**, are the main tools required to address the insulin-resistant hyperglycemia induced by alpelisib. In this report, based on the consensus of **14 oncologists and seven endocrinologists**…"

### 2.12 Goncalves & Farooki 管理綜論 — PMID 35075945（【L3】📌）
URL: https://europepmc.org/articles/PMC8793384

> "PI3Ki-induced hyperglycemia results in a compensatory increase in insulin release, which has been shown to reduce the efficacy of treatment by reactivating the PI3K pathway in preclinical models."

> "Risk factors for the development of hyperglycemia include **older age (≥75 years), overweight/obese at baseline, and family history of diabetes**."

> "Medications that do not affect the PI3K pathway are preferred as the primary and secondary agents for the management of hyperglycemia. These include **metformin, sodium-glucose co-transporter 2 inhibitors, thiazolidinediones, and α-glucosidase inhibitors. Insulin should only be considered as a last-line agent for PI3Ki-associated hyperglycemia due to its stimulatory effect of PI3K signaling.**"

**⚠️ 撰寫禁忌提醒**：此段所述「insulin 為 last-line」係針對 **慢性血糖控制策略**。**不可援引此句去延誤嚴重高血糖／DKA／HHS 之急性期 insulin 治療**（見 §2.17–2.20 各 DKA/HHS 個案，急性期均以 IV insulin 處置後迅速緩解）。

### 2.13 Hopkins insulin feedback（Nature） — PMID 30051890（【L5】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/30051890/

> "As p110α mediates virtually all cellular responses to insulin, targeted inhibition of this enzyme disrupts glucose metabolism in multiple tissues. For example, blocking insulin signalling promotes glycogen breakdown in the liver and prevents glucose uptake in the skeletal muscle and adipose tissue, resulting in transient hyperglycaemia within a few hours of PI3K inhibition."

> "Here we show, in several model tumours in mice, that systemic glucose-insulin feedback caused by targeted inhibition of this pathway is sufficient to activate PI3K signalling, even in the presence of PI3K inhibitors. This insulin feedback can be prevented using dietary or pharmaceutical approaches, which greatly enhance the efficacy/toxicity ratios of PI3K inhibitors."

### 2.14 Noch — insulin feedback 於 GBM — PMID 37399061（【L5】+【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/37399061/

> "We found that PI3K inhibition induces hyperglycemia and hyperinsulinemia in mice and that combining metformin with PI3K inhibition improves the treatment efficacy in an orthotopic GBM xenograft model. Through examination of clinical trial data, we found that **hyperglycemia was an independent factor associated with poor progression-free survival in patients with GBM**."

### 2.15 SGLT2i 於 SOLAR-1 / BYLieve — PMID 39177931（【L2】subanalysis +【L5】📌）
URL: https://europepmc.org/articles/PMC11452482

> "Hyperglycemia adverse events (AEs) were compared between patients receiving SGLT2i with alpelisib (**n = 19**) and a propensity score-matched cohort not receiving SGLT2i (**n = 74**) in both trials."

> "Compared with a matched set of patients without SGLT2i, patients receiving SGLT2i had **4.9 and 6.4 times lower rates of grade ≥ 3 hyperglycemia AEs and hyperglycemia AEs resulting in alpelisib dose adjustments, interruptions, or withdrawals**, respectively, and a relative reduction in risk of experiencing these AEs (70.6% and 35.7%)."

> "No signs of ketosis or drug-drug interaction were observed when metformin and dapagliflozin was administered with alpelisib. Alpelisib antitumor efficacy was maintained when used with dapagliflozin in tumor-bearing rats."

**⚠️ 注意樣本數**：SGLT2i 組僅 **n=19**，為 post-hoc propensity-matched 分析，非隨機分派。

### 2.16 Liu — MSKCC PI3K/AKT inhibitor 高血糖大宗回溯 — PMID 35212193（【L4】📌）
URL: https://europepmc.org/articles/PMC9041081

> "**Four hundred and ninety-one patients** with 10 unique cancer types who received a PI3K or AKT inhibitor were included… **Twelve percent of patients required a dose interruption, 6% of patients required a dose reduction and 2% of patients were hospitalized** to manage hyperglycemia."

> "**No events occurred among patients receiving β-, γ-, or δ- specific PI3K inhibitor.**"

> "**SGLT2 inhibitors were associated with the greatest reductions in blood sugar, followed by metformin. At least one case of euglycemic diabetic ketoacidosis (DKA) occurred in a patient on PI3K inhibitor and SGLT2 inhibitor.** Body mass index ≥ 25 and HbA1c ≥ 5.7 are were independently significant predictors of developing hyperglycemia."

> "SGLT2-inhibitor may be a particularly effective second-line option after metformin **but there is a low risk of euglycemic DKA, which can be deadly**."

### 2.17 Shen — MSKCC alpelisib 高血糖發生率 — PMID 37743730（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/37743730/

> "Among **247 patients**, baseline median body mass index was 25.4 kg/m2 and median hemoglobin A1c (HbA1c) was 5.5%. A total of **152 patients (61.5%) developed any-grade hyperglycemia and 72 patients (29.2%) developed grade 3-4 hyperglycemia; median time to onset was 16 days.**"

> "rates of hyperglycemia were significantly higher in patients treated as standard care versus on a clinical trial (**any-grade hyperglycemia 80.3% vs. 34.0%, grade 3-4 hyperglycemia 40.2% vs. 13.0%, p < .001**)."

> "Baseline HbA1c was significantly associated with development of hyperglycemia (p < .001) and alpelisib dose reduction/discontinuation (p = .015)."

### 2.18 Rodón — 風險模型 — PMID 38439079（【L2】pooled +【L4】📌）
URL: https://europepmc.org/articles/PMC10913434

> "A random forest model identified **5 baseline characteristics most associated with risk of developing grade 3/4 hyperglycemia (fasting plasma glucose, body mass index, HbA1c, monocytes, age)**."

> "Among patients in SOLAR-1 (alpelisib + fulvestrant arm) with PIK3CA mutations, **median progression-free survival was similar between the high- and low-risk groups (11.0 vs. 10.9 months)**."

### 2.19 ITACA 期中 — PMID 40152314（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/40152314/

> "This exploratory interim analysis of the ongoing ITACA trial included **23 patients**… Most patients, **21 (91.3%), experienced any-grade hyperglycemia (Grade 1: 9 [39.1%], Grade 2: 8 [34.8%], Grade 3: 4 [17.4%], and Grade 4: 0 [0.0%]) within the first week of alpelisib initiation. The median grade 2-4 hyperglycemia-free survival was 6 days (95% CI 3; 44 days).**"

> "This exploratory interim analysis demonstrated the rapid onset of hyperglycemia in patients receiving alpelisib, **even with the ITACA trial's dietary interventions**."

### 2.20 Loke — alpelisib DKA — PMID 39896940（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/39896940/

> "On presentation, blood glucose level was **612 mg/dL** and hemoglobin A1c level was **11.9% (107 mmol/mol)**, a 4.6% (27 mmol/mol) increase from 2 months prior. **The patient was started on intravenous insulin and alpelisib was held resulting in rapid resolution of the patient's hyperglycemia and ketoacidosis.**"

> "Most cases can be controlled with oral agents; however, **insulin therapy is required in rare instances**. Although more effective for glycemic control, insulin therapy has the potential to decrease the antitumor effects of alpelisib."

### 2.21 Chafai — HHS + DKA 混合狀態 — PMID 35750516（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/35750516/

> 標題：「An atypical alpelisib-induced hyperglycemic hyperosmolar and diabetic ketoacidosis state: A case report and **critical analysis of alpelisib-induced hyperglycemia management guidelines**」

**註**：PubMed 未提供本篇 abstract 內文（abstract 欄位為空）。**Round 1 不得對其內文作任何具體斷言**，須待全文落地。

### 2.22 Inavolisib 誘發 fulminant-like diabetes + HHS — PMID 42181200（【L4】📌）
URL: https://europepmc.org/articles/PMC13194030

> "A 59-year-old female patient with metastatic breast cancer developed rapid-onset and severe hyperglycemia (**blood glucose: 48.0 mmol/L** at emergency presentation) progressing to **HHS within 72 hours** of initiating Inavolisib therapy. She presented with fatigue but showed no evidence of ketoacidosis. She had no personal or family history of diabetes mellitus…"

> "Admission laboratory findings included **glycated hemoglobin A1c (HbA1c) 5.7%** (reference: 4.0-6.0%), fasting plasma glucose 8.6 mmol/L, **fasting insulin 41.5 μU/mL** (reference: 2.6-24.9 μU/mL), and **fasting C-peptide 10.2 ng/mL** (reference: 1.1-4.4 ng/mL), Diabetes-related autoantibodies (ICA, GADA, IAA) were negative. **After discontinuation of Inavolisib and administration of intensive insulin therapy, the patient's hyperglycemia resolved rapidly.**"

> "**Normal baseline glycemic indices do not reliably exclude the risk of severe toxicity.** Early metabolic assessment, close glucose monitoring, prompt interruption of inavolisib when clinically indicated, and **rapid insulin-based management** are essential."

**⚠️ 這是對「一律避免 insulin」論點最重要的反例。急性 HHS／DKA 時 insulin 為必要治療。**

### 2.23 Leung — DKA 與 rechallenge — PMID 36330532（【L4】📌）
URL: https://europepmc.org/articles/PMC9624212

> "A case is presented on a patient with metastatic breast cancer and type 2 diabetes admitted for DKA **eleven days after starting alpelisib**. Since DKA is implicated in antihyperglycemics that inhibit sodium-glucose cotransporter-2 (SGLT2) inhibitors, her empagliflozin was discontinued… After the DKA resolved, she was discharged and restarted alpelisib. **Within 4 hours of taking the first dose, the patient developed a second episode of DKA**, and alpelisib treatment was stopped permanently."

> "**Restarting alpelisib can result in severe hyperglycemia or DKA within 24 hours of the first dose.** … **Continuous glucose monitoring and hospital admission are recommended during rechallenge.**"

### 2.24 Bowman — SGLT2i 誘發 ketoacidosis（taselisib） — PMID 28856166（【L4】📌）
URL: https://europepmc.org/articles/PMC5571767

> "A 69-year-old female patient with no previous history of diabetes mellitus was enrolled in a clinical trial for taselisib therapy in stage IV breast cancer. Hyperglycemia treatment with metformin was insufficient and not tolerated. **The addition of canagliflozin daily resulted in ketoacidosis and hospitalization within 1 week.**"

> "This case report brings together 2 poorly understood and relatively understudied disorders of glucose homeostasis: hyperglycemia due to PI3K inhibition and **euglycemic ketoacidosis due to dehydration/SGLT2 inhibition**."

**⚠️ 與「癌症病人腹瀉／食慾不佳／脫水」高度相關 — SGLT2i 在脫水病人有 euglycemic DKA 風險。**

### 2.25 Blow — 極低碳水飲食 + SGLT2i — PMID 34259084（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/34259084/

> "Currently, there are no clear guidelines on how to manage hyperglycemia due to alpelisib when metformin is not effective. In this case series, we review **3 subjects** with ABC that developed hyperglycemia during alpelisib-fulvestrant therapy and were successfully managed with dietary and pharmacologic interventions. These cases provide **anecdotal evidence** to support the use of sodium-glucose co-transporter-2 inhibitors (SGLT2i) and very low carbohydrate diets."

### 2.26 Pla Peris — flash glucose monitoring 描繪藥效動力學 — PMID 35178031（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/35178031/

> "**Development of hyperglycemia is fast, already observed 24 hours after initiation of therapy.** FGM shows severe and persistent hyperglycemia during most of the day, **with a significant downward effect in the 4 hours after each daily intake**, which evidences the strong but transitory effect of the drug enzyme blockade. C-peptide level is remarkable in accordance with drug pharmacodynamics, **consistent with a significant insulin resistance**."

### 2.27 Cook — 高齡病人的照護負擔（質性） — PMID 33752998（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/33752998/

> "**Thirty-four women with a median age of 72 (range: 65, 85)** are the subject of this report; **twelve had been started on insulin, four had been hospitalized for hyperglycemia, and eleven appeared to stop alpelisib because of hyperglycemia.**"

> "Oncologists should assess older patients for the requisite abilities and resources for managing alpelisib-induced hyperglycemia in the event it occurs."

### 2.28 Ziegengeist — FAERS DKA 訊號 — PMID 38245400（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/38245400/

> "Pharmacovigilance database analysis revealed significance in reporting among **87 DKA cases with alpelisib (ROR 9.84, 95% confidence interval 7.3-13.2)**, including hospitalization and death as reported outcomes. Review of **11 published case reports reveals median onset of DKA at 14 days** with successful rechallenge possible."

### 2.29 Burnette — 預防性方案的單中心經驗 — PMID 36409396（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/36409396/

> "**One week before ALP initiation, patients started an insulin-sensitizer.** Patients had fasting plasma glucose (FPG) levels drawn **day 8, 15, 28, then monthly**."

> "**Sixteen women** were included with median age of 59 years… **By day 28, 9 patients (56%) had G2-4 HG, with only 3 (19%) G3 and zero G4.** Patients with G2-4 HG had a median of 2 risk factors compared to only 1 if no HG (p = 0.03)."

> "Implementation of a HG prophylaxis protocol with ALP in a single-center study demonstrated **fewer G3-4 HG events compared to that seen in SOLAR-1 (19% vs 36.6%)**."

**⚠️ n=16，單中心，無對照。**

### 2.30 Moore — 預防與監測策略 — PMID 39462728（【L3】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/39462728/

> "identify baseline risk factors of patients at increased risk for developing hyperglycemia, which include **older age, obesity, and glycosylated hemoglobin (HbA1c) 5.7%-6.4% (prediabetes or Type 2 diabetes)**."

> "recommend a **low-carbohydrate (60-130 g/day) diet** along with regular exercise to all patients prior to initiating the PI3Ki. **Prophylactic metformin may be considered in all patients starting a PI3Ki with HbA1c ≤6.4%.**"

> "existing recommendations support monitoring **fasting blood glucose (FBG) once weekly (twice-weekly for intermediate-risk, daily for high-risk patients) and HbA1c every 3 months** upon initiation of PI3Ki… **postprandial glucose monitoring** because it is an early indicator of glucose intolerance."

> "If hyperglycemia develops, **metformin (first-line) and/or sodium glucose co-transporter 2 inhibitors or thiazolidinediones (second-/third-line)** are the preferred agents; consider early referral to an endocrinologist."

### 2.31 Jhaveri — 四藥（everolimus / alpelisib / capivasertib / inavolisib）毒性比較 — PMID 41604817（【L3】📌）
URL: https://europepmc.org/articles/PMC12865632

> "This review summarizes available safety data from **phase III randomized clinical trials for approved PI3K/AKT/mTOR pathway-targeted therapies (everolimus, alpelisib, capivasertib, and inavolisib)**, including incidence, severity, adverse event-related dose modifications, and time to onset."

**這是「不可把所有 PI3K／AKT inhibitors 當成同一類」最關鍵的比較用全文，Round 2 務必取得。**

### 2.32 CAPItello-291 AE 專篇（capivasertib，比較用） — PMID 39241495（【L2】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/39241495/

> "Safety analyses included 705 patients: capivasertib-fulvestrant (n = 355) and placebo-fulvestrant (n = 350). Frequent any-grade AEs with capivasertib-fulvestrant were **diarrhea (72.4%), rash (38.0%), and nausea (34.6%)**; frequent grade ≥3 AEs were **rash (12.1%), diarrhea (9.3%), and hyperglycemia (2.3%)**."

> "Diarrhea, rash, and hyperglycemia occurred shortly after starting capivasertib-fulvestrant [median days to onset (interquartile range) of any grade: 8 (2-22), 12 (10-15), and **15 (1-51)**, respectively]"

**註**：capivasertib 為 **AKT inhibitor**，且採 **intermittent dosing（4 days on, 3 days off）**；其 grade ≥3 hyperglycemia 2.3%，與 alpelisib 差距極大。**分開陳述。**

### 2.33 FDA capivasertib 核准摘要 — PMID 39159418（【L1】-adjacent 📌）
URL: https://pubmed.ncbi.nlm.nih.gov/39159418/

> "Patients were randomly assigned 1:1 to receive **capivasertib 400 mg twice daily for 4 days per week** with fulvestrant versus placebo with fulvestrant."

> "Key concerns included **hyperglycemia (18% all-grade, 2.8% Grade ≥3)**, cutaneous toxicity (58% all-grade, 17% Grade ≥3), and diarrhea (72% all-grade, 9% Grade ≥3)."

### 2.34 FDA alpelisib 核准摘要 — PMID 33168657（【L1】-adjacent 📌）
URL: https://pubmed.ncbi.nlm.nih.gov/33168657/

> "On May 24, 2019, the FDA granted regular approval to alpelisib in combination with fulvestrant for postmenopausal women, and men, with hormone receptor (HR)-positive, HER2-negative, PIK3CA-mutated, advanced or metastatic breast cancer…"

> "The most common adverse reactions, including laboratory abnormalities, on the alpelisib plus fulvestrant arm were **increased glucose, increased creatinine, diarrhea, rash, decreased lymphocyte count, increased gamma glutamyl transferase, nausea, increased alanine aminotransferase, fatigue, decreased hemoglobin, increased lipase, decreased appetite, stomatitis, vomiting, decreased weight, decreased calcium, decreased glucose, prolonged activated partial thromboplastin time, and alopecia.**"

**註意「increased creatinine」「decreased appetite」「decreased weight」「vomiting」「diarrhea」——與使用者要求顧及的腹瀉／體重下降／食慾不佳／脫水／腎功能波動直接對應。**

### 2.35 FDA inavolisib 核准摘要 — PMID 40845250（【L1】-adjacent 📌）
URL: https://pubmed.ncbi.nlm.nih.gov/40845250/

> "Approval was based on INAVO120, a randomized, double-blind, placebo-controlled trial in **325 patients**… Patients were randomly assigned (1:1) to either inavolisib (n = 161) or placebo (n = 164) in combination with palbociclib and fulvestrant."

> "Consistent with the PI3Kα inhibitor class, common adverse reactions noted with inavolisib included **hyperglycemia, stomatitis, diarrhea, and rash**."

### 2.36 統合分析 — PMID 40535135（📌）
URL: https://pubmed.ncbi.nlm.nih.gov/40535135/

> "A total of **five randomized controlled trials (RCTs) involving 3,011 patients** were included… PFS (HR = 0.74, 95% CI 0.67-0.80, P < 0.0001) and the objective response rate (ORR) (RR = 1.80, 95% CI: 1.39-2.35, P < 0.0001)"

> "the incidence of grade ≥3 events was significantly increased in the PI3K inhibitors combined with fulvestrant group (**RR=2.11, 95% CI: 1.73-2.58, P<0.0001**), particularly **hyperglycemia, rash, and transaminitis (ALT)**."

### 2.37 統合分析（跨藥物類別 AE 比較） — PMID 29108713（📌）
URL: https://pubmed.ncbi.nlm.nih.gov/29108713/

> "**Sixteen studies (n=8529 patients)** were included. The addition of targeted agents to ET was associated with a significant higher risk of grade 3-4 AEs: OR 2.86 (95% CI 2.49-3.27) for CDK4/6 inhibitors, 1.88 (95% CI 1.39-2.53) for mTOR inhibitors, **2.05 (95% CI 1.63-2.58) for PI3K inhibitors**, and 2.48 (95% CI 1.09-5.66) for anti-HER2 agents."

> "The highest class-specific risks were … **hyperglycemia grade 3-4 for PI3K inhibitors (OR 40.93; 95% CI 10.08-166.22)**"

### 2.38 Ismail — 全國保險申報資料 — PMID 42159385（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/42159385/

> "In **546 participants** treated with alpelisib, the **median Time on Therapy (TOT) was 87.5 days (IQR, 28.0-173.7)**… **Antidiabetic agent(s) usage increased from 20.0% to 34.3% pre- and post-alpelisib initiation**, respectively. Among those who started antidiabetic agents after alpelisib, **81.8% were prescribed metformin and 44% insulin**."

> "The use of antidiabetic agent(s) after starting alpelisib was associated with a **longer TOT (HR = 0.76, 95% CI, 0.61-0.93, p = 0.008)**"

**注意：real-world 中 44% 曾用 insulin — 與試驗族群與共識建議的落差值得討論。**

### 2.39 Bello Roufai — 法國 early access（real-life 最大宗） — PMID 36611120（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/36611120/

> "Eleven centers provided individual data on **233 consecutive patients**… After a median follow-up of 7.1 months and 168 events, **median PFS was 5.3 months (95% CI: 4.7-6.0)**… **N = 91 (39.1%) patients discontinued alpelisib due to adverse events.**"

### 2.40 Sarfraz — 單中心 real-world — PMID 38011835（【L4】📌）
URL: https://pubmed.ncbi.nlm.nih.gov/38011835/

> "A total of **76 women** treated with alpelisib + ET were included… The estimated **median progression-free survival was 5.2 months (95% CI, 4.1-8.0)**… **Approximately 31.6% of patients permanently discontinued alpelisib due to AEs, and 32.9% had at least one dose reduction. The most common grade 3/4 AEs were hyperglycemia (21%), fatigue (13.2%), and diarrhea (10.5%).**"

### 2.41 ADA Standards of Care 2026, Ch.3 — PMID 41358891（【L3】📌）
URL: https://europepmc.org/articles/PMC12690170

> "The American Diabetes Association (ADA) 'Standards of Care in Diabetes' includes the ADA's current clinical practice recommendations and is intended to provide the components of diabetes care, general treatment goals and guidelines, and tools to evaluate quality of care."

**註**：本輪僅取得章節層級 abstract。**metformin 之 eGFR 分層劑量建議屬全文內容，Round 1 不得引述具體數值。**

---

## 3. 給 Round 2（全文下載階段）的注意事項

1. **仿單為第一優先缺口**。Piqray（alpelisib）、Itovebi（inavolisib）、Truqap（capivasertib）之 FDA/EMA/TFDA label 必須另行取得，否則所有【L1】等級的劑量調整表（dose modification for hyperglycemia，含 FPG 分級門檻與減量階梯）**在本回顧中無可驗證來源**。
2. **BYLieve 的 Expression of Concern（PMID 38142701）必須與 BYLieve 數據同時落地**。
3. **alpelisib vs inavolisib vs capivasertib 三者分開**：優先取得 PMID 41604817（Jhaveri 2026）全文，該篇為唯一橫向比較四種藥物 phase III 安全性的來源。
4. **METALLICA 全文必讀 inclusion/exclusion criteria**，以確認其排除已知糖尿病族群，避免過度外推。
5. **腹瀉／脫水／腎功能** 相關證據目前僅零星散在各 AE 綜論與 Bowman 2017 的 euglycemic DKA 個案。Round 2 需補搜 `SGLT2 inhibitor euglycemic ketoacidosis dehydration oncology`、`metformin lactic acidosis eGFR cancer`。
6. 所有本檔內的 abstract 引文在全文落地後，應以全文原句取代並升級標記為 📄。

---

## 4. 批次下載清單（必拿，供 fetch.py）

```batch
31091374,SOLAR1_Andre_2019
33246021,SOLAR1_OS_Andre_2021
32416251,SOLAR1_AE_Rugo_2020
33780274,SOLAR1_PRO_Ciruelos_2021
33794206,BYLieve_Rugo_2021
39637900,BYLieve_Rugo_2024
38142701,BYLieve_EoC_2024
39476340,INAVO120_Turner_2024
40454641,INAVO120_OS_Jhaveri_2025
42202490,INAVO120_Safety_Im_2026
40513140,GO39374_Gambardella_2025
38638399,METALLICA_LlombartCussac_2024
39177931,SGLT2i_Borrego_2024
40152314,ITACA_Pancirov_2025
39241495,CAPItello291_AE_Rugo_2024
33168657,FDA_Alpelisib_Narayan_2021
40845250,FDA_Inavolisib_Wedam_2025
39159418,FDA_Capivasertib_Dilawari_2024
38297009,Delphi_Gallagher_2024
35406370,Consensus_Tankova_2022
35075945,Mgmt_Goncalves_2022
35016012,Multidisc_Rugo_2022
39462728,Prevention_Moore_2025
41604817,ToxMgmt_Jhaveri_2026
41345397,Capivasertib_Mgmt_Iyengar_2025
41358891,ADA_SOC2026_Ch3
30051890,InsulinFeedback_Hopkins_2018
37399061,InsulinFeedback_Noch_2023
37743730,RealWorld_Shen_2023
35212193,RealWorld_Liu_2022
38439079,RiskModel_Rodon_2024
36409396,Prophylaxis_Burnette_2023
38245400,FAERS_DKA_Ziegengeist_2024
42159385,Claims_Ismail_2026
36611120,FrenchEAP_BelloRoufai_2023
33752998,Elderly_Cook_2021
39896940,DKA_Loke_2025
35750516,HHS_DKA_Chafai_2022
42181200,Inavolisib_HHS_Li_2026
36330532,DKA_Rechallenge_Leung_2022
28856166,EuglycemicDKA_Bowman_2017
34259084,VLCD_SGLT2i_Blow_2021
35178031,FGM_PlaPeris_2022
40535135,Meta_Li_2025
29108713,Meta_Martel_2018
```
