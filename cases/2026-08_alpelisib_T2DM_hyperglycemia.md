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

## 2d. 【08/14 更新】達標了——啟動 250 mg 恢復；風險反轉為低血糖

**血糖走勢（晨間 05–06:00 為空腹，其餘為餐前/餐後）**：

| 日期 | 空腹 | 日間值 | 事件 |
|---|---|---|---|
| 08/11 | 255 | 325／346／505／498 | 停 alpelisib（第 0 天） |
| 08/12 | 310（lab 369） | 338／285／324 | 停口服藥；Toujeo 12 單位＋Novorapid 6 單位 tid |
| 08/13 | **125** ✅ | 208／290／318 | **空腹達標（停藥第 2 天，3–5 天窗內）**；停餐前 Novorapid，改 Glucophage 1# tid pc（1500 mg/day）；21:00 校正 4 單位 |
| 08/14 | **107** ✅ | 206 | 連續第 2 天達標；**趨勢仍在下降** |

同日新資訊：**HbA1c 7.8%**——basal 的糖尿病控制原本就未達標（非單純 alpelisib 造成）。

**判讀**：

1. **恢復條件已成立**：晨間空腹 125（08/13）→ 107（08/14），於停藥後 3–5 天窗內達 ≤160 → 依仿單**以 250 mg QD 恢復 alpelisib**。回穩速度完全符合預測（第 2–3 天回落、第 3–5 天趨穩），也再次印證 08/12 的判讀——當時壓不下來是 insulin 不足，不是藥沒退。
2. **現在的風險是低血糖，不是高血糖**：空腹 107 且仍在降、Toujeo 12 單位未動、alpelisib 尚未恢復。**兩條路二選一，今天就要決定**：
   - **恢復 alpelisib 250 mg（建議，儘速）**：血糖將於 24–48 小時內回升 → Toujeo 12 單位**先維持**，恢復後首 3 天血糖 QID 監測，之後依晨值調整
   - **暫不恢復**：今晚 Toujeo **12 → 8–10 單位**，否則明晨可能 <70
3. **Metformin 1500 mg/day（1# tid）的兩個前提要補**：①複驗 creatinine/eGFR（08/12 的 48–51 含 prerenal 成分，補水後應改善；eGFR 45–59 上限 2000，1500 合規）②確認血酮已 <0.6、HCO3 回升（08/12 為 0.9／17.6，複驗結果未見報告）。
4. **日間餐後 200–320 未解**：餐前 Novorapid 已停，恢復 alpelisib 後這塊會再惡化。預案：恢復後若餐前值持續 >250 → 重新加餐前 insulin（或上調 Toujeo）；酮體正常＋進食穩定後可重新評估 dapagliflozin（alpelisib 恢復後其「不經 PI3K 路徑」的優勢更重要）。
5. **HbA1c 7.8% 的長期課題**：目標 <7.5%（預後良好層）；出院方案朝 metformin（≤2000）±SGLT2i±basal 規劃，內分泌門診接手。

---

## 2e. 【08/21 更新】150 mg 再挑戰失敗 → 現以 37.5 mg（1/4 錠）續用中：血糖端已穩，未解的是腫瘤端

### 實際發生的事（08/14–08/21）

團隊於 08/14 恢復 Piqray，但劑量是 **150 mg（1# QD）**，而非仿單減一階的 250 mg；當晚血糖即衝 377，08/15 晨間空腹 **305 → 二度 Grade 3 → 再停藥**。08/15 起降糖方案定為 **Toujeo 14 單位 QD＋NovoRapid 8 單位 TID AC＋Glucophage 1# TID PC（1500 mg/day）**。停藥後空腹再次於第 2 天回落達標（160，08/17）——與第一次中斷完全相同的 24–72 小時規律。08/18 起改以 **150 mg 之 1/4 錠（約 37.5 mg）QD** 續用至今。

| 日期 | 晨間空腹 | 日間值（AC/PC） | Piqray | 事件 |
|---|---|---|---|---|
| 08/14 | 107 ✅ | 206／179／**377**(21:03) | **150 mg 1#（恢復日）** | 以 150 mg 恢復（非仿單之 250）；當晚即 377 |
| 08/15 | **305** ❌ | 290(PC)／349／451 | 停 | **二度 Grade 3 → 再停藥**；Toujeo 上調 14 單位、重啟 NovoRapid 8 單位 tid ac |
| 08/16 | 276 | 287／303／213(PC) | 停 | |
| 08/17 | **160** ✅ | 229／219／327 | 停 | 停藥第 2 天空腹達標（3–5 天窗內，第二次驗證回落規律） |
| 08/18 | 164 | 146／184／178 | **37.5 mg（1/4#）起** | 164 為 Grade 2 下緣（血糖機 ±15% 邊際值） |
| 08/19 | **134** ✅ | 247／229／354／287 | 37.5 mg | 晚間峰 354 |
| 08/20 | **133** ✅ | 233／304／322／187 | 37.5 mg | HR 105 |
| 08/21 | **158** ✅ | 266（午前） | 37.5 mg | 本日；nausea G1、fatigue G1 |

