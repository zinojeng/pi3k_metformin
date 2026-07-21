# citations_round2.md — 第二輪深挖（共引文獻補抓）

- **產生日期**：2026-07-21
- **上游**：`來源/citations_round1.md` / `scratch/batch1.txt`（45 筆）已落地之 `原始PDF/*.md`
- **本輪筆數**：24 筆

## 0. 方法與一項重大限制（必須先讀）

> **原定作法**：逐篇讀 `原始PDF/*.md` 的 `## References` 段落做共引統計。
> **實際情形**：第一輪的 JATS→Markdown 轉檔器（`scratch/fetch_epmc.py`）在 `walk()` 中
> 明確 `continue` 掉了 `ref-list`／`back` 節點，因此 **`原始PDF/*.md` 內完全沒有參考文獻清單**；
> 少數檔案雖有 `#### References` 標題，其下內容為空（已實測 `METALLICA_LlombartCussac_2024`、
> `ITACA_Pancirov_2025`）。（附註：統計進行當下另有 25 個檔案因 macOS TCC 暫時不可讀，
> 該限制稍後於同一階段內解除、45 檔全部可讀，但**參考文獻清單缺席**此一根本原因不變。）
> **因此共引統計無法從本地檔案內文完成。**
>
> **替代作法（本輪實際採用）**：以 Europe PMC `/MED/{PMID}/references` API，
> 對第一輪 **全部 45 個 PMID** 取回其參考文獻清單（實得 1,318 筆 reference，
> 43/45 篇有 reference 資料；`BYLieve_EoC_2024`、`Inavolisib_HHS_Li_2026`、`Meta_Martel_2018` 回傳 0 筆），
> 再統計被 **≥2 篇**第一輪論文共同引用者。原始資料存於 `scratch/refs_raw.json`、`scratch/cocite.json`，可稽核。
> 下表「共引次數」欄位皆可由 `scratch/cocite.json` 反查驗證。

> **未採用之判準說明**：任務要求挑出附近出現 "landmark"／"first to show"／"largest cohort" 字眼之引用。
> 由於本地檔案無參考文獻段落、且無 in-text citation 上下文可 grep，**此判準本輪無法執行**，
> 改以純共引次數 + 主題相關性挑選。**本回顧未取得可驗證來源**以支持任何「landmark」措辭。

## 1. 任務指定目標之達成情形

| 任務指定項目 | 結果 |
|---|---|
| Hopkins/Goncalves 等 insulin feedback 之 Nature 系列 | **部分達成**。`Hopkins BD, et al. Nature 2018`（PMID 30051890，suppression of insulin feedback／ketogenic diet）**第一輪即已落地全文**（`原始PDF/InsulinFeedback_Hopkins_2018.md`，PMC6197057）。本輪補 `Goncalves MD, Hopkins BD, Cantley LC. NEJM 2018`（PMID 30462943，共引 14 次，全批次最高）與 `Juric D, et al. Nature 2015`（PMID 25409150）。 |
| 「PI3K 抑制 → insulin resistance／hepatic glucose output ↑」之 primary mechanistic study | **已取得**：`Crouthamel MC, et al. Clin Cancer Res 2009`（PMID 19118049）—— 小鼠模型直接量測 liver glycogen、gluconeogenesis 與 peripheral glucose uptake。 |
| 「hyperinsulinemia 重新活化腫瘤 PI3K signaling」之原始前臨床研究 | **主要來源已於第一輪落地**（Hopkins 2018 Nature，全文可 grep）。本輪未再找到共引 ≥2 且未落地之其他原始前臨床研究；**除上述外本回顧未取得可驗證來源**。 |
| SOLAR-1／INAVO120／BYLieve 主論文 | **第一輪已抓取**（PMID 31091374／39476340／33794206），但因 NEJM／Lancet Oncol 非 OA 且 LlamaParse 金鑰不可讀，**僅落地 abstract（📌）**。本輪環境限制未變，**無法補為全文**。 |

## 2. 本輪清單

