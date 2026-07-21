# J. 演講大綱（30 分鐘，14 張投影片）

> **時間配置**：S1–S2 開場 3 分｜S3–S5 機轉與兩藥差異 7 分｜S6–S7 風險分層 4 分｜S8–S10 metformin 與處置 8 分｜S11–S12 安全紅線與加藥 4 分｜S13–S14 監測、爭議、收尾 4 分。
> **標記**：每張投影片下方標示對應之本文章節與所答之臨床問題編號。

---

## S1. 為什麼今天要談這件事

- PI3Kα 抑制劑的高血糖是 **on-target、可預期、有時間窗**的事件，不是意外
- alpelisib FDA 仿單：hyperglycemia **65%**、Grade 3 **33%**、Grade 4 **3.9%**、ketoacidosis **0.7%（n=2）**【L1】[label_alpelisib.md]
- 04/2026 FDA 仿單已寫入「Severe **or fatal** hyperglycemia, **including ketoacidosis**」【L1】[label_inavolisib.md]
- 內分泌科不是「事後會診」，而是**起始治療前**就該進場
- 本場的三條主線：機轉 → 分層 → 處置；外加一條安全紅線

**建議圖表**：圖 —「雙藥時間軸」：Day 0 起始 → **alpelisib 中位 15 天**（仿單 grade ≥2，range 5–517；SOLAR-1 全文 grade ≥3 亦為 15 天，range 5–395📄[SOLAR1_AE_Rugo_2020.md]；MSKCC 真實世界 16 天📄[MSKCC_RealWorld_Shen_2023.md]）／**inavolisib 中位 7.0 天**（range 2–955）→ 改善：alpelisib grade ≥3 中位 **6 天**（range 4–7，SOLAR-1 全文📄）、inavolisib FPG >160 mg/dL 者 96.3% 改善 ≥1 級、中位 **8 天**。**三個獨立來源都落在 15–16 天，可直接在圖上並列**（數據：[label_alpelisib.md][label_inavolisib.md][SOLAR1_AE_Rugo_2020.md][MSKCC_RealWorld_Shen_2023.md][INAVO120_Safety_Im_2026.md]）

**對應**：A 摘要

---

## S2. 名詞先講清楚：不是所有 PI3K 抑制劑都一樣

- ADA SOC—2026 用的類別詞是 **PI3Kα inhibitor**，Rec 9.35a 逐字寫「PI3K inhibitors **that affect the α isoform**（e.g., alpelisib and inavolisib）」【L3】[guideline_ada_comparators.md]
- idelalisib（δ）、duvelisib（δ/γ）、copanlisib（pan, IV）**不在**這些建議之內
- capivasertib 是 **AKT inhibitor**，不可外推
- MSKCC n=491：所有因高血糖之治療中斷／減量／住院皆發生在 AKT（5%）／α（13%）／pan-PI3K（5%）使用者【L4】[RealWorld_Liu_2022.md]
  - ⚠ 該文分母是「治療中斷事件」，**未報告 β/γ/δ 組的高血糖發生率為零**

**建議圖表**：表 — 「PI3K isoform 選擇性 × 給藥途徑 × 高血糖負擔」四欄對照表（alpelisib / inavolisib / capivasertib / idelalisib-duvelisib-copanlisib）

**對應**：D-0

---

## S3. 機轉圖：一張圖說完為什麼會高血糖

- p110α 是 insulin receptor → IRS → PI3K → AKT 軸的關鍵節點
- 抑制後三件事同時發生：**骨骼肌／脂肪葡萄糖攝取下降、肝糖輸出上升、代償性 hyperinsulinemia**
- 這是 **class effect 的機轉性後果**，不是特異體質
- 因此「先觀察看看」是錯的策略——時間窗在**第 1–2 週**

**建議圖表**：圖 —「PI3Kα 抑制 → insulin resistance 機轉流程圖」：Insulin → IR → IRS1/2 → **p110α（打叉）** → AKT ↓ → 分三箭頭：①GLUT4 轉位↓（肌肉/脂肪攝取↓）②FOXO1 去抑制 → 肝糖新生↑ ③血糖↑ → β 細胞代償 → insulin↑ → 回饋箭頭指回 IR（虛線，標【L5】前臨床）

