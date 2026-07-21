# 原始PDF/ 落地清冊（inventory）— Round 1 + Round 2

> ## 🔴 定稿前更正（2026-07-21，總編輯）
>
> 本清冊之部分 📄／📌 標記與計數**已於定稿前被實測結果取代**。以 `MISSING_FULLTEXT.md` 為準：
>
> 1. `SOLAR1_AE_Rugo_2020.md`（81,542 bytes）、`INAVO120_Turner_2024.md`（78,182 bytes）、`RealWorld_Shen_2023.md`（31,836 bytes）**已落地全文，改標 📄**。
> 2. `原始PDF/*.md` 實測為 **71 檔**（非 70），其中 **2 組為重複落地**（METALLICA PMID 38638399、Shen 2023 PMID 37743730），故獨立文獻為 **69 篇**。
> 3. 以 <5,000 bytes 為 abstract-only 判準實測：**📄 40 篇／📌 29 篇**，全文取得率約 **58%**（非先前之 38／31／55%）。
> 4. §7 關於「FDA/EMA 仿單未取得」之敘述已於前次更正；`來源/label_alpelisib.md`（51,926 bytes）與 `來源/label_inavolisib.md`（37,305 bytes）**完整落地且含逐字 hyperglycemia dose-modification table**，【L1】論斷有可驗證來源。
>
> 以下原始內容保留供追溯，**計數請勿再引用**。


- **產生日期**：2026-07-21
- **本檔為重新產生（非追加）**：`來源/inventory.md` 在本工作階段**不可讀**（macOS TCC EPERM），無法以「讀取後追加」方式更新，故由 `scratch/fetch_report.json` + `scratch/fetch_report2.json` **完整重新產生**，內容涵蓋兩輪。Round 1 各欄位與原檔同源（design 欄取自 `scratch/make_inventory.py` 之 DESIGN 表）。
- **標記定義**：📄 = 本地有全文可 grep；📌 = 僅有 abstract／metadata，**禁止對其內文細節作具體斷言**。

> **⚠️ 執行環境限制（兩輪皆適用）**
>
> `scripts/fetch.py` 與 `.env` 無法被任何子行程讀取（macOS TCC 對 `~/Documents`）。Round 2 已依指示實測 `set -a && source .env && set +a && python3 scripts/fetch.py --batch scratch/batch2.txt`，結果為 `(eval):source:1: no such file or directory: .env`（exit 127）。故兩輪均改用等效之 Europe PMC／NCBI open-access 管線（`scratch/fetch_epmc.py`、`scratch/fetch_epmc2.py`）。
> **LlamaParse（非 OA PDF）路徑兩輪皆未執行**，因金鑰在不可讀的 `.env` 內。所有非 OA 文獻（NEJM、Lancet Oncol、Ann Oncol、JCO、Cell 部分、Mol Cancer Ther 等）因此只落地 abstract（📌）。

> **⚠️ 另一項限制**：本工作階段中 `原始PDF/` 內 **45 個 Round 1 檔案有 25 個無法被讀取**（同樣 TCC EPERM），清單見 §6。這些檔案存在於磁碟且 Round 1 已寫入，但本階段**無法 grep 其內容**。

---

## Round 1：已落地全文（📄）— 26 篇

