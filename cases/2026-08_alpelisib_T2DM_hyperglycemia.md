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

## 4. SOAP（Progression Note 建議版，08/11 更新）

**S:** Known T2DM on alpelisib 300 mg QD + fulvestrant for stage IV luminal A breast cancer. Progressive hyperglycemia despite metformin up-titration and dapagliflozin initiation. Fatigue G1; oral intake fair; no nausea/vomiting, abdominal pain, or dyspnea.

**O:** BT 36.3, **HR 108**, RR 18, BP 120/66, GCS 15. Skin: erythematous rash (alpelisib-related, grade to be documented). No Kussmaul breathing; abdomen soft.
**Morning fasting glucose trend (mg/dL): 181 (08/07) → 162 (08/08) → 173 (08/09) → 218 (08/10) → 255 (08/11)** — rising ×4 days despite oral escalation. Daytime excursions: pre-dinner 373, PC 478 → Novorapid rescue, pre-lunch 339. Ketones/HbA1c/eGFR: pending.

**A:**
1. **Alpelisib-associated hyperglycemia, now CTCAE Grade 3 by fasting glucose (FPG 255, >250) as of 08/11**, rising ×4 days on background T2DM despite metformin + SGLT2i — per PIQRAY label Table 3: **interrupt alpelisib**, IV hydration, assess ketosis/electrolytes; oral agents insufficient → basal insulin indicated. DKA/HHS not yet excluded (ketones pending; on SGLT2i — euglycemic DKA also possible). Sinus tachycardia — likely osmotic-diuresis volume depletion.
2. Stage IV breast cancer — alpelisib **held** as of 08/11; fulvestrant continues. Resumption plan per label: FPG ≤160 within 3–5 days (08/14–16) → resume at **250 mg QD** (one dose level down); not at target by 21 days (~08/30–09/01) → discuss permanent discontinuation.
3. Rash, suspect alpelisib dermatologic AE — grade and treat.
4. HTN — stable on Exforge.

**P:**
- **Hold alpelisib from 08/11**; confirm 255 with STAT venous glucose (confirmation, not a reason to delay management); fulvestrant continues
- **Blood ketone (β-OHB) + electrolytes + renal function/eGFR + HbA1c STAT**; if ketone positive → DKA/HHS pathway (hold oral agents incl. SGLT2i, IV insulin + fluids)
- IV normal saline (ongoing); reassess volume status and HR
- **Start basal insulin glargine 0.1–0.2 U/kg qhs today**; keep Novorapid correction for pre-meal >250; avoid sulfonylurea
- **⚠ Anticipate rapid glucose fall 24–72 h after alpelisib interruption — down-titrate basal/bolus insulin daily**; metformin is the last agent to reduce
- Continue metformin (confirm tablet strength; ≤2000–3000 mg/day only if eGFR ≥60, no significant diarrhea; hold 48 h peri-contrast) and dapagliflozin 10 mg QD if oral intake adequate — suspend SGLT2i and check ketones if intake poor/vomiting
- **Resolve duplication**: Glucophage + Forxiga (inpatient) OR Xigduo XR (discharge) — not both
- Glucose QID (AC tid + HS); **morning fasting value drives resumption decision**; mark calendar: **08/14–16 (resume-at-250 mg window)**, **08/30–09/01 (21-day limit)**; endocrine co-management (arranged)
- Rash: grade, antihistamine ± topical steroid; dermatology if grade ≥2 progressing
- Education: after resumption, daily home fasting SMBG ×2 weeks, report ≥160; ketone warning signs; diarrhea ≥4/day report

---

## 5. 本例對照 protocol 的教學重點

1. **分級只看晨間空腹**——478（PC）會誘導過度反應（誤判 Grade 4 而停藥），173–218 的晨間 FPG 才是 Grade 2 的正確定位；「續用 Piqray」因此是**對**的，但必須配上 21 天倒數與 >250 警戒線才完整。
2. **T2DM baseline = 高風險族群**：SOLAR-1 diabetic subgroup G3-4 高血糖 83.3%（10/12）；EMA 對已知糖尿病者要求內分泌照會（本例已會診 ✅）。
3. **複方藥是隱形炸彈**：Xigduo＝Forxiga＋Glucophage，交接時最容易重複。
4. **SGLT2i 是好的第二線，但要買保險**（酮體基線值＋sick-day rules）。
5. **住院是把血糖藥架構化的機會**：出院前把「晨間 FPG 分級 → 對應動作」教給病人與家屬，返家後才守得住 21 天倒數。