**對應**：B-1、B-2（Q1）

---

## S4. Insulin feedback：這條回饋線的證據強度到底多強？

- Hopkins 2018 小鼠模型：insulin 回升可部分回復 pAKT、幾乎完全回復 pS6【L5】[InsulinFeedback_Hopkins_2018.md]
- **但同一篇研究中，metformin 對血糖（p=0.2136）、C-peptide（p=0.7566）、pS6（p=0.6186）三項皆未達顯著**
- 顯著者為 SGLT2i（<0.0001／0.0386／<0.0001）與 ketogenic diet（0.007／0.0117／<0.0001）
- **人體療效終點尚無驗證**：這是【L5】，不是【L2】
- 誠實的結論：insulin-sparing 的正當理由應掛在「**維持 dose intensity、避免 DKA/HHS**」，而不是「避免餵養腫瘤」

**建議圖表**：表 —「Hopkins 2018 三種介入 × 三個終點的 p 值對照表」（metformin／SGLT2i／ketogenic diet × 血糖／C-peptide／pS6），紅框標出 metformin 三個不顯著的 p 值

**對應**：B-3（Q2）、B-5

---

## S5. alpelisib vs inavolisib：必須分開講的五件事

- 發生率：alpelisib FDA **65%／G3 33%／G4 3.9%**；inavolisib FDA fasting glucose increased **85%／G3 12%／G4 0.6%**【L1】
- **原始論文（現有全文📄）**：SOLAR-1 preferred term **181/284＝63.7%**（G3 **93 人 32.7%**、G4 **11 人 3.9%**），AESI grouped term **187/284＝65.8%／grade ≥3 108 人 38.0%**【L2】[SOLAR1_AE_Rugo_2020.md]；INAVO120 grouped term **95/162＝58.6%**、**Grade 3 or 4 合併 9/162＝5.6%**（⚠ NEJM 原文**未拆分** G3 與 G4）【L2】[INAVO120_Turner_2024.md]；G3 5.6%、無 G4-5、無 DKA 見安全性專文【L2】[INAVO120_Safety_Im_2026.md]
- 中位發生：**15 天（range 5–395）vs 7.0 天（range 2–955）**
- 族群：INAVO120 收案要求 **fasting glucose <126 mg/dL、HbA1c <6.0%**、排除需持續治療之糖尿病；中位體重 **63.0 kg**、BMI ≥30 僅 **17.5%**、亞洲人 **38.2%**；且 **98.8% 為 CDK4/6i-naive（一線設定）**【L2】[INAVO120_Turner_2024.md]。SOLAR-1 則 **56% prediabetic、4% diabetic**、中位年齡 62 歲【L2】[SOLAR1_AE_Rugo_2020.md]
- ⚠ **不可 cross-trial compare**：CTCAE 版本不同（v4.03 vs v5.0）、term 不同（preferred vs grouped）、族群不同。INAVO120 作者自己逐字寫「Cross-trial comparisons should be made with caution」【L2】[INAVO120_Turner_2024.md]

**建議圖表 1**：表 —「alpelisib vs inavolisib FPG 門檻與處置對照表」：四層 FPG（>ULN–160／>160–250／>250–500／>500 mg/dL）× 兩藥之 withhold／dose-reduce／permanent-discontinue 規則，並用底色標出**最大差異列（>160–250：alpelisib 不調整 vs inavolisib withhold）**

**建議圖表 2（新增，全文到位後才畫得出來）**：圖 —「同一個試驗、四種數字」對照條：SOLAR-1 **65%（FDA）／67.3%（EMA）／63.7%（preferred term）／65.8%（AESI grouped）**；INAVO120 **85%（FDA 實驗室值）／59.9%（EMA AE term）／58.6%（NEJM grouped term）**。用一句標題壓住：「**比較之前，先確認 term 與分母**」【L1】【L2】

**對應**：C-1、C-2、C-3、C-4（Q3、Q4）

