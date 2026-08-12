# 案例討論：Alpelisib 治療中之 T2DM 病人高血糖（2026-08）

> 去識別化案例，供教學與 protocol 對照使用。依據：`PROTOCOL.md`（§2–§7）、FDA PIQRAY 仿單、Glucophage 仿單（§G-2.4b）。**非個別醫療指示，劑量決策由主治團隊確認。**

---

## 1. 病例摘要

- 左乳 invasive ductal carcinoma，cT4N2aM1 stage IV（肺、肝、骨轉移），ER 100%＋/PR 100%＋/HER2−，Luminal A
- 疾病進展後改 **alpelisib（Piqray）2# QD（300 mg）＋ fulvestrant（Faslodex）**
- 既往：**T2DM**、高血壓（Exforge）
- 住院中，癌症治療副作用評估：高血糖（另有 fatigue G1、皮膚 active lesions and red rash）
- Vital signs：BT 36.3、**HR 108**、RR 18、BP 120/66；GCS E4V5M6
- 血糖（病房血糖機，mg/dL）：

| 時間 | 值 | 屬性 | 判讀 |
|---|---|---|---|
| 08/07 晨 | **181** | 晨間空腹 | FPG → Grade 2 |
| 08/08 晨 | **162** | 晨間空腹 | FPG → Grade 2（低點） |
| 08/09 05:00 | **173** | 晨間空腹 | FPG → Grade 2 |
| 08/09 17:00 | 373 | 晚餐前 AC | 非晨間空腹，不作分級用 |
| 08/09 21:37 | 478 | PC → 給 Novorapid | 餐後值，不作分級用 |
| 08/09 22:42 | 388 | AC | 非空腹 |
| 08/10 05:00 | **218** | 晨間空腹 | FPG → Grade 2 |
| 08/10 11:12 | 339 | 午餐前 AC | 非晨間空腹 |
| **08/11 晨** | **255** | 晨間空腹 | **FPG → Grade 3（>250）**，且為連續第 4 天上升 |

---

## 2. 關鍵判讀（08/10 前的狀態）：Grade 2——「續用 Piqray」當時是對的

> ⚠ **本節反映 08/10 以前的判讀；08/11 晨間 FPG 255 已升級 Grade 3，現行處置見 §2b。**

仿單明文：**劑量調整只依空腹血糖（FPG）**。本例晨間空腹值 173 → 218 mg/dL，屬 **Grade 2（161–250）**；477/478、373、339 皆為餐前／餐後隨機值，**不進入分級**。

依 PIQRAY 仿單 Table 3（Grade 2）：

- **Alpelisib 300 mg 續用、不停藥、不減量** ✅（與目前 care plan 一致）
- 同時**加強降糖治療**，並啟動 **21 天倒數**：自加強降糖治療日（08/09）起算，**判定日 08/30**——若屆時晨間 FPG 仍 >160 → alpelisib 減一階至 **250 mg QD**
- **警戒線**：任何一次**晨間空腹** >250 → 改走 Grade 3 流程（**中斷 alpelisib**、3–5 天內達 ≤160 → 以 250 mg 恢復；21 天未達 ≤160 → 永久停藥）。08/09 晚間曲線已衝到 478（PC），離線不遠，監測不可鬆

---

## 2b. 【08/11 更新】晨間 FPG 255 → 升級 Grade 3：中斷 alpelisib

08/11 晨間空腹 **255 mg/dL** 已跨過 Grade 3 門檻（>250），且是在 metformin 上調＋Forxiga 加入之後仍**連續四天上升**（162 → 173 → 218 → 255）——這不是單點雜訊，是治療壓不住的趨勢。§2 的「Grade 2 續用」判讀**自今日起失效**。

依 PIQRAY 仿單 Table 3（Grade 3）：