| # | PMID | slug | 共引次數 | 年 | 期刊 | 主題群 | design | 等級 | 補抓理由 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 30462943 | `Mech_Goncalves_NEJM_2018` | **14x** | 2018 | N Engl J Med | 機轉 | narrative review（NEJM Review Article） | 【L5】 | **任務指定之 Hopkins/Goncalves/Cantley 系列**。全 45 篇中被共引 **14 次**，為第一輪引用次數最高的機轉文獻。闡述 PI3K–insulin 軸與 growth disorders/cancer 之關聯。 |
| 2 | 28802037 | `Mech_Fruman_Cell_2017` | **6x** | 2017 | Cell | 機轉 | narrative review（Cell） | 【L5】 | 共引 **6 次**。Fruman/Hopkins 合著，PI3K pathway 在人類疾病（含代謝）之總論。 |
| 3 | 19118049 | `Mech_Crouthamel_AKT_2009` | **3x** | 2009 | Clin Cancer Res | 機轉 | preclinical（mouse, GSK690693 pan-AKT inhibitor） | 【L5】 | 共引 **3 次**。**任務指定「hepatic glucose output 上升 / insulin resistance」之 primary mechanistic study**：小鼠實驗直接測 liver glycogen、fasting、tracer uptake，並試驗 antidiabetic agents 與低碳水飲食之緩解效果。 |
| 4 | 30263000 | `Mech_Huang_ObesityT2D_2018` | **4x** | 2018 | Int J Biol Sci | 機轉 | narrative review | 【L5】 | 共引 **4 次**。PI3K/AKT 於 obesity 與 T2D 之生理角色，為「抑制該軸即造成 insulin resistance」提供背景。 |
| 5 | 24608574 | `Preclin_Fritsch_BYL719_2014` | **11x** | 2014 | Mol Cancer Ther | 機轉/藥理 | preclinical characterization | 【L5】 | 共引 **11 次**。alpelisib（NVP-BYL719）之原始藥理特性論文，為 alpelisib **isoform-α 選擇性**之一手依據（支撐「不可與 pan-PI3K 混為一談」）。 |
| 6 | 34544753 | `Preclin_Song_Inavolisib_2022` | **5x** | 2021 | Cancer Discov | 機轉/藥理 | preclinical（Cancer Discov） | 【L5】 | 共引 **5 次**。inavolisib(GDC-0077) **誘導突變型 PI3Kα 降解**之機轉論文——這是 inavolisib 與 alpelisib 藥理上分開陳述的關鍵一手證據。 |
| 7 | 36455032 | `Preclin_Hanan_Inavolisib_2022` | **4x** | 2022 | J Med Chem | 機轉/藥理 | medicinal chemistry / discovery | 【L5】 | 共引 **4 次**。inavolisib 之發現與選擇性描述，同上，用於區隔兩藥。 |
| 8 | 32274666 | `Mech_Drullinsky_2020` | **3x** | 2020 | Breast Cancer Res Treat | 機轉 | narrative review | 【L5】 | 共引 **3 次**。直接處理「PI3K 抑制劑抗腫瘤活性與不良反應（含高血糖）之機轉基礎」。 |
| 9 | 22778315 | `Mgmt_Busaidy_JCO_2012` | **4x** | 2012 | J Clin Oncol | 處置 | expert review / management guidance | 【L3】 | 共引 **4 次**。PI3K-Akt-mTOR 標靶藥物代謝副作用處置之**早期奠基性**文獻，多篇第一輪共識文章之處置演算法源頭。 |
| 10 | 31626273 | `Mgmt_Nunnery_Mayer_2019` | **4x** | 2019 | Ann Oncol | 處置 | narrative review | 【L3】 | 共引 **4 次**。isoform-α specific PI3K 抑制劑毒性處置，針對性最強。 |
| 11 | 33144920 | `Meta_Shields_Tox_2020` | **4x** | 2020 | Oncotarget | 毒性量化 | systematic review + meta-analysis | 【L2(SR)】 | 共引 **4 次**。alpelisib 毒性 endpoint 之 SR/meta，可補第一輪高血糖發生率之量化來源。 |
| 12 | 35000092 | `Discont_Cheung_2022` | **6x** | 2022 | Breast Cancer Res Treat | 真實世界 | retrospective cohort | 【L4】 | 共引 **6 次**。alpelisib **停藥原因**分析，直接關乎高血糖導致之治療中斷。 |
| 13 | 33244501 | `DKA_Farah_2020` | **7x** | 2020 | AACE Clin Case Rep | DKA | case report | 【L4】 | 共引 **7 次**，為第一輪被共引最多之 DKA 個案文獻。 |
| 14 | 34095470 | `DKA_Carrillo_2021` | **5x** | 2020 | AACE Clin Case Rep | DKA | case report + literature review | 【L4】 | 共引 **5 次**。alpelisib 誘發 DKA 之個案與文獻回顧。 |
| 15 | 30728224 | `DKA_Danne_Consensus_2019` | **3x** | 2019 | Diabetes Care | DKA | international consensus statement | 【L3】 | 共引 **3 次**。DKA 風險管理國際共識（SGLT 抑制劑情境），與第一輪 SGLT2i／euglycemic DKA 主題直接相扣，用於**警示 SGLT2i 之 DKA 風險**。 |
| 16 | 11832527 | `DPP_Knowler_2002` | **3x** | 2002 | N Engl J Med | metformin | randomized controlled trial (DPP) | 【L2】 | 共引 **3 次**。metformin 預防糖尿病之 landmark RCT；用於為 METALLICA 之 metformin 策略提供**背景**，而非取代其單臂設計之限制。 |
| 17 | 37256976 | `CAPItello291_Turner_2023` | **6x** | 2023 | N Engl J Med | 試驗主論文 | randomized phase 3 (CAPItello-291) | 【L2】 | 共引 **6 次**。第一輪僅取得 CAPItello-291 之 **AE 次分析**，**主論文缺漏**，本輪補上（capivasertib 為 AKT 抑制劑，須與 PI3Kα 抑制劑分開陳述）。 |
| 18 | 30543347 | `Alpelisib_Juric_JAMAOnc_2019` | **6x** | 2019 | JAMA Oncol | 試驗主論文 | phase 1b expansion | 【L2】 | 共引 **6 次**。alpelisib+fulvestrant 之早期關鍵試驗。 |
| 19 | 33186740 | `SANDPIPER_Dent_2021` | **6x** | 2020 | Ann Oncol | 試驗主論文 | randomized phase 3 (SANDPIPER, taselisib) | 【L2】 | 共引 **6 次**。taselisib（另一 PI3K 抑制劑）之 phase 3，**支撐「不同 PI3K 抑制劑毒性側寫不同」之對照**。 |
| 20 | 29401002 | `Alpelisib_Juric_JCO_2018` | **4x** | 2018 | J Clin Oncol | 試驗主論文 | phase Ia dose-escalation | 【L2】 | 共引 **4 次**。alpelisib 首篇人體劑量遞增試驗，高血糖 DLT 之原始描述。 |
| 21 | 39236276 | `Inavolisib_Jhaveri_JCO_2024` | **3x** | 2024 | J Clin Oncol | 試驗主論文 | phase I/Ib | 【L2】 | 共引 **3 次**。inavolisib+palbociclib+ET 之早期試驗，INAVO120 之前導。 |
| 22 | 25409150 | `Resist_Juric_PTEN_2015` | **2x** | 2014 | Nature | 機轉/抗藥 | preclinical + clinical correlate（Nature） | 【L5】 | 共引 **2 次**。PTEN loss 造成 PI3Kα 抑制劑抗藥，為 PI3K 訊息回饋之 Nature 系列一手研究。 |
| 23 | 32067679 | `Landscape_Mosele_2020` | **8x** | 2020 | Ann Oncol | 流行病學 | cohort / molecular landscape | 【L4】 | 共引 **8 次**。PIK3CA 突變轉移性乳癌之預後與分子圖譜，界定適用族群。 |
| 24 | 28576675 | `BELLE2_Baselga_2017` | **9x** | 2017 | Lancet Oncol | 試驗主論文 | randomized phase 3 (BELLE-2, buparlisib) | 【L2】 | 共引 **9 次**。**pan-PI3K** buparlisib 之 phase 3；本輪特別納入以支撐「pan-PI3K 與 isoform-α 選擇性抑制劑之毒性不可等同」之論述。 |