---

## S6. 起始前分層：七項基線評估

- **HbA1c**（<5.7 / 5.7–6.4 / ≥6.5；≥8.0% 視為不建議起始）、**FPG**（<100 / 100–125 / ≥126）
- **BMI**（<25 / 25–29.9 / ≥30）——BMI 25–29.9 已達 OR 4.0–5.4，勿低估【L4】[RealWorld_Liu_2022.md]
- **年齡**：alpelisib 仿單門檻 **≥75**；inavolisib EMA 門檻 **≥45**——**不是同一個切點**
- **併用全身性類固醇**（含 rash 處置用的 prednisone）、**既往 GDM／糖尿病家族史**
- **eGFR**：這是「降糖藥可用性與脫水風險」的分層，不是 PI3Ki 高血糖本身的風險因子

**建議圖表**：表 —「三層基線風險分層表（🟢低／🟡中／🔴高）」七列版，最右欄標【L1–L4】證據等級

**對應**：D-1、D-2、D-4（Q5）

---

## S7. 分層真的有預測力嗎？兩組硬數字

- INAVO120 風險因子個數梯度：0 項 G3–4 **2.2%**／1 項 **8.0%**／2 項 **12.5%**／3 項 **33.3%**【L2】[INAVO120_Safety_Im_2026.md]
- Rodón 隨機森林（n=505 建模、BYLieve n=340 驗證）：SOLAR-1 高風險組 G3/4 **90.6%（96/106）** vs 低風險組 **6.7%（12/178）**【L2】[RiskModel_Rodon_2024.md]
- **但高低風險組 PFS 相同（11.0 vs 10.9 個月）**——分層是為了配置監測資源，不是為了篩掉病人
- ⚠ 反例：inavolisib HHS 個案為 **59 歲、BMI 19.55、HbA1c 5.7%**，**72 小時內**血糖飆至 48.0 mmol/L【L4】[Inavolisib_HHS_Li_2026.md]
  - 原文逐字：「patients **without high-risk factors** may still experience severe drug-related adverse effects」

- 🔴 **真實世界的分子完全不同（MSKCC n=247，alpelisib，全文已到位📄）**：any-grade **61.5%**、G3–4 **29.2%**（G3 22.7%＋G4 6.5%）；但拆成 **standard care 80.3%／40.2%** vs **clinical trial 34.0%／13.0%（p<.001）**；即使只比同為 300 mg 的試驗次族群（n=33）仍為 **80% vs 52%（p<.001）**【L4】[MSKCC_RealWorld_Shen_2023.md]
  - 基線 HbA1c 是**獨立**預測因子：BMI 與 HbA1c 有交互作用（p=.005），同入模型後**只有 HbA1c 仍顯著（p<.001）**
  - ⚠ 統計法為 **Pearson's χ²**，非多變項迴歸；兩組基線不可比，**不可解讀為因果**

**建議圖表 1**：圖 — 長條圖「風險因子個數（0/1/2/3）vs Grade 3–4 高血糖率」（INAVO120 Table 4 數據），旁邊放一個紅色註記框標示 HHS 個案為低風險族群

**建議圖表 2（新增）**：圖 — 並排長條「試驗 vs 真實世界」：INAVO120 5.6%｜SOLAR-1 36.6%｜MSKCC 臨床試驗組 13.0%｜MSKCC standard care 40.2%，下方標語「**你門診的病人比較像最右邊那根**」【L2】【L4】[MSKCC_RealWorld_Shen_2023.md]

**對應**：D-1、D-6、D-7、C-5

---

## S8. Metformin 三欄決策：預防性／治療性／不適合

- **A 欄（預防性）**：alpelisib + 高風險（prediabetes、BMI ≥30、≥70 歲）→ FDA 措辭是「**Consider** premedication」，不是 shall
- **B 欄（治療性）**：已發生高血糖 → metformin 為第一線，仿單滴定 **500 QD → 500 BID → 早 500／晚 1000 → 1000 BID**【L1】[label_alpelisib.md]
- **C 欄（不適合）**：eGFR <30 禁忌；eGFR 30–44 不得新起始；嚴重腹瀉／嘔吐／脫水／即將顯影劑檢查
- **腹瀉時的處置順序**：先動 metformin，不要先減 alpelisib（Tankova：「Maintenance of alpelisib therapy, rather than metformin, is preferred in cases of diarrhea」）【L3】[Consensus_Tankova_2022.md]