1. **今日起暫停 alpelisib**（今晨劑量若已服，明日起停）。可同步以**靜脈血糖複驗**確認（血糖機 ±15% 誤差，255 為邊際值）——但複驗是確認、不是拖延理由：即使複驗 240，四天上升的趨勢仍支持積極處置
2. **立即驗血酮（β-OHB）＋電解質**——Grade 3 的必要動作，且病人正在用 SGLT2i
3. **IV 輸液**（已在給 ✅）；處理電解質異常
4. **降糖治療升階**：口服已近滿載（metformin＋SGLT2i）→ **今日加 basal insulin**（glargine 0.1–0.2 U/kg qhs），Novorapid 校正照舊
5. **新計時器**：
   - **3–5 天窗（08/14–08/16）**：FPG 降至 ≤160 → **以 250 mg（降一階）恢復** alpelisib
   - 08/16 仍未達 ≤160 → 內分泌主導（已共管 ✅），繼續停藥
   - **21 天大限（約 08/30–09/01）**：仍未達 ≤160 → **永久停用 alpelisib** 之討論
6. **⚠ 停藥後的反向陷阱（本例特別重要）**：alpelisib 中斷後血糖多在 **24–72 小時內明顯回落**——今天才加上的 basal insulin 與 Novorapid 必須**每日下修**，否則 48–72 小時後會低血糖；metformin 最後動。SGLT2i 若進食正常可續用（有助快速達標、爭取 3–5 天窗內恢復），但任何進食變差／嘔吐即暫停並驗酮
7. **恢復後的長期布局**：以 250 mg 恢復後，此病人（baseline T2DM、Grade 3 病史）屬**高復發風險**——恢復日起監測回到每日晨間 FPG × 2 週，並預先決定「再犯 Grade 3」時的方案（仿單：再減一階至 200 mg 或依 21 天規則停藥）

---

## 2c. 【08/12 更新】血酮 0.9＋代謝性酸中毒＋eGFR 48–51 → 停口服藥、insulin 全面接手

**新數據**：
- 血糖：08/11 05:00 255 → 11:00 346 → 20:58 **505** → 22:45 498；08/12 晨 **310／369**（停 alpelisib 第 2 天，晨間空腹仍 Grade 3）
- Insulin 實際給量：Toujeo 8 單位（08/11、08/12）＋ Novorapid 4＋8＋6 單位——**一日總量約 26 單位，對這個血糖量級明顯不足**
- 血液氣體（08/12 05:53）：pH 7.397、PCO2 28.4、**HCO3 17.6、BE −7.5** → **代償性代謝性酸中毒**；anion gap ≈ 131−(102+17.6) ≈ **11（正常）**
- **血酮 0.9 mmol/L（參考 <0.6）**——輕度酮症，未達 DKA（pH 正常、AG 正常、酮 <3.0），但病人正在用 dapagliflozin，這是必須立刻反應的警訊
- 腎功能：Crea 1.17、**eGFR 48.8（MDRD）／50.6（CKD-EPI）／C-G 41**；BUN/Cr ≈ 23 → 有 prerenal（脫水）成分
- Na 131（血糖校正後 ≈135，translocational）；K 4.5–4.8 正常；CBC 無感染像；HR 已由 108 → 80–85、體溫正常、BP 102–136/57–75

**判讀與動作**：

1. **Dapagliflozin（Forxiga）今日暫停**——酮體升高＋代謝性酸中毒是 SGLT2i 的 sick-day 停藥指徵；繼續用下去是往 ketoacidosis 推。酮體 <0.6、酸中毒矯正、進食正常後再評估恢復
2. **Metformin 今日暫停**——三重理由：eGFR <60（且 C-G 41）、代謝性酸中毒進行中、volume depletion。**原「2# TID＝3000 mg」計畫正式作廢**：eGFR 45–59 依 protocol 上限應回到 ≤2000 mg/day 且加密腎功能監測；eGFR 若進一步 <45 → 減半或不用
3. **Insulin 升級為主力（本事件現在是 insulin-requiring）**：Toujeo 8 單位顯著不足——建議今晚上調至 **12 單位**（之後每日依晨值 +2–4 單位滴定），並改為**三餐固定劑量 Novorapid（4–6 單位）＋校正量表**，不要只靠事後校正追。口服藥停用後 insulin 需求會再上升，滴定要積極
4. **輸液持續**（isotonic saline）——同時處理 prerenal 與酮症；今晚複驗：血酮、靜脈血氣、電解質（含 K）、血糖 q4–6h
5. **惡化界線（任一達標 → DKA 流程、IV insulin infusion）**：血酮 ≥3.0、pH <7.30、HCO3 <15、意識改變或嘔吐無法進食
6. **Alpelisib 計時器不變**：晨間空腹 310–369 → 續停；**任一天晨值 ≤160（於 ~08/30 前）→ 以 250 mg 恢復**；08/30–09/01 仍未達標 → 永久停藥討論。注意：現在停了口服藥、insulin 未到位前，達標日會往後移——**這正是「3–5 天窗內積極治療」的代價教訓**
7. 次要：Na 131 為高血糖之 translocational（校正 ≈135），血糖改善後複驗即可；確認 HbA1c 是否已採
8. **恢復 alpelisib（250 mg）當天的預案**：屆時病人將在較高劑量 insulin 上——恢復後血糖會再升，但**若再次中斷則需立即下修 insulin**；出院前把「alpelisib 開/停 ↔ insulin 加/減」的聯動教給病人與家屬