### 判讀一：血糖端——分級決策值已連續達標

晨間空腹 134 → 133 → 158，**連續 3 天 ≤160（Grade 1）**；日間餐前/餐後 200–354 不進入分級（劑量決策只用 FPG）。在「37.5 mg＋basal-bolus＋metformin 1500」的組合下，空腹血糖是壓得住的。殘餘問題是**晚餐段峰值（304–354）**，屬降糖藥調整範疇，不觸發抗癌藥動作。

### 判讀二：腫瘤端——37.5 mg 是仿單外劑量，這是現在真正要決策的事

依 PIQRAY 仿單【L1，`來源/label_alpelisib.md`】：

- 減量階梯只有 **300 → 250 → 200 mg**，最多減兩階；「若需減至 200 mg 以下，**永久停用 PIQRAY**」（Table 1 註 2）。
- 錠劑須整顆吞服，「**不可咀嚼、壓碎或剝半**」；破損不完整之錠劑不可服用——1/4 錠除了劑量本身仿單外，膜衣錠剝切後實際暴露量也無法保證。
- 依仿單邏輯走：08/11 第一次 Grade 3 → 應以 250 恢復；08/15 第二次 Grade 3 → 應以 **200 mg**（第二階）恢復。團隊實際走了 150 → 37.5，等於已離開仿單路徑兩步。
- **150 mg 與 37.5 mg 的抗癌療效，本回顧未取得可驗證來源**（SOLAR-1 減量階梯同樣止於 200 mg/day【L2，`來源/fulltext_facts_SOLAR1.md`】）。37.5 mg 目前「血糖可控」的代價可能是「療效未知」。

**給腫瘤科的三個選項（需明確擇一並記錄於病歷）：**

| 選項 | 內容 | 依據與代價 |
|---|---|---|
| A. 依仿單停藥 | 永久停用 alpelisib，fulvestrant 續用，由腫瘤科評估換線 | 仿單正規路徑（兩次 Grade 3 後已無仿單內空間可退） |
| B. 以 200 mg 再試一次 | 仿單內最後一階（200 mg 錠，不必剝）；配現行 basal-bolus＋metformin，可再加 dapagliflozin 後再挑戰 | 註意：08/14 的 150 mg 失敗**不能直接外推**——當時僅 Toujeo 12＋metformin、無餐前 insulin，降糖火力與現在不同。挑戰日起血糖 QID×3 天，FPG >250 即停 |
| C. 維持 37.5 mg | 現況 | Off-label、療效無來源、剝錠劑量不準——若選此路，病歷須載明為知情決策 |

### 判讀三：現行計時器

- 第二次中斷（08/15）之 3–5 天窗：**08/17 已達標 ✅**，恢復條件成立（惟恢復劑量如上為爭點）。
- 21 天永久停藥計時（FPG 未達 ≤160 者適用）**未被觸發**——兩次中斷空腹都在第 2 天回落。本例的問題從來不是「壓不下來」，是「藥一回來就彈」。

### 本次建議（依優先序）

1. **腫瘤科決策 A/B/C 三選一並記錄**（上表）——這是本週最重要的一件事，血糖團隊配合任一選項都有對應方案。
2. **降糖方案維持並微調**：Toujeo 14 單位＋NovoRapid 8 單位 tid＋metformin 1500 續用。滴定規則：FPG >160 連 2 天 → Toujeo +2 單位；FPG <90 或任一值 <70 → Toujeo −2 單位；**晚餐段峰值 304–354 → 晚餐前 NovoRapid 8 → 10 單位**（每 2–3 天依晚餐後值再 +2）。
3. **Dapagliflozin 再評估**：血酮複驗 <0.6＋進食正常＋eGFR 複驗 ≥45 三條件到齊 → 恢復 Forxiga 10 mg QD——不經 insulin 路徑、主攻日間高血糖，若走選項 B 尤其值得先上。Sick-day rules 衛教不可省（nausea G1 現在就存在，若惡化到影響進食 → 當日停 SGLT2i 並驗酮）。
4. **待補檢驗（08/12 之後未見報告）**：creatinine/eGFR（決定 metformin 1500 合規性與上限）、血酮複驗、電解質。HbA1c 7.3（08/07）→ 7.8（08/12）已知，下次 q3mo。
5. **HR 105 持續竇速**：血糖已改善、輸液進行中仍 >100——複查血色素、感染指標、volume status，不要全部歸因高血糖。
6. **低血糖預案不變**：若 Piqray 再停（任何原因），**同日** Toujeo 14 → 10–12 單位、NovoRapid 減半或停，metformin 最後動。
7. **出院規劃**：metformin ≤2000 mg/day（eGFR 45–59 期間）、basal insulin 居家自我滴定表、每日晨間空腹自測且 ≥160 回報、內分泌與腫瘤科共同追蹤；HbA1c 目標 <7.5%。

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