**建議圖表**：表 —「Metformin 三欄決策表」（A 預防性／B 治療性／C 不適合 × 適用族群／起始劑量與滴定／風險與注意事項／證據等級）

**對應**：E 全章（Q6、Q7）、G-2、G-3（Q10、Q11）

---

## S9. METALLICA：講證據，也講分寸

- 單臂 phase 2，n=68：cohort A（正常血糖）Grade 3–4 **1/48（2.1%，95% CI 0.5–11.1）**；cohort B（prediabetes）**3/20（15.0%，95% CI 5.6–37.8）**【L2】[METALLICA_LlombartCussac_2024.md]
- Regimen：alpelisib 前 **7 天**起 metformin **500 mg BID ×3 天 → 1000 mg BID**
- 🔴 **不得作出的推論**：無對照組、歷史對照、n=68（cohort B 僅 20 人、CI 極寬）、**排除既有糖尿病**、篩檢 233 收 68（29.2%）
- **代價**：任何級腹瀉 **67.6%**、Grade ≥3 **13.2%**；metformin 減量 **36.8%**、停用 **11.8%**；僅服 metformin 的第 1 週即 **14.7%** 腹瀉
- **反向訊號**：GO39374 arm F 有風險因子者**即使早期給 metformin**，Grade 3 高血糖仍達 **40.0%（8/20）**【L2】[GO39374_Gambardella_2025.md]
- 🆕 **歷史對照的門檻可能設得太寬（SOLAR-1 全文到位後才看得出來）📄**：METALLICA cohort A（血糖正常者）的虛無假設門檻是 **25%**，但 SOLAR-1 中 **baseline normal 次族群**實際 grade 3+4 僅約 **18.6%（G3 16.8%＋G4 1.8%）**；cohort B 的 **40%** 門檻則接近 SOLAR-1 prediabetic 次族群的 **48.4%（43.4%＋5.0%）**【L2】[SOLAR1_AE_Rugo_2020.md]。**兩個 cohort 的門檻取自試驗整體率而非對應次族群**，會讓 cohort A 的 P<0.0001 看起來比實際更有說服力。（此為本回顧依兩篇全文所作之數字對照，非任一原文之結論）

**建議圖表**：圖 — 天平圖：左盤「G3–4 高血糖 2.1%／15.0%（單臂、無對照）」vs 右盤「G≥3 腹瀉 13.2%、metformin 減量 36.8%、停用 11.8%」，下方橫幅標「FDA 措辭＝Consider，不是 Shall」

**對應**：E §7、G-1（Q8）、I-2-1

---

## S10. 發生高血糖了：以 FPG 為主軸的處置流程

- **第一步不是測 FPG，是篩紅旗**：意識改變、呼吸急促／Kussmaul、嚴重脫水、腹痛嘔吐、酮體陽性 → 直接進急症流程
- 無紅旗才進 FPG 分層：>ULN–160 / >160–250 / >250–500 / >500 mg/dL（＝8.9 / 13.9 / 27.8 mmol/L）
- **兩藥在 >160–250 這一層規則不同**（alpelisib 不調整、inavolisib withhold）
- >250–500：**兩藥都要求 interrupt + IV hydration + 處理 electrolyte／ketoacidosis／hyperosmolar**
- >500：24 小時內複驗；alpelisib 確認仍 >500 即**永久停藥**，inavolisib 則為 withhold、30 天內再犯才永久停藥

**建議圖表**：圖 — 全頁決策流程圖（flowchart）：頂端「紅旗篩檢」菱形 →（是）急症流程／（否）→ FPG 四層分層 → 分歧為 alpelisib 欄與 inavolisib 欄兩條平行路徑；紅旗方塊用紅色、metformin 方塊用藍色