| slug | PMID | 標題 | 年 | 期刊 | design | 等級 | 字元數 | 標記 |
|---|---|---|---|---|---|---|---|---|
| `INAVO120_Safety_Im_2026` | 42202490 | Safety analyses of the INAVO120 randomised phase III trial of inavolisib or placebo with palbociclib-fulvestrant in patients with PIK3CA-mutated, hormone receptor-positive, HER2-negative, endocrine-resistant advanced breast cancer. | 2026 | ESMO Open | phase 3 safety analysis | 【L2】 | 53,449 | 📄 |
| `GO39374_Gambardella_2025` | 40513140 | Safety overview and management of inavolisib alone and in combination therapies in PIK3CA-mutated, HR-positive, HER2-negative advanced breast cancer (GO39374). | 2025 | ESMO Open | phase I/Ib dose-escalation/-expansion | 【L2】 | 53,437 | 📄 |
| `Multidisc_Rugo_2022` | 35016012 | A multidisciplinary approach to optimizing care of patients treated with alpelisib. | 2021 | The Breast : Official Journal of the European Society of Mastology | narrative review / management guidance | 【L3】 | 48,666 | 📄 |
| `Capivasertib_Mgmt_Iyengar_2025` | 41345397 | Optimizing clinical monitoring and management guidelines for capivasertib in HR-positive/HER2-negative advanced breast cancer: expert opinion. | 2025 | NPJ Breast Cancer | expert opinion | 【L3】 | 47,664 | 📄 |
| `ToxMgmt_Jhaveri_2026` | 41604817 | Clinical management of common toxicities with inhibitors targeting the PI3K/AKT/mTOR pathway in breast cancer. | 2026 | ESMO Open | pooled phase III safety review + guidance | 【L3】 | 44,916 | 📄 |
| `Mgmt_Goncalves_2022` | 35075945 | Management of Phosphatidylinositol-3-Kinase Inhibitor-Associated Hyperglycemia. | 2022 | Integrative Cancer Therapies | narrative review / management guidance | 【L3】 | 44,026 | 📄 |
| `Delphi_Gallagher_2024` | 38297009 | Managing hyperglycemia and rash associated with alpelisib: expert consensus recommendations using the Delphi technique. | 2024 | NPJ Breast Cancer | modified Delphi consensus | 【L3】 | 41,724 | 📄 |
| `CAPItello291_AE_Rugo_2024` | 39241495 | Capivasertib and fulvestrant for patients with hormone receptor-positive advanced breast cancer: characterization, time course, and management of frequent adverse events from the phase III CAPItello-291 study. | 2024 | ESMO Open | phase 3 safety analysis | 【L2】 | 40,856 | 📄 |
| `METALLICA_LlombartCussac_2024` | 38638399 | Preventing alpelisib-related hyperglycaemia in HR+/HER2-/PIK3CA-mutated advanced breast cancer using metformin (METALLICA): a multicentre, open-label, single-arm, phase 2 trial. | 2024 | eClinicalMedicine | multicentre, open-label, SINGLE-ARM, phase 2 | 【L2】 | 40,436 | 📄 |
| `InsulinFeedback_Hopkins_2018` | 30051890 | Suppression of insulin feedback enhances the efficacy of PI3K inhibitors. | 2018 | Nature | preclinical (mouse tumor models) | 【L5】 | 40,239 | 📄 |
| `Consensus_Tankova_2022` | 35406370 | Management Strategies for Hyperglycemia Associated with the α-Selective PI3K Inhibitor Alpelisib for the Treatment of Breast Cancer. | 2022 | Cancers | expert consensus (14 oncologists + 7 endocrinologists) | 【L3】 | 37,186 | 📄 |
| `FDA_Capivasertib_Dilawari_2024` | 39159418 | US Food and Drug Administration Approval Summary: Capivasertib With Fulvestrant for Hormone Receptor-Positive, Human Epidermal Growth Factor Receptor 2-Negative Locally Advanced or Metastatic Breast Cancer With &lt;i&gt;PIK3CA&lt;/i&gt;/&lt;i&gt;AKT1&lt;/i&gt;/&lt;i&gt;PTEN&lt;/i&gt; Alterations. | 2024 | Journal of clinical oncology : official journal of the American Society of Clinical Oncology | regulatory approval summary | 【L1-adjacent】 | 36,295 | 📄 |
| `FDA_Alpelisib_Narayan_2021` | 33168657 | FDA Approval Summary: Alpelisib Plus Fulvestrant for Patients with HR-positive, HER2-negative, PIK3CA-mutated, Advanced or Metastatic Breast Cancer. | 2020 | Clinical cancer research : an official journal of the American Association for Cancer Research | regulatory approval summary | 【L1-adjacent】 | 34,191 | 📄 |
| `SGLT2i_Borrego_2024` | 39177931 | SGLT2 inhibition improves PI3Kα inhibitor-induced hyperglycemia: findings from preclinical animal models and from patients in the BYLieve and SOLAR-1 trials. | 2024 | Breast Cancer Research and Treatment | preclinical animal + propensity-matched trial subanalysis | 【L2/L5】 | 32,421 | 📄 |
| `RealWorld_Shen_2023` | 37743730 | Incidence, risk factors, and management of alpelisib-associated hyperglycemia in metastatic breast cancer. | 2023 | Cancer | single-centre retrospective (n=247, MSKCC) | 【L4】 | 31,683 | 📄 |
| `Inavolisib_HHS_Li_2026` | 42181200 | Inavolisib-induced fulminant-like diabetes and hyperosmolar hyperglycemic state: a case report. | 2026 | Frontiers in Endocrinology | case report | 【L4】 | 30,833 | 📄 |
| `RealWorld_Liu_2022` | 35212193 | Characterization, management, and risk factors of hyperglycemia during PI3K or AKT inhibitor treatment. | 2022 | Cancer Medicine | retrospective (n=491) | 【L4】 | 30,539 | 📄 |
| `ITACA_Pancirov_2025` | 40152314 | Dynamics of hyperglycemia of patients treated with alpelisib: exploratory interim analysis of ITACA trial. | 2025 | The Oncologist | prospective trial, exploratory interim analysis (n=23) | 【L2】 | 30,054 | 📄 |
| `Meta_Li_2025` | 40535135 | Efficacy and safety of PI3K inhibitors combined with fulvestrant for HR+/HER2- advanced breast cancer: a systematic review and meta-analysis. | 2025 | Frontiers in Oncology | SR + meta-analysis（5 RCT, n=3,011） | 【L2(SR)】 | 29,928 | 📄 |
| `SOLAR1_PRO_Ciruelos_2021` | 33780274 | Patient-Reported Outcomes in Patients With PIK3CA-Mutated Hormone Receptor-Positive, Human Epidermal Growth Factor Receptor 2-Negative Advanced Breast Cancer From SOLAR-1. | 2021 | Journal of Clinical Oncology | phase 3 PRO analysis | 【L2】 | 29,616 | 📄 |
| `RiskModel_Rodon_2024` | 38439079 | A risk analysis of alpelisib-induced hyperglycemia in patients with advanced solid tumors and breast cancer. | 2024 | Breast Cancer Research : BCR | pooled trial data + machine-learning risk model | 【L2/L4】 | 26,423 | 📄 |
| `DKA_Rechallenge_Leung_2022` | 36330532 | Ketoacidosis in a Patient with Type 2 Diabetes Requiring Alpelisib: Learnings and Observations Regarding Alpelisib Initiation and Rechallenge. | 2022 | OncoTargets and Therapy | case report（含 rechallenge） | 【L4】 | 23,485 | 📄 |
| `FGM_PlaPeris_2022` | 35178031 | Alpelisib-Induced Diabetes Mellitus: Case Report, Pharmacodynamics and Management Considerations. | 2022 | Frontiers in Endocrinology | case report + flash glucose monitoring | 【L4】 | 19,010 | 📄 |
| `VLCD_SGLT2i_Blow_2021` | 34259084 | Treating Alpelisib-Induced Hyperglycemia with Very Low Carbohydrate Diets and Sodium-Glucose Co-Transporter 2 Inhibitors: A Case Series. | 2021 | Integrative Cancer Therapies | case series (n=3) | 【L4】 | 18,896 | 📄 |
| `DKA_Loke_2025` | 39896940 | Alpelisib-Induced Diabetic Ketoacidosis and Insulin-Resistant Hyperglycemia. | 2025 | AACE Clinical Case Reports | case report | 【L4】 | 14,835 | 📄 |
| `EuglycemicDKA_Bowman_2017` | 28856166 | Ketoacidosis With Canagliflozin Prescribed for Phosphoinositide 3-Kinase Inhibitor-Induced Hyperglycemia: A Case Report. | 2017 | Journal of Investigative Medicine High Impact Case Reports | case report（taselisib + SGLT2i） | 【L4】 | 12,668 | 📄 |