---

## 3. 建議（依優先序）

### 3-1. 🔴 用藥安全——先解決處方重複

Care plan 同時出現 **Xigduo**（dapagliflozin＋metformin 複方）與 **Glucophage＋Forxiga**（同成分之單方組合）。三者併開會造成 **dapagliflozin 加倍＋metformin 超量**。二擇一：

- 方案 A：**Glucophage＋Forxiga 10 mg QD**（單方分開、劑量好調——住院滴定期建議）
- 方案 B：出院後改 **Xigduo XR** 簡化（停 Glucophage 與 Forxiga 單方）

### 3-2. Metformin 劑量核算（Glucophage 1#→2# TID）

- 若為 **500 mg 錠**：2# TID = **3000 mg/day** = 歐盟仿單上限（美國上限 2550）。依 §G-2.4b：**僅在 eGFR ≥60 且無明顯腹瀉**時可行；劑量反應在 2000 mg 已近平頂（Garber 1997），且本例**已加了 SGLT2i**——**建議先以 1000 mg BID–TID（2000–3000）觀察，優先確認 eGFR 再上滿**
- 若為 **850 mg 錠**：2# TID = 5100 mg/day，**超過所有仿單上限，不可**——請核對錠劑規格
- 顯影劑 CT 追蹤前後 48 小時之 metformin 暫停規則一併醫囑化

### 3-3. SGLT2i（Forxiga）起始安全清單（euglycemic DKA 預防）

T2DM＋alpelisib＋住院中起始 SGLT2i，逐項確認：①目前進食量足夠、無持續嘔吐腹瀉 ②eGFR ≥30（且 ≥45 效果較佳）③**起始前驗血酮 β-OHB**（本例日間血糖 >250 本就該驗）④衛教：倦怠／噁心／腹痛 → 立即驗酮；生病日（無法進食）暫停 Forxiga；手術/大腸鏡前 5 天停 ⑤避免極低碳水飲食。已有 PI3Ki＋SGLT2i 之 euglycemic DKA 個案（glucose 143 仍酮酸中毒）——**血糖不高不能排除**。

### 3-4. 立即補做的檢驗

- **血酮（β-OHB）**：日間值 >250–478 卻無酮體紀錄——Grade 3 範圍的值出現過就必須驗
- 電解質（Na/K）、renal function/eGFR（決定 metformin 3000 與 inavolisib 無關但影響 Forxiga）、HbA1c（近 3 個月無值的話）
- **HR 108 的解讀**：滲透性利尿→volume depletion 是最可能原因，IV fluid 已給 ✅；仍需排除感染、疼痛、貧血

### 3-5. Insulin 的定位（本例為 baseline T2DM，門檻要放低）

- Novorapid rescue ✅ 符合仿單（Grade 3 值域允許 insulin rescue 1–2 天）
- SOLAR-1 中 baseline diabetic 者 **5/12 用到 insulin**——本例若三餐前持續 >250 儘管口服藥升階，**直接加 basal insulin（如 glargine 0.1–0.2 U/kg qhs）**，不要只靠 sliding scale 追
- **避免 sulfonylurea**（反彈性低血糖）
- **反向陷阱**：若日後 alpelisib 因故中斷，血糖 24–72 小時內回落——**同日下修 insulin**，metformin 最後停

### 3-6. 監測與時間軸（寫進醫囑與行事曆）