**對應**：F-0、F-1、F-2（Q9）

---

## S11. 🔴 安全紅線：insulin 不可延誤

- ADA Rec **9.35b（E）**：insulin「**reserved for severe hyperglycemia and hyperglycemic crises**」——這句話的意思是「**重症時是適應症**」，不是「禁用」【L3】[guideline_ada_comparators.md]
- alpelisib 仿單 Table 3 註³：「insulin may be used for **1-2 days** until hyperglycemia resolves. However, this may not be necessary in the majority…」——**是短期、有明確終點的用法**【L1】
- inavolisib EMA §4.4：「**Short-term insulin may be used as rescue treatment** for hyperglycaemia」【L1】
- 本地四個個案反證「多為 non-ketotic」不能當個別病人的保證：inavolisib 72 小時 HHS；alpelisib 血糖 **1137 mg/dL** DKA（前 36 小時用 **166 units** insulin）；612 mg/dL DKA；rechallenge 後 **4 小時**再發 DKA
- **SOLAR-1 全文的作者結論（現可逐字引用📄）**：「**short-term insulin is clearly effective for managing acute cases as well as more severe hyperglycemia associated with alpelisib and not controlled by oral antihyperglycemic medications alone**」【L2】[SOLAR1_AE_Rugo_2020.md]
- **實際用量規模**：SOLAR-1 alpelisib 組共 **52 人**用過 insulin（diabetic 5/12、prediabetic 34/159、normal 13/113），其中 **33 人為長期（>2 天）、19 人為 rescue**【L2】[SOLAR1_AE_Rugo_2020.md]；INAVO120 為 **11/162（6.8%）**、中位僅 **5.0 天**【L2】[INAVO120_Safety_Im_2026.md]；MSKCC 真實世界 **16/101（15.8%）**【L4】[MSKCC_RealWorld_Shen_2023.md]
- **停藥後 24–72 小時 insulin 需求會急速下降**（HHS 個案 46 IU/day 一週內完全停用）→ 這是「用了要盯著減」，不是「不敢用」
- **可逆性有硬數據**：SOLAR-1 全文逐字「**All patients who developed hyperglycemia had grade 0 or 1 hyperglycemia following discontinuation of alpelisib**」【L2】[SOLAR1_AE_Rugo_2020.md]

**建議圖表**：表 —「紅旗症狀 × 立即動作」清單表（症狀／檢驗閾值／動作／來源），最下方一行加粗紅字：「任一紅旗 → 跳過分層，立即靜脈輸液＋insulin，同時停藥」

**對應**：B-5、F-3（Q13）、H.3、E §5、D-7

---

## S12. Metformin 不夠時加什麼？

- 校正後降糖幅度（MSKCC n=491）：**SGLT2i −48 mg/dL**、metformin −28、SU −38、insulin −22【L4】[RealWorld_Liu_2022.md]
- **真實世界的用藥組合（MSKCC n=247，分母＝101 名接受降糖治療者）📄**：metformin **89.1%**、SGLT2i **19.8%**、insulin **15.8%**、DPP4i **11.9%**、TZD **7.9%**、SU **5.9%**；**68.3% 只需一種藥、8.9% 需 ≥3 種**【L4】[MSKCC_RealWorld_Shen_2023.md]
  - 對照 SOLAR-1（分母＝163 名接受降糖藥者）：metformin **87.1%**、**41.1% 只需一種、28.8% 需 ≥3 種**【L2】[SOLAR1_AE_Rugo_2020.md]
  - Metformin 單方之中位緩解時間 **16 天（IQR 7–26）**；需在 metformin 外加藥者 **26 天（IQR 14–64）**，顯著較長（p=.024）——⚠ 這是 **confounding by indication**（加藥者本來就比較難控），不是「加藥比較慢」
  - SGLT2i 單方在該世代**僅 3 人**，與 metformin 單方無顯著差異（p=.5）→ **本研究無法支持 SGLT2i 優於 metformin**