## Round 1：僅落地 abstract（📌）— 19 篇

> 檔案存在但檔頭標 `<!-- fulltext_status: ABSTRACT_ONLY -->`，**只能引用 abstract 句子**。

| slug | PMID | 標題 | 年 | 期刊 | design | 等級 | 字元數 | 標記 | 原因 |
|---|---|---|---|---|---|---|---|---|---|
| `ADA_SOC2026_Ch3` | 41358891 | 3. Prevention or Delay of Diabetes and Associated Comorbidities: Standards of Care in Diabetes-2026. | 2026 | Diabetes care | society clinical practice guideline | 【L3】 | 1,734 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `BYLieve_EoC_2024` | 38142701 | Expression of concern-Alpelisib plus fulvestrant in PIK3CA-mutated, hormone receptor-positive advanced breast cancer after a CDK4/6 inhibitor (BYLieve): one cohort of a phase 2, multicentre, open-label, non-comparative study. | 2024 | The Lancet. Oncology | editorial notice (Expression of concern) | 【L2】 | 1,136 | 📌 | 無 PMC 全文（非 OA） |
| `BYLieve_Rugo_2021` | 33794206 | Alpelisib plus fulvestrant in PIK3CA-mutated, hormone receptor-positive advanced breast cancer after a CDK4/6 inhibitor (BYLieve): one cohort of a phase 2, multicentre, open-label, non-comparative study. | 2021 | The Lancet. Oncology | phase 2, single-arm, non-comparative | 【L2】 | 3,657 | 📌 | 無 PMC 全文（非 OA） |
| `BYLieve_Rugo_2024` | 39637900 | Alpelisib plus fulvestrant in PIK3CA-mutated, hormone receptor-positive advanced breast cancer after a CDK4/6 inhibitor (BYLieve): one cohort of a phase 2, multicentre, open-label, non-comparative study. | 2024 | The Lancet. Oncology | phase 2, single-arm, non-comparative | 【L2】 | 3,660 | 📌 | 無 PMC 全文（非 OA） |
| `Claims_Ismail_2026` | 42159385 | Assessment of alpelisib-induced hyperglycemia in a real-world setting: A nationwide claims data analysis. | 2026 | Journal of oncology pharmacy practice : official publication of the International Society of Oncology Pharmacy Practitioners | retrospective longitudinal claims (n=546) | 【L4】 | 2,812 | 📌 | 無 PMC 全文（非 OA） |
| `Elderly_Cook_2021` | 33752998 | Alpelisib-induced hyperglycemia in older patients with breast Cancer: Qualitative findings. | 2021 | Journal of geriatric oncology | qualitative chart review (n=34, age >=65) | 【L4】 | 2,543 | 📌 | 無 PMC 全文（非 OA） |
| `FAERS_DKA_Ziegengeist_2024` | 38245400 | Alpelisib-Induced Diabetic Ketoacidosis: A Pharmacovigilance Analysis of the FDA Adverse Event Reporting System and Review of the Literature. | 2024 | Clinical breast cancer | disproportionality analysis (FAERS) + literature review | 【L4】 | 2,775 | 📌 | 無 PMC 全文（非 OA） |
| `FDA_Inavolisib_Wedam_2025` | 40845250 | US Food and Drug Administration Approval Summary: Inavolisib With Palbociclib and Fulvestrant for Endocrine-Resistant, &lt;i&gt;PIK3CA&lt;/i&gt;-Mutated, Hormone Receptor-Positive, Human Epidermal Growth Factor Receptor 2-Negative, Locally Advanced or Metastatic Breast Cancer. | 2025 | Journal of clinical oncology : official journal of the American Society of Clinical Oncology | regulatory approval summary | 【L1-adjacent】 | 2,806 | 📌 | 無 PMC 全文（非 OA） |
| `FrenchEAP_BelloRoufai_2023` | 36611120 | Alpelisib and fulvestrant in PIK3CA-mutated hormone receptor-positive HER2-negative advanced breast cancer included in the French early access program. | 2023 | Oncogene | prospective registry / real-life (n=233) | 【L4】 | 2,377 | 📌 | 無 PMC 全文（非 OA） |
| `HHS_DKA_Chafai_2022` | 35750516 | An atypical alpelisib-induced hyperglycemic hyperosmolar and diabetic ketoacidosis state: A case report and critical analysis of alpelisib-induced hyperglycemia management guidelines. | 2022 | Annales d'endocrinologie | case report + guideline critique | 【L4】 | 1,057 | 📌 | 無 PMC 全文（非 OA） |
| `INAVO120_OS_Jhaveri_2025` | 40454641 | Overall Survival with Inavolisib in PIK3CA-Mutated Advanced Breast Cancer. | 2025 | The New England journal of medicine | phase 3 final OS analysis | 【L2】 | 2,745 | 📌 | 無 PMC 全文（非 OA） |
| `INAVO120_Turner_2024` | 39476340 | Inavolisib-Based Therapy in &lt;i&gt;PIK3CA&lt;/i&gt;-Mutated Advanced Breast Cancer. | 2024 | The New England journal of medicine | randomized double-blind phase 3 (INAVO120) | 【L2】 | 2,714 | 📌 | 無 PMC 全文（非 OA） |
| `InsulinFeedback_Noch_2023` | 37399061 | Insulin feedback is a targetable resistance mechanism of PI3K inhibition in glioblastoma. | 2023 | Neuro-oncology | preclinical + retrospective phase 2 trial analysis | 【L5/L4】 | 2,632 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `Meta_Martel_2018` | 29108713 | Risk of adverse events with the addition of targeted agents to endocrine therapy in patients with hormone receptor-positive metastatic breast cancer: A systematic review and meta-analysis. | 2018 | Cancer treatment reviews | SR + meta-analysis（16 studies, n=8,529） | 【L2(SR)】 | 2,681 | 📌 | 無 PMC 全文（非 OA） |
| `Prevention_Moore_2025` | 39462728 | Effective Strategies for the Prevention and Mitigation of Phosphatidylinositol-3-Kinase Inhibitor-Associated Hyperglycemia: Optimizing Patient Care. | 2025 | Clinical breast cancer | expert review / management guidance | 【L3】 | 2,889 | 📌 | 無 PMC 全文（非 OA） |
| `Prophylaxis_Burnette_2023` | 36409396 | Evaluation of alpelisib-induced hyperglycemia prophylaxis and associated risk factors in PIK3CA-mutated hormone-receptor positive, human epidermal growth factor-2 negative advanced breast cancer. | 2023 | Breast cancer research and treatment | single-centre retrospective (n=16) | 【L4】 | 2,676 | 📌 | 無 PMC 全文（非 OA） |
| `SOLAR1_AE_Rugo_2020` | 32416251 | Time course and management of key adverse events during the randomized phase III SOLAR-1 study of PI3K inhibitor alpelisib plus fulvestrant in patients with HR-positive advanced breast cancer. | 2020 | Annals of oncology : official journal of the European Society for Medical Oncology | phase 3 safety/AE analysis | 【L2】 | 3,395 | 📌 | 無 PMC 全文（非 OA） |
| `SOLAR1_Andre_2019` | 31091374 | Alpelisib for PIK3CA-Mutated, Hormone Receptor-Positive Advanced Breast Cancer. | 2019 | The New England journal of medicine | randomized phase 3 (SOLAR-1) | 【L2】 | 3,401 | 📌 | 無 PMC 全文（非 OA） |
| `SOLAR1_OS_Andre_2021` | 33246021 | Alpelisib plus fulvestrant for PIK3CA-mutated, hormone receptor-positive, human epidermal growth factor receptor-2-negative advanced breast cancer: final overall survival results from SOLAR-1. | 2021 | Annals of oncology : official journal of the European Society for Medical Oncology | phase 3 final OS analysis | 【L2】 | 3,415 | 📌 | 無 PMC 全文（非 OA） |