| 項目 | 內容 |
|---|---|
| 住院中 | 血糖 QID（三餐 AC＋HS）；**晨間 05:00 AC 為分級決策值** |
| ~~計時器 1~~ | ~~21 天倒數（Grade 2）：08/09 起算 → 判定日 08/30~~ **已於 08/11 被 Grade 3 事件取代（見 §2b）** |
| **計時器 2（現行）** | **08/11 中斷 Piqray → 3–5 天窗 08/14–08/16**：FPG ≤160 → 以 250 mg 恢復；未達 → 內分泌主導續停 |
| **計時器 3（現行）** | **21 天大限 08/30–09/01**：仍未達 ≤160 → 永久停藥討論 |
| 出院衛教 | 每日晨間空腹自測；**≥160 回報**；酮體警訊；腹瀉每日 ≥4 次回報 |
| 追蹤 | HbA1c q3mo；eGFR（metformin 高劑量下）；長期 metformin 者 B12 |

### 3-7. 其他

- **皮疹**：alpelisib rash 常見（any-grade 約 36–54%），請分級記錄；G1–2 → 口服抗組織胺±外用類固醇；G3 → 另有停藥規則，勿與高血糖流程混用
- 病歷勘誤：Assessment 之 "antihyper**lipid**emic" 應為 "antihyper**glyc**emic"；建議補記高血糖 **CTCAE grade 與計時器日期**，利於跨團隊交接

---

## 4. SOAP 精簡版（08/12 最新，無縮寫、可直接用）

**Subjective:** Type 2 diabetes mellitus; alpelisib held since August 11 (day 2) for Grade 3 hyperglycemia; fulvestrant continues. Glucose remains high despite basal and rescue insulin. Eating fair; no vomiting, abdominal pain, or dyspnea; feels less fatigued.

**Objective:** Heart rate improved to 80–85, afebrile, blood pressure 102–136/57–75, fully alert. Glucose: 255 → 346 → **505** → 498 (August 11), morning fasting **310／369** (August 12). Insulin received: Toujeo (glargine 300 units per milliliter) 8 units nightly; insulin aspart 4＋8＋6 units. Venous blood gas: pH 7.397, bicarbonate **17.6**, base excess −7.5 — **compensated metabolic acidosis**, anion gap about 11 (normal). **Blood ketone 0.9 millimoles per liter (elevated; reference below 0.6).** Creatinine 1.17, **estimated glomerular filtration rate 48–51**; blood urea nitrogen 27 (ratio suggests volume depletion). Sodium 131 (about 135 after glucose correction), potassium 4.5–4.8. Complete blood count unremarkable.

**Assessment:**
1. **Alpelisib-associated Grade 3 hyperglycemia, day 2 of drug interruption — still above target**, now with **early ketosis (0.9) and compensated metabolic acidosis while on dapagliflozin**, plus reduced kidney function (estimated glomerular filtration rate 48–51) with a prerenal component. Not diabetic ketoacidosis at this point (normal pH and anion gap), but oral agents are no longer safe and current insulin dosing is insufficient.
2. Stage IV breast cancer — alpelisib on hold; fulvestrant continues.
3. Hyponatremia 131 — translocational from hyperglycemia.
4. Suspected alpelisib rash; hypertension stable.

**Plan:**
- **Stop dapagliflozin today** (ketosis plus metabolic acidosis = sick-day rule); reassess only when ketone below 0.6, acidosis resolved, and eating well.
- **Stop metformin today** (estimated glomerular filtration rate below 60 with acidosis and volume depletion); when restarted later, maximum 2000 milligrams per day — **the previous 3000-milligram plan is cancelled**.
- **Escalate insulin — now the main therapy**: increase Toujeo from 8 to **12 units tonight**, then adjust by 2–4 units daily by the morning value; add **scheduled insulin aspart 4–6 units before each meal** plus a correction scale.
- Continue intravenous normal saline; recheck blood ketone, venous blood gas, electrolytes tonight; glucose every 4 to 6 hours.
- **Escalation criteria to the diabetic ketoacidosis pathway (intravenous insulin infusion)**: ketone 3.0 or above, pH below 7.30, bicarbonate below 15, vomiting, or altered consciousness.
- Alpelisib: keep holding; **resume at 250 milligrams once the morning fasting glucose reaches 160 or below (any day before about August 30)**; if still above 160 by August 30 to September 1, discuss permanent discontinuation.
- Recheck sodium after glucose improves; confirm glycated hemoglobin has been sent; monitor kidney function during rehydration.
- Before discharge, teach the link between alpelisib on/off and insulin dose up/down to prevent hypoglycemia.

