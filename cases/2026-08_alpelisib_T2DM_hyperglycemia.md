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
| 08/09 05:00 | **173** | 晨間空腹（AC） | **FPG → Grade 2**（161–250） |
| 08/09 17:00 | 373 | 晚餐前 AC | 非晨間空腹，不作分級用 |
| 08/09 21:37 | 478 | PC → 給 Novorapid | 餐後值，不作分級用 |
| 08/09 22:42 | 388 | AC | 非空腹 |
| 08/10 05:00 | **218** | 晨間空腹（AC） | **FPG → Grade 2**（161–250） |
| 08/10 11:12 | 339 | 午餐前 AC | 非晨間空腹 |

---

## 2. 關鍵判讀：這是 Grade 2，不是 Grade 3——所以「續用 Piqray」是對的

仿單明文：**劑量調整只依空腹血糖（FPG）**。本例晨間空腹值 173 → 218 mg/dL，屬 **Grade 2（161–250）**；477/478、373、339 皆為餐前／餐後隨機值，**不進入分級**。

依 PIQRAY 仿單 Table 3（Grade 2）：

- **Alpelisib 300 mg 續用、不停藥、不減量** ✅（與目前 care plan 一致）
- 同時**加強降糖治療**，並啟動 **21 天倒數**：自加強降糖治療日（08/09）起算，**判定日 08/30**——若屆時晨間 FPG 仍 >160 → alpelisib 減一階至 **250 mg QD**
- **警戒線**：任何一次**晨間空腹** >250 → 改走 Grade 3 流程（**中斷 alpelisib**、3–5 天內達 ≤160 → 以 250 mg 恢復；21 天未達 ≤160 → 永久停藥）。08/09 晚間曲線已衝到 478（PC），離線不遠，監測不可鬆

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
| 計時器 1 | **21 天倒數：08/09 起算 → 判定日 08/30**，晨 FPG 仍 >160 → Piqray 減至 250 mg |
| 計時器 2（備用） | 任一晨間 FPG >250 → 中斷 Piqray，啟動 3–5 天窗（達 ≤160 → 250 mg 恢復） |
| 出院衛教 | 每日晨間空腹自測；**≥160 回報**；酮體警訊；腹瀉每日 ≥4 次回報 |
| 追蹤 | HbA1c q3mo；eGFR（metformin 高劑量下）；長期 metformin 者 B12 |

### 3-7. 其他

- **皮疹**：alpelisib rash 常見（any-grade 約 36–54%），請分級記錄；G1–2 → 口服抗組織胺±外用類固醇；G3 → 另有停藥規則，勿與高血糖流程混用
- 病歷勘誤：Assessment 之 "antihyper**lipid**emic" 應為 "antihyper**glyc**emic"；建議補記高血糖 **CTCAE grade 與計時器日期**，利於跨團隊交接

---

## 4. SOAP（Progression Note 建議版）

**S:** Known T2DM on alpelisib 300 mg QD + fulvestrant for stage IV luminal A breast cancer. Hyperglycemia noted on ward monitoring; denies polyuria/polydipsia complaints documented; fatigue G1; no nausea/vomiting, oral intake fair. No abdominal pain or dyspnea.

**O:** BT 36.3, **HR 108**, RR 18, BP 120/66, GCS 15. Skin: erythematous rash (alpelisib-related, grade to be documented). No Kussmaul breathing; abdomen soft.
Glucose (mg/dL): **morning fasting 173 (08/09) → 218 (08/10)**; pre-dinner 373, PC 478 → Novorapid rescue given, 388; pre-lunch 339. Ketones/HbA1c/eGFR: pending.

**A:**
1. **Alpelisib-associated hyperglycemia, CTCAE Grade 2 by fasting glucose (FPG 161–250)**, on background T2DM — per PIQRAY label: continue alpelisib 300 mg, intensify anti-hyperglycemic therapy, **21-day clock started 08/09 (decision date 08/30)**; interrupt if any morning FPG >250. Daytime excursions to 478 (post-prandial) reflect severe insulin resistance; DKA not yet excluded (ketones pending). Sinus tachycardia — likely volume depletion from osmotic diuresis.
2. Stage IV breast cancer on alpelisib + fulvestrant — continue.
3. Rash, suspect alpelisib dermatologic AE — grade and treat.
4. HTN — stable on Exforge.

**P:**
- Check **blood ketone (β-OHB)** now + electrolytes, renal function/eGFR, HbA1c; escalate to DKA/HHS pathway if ketone positive (hold oral agents, IV insulin + fluids)
- IV normal saline support (ongoing); reassess volume status and HR
- **Resolve duplication**: choose Glucophage + Forxiga 10 mg QD (inpatient) OR Xigduo XR (discharge) — not both
- Metformin: confirm tablet strength; target 1000 mg BID–TID (2000–3000 mg/day) **only if eGFR ≥60 and no significant diarrhea**; hold 48 h peri-contrast
- Dapagliflozin 10 mg QD with ketone/sick-day education (euglycemic DKA precaution)
- Novorapid rescue for pre-meal >250; **add basal insulin (glargine 0.1–0.2 U/kg qhs) if pre-meal values persist >250 despite oral escalation**; avoid sulfonylurea; down-titrate insulin promptly if alpelisib later interrupted
- Continue alpelisib 300 mg QD; **interrupt if any morning FPG >250** (then 3–5 day window, resume at 250 mg once FPG ≤160)
- Glucose QID (AC tid + HS); morning fasting value is the dose-decision metric; endocrine co-management (arranged)
- Rash: grade, antihistamine ± topical steroid; dermatology if grade ≥2 progressing
- Discharge education: home fasting SMBG daily, report ≥160; ketone warning signs; diarrhea ≥4/day report

---

## 5. 本例對照 protocol 的教學重點

1. **分級只看晨間空腹**——478（PC）會誘導過度反應（誤判 Grade 4 而停藥），173–218 的晨間 FPG 才是 Grade 2 的正確定位；「續用 Piqray」因此是**對**的，但必須配上 21 天倒數與 >250 警戒線才完整。
2. **T2DM baseline = 高風險族群**：SOLAR-1 diabetic subgroup G3-4 高血糖 83.3%（10/12）；EMA 對已知糖尿病者要求內分泌照會（本例已會診 ✅）。
3. **複方藥是隱形炸彈**：Xigduo＝Forxiga＋Glucophage，交接時最容易重複。
4. **SGLT2i 是好的第二線，但要買保險**（酮體基線值＋sick-day rules）。
5. **住院是把血糖藥架構化的機會**：出院前把「晨間 FPG 分級 → 對應動作」教給病人與家屬，返家後才守得住 21 天倒數。