## 4-0. SOAP 短版（08/21，病房交班用）

**S:** Alpelisib 37.5 mg (1/4 of 150 mg tab) daily since 8/18, after second Grade 3 hyperglycemia (FPG 305) on 150 mg rechallenge 8/14–15. Nausea G1, fatigue G1. Eating well; no hypoglycemia.

**O:** FPG 134 → 133 → 158 (8/19–21) — **≤160 for 3 consecutive days**. Daytime values 187–354, dinner peaks 304–354. HR 105, afebrile. Regimen: Toujeo 14 U qd + NovoRapid 8 U tid ac + metformin 500 mg tid pc. HbA1c 7.8% (8/12). Repeat eGFR/ketone: pending.

**A:**
1. Alpelisib-associated hyperglycemia — FPG at target (Grade 1) on current regimen; residual dinner-time hyperglycemia = insulin-titration issue.
2. **37.5 mg is off-label** (label: minimum dose level 200 mg, below 200 → permanently discontinue; tablets must not be split) — oncology decision needed: discontinue / rechallenge 200 mg whole tablet / continue off-label with documentation.
3. Persistent sinus tachycardia 105.
4. eGFR + ketone reverification outstanding (gates metformin ceiling and dapagliflozin restart).

**P:**
- Keep Toujeo 14 U + NovoRapid 8 U tid + metformin 1500 mg/day; **dinner NovoRapid 8 → 10 U** for evening peaks; Toujeo +2 U if FPG >160 ×2 days, −2 U if FPG <90 or any value <70.
- Recheck creatinine/eGFR, blood ketone, electrolytes; if ketone <0.6 + eGFR ≥45 + eating well → restart dapagliflozin 10 mg qd (sick-day education).
- Oncology to choose and document alpelisib option (discontinue / 200 mg rechallenge / off-label 37.5 mg).
- Work up HR >100 (hemoglobin, infection, volume).
- If alpelisib stopped again → reduce insulin the **same day** (Toujeo → 10–12 U, halve/stop NovoRapid).

---

## 4. SOAP 精簡版（08/21 最新，無縮寫、可直接用）

**Subjective:** Alpelisib was resumed on August 14 at 150 milligrams once daily (off-label dose), stopped again on August 15 for recurrent Grade 3 hyperglycemia (fasting 305), and restarted on August 18 at one-quarter of a 150-milligram tablet (about 37.5 milligrams) once daily, continuing to date. Grade 1 nausea and Grade 1 fatigue. Eating adequately; no vomiting, abdominal pain, or hypoglycemia symptoms.

**Objective:** Heart rate 105, other vital signs stable, fully alert. Morning fasting glucose: 305 (August 15, on 150 milligrams) → 276 → 160 (August 17, off drug) → 164 (August 18, quarter-tablet started) → **134 → 133 → 158 (August 19–21, three consecutive days at or below 160)**. Daytime pre- and post-meal values 187–354, with dinner-time peaks 304–354. Current regimen since August 15: Toujeo 14 units once daily, insulin aspart 8 units before each meal, metformin 500 milligrams three times daily after meals (1500 milligrams per day). Glycated hemoglobin 7.8% (August 12). Repeat kidney function and blood ketone since August 12: not yet reported.

**Assessment:**
1. Alpelisib-associated hyperglycemia, second Grade 3 episode (August 15) after resumption at 150 milligrams; fasting glucose again fell within 2 days off drug. On the current combination (quarter-tablet alpelisib plus basal-bolus insulin plus metformin), **fasting glucose — the only value that drives dose decisions — has been at or below 160 for three consecutive days.** Residual dinner-time hyperglycemia 304–354 is an insulin-titration issue, not a trigger for anticancer-drug action.
2. **The unresolved issue is oncologic, not glycemic: 37.5 milligrams is outside the label.** The prescribing information permits only 300 → 250 → 200 milligrams, mandates permanent discontinuation if a dose below 200 is required, and prohibits splitting the film-coated tablets. No efficacy data exist for 150 or 37.5 milligrams. Per the label pathway, the second Grade 3 episode would have called for resumption at 200 milligrams.
3. Persistent sinus tachycardia (105) despite improved glucose — needs evaluation beyond hyperglycemia.
4. Kidney function and ketone reverification still outstanding; these gate both the metformin dose ceiling and any dapagliflozin restart.