## Round 1：完全失敗 — 0 篇

- 無。

---

## Round 2：已落地全文（📄）— 12 篇

| slug | PMID | 共引 | 標題 | 年 | 期刊 | design | 等級 | 字元數 | 標記 |
|---|---|---|---|---|---|---|---|---|---|
| `Mech_Fruman_Cell_2017` | 28802037 | 6x | The PI3K Pathway in Human Disease. | 2017 | Cell | narrative review（Cell） | 【L5】 | 135,507 | 📄 |
| `Preclin_Song_Inavolisib_2022` | 34544753 | 5x | RTK-Dependent Inducible Degradation of Mutant PI3Kα Drives GDC-0077 (Inavolisib) Efficacy. | 2022 | Cancer Discovery | preclinical（Cancer Discov） | 【L5】 | 65,705 | 📄 |
| `BELLE2_Baselga_2017` | 28576675 | 9x | Buparlisib plus fulvestrant versus placebo plus fulvestrant in postmenopausal, hormone receptor-positive, HER2-negative, advanced breast cancer (BELLE-2): a randomised, double-blind, placebo-controlled, phase 3 trial. | 2017 | The Lancet. Oncology | randomized phase 3 (BELLE-2, buparlisib) | 【L2】 | 52,467 | 📄 |
| `DKA_Danne_Consensus_2019` | 30728224 | 3x | International Consensus on Risk Management of Diabetic Ketoacidosis in Patients With Type 1 Diabetes Treated With Sodium-Glucose Cotransporter (SGLT) Inhibitors. | 2019 | Diabetes Care | international consensus statement | 【L3】 | 43,318 | 📄 |
| `Mech_Huang_ObesityT2D_2018` | 30263000 | 4x | The PI3K/AKT pathway in obesity and type 2 diabetes. | 2018 | International Journal of Biological Sciences | narrative review | 【L5】 | 38,590 | 📄 |
| `Inavolisib_Jhaveri_JCO_2024` | 39236276 | 3x | Phase I/Ib Trial of Inavolisib Plus Palbociclib and Endocrine Therapy for &lt;i&gt;PIK3CA&lt;/i&gt;-Mutated, Hormone Receptor-Positive, Human Epidermal Growth Factor Receptor 2-Negative Advanced or Metastatic Breast Cancer. | 2024 | Journal of Clinical Oncology | phase I/Ib | 【L2】 | 37,411 | 📄 |
| `CAPItello291_Turner_2023` | 37256976 | 6x | Capivasertib in Hormone Receptor-Positive Advanced Breast Cancer. | 2023 | The New England journal of medicine | randomized phase 3 (CAPItello-291) | 【L2】 | 35,120 | 📄 |
| `SANDPIPER_Dent_2021` | 33186740 | 6x | Phase III randomized study of taselisib or placebo with fulvestrant in estrogen receptor-positive, PIK3CA-mutant, HER2-negative, advanced breast cancer: the SANDPIPER trial. | 2020 | Annals of oncology : official journal of the European Society for Medical Oncology | randomized phase 3 (SANDPIPER, taselisib) | 【L2】 | 31,922 | 📄 |
| `Mgmt_Nunnery_Mayer_2019` | 31626273 | 4x | Management of toxicity to isoform α-specific PI3K inhibitors. | 2019 | Annals of Oncology | narrative review | 【L3】 | 26,776 | 📄 |
| `Resist_Juric_PTEN_2015` | 25409150 | 2x | Convergent loss of PTEN leads to clinical resistance to a PI(3)Kα inhibitor. | 2014 | Nature | preclinical + clinical correlate（Nature） | 【L5】 | 23,927 | 📄 |
| `Meta_Shields_Tox_2020` | 33144920 | 4x | A systematic review and meta-analysis of selected toxicity endpoints of alpelisib. | 2020 | Oncotarget | systematic review + meta-analysis | 【L2(SR)】 | 19,656 | 📄 |
| `DKA_Carrillo_2021` | 34095470 | 5x | Alpelisib-Induced Diabetic Ketoacidosis: A Case Report and Review of Literature. | 2021 | AACE Clinical Case Reports | case report + literature review | 【L4】 | 16,125 | 📄 |