---

### 前一日版本（08/11）

**Subjective:** Type 2 diabetes mellitus, on alpelisib 300 milligrams daily plus fulvestrant for stage IV breast cancer. Glucose rising despite metformin and dapagliflozin. Mild fatigue only; eating fair; no nausea, vomiting, or dyspnea.

**Objective:** Heart rate 108, other vital signs stable, fully alert. Erythematous rash. **Morning fasting glucose 181 → 162 → 173 → 218 → 255 mg/dL (August 7–11)**; post-dinner peak 478 → insulin aspart rescue. Ketone, glycated hemoglobin, renal function pending.

**Assessment:**
1. **Alpelisib-induced hyperglycemia, Grade 3 (fasting 255 on August 11)**, rising four days despite two oral agents, on background type 2 diabetes; ketoacidosis not yet excluded; tachycardia likely volume depletion.
2. Stage IV breast cancer — **alpelisib held today**; fulvestrant continues.
3. Suspected alpelisib rash.
4. Hypertension, stable.

**Plan:**
- Hold alpelisib; confirm 255 with venous glucose; continue fulvestrant.
- Immediate blood ketone, electrolytes, renal function, glycated hemoglobin; ketone positive → ketoacidosis pathway.
- Continue intravenous saline.
- Start glargine 0.1–0.2 units per kilogram at bedtime; insulin aspart correction for pre-meal >250; no sulfonylurea.
- Glucose will fall within 24–72 hours off alpelisib — **down-titrate insulin daily**.
- Continue metformin and dapagliflozin if eating well (hold dapagliflozin and check ketone if intake poor); **choose one regimen — Glucophage plus Forxiga, or Xigduo — never both**.
- Glucose four times daily; **morning fasting value decides resumption: ≤160 by August 14–16 → resume at 250 milligrams; still >160 by about August 30 → discuss permanent discontinuation.**
- Endocrinology co-management; rash: grade and treat; teach patient to report fasting ≥160 and ketone warning signs.

---

### 4b. 完整版（同日，含細節）

**Subjective:**
The patient has known type 2 diabetes mellitus and is receiving alpelisib 300 milligrams once daily together with fulvestrant for stage IV luminal A breast cancer. Progressive hyperglycemia has developed despite up-titration of metformin and initiation of dapagliflozin. She reports grade 1 fatigue. Oral intake is fair. She denies nausea, vomiting, abdominal pain, and shortness of breath.

**Objective:**
Body temperature 36.3 degrees Celsius, **heart rate 108 beats per minute**, respiratory rate 18 breaths per minute, blood pressure 120/66 millimeters of mercury, Glasgow Coma Scale 15 (fully alert). Skin: erythematous rash, suspected to be related to alpelisib; grade to be documented. No deep or labored (Kussmaul) breathing; abdomen soft.
**Morning fasting blood glucose trend (milligrams per deciliter): 181 (August 7) → 162 (August 8) → 173 (August 9) → 218 (August 10) → 255 (August 11)** — rising for four consecutive days despite escalation of oral anti-hyperglycemic agents. Daytime values: 373 before dinner and 478 after dinner (insulin aspart given as rescue) on August 9; 339 before lunch on August 10. Blood ketone, glycated hemoglobin, and estimated glomerular filtration rate: pending.