**Plan:**
- **Oncology to choose and document one of three options:** (A) permanently discontinue alpelisib per label and reassess systemic therapy (fulvestrant continues); (B) rechallenge at 200 milligrams — the last on-label dose level, using whole tablets — under the current, stronger glycemic regimen (note: the August 14 failure at 150 milligrams occurred without prandial insulin and is not directly comparable), with glucose four times daily for 3 days and interruption if fasting glucose exceeds 250; or (C) knowingly continue 37.5 milligrams off-label with documentation that efficacy is unestablished and quarter-tablet dosing is imprecise.
- Continue Toujeo 14 units, insulin aspart 8 units three times daily, metformin 1500 milligrams per day. Titration: fasting above 160 on 2 consecutive days → Toujeo up 2 units; fasting below 90 or any value below 70 → Toujeo down 2 units; **dinner insulin aspart 8 → 10 units for the 304–354 evening peaks.**
- Recheck creatinine (estimated glomerular filtration rate), blood ketone, and electrolytes; if ketone below 0.6, intake stable, and estimated glomerular filtration rate 45 or above → restart dapagliflozin 10 milligrams once daily (insulin-independent mechanism; targets daytime values; sick-day education mandatory given ongoing Grade 1 nausea).
- Work up persistent heart rate above 100: hemoglobin, infection markers, volume status.
- If alpelisib is stopped again for any reason: reduce Toujeo to 10–12 units and halve or stop insulin aspart the same day; metformin last.
- Discharge planning: metformin at or below 2000 milligrams per day while estimated glomerular filtration rate is 45–59; home basal-insulin self-titration sheet; daily morning fasting self-monitoring with reporting of any value 160 or above; joint endocrinology–oncology follow-up; glycated hemoglobin target below 7.5%.

---

### 前一版本（08/14）

**Subjective:** Alpelisib held since August 11 for Grade 3 hyperglycemia. Feeling well, eating normally; no hypoglycemia symptoms, nausea, or vomiting.

**Objective:** Morning fasting glucose 255 (August 11) → 310 (August 12) → **125 (August 13) → 107 (August 14, still trending down)**; post-meal values 206–338, improving. **Glycated hemoglobin 7.8%.** Current regimen: Toujeo 12 units nightly since August 12; prandial insulin aspart stopped August 13; metformin 500 milligrams three times daily after meals restarted August 13; single 4-unit correction August 13, 21:00. Repeat kidney function and ketone after rehydration: to be confirmed.

**Assessment:**
1. Alpelisib-associated Grade 3 hyperglycemia — **fasting glucose reached target (160 or below) on day 2 to 3 of interruption, within the 3-to-5-day window; criteria met to resume alpelisib at 250 milligrams once daily.** With alpelisib still off and basal insulin unchanged, the immediate risk has shifted to **hypoglycemia** (fasting 107 and falling).
2. Glycated hemoglobin 7.8% — pre-existing suboptimal diabetes control, needs a long-term outpatient plan.
3. Residual postprandial hyperglycemia (206–318) after prandial insulin was stopped.
4. Kidney function and ketosis — reverify after volume repletion (metformin restarted at 1500 milligrams per day).

**Plan:**
- **Resume alpelisib at 250 milligrams once daily today** (coordinate with oncology); expect glucose to rise within 24 to 48 hours — keep Toujeo at 12 units through resumption; glucose four times daily for the first 3 days, then adjust by the morning fasting value.
- **If resumption is delayed for any reason: reduce Toujeo to 8–10 units tonight** to prevent overnight hypoglycemia.
- Confirm repeat creatinine (estimated glomerular filtration rate) and blood ketone before fixing metformin at 1500 milligrams per day; ceiling 2000 milligrams per day while estimated glomerular filtration rate is 45–59.
- After resumption, if pre-meal glucose stays above 250: re-add prandial insulin aspart or increase Toujeo; reassess dapagliflozin once ketone is below 0.6 and intake is stable.
- Daily morning fasting glucose for 2 weeks after resumption (this value drives all dose decisions); patient to report any fasting value 160 or above; if alpelisib is ever interrupted again, reduce insulin the same day.
- Long-term: target glycated hemoglobin below 7.5%; outpatient regimen metformin (2000 milligrams per day or less) with or without a sodium-glucose cotransporter 2 inhibitor and basal insulin; endocrinology follow-up.

---

### 前一版本（08/12）

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