- **SGLT2i 的兩面性**：Borrego propensity-matched（n=19 vs 74）顯示 G≥3 事件率降 **70.6%**（HR 0.294）【L4】；但同一份 MSKCC 資料中**僅 15 人用 SGLT2i 即出現 1 例 euglycemic DKA**（pH 7.26、bicarb 13、anion gap 21）
- **癌症病人情境優先**：惡病質／體重下降者避開 SGLT2i 與 GLP-1 RA；優先考慮 pioglitazone、DPP-4i
- 觀察等待期不同：metformin **2 週**、SGLT2i **2 天**、DPP-4i **1 週**、GLP-1 RA **1 週**、TZD **6 週**【L3】[Delphi_Gallagher_2024.md]
- **三份共識排序不一致，本回顧原文並陳、不做調和**

**建議圖表**：表 —「第二線降糖藥比較表」（藥類 × 預期降糖幅度 × 起效時間 × 在癌症病人的特有風險 × 證據等級），SGLT2i 列加 ⚠ euglycemic DKA 警示

**對應**：H 全章（Q12）

---

## S13. 監測與多專科分工

- alpelisib：前 **2 週每週 ≥1 次** → 之後 ≥每 4 週；HbA1c 每 3 個月【L1】
- inavolisib：**D1–7 每 3 天 → D8–28 每週 → 續 8 週每 2 週 → 其後每 4 週**【L1】
- **HbA1c 抓不到早期高峰**：ADA 逐字「A1C alone may not capture the early peak of hyperglycemia noted with PI3Kα inhibitors」【L3】→ 必須靠 SMBG／CGM
- **酮體**：EMA 要求併用類固醇或有 intercurrent infection 者加驗 **ketones（以血酮為佳）**【L1】
- MDT 四方分工：Oncology（劑量決策）／Endocrinology（降糖方案、**高風險者起始前即照會**）／Pharmacy（交互作用、顯影劑前後停 metformin）／Nutrition（碳水攝取、**同時監看體重與食慾**）

**建議圖表**：表 —「alpelisib vs inavolisib 監測時程對照表」（時間軸列：D1–7 / D8–14 / D15–28 / 週 5–12 / 之後；兩欄分列兩藥頻率），加一列 HbA1c 與一列 ketone

**對應**：M 全章（Q15、Q16）

---

## S14. 還沒有答案的事 + 五句 take-home

- **證據缺口**：沒有 head-to-head 隨機比較；沒有預防性 metformin 的隨機對照試驗
  - INAVO120 的 protocol **只是「allowed」**預防性 metformin，**未隨機化、未報告其對發生率的影響**；實際使用者僅 **12/162（7.4%）**【L2】[INAVO120_Turner_2024.md][INAVO120_Safety_Im_2026.md]
  - **inavolisib 的 FDA PI 全文未出現 metformin 字樣**；EMA SmPC 僅寫「can be considered in patients with risk factors」【L1】[label_inavolisib.md]
- 缺乏亞洲／低 BMI 族群專門資料（INAVO120 亞洲人 38.2%，但未報告亞洲次族群之高血糖率）；`monocytes` 入選 Rodón 模型但無切點
- **三篇關鍵論文（SOLAR-1 AE、INAVO120 主論文、MSKCC Shen 2023）雖已取得全文，其未報告項目仍是硬缺口**：SOLAR-1 未報告 metformin 之 titration 排程與 DKA 事件數；INAVO120 未拆分 G3／G4、未報告 time to onset 與停藥率明細；MSKCC 未報告 DKA 人數與腎功能資料
- **爭議**：ketogenic diet 在四份來源的碳水門檻分歧（60–130 g／<50 g／<100 g／30–40% 熱量）；GLP-1 RA 與 DPP-4i 之排序三份共識不一致
- 收尾以 L 章五句 take-home message 作結

**建議圖表**：表 —「證據等級總覽：本場每一條核心建議的【L1–L5】分類」（建議 × 證據等級 × 來源 × 是否有隨機證據），最後一列留白處標明「**預防性 metformin：無【L2】隨機證據**」

**對應**：I 全章（Q17）、L