## Round 2：僅落地 abstract（📌）— 12 篇

> 檔案存在但檔頭標 `<!-- fulltext_status: ABSTRACT_ONLY -->`，**只能引用 abstract 句子**。

| slug | PMID | 共引 | 標題 | 年 | 期刊 | design | 等級 | 字元數 | 標記 | 原因 |
|---|---|---|---|---|---|---|---|---|---|---|
| `Alpelisib_Juric_JAMAOnc_2019` | 30543347 | 6x | Alpelisib Plus Fulvestrant in PIK3CA-Altered and PIK3CA-Wild-Type Estrogen Receptor-Positive Advanced Breast Cancer: A Phase 1b Clinical Trial. | 2019 | JAMA oncology | phase 1b expansion | 【L2】 | 3,805 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `Alpelisib_Juric_JCO_2018` | 29401002 | 4x | Phosphatidylinositol 3-Kinase α-Selective Inhibition With Alpelisib (BYL719) in PIK3CA-Altered Solid Tumors: Results From the First-in-Human Study. | 2018 | Journal of clinical oncology : official journal of the American Society of Clinical Oncology | phase Ia dose-escalation | 【L2】 | 3,503 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `DKA_Farah_2020` | 33244501 | 7x | DIABETIC KETOACIDOSIS ASSOCIATED WITH ALPELISIB TREATMENT OF METASTATIC BREAST CANCER. | 2020 | AACE clinical case reports | case report | 【L4】 | 2,655 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `DPP_Knowler_2002` | 11832527 | 3x | Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. | 2002 | The New England journal of medicine | randomized controlled trial (DPP) | 【L2】 | 2,737 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `Discont_Cheung_2022` | 35000092 | 6x | Factors leading to alpelisib discontinuation in patients with hormone receptor positive, human epidermal growth factor receptor-2 negative breast cancer. | 2022 | Breast cancer research and treatment | retrospective cohort | 【L4】 | 2,742 | 📌 | 無 PMC 全文（非 OA） |
| `Landscape_Mosele_2020` | 32067679 | 8x | Outcome and molecular landscape of patients with PIK3CA-mutated metastatic breast cancer. | 2020 | Annals of oncology : official journal of the European Society for Medical Oncology | cohort / molecular landscape | 【L4】 | 2,229 | 📌 | 無 PMC 全文（非 OA） |
| `Mech_Crouthamel_AKT_2009` | 19118049 | 3x | Mechanism and management of AKT inhibitor-induced hyperglycemia. | 2009 | Clinical cancer research : an official journal of the American Association for Cancer Research | preclinical（mouse, GSK690693 pan-AKT inhibitor） | 【L5】 | 2,886 | 📌 | 無 PMC 全文（非 OA） |
| `Mech_Drullinsky_2020` | 32274666 | 3x | Mechanistic basis for PI3K inhibitor antitumor activity and adverse reactions in advanced breast cancer. | 2020 | Breast cancer research and treatment | narrative review | 【L5】 | 2,653 | 📌 | 無 PMC 全文（非 OA） |
| `Mech_Goncalves_NEJM_2018` | 30462943 | 14x | Phosphatidylinositol 3-Kinase, Growth Disorders, and Cancer. | 2018 | The New England journal of medicine | narrative review（NEJM Review Article） | 【L5】 | 828 | 📌 | 無 PMC 全文（非 OA） |
| `Mgmt_Busaidy_JCO_2012` | 22778315 | 4x | Management of metabolic effects associated with anticancer agents targeting the PI3K-Akt-mTOR pathway. | 2012 | Journal of clinical oncology : official journal of the American Society of Clinical Oncology | expert review / management guidance | 【L3】 | 2,693 | 📌 | ncbi_efetch: 取回之 XML 無可用 body（publisher 不開放全文下載） |
| `Preclin_Fritsch_BYL719_2014` | 24608574 | 11x | Characterization of the novel and specific PI3Kα inhibitor NVP-BYL719 and development of the patient stratification strategy for clinical trials. | 2014 | Molecular cancer therapeutics | preclinical characterization | 【L5】 | 2,439 | 📌 | 無 PMC 全文（非 OA） |
| `Preclin_Hanan_Inavolisib_2022` | 36455032 | 4x | Discovery of GDC-0077 (Inavolisib), a Highly Selective Inhibitor and Degrader of Mutant PI3Kα. | 2022 | Journal of medicinal chemistry | medicinal chemistry / discovery | 【L5】 | 1,982 | 📌 | 無 PMC 全文（非 OA） |