## 3. 共引來源明細（可稽核）

下表列出每筆之「第一輪哪些論文引用了它」，可用 `scratch/cocite.json` 的 `who` 欄位 grep 驗證。

| PMID | slug | 被下列第一輪論文引用 |
|---|---|---|
| 30462943 | `Mech_Goncalves_NEJM_2018` | `Consensus_Tankova_2022`, `DKA_Rechallenge_Leung_2022`, `Delphi_Gallagher_2024`, `FAERS_DKA_Ziegengeist_2024`, `HHS_DKA_Chafai_2022`, `InsulinFeedback_Noch_2023`, `Mgmt_Goncalves_2022`, `Multidisc_Rugo_2022`, `Prevention_Moore_2025`, `RealWorld_Liu_2022`, `RealWorld_Shen_2023`, `SOLAR1_AE_Rugo_2020`, `SOLAR1_Andre_2019`, `VLCD_SGLT2i_Blow_2021` |
| 28802037 | `Mech_Fruman_Cell_2017` | `Consensus_Tankova_2022`, `Delphi_Gallagher_2024`, `InsulinFeedback_Hopkins_2018`, `Mgmt_Goncalves_2022`, `Multidisc_Rugo_2022`, `RealWorld_Shen_2023` |
| 19118049 | `Mech_Crouthamel_AKT_2009` | `Mgmt_Goncalves_2022`, `Multidisc_Rugo_2022`, `RealWorld_Liu_2022` |
| 30263000 | `Mech_Huang_ObesityT2D_2018` | `Claims_Ismail_2026`, `DKA_Loke_2025`, `Mgmt_Goncalves_2022`, `Multidisc_Rugo_2022` |
| 24608574 | `Preclin_Fritsch_BYL719_2014` | `BYLieve_Rugo_2021`, `BYLieve_Rugo_2024`, `Consensus_Tankova_2022`, `Delphi_Gallagher_2024`, `FrenchEAP_BelloRoufai_2023`, `Multidisc_Rugo_2022`, `RiskModel_Rodon_2024`, `SGLT2i_Borrego_2024`, `SOLAR1_AE_Rugo_2020`, `SOLAR1_Andre_2019`, `SOLAR1_OS_Andre_2021` |
| 34544753 | `Preclin_Song_Inavolisib_2022` | `FDA_Inavolisib_Wedam_2025`, `INAVO120_OS_Jhaveri_2025`, `INAVO120_Safety_Im_2026`, `INAVO120_Turner_2024`, `ToxMgmt_Jhaveri_2026` |
| 36455032 | `Preclin_Hanan_Inavolisib_2022` | `FDA_Inavolisib_Wedam_2025`, `INAVO120_OS_Jhaveri_2025`, `INAVO120_Turner_2024`, `ToxMgmt_Jhaveri_2026` |
| 32274666 | `Mech_Drullinsky_2020` | `Delphi_Gallagher_2024`, `Mgmt_Goncalves_2022`, `Prevention_Moore_2025` |
| 22778315 | `Mgmt_Busaidy_JCO_2012` | `Consensus_Tankova_2022`, `DKA_Loke_2025`, `EuglycemicDKA_Bowman_2017`, `Multidisc_Rugo_2022` |
| 31626273 | `Mgmt_Nunnery_Mayer_2019` | `Capivasertib_Mgmt_Iyengar_2025`, `Claims_Ismail_2026`, `FGM_PlaPeris_2022`, `Mgmt_Goncalves_2022` |
| 33144920 | `Meta_Shields_Tox_2020` | `Consensus_Tankova_2022`, `DKA_Loke_2025`, `FGM_PlaPeris_2022`, `ITACA_Pancirov_2025` |
| 35000092 | `Discont_Cheung_2022` | `ADA_SOC2026_Ch3`, `Claims_Ismail_2026`, `FAERS_DKA_Ziegengeist_2024`, `ITACA_Pancirov_2025`, `Prevention_Moore_2025`, `RealWorld_Shen_2023` |
| 33244501 | `DKA_Farah_2020` | `Consensus_Tankova_2022`, `DKA_Loke_2025`, `DKA_Rechallenge_Leung_2022`, `FAERS_DKA_Ziegengeist_2024`, `HHS_DKA_Chafai_2022`, `Mgmt_Goncalves_2022`, `RealWorld_Shen_2023` |
| 34095470 | `DKA_Carrillo_2021` | `DKA_Loke_2025`, `DKA_Rechallenge_Leung_2022`, `FAERS_DKA_Ziegengeist_2024`, `Mgmt_Goncalves_2022`, `RealWorld_Shen_2023` |
| 30728224 | `DKA_Danne_Consensus_2019` | `Mgmt_Goncalves_2022`, `Multidisc_Rugo_2022`, `Prevention_Moore_2025` |
| 11832527 | `DPP_Knowler_2002` | `ADA_SOC2026_Ch3`, `Consensus_Tankova_2022`, `RealWorld_Shen_2023` |
| 37256976 | `CAPItello291_Turner_2023` | `CAPItello291_AE_Rugo_2024`, `Capivasertib_Mgmt_Iyengar_2025`, `GO39374_Gambardella_2025`, `INAVO120_Turner_2024`, `Prevention_Moore_2025`, `ToxMgmt_Jhaveri_2026` |
| 30543347 | `Alpelisib_Juric_JAMAOnc_2019` | `BYLieve_Rugo_2021`, `BYLieve_Rugo_2024`, `RiskModel_Rodon_2024`, `SOLAR1_AE_Rugo_2020`, `SOLAR1_OS_Andre_2021`, `SOLAR1_PRO_Ciruelos_2021` |
| 33186740 | `SANDPIPER_Dent_2021` | `INAVO120_Turner_2024`, `Meta_Li_2025`, `Mgmt_Goncalves_2022`, `Prevention_Moore_2025`, `RealWorld_Liu_2022`, `ToxMgmt_Jhaveri_2026` |
| 29401002 | `Alpelisib_Juric_JCO_2018` | `Consensus_Tankova_2022`, `RiskModel_Rodon_2024`, `SOLAR1_Andre_2019`, `SOLAR1_OS_Andre_2021` |
| 39236276 | `Inavolisib_Jhaveri_JCO_2024` | `GO39374_Gambardella_2025`, `INAVO120_OS_Jhaveri_2025`, `INAVO120_Safety_Im_2026` |
| 25409150 | `Resist_Juric_PTEN_2015` | `SOLAR1_Andre_2019`, `ToxMgmt_Jhaveri_2026` |
| 32067679 | `Landscape_Mosele_2020` | `BYLieve_Rugo_2021`, `BYLieve_Rugo_2024`, `Consensus_Tankova_2022`, `FDA_Alpelisib_Narayan_2021`, `FrenchEAP_BelloRoufai_2023`, `METALLICA_LlombartCussac_2024`, `Meta_Li_2025`, `SOLAR1_OS_Andre_2021` |
| 28576675 | `BELLE2_Baselga_2017` | `Consensus_Tankova_2022`, `Meta_Li_2025`, `Prevention_Moore_2025`, `RiskModel_Rodon_2024`, `SOLAR1_AE_Rugo_2020`, `SOLAR1_Andre_2019`, `SOLAR1_OS_Andre_2021`, `SOLAR1_PRO_Ciruelos_2021`, `ToxMgmt_Jhaveri_2026` |

## 4. 落地批次

```batch
30462943,Mech_Goncalves_NEJM_2018
28802037,Mech_Fruman_Cell_2017
19118049,Mech_Crouthamel_AKT_2009
30263000,Mech_Huang_ObesityT2D_2018
24608574,Preclin_Fritsch_BYL719_2014
34544753,Preclin_Song_Inavolisib_2022
36455032,Preclin_Hanan_Inavolisib_2022
32274666,Mech_Drullinsky_2020
22778315,Mgmt_Busaidy_JCO_2012
31626273,Mgmt_Nunnery_Mayer_2019
33144920,Meta_Shields_Tox_2020
35000092,Discont_Cheung_2022
33244501,DKA_Farah_2020
34095470,DKA_Carrillo_2021
30728224,DKA_Danne_Consensus_2019
11832527,DPP_Knowler_2002
37256976,CAPItello291_Turner_2023
30543347,Alpelisib_Juric_JAMAOnc_2019
33186740,SANDPIPER_Dent_2021
29401002,Alpelisib_Juric_JCO_2018
39236276,Inavolisib_Jhaveri_JCO_2024
25409150,Resist_Juric_PTEN_2015
32067679,Landscape_Mosele_2020
28576675,BELLE2_Baselga_2017
```