**Assessment:**
1. **Alpelisib-associated hyperglycemia, now Grade 3 by the Common Terminology Criteria for Adverse Events, based on a morning fasting blood glucose of 255 milligrams per deciliter (above 250) on August 11**, rising for four consecutive days in a patient with pre-existing type 2 diabetes mellitus despite metformin plus a sodium-glucose cotransporter 2 inhibitor. According to the PIQRAY prescribing information (Table 3), this requires **interruption of alpelisib**, intravenous hydration, and assessment for ketosis and electrolyte disturbances. Oral agents are insufficient; basal insulin is indicated. Diabetic ketoacidosis and hyperosmolar hyperglycemic state have not yet been excluded (ketone result pending; note that the patient is taking a sodium-glucose cotransporter 2 inhibitor, so ketoacidosis with near-normal glucose is also possible). Sinus tachycardia is most likely due to volume depletion from osmotic diuresis.
2. Stage IV breast cancer — alpelisib **held** as of August 11; fulvestrant continues. Resumption plan per the prescribing information: if fasting blood glucose falls to 160 milligrams per deciliter or below within 3 to 5 days (August 14 to 16), resume alpelisib at **250 milligrams once daily** (one dose level lower); if not at target by 21 days (approximately August 30 to September 1), discuss permanent discontinuation.
3. Rash, suspected alpelisib-related dermatologic adverse event — to be graded and treated.
4. Hypertension — stable on amlodipine/valsartan (Exforge).

**Plan:**
- **Hold alpelisib from August 11**; confirm the value of 255 with an immediate venous plasma glucose (for confirmation only — management should not be delayed while waiting); continue fulvestrant.
- **Check blood beta-hydroxybutyrate (ketone), electrolytes, renal function with estimated glomerular filtration rate, and glycated hemoglobin immediately**; if ketone is positive, proceed to the diabetic ketoacidosis / hyperosmolar hyperglycemic state pathway (stop oral anti-hyperglycemic agents including the sodium-glucose cotransporter 2 inhibitor; give intravenous insulin and fluids).
- Continue intravenous normal saline; reassess volume status and heart rate.
- **Start basal insulin glargine 0.1 to 0.2 units per kilogram at bedtime today**; continue insulin aspart (Novorapid) correction doses for pre-meal glucose above 250 milligrams per deciliter; avoid sulfonylurea drugs.
- **Anticipate a rapid fall in blood glucose within 24 to 72 hours after alpelisib interruption — reduce the basal and correction insulin doses every day accordingly to prevent hypoglycemia**; metformin should be the last agent to be reduced.
- Continue metformin (confirm tablet strength; total daily dose 2000 to 3000 milligrams only if estimated glomerular filtration rate is 60 or above and there is no significant diarrhea; withhold for 48 hours around iodinated-contrast imaging) and dapagliflozin 10 milligrams once daily provided oral intake remains adequate — suspend dapagliflozin and check ketones if intake becomes poor or vomiting develops.
- **Resolve the medication duplication**: use either Glucophage plus Forxiga (during admission) or the combination tablet Xigduo XR (at discharge) — not both together, because Xigduo XR already contains both dapagliflozin and metformin.
- Blood glucose monitoring four times daily (before each meal and at bedtime); **the morning fasting value is the metric that drives the resumption decision**; mark the calendar: **August 14 to 16 (window to resume at 250 milligrams)** and **August 30 to September 1 (21-day limit)**; continue co-management with the endocrinology team.
- Rash: document the grade; give an oral antihistamine with or without a topical corticosteroid; consult dermatology if grade 2 or higher and progressing.
- Education: after resumption, the patient should check a fasting fingerstick glucose at home every morning for two weeks and report any value of 160 milligrams per deciliter or above; teach the warning signs of ketoacidosis (fatigue, nausea, abdominal pain); report diarrhea of four or more episodes per day.

---

## 5. 本例對照 protocol 的教學重點

1. **分級只看晨間空腹**——478（PC）會誘導過度反應（誤判 Grade 4 而停藥），173–218 的晨間 FPG 才是 Grade 2 的正確定位；「續用 Piqray」因此是**對**的，但必須配上 21 天倒數與 >250 警戒線才完整。
2. **T2DM baseline = 高風險族群**：SOLAR-1 diabetic subgroup G3-4 高血糖 83.3%（10/12）；EMA 對已知糖尿病者要求內分泌照會（本例已會診 ✅）。
3. **複方藥是隱形炸彈**：Xigduo＝Forxiga＋Glucophage，交接時最容易重複。
4. **SGLT2i 是好的第二線，但要買保險**（酮體基線值＋sick-day rules）。
5. **住院是把血糖藥架構化的機會**：出院前把「晨間 FPG 分級 → 對應動作」教給病人與家屬，返家後才守得住 21 天倒數。