## Round 2：完全失敗 — 0 篇

- 無。

---

## 防資料污染驗證（Round 2）

方法同 Round 1：比對檔頭 `<!-- epmc_title -->` 與內文第一個 `# 標題`（`scratch/verify2.py`）。

| 判定 | 篇數 | 說明 |
|---|---|---|
| OK（≥0.72） | 23 | metadata 與內文標題一致 |
| 誤報（已人工排除） | 1 | `Inavolisib_Jhaveri_JCO_2024`：metadata 標題含 HTML escape `&lt;i&gt;PIK3CA&lt;/i&gt;`，而內文標題為已渲染之 `PIK3CA`，且 en-dash vs hyphen 差異，使相似度降至 0.402。**PMID 39236276、DOI 10.1200/jco.24.00110 兩者一致，確認為同一篇，非污染。** |
| POLLUTED（已刪除） | 0 | 本輪**無**內容與 metadata 不符之檔案 |

**結論：Round 2 共 24 篇，0 篇 polluted，無檔案因污染被刪除。**

---

## 統計總表

| | Round 1 | Round 2 | 合計 |
|---|---|---|---|
| 清單篇數 | 45 | 24 | 69 |
| 全文 📄 | 26 | 12 | **38** |
| 僅 abstract 📌 | 19 | 12 | 31 |
| 全文率 | 57% | 50% | 55% |

## §6 為何第二輪共引統計未使用本地檔案

**根本原因：`原始PDF/*.md` 內完全沒有參考文獻清單。** Round 1 的 JATS→Markdown 轉檔器（`scratch/fetch_epmc.py` 的 `walk()`）明確 `continue` 掉 `ref-list`／`back` 節點。少數檔案雖有 `#### References` 標題，其下內容為空。已對全部 45 檔實測：**0 檔** 的 References 段落含任何可解析的文獻條目。

因此第二輪共引統計改以 Europe PMC `/MED/{PMID}/references` API 完成（見 `來源/citations_round2.md` §0），原始資料留存於 `scratch/refs_raw.json`、`scratch/cocite.json`。

> 附註：統計進行當下另有 25 個 Round 1 檔案因 macOS TCC 暫時不可讀；該限制稍後於同一工作階段內解除，本清冊產生時 **45 檔全部可讀**。但此為次要因素——即使全部可讀，仍因無參考文獻清單而無法做共引統計。

## §7 仍未取得全文之關鍵缺口

1. ~~**FDA/EMA/TFDA 正式仿單（Piqray／Itovebi／Truqap）兩輪皆未取得** → 所有【L1】等級之 hyperglycemia dose-modification table **本回顧未取得可驗證來源**。~~
   > **⛔ 本條原判定為誤，已於 2026-07-21 撤銷（retracted）。**
   >
   > **誤判原因**：撰寫本條時僅掃描 `原始PDF/` 目錄，**未計入 `來源/` 目錄**。正式仿單並非以 PubMed 文獻管線取得，故不落在 `原始PDF/`，而是另存於 `來源/`。以「`原始PDF/` 無此檔」推論「本回顧未取得」屬範圍錯誤。
   >
   > **實際已落地之來源檔（三個，均可 grep）**：
   >
   > | 檔案 | 大小 | 內容 |
   > |---|---|---|
   > | `來源/label_alpelisib.md` | 51,926 bytes | FDA **PIQRAY NDA 212526 s009**（Revised **01/2024**，含 Warnings and Precautions, Hyperglycemia (5.3) 01/2024）逐字內容；EMA SmPC；**VIJOICE**；TFDA 中文仿單（**衛部藥輸字第 027995 號**） |
   > | `來源/label_inavolisib.md` | 37,305 bytes | FDA **ITOVEBI NDA 219249**（Revised **04/2026**，含 Warnings and Precautions, Hyperglycemia (5.1) **09/2025** 條目修訂）；EMA SmPC（**EU/1/25/1942**） |
   > | `來源/guideline_ada_comparators.md` | 43,567 bytes | capivasertib／**TRUQAP** 比較資料（capivasertib/TRUQAP 提及 39 處） |
   >
   > **兩份 label 檔皆含逐字 blockquote 之 hyperglycemia dose-modification / monitoring 表**（例：`label_alpelisib.md` §5.3 全文、Grade 3/4 FPG 分級與劑量調整；`label_inavolisib.md` §5.1）。章節 `章節/C_兩藥比較.md` 已實際引用此二檔 **128 次**（`label_alpelisib.md` 63 次、`label_inavolisib.md` 65 次）。
   >
   > **結論：【L1】等級之 hyperglycemia dose-modification 論斷有可驗證來源，得正常引用**，引用時標註 `[來源/label_alpelisib.md]` 或 `[來源/label_inavolisib.md]`。
   >
   > **真正未取得的僅有兩項（範圍遠小於原陳述）**：
   > 1. **TFDA 官網直接下載的 PDF**——已以醫院公開之**同一份核准仿單**（衛部藥輸字第 027995 號）替代，內容等同，僅取得管道不同。
   > 2. **EMA SmPC 的確切 revision date**——PDF 該欄位為空白，故無法標註版本日期；SmPC 正文內容本身已落地。
2. **SOLAR-1／INAVO120／BYLieve 三個主論文仍僅有 abstract（📌）**（PMID 31091374／39476340／33794206），其劑量調整表、subgroup、supplementary table **不得引用**。
3. Round 2 中下列高共引文獻僅落地 abstract：`Mech_Goncalves_NEJM_2018`(14x)、`Preclin_Fritsch_BYL719_2014`(11x)、`Mech_Crouthamel_AKT_2009`(3x)、`Mgmt_Busaidy_JCO_2012`(4x)。
4. `Mech_Goncalves_NEJM_2018` 之檔案僅 828 字元——Europe PMC **連 abstract 內文都未回傳**（NEJM Review Article 無結構化 abstract）→ **現階段不得對其內文作任何斷言**。
5. 若要走 LlamaParse 路徑，需先解除 `~/Documents` 的 TCC 限制，或把 `.env`、`scripts/`、`原始PDF/` 搬到 Claude Code 可讀取的位置。

