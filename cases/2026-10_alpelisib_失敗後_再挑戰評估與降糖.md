# 案例討論（續）：Alpelisib 因高血糖失敗後，能否再試？（2026-10）

> 去識別化案例（已移除病歷號、醫師姓名、確切年齡與歷年治療日期），供教學與 protocol 對照使用。依據：`PROTOCOL.md`（§1.1、§3、§4.1、§7、附錄 C）。**非個別醫療指示，劑量決策由主治團隊確認。**
>
> **連續性說明**：本例的腫瘤特徵、共病、用藥與 `2026-08_alpelisib_T2DM_hyperglycemia.md` 高度吻合（左乳 IDC stage IV、ER/PR 100%＋/HER2−、T2DM＋高血壓、Exforge、alpelisib），**疑似同一病人**；以下判讀以此為前提，**請臨床端確認**。若確為同一人，08 月的兩次 Grade 3 與酮症事件即為本次評估的關鍵既往史。

---

## 1. 病例摘要（2026-10-01～10-06）

- 60 多歲女性；左乳 invasive ductal carcinoma，stage IV（骨、肝、淋巴結轉移），Luminal A，**PIK3CA H1047R**（NGS）；ECOG 0
- 治療史（略）：CDK4/6i、aromatase inhibitor、fulvestrant、everolimus 核准、多線化療；2026-07 因 PD 改 **alpelisib（Piqray）＋ fulvestrant**（健保核准）
- 2026-10-01：病歷記載「alpelisib 後血糖持續偏高，擬改 **Truqap（capivasertib）**」
- 2026-10-05 PET：全身代謝性疾病進展；**肝 S5 新轉移**，其餘穩定；醫囑「arrange try PIK3CA again」，並照會代謝科：**能否再用 Piqray？血糖如何控制？**
- 共病：T2DM、高血壓（Exforge）；鼻竇炎（Augmentin 1000 mg BID）
- 生命徵象：BT 36.8、**HR 107**、RR 18、BP 115/59；GCS E4V5M6
- 目前降糖：Glucophage 1# BID（單位劑量未註明）＋ **Qtern**（dapagliflozin＋saxagliptin）QD；Care Plan 另寫 **Xigduo**＋Glucophage
- 檢驗：**HbA1c 8.00%**（10/01）；Hb 9.6、WBC 7.4、PLT 323；**本次未見 creatinine／eGFR／血酮**

### 病房血糖機（mg/dL，AC）

| 日期 | 晨間（FPG 替代） | 分級 | 晚餐前 |
|---|---|---|---|
| 10/01 | （檢驗室 Glucose 193，09:28，空腹與否未註明，不分級）| — | 187 |
| 10/02 | **211** | G2（>160–250）| 182 |
| 10/03 | **174** | G2 | 201 |
| 10/04 | **141** | G1（≤160）| 211 |
| 10/05 | **172** | G2 | 136 |
| 10/06 | **138** | G1 | — |

---

## 2. 判讀

1. **趨勢改善但未穩定**：晨間 211 → 138，但 10/05 彈回 172；**晚餐前值（182–211）高於晨間**，問題在日間而非空腹。
2. **HbA1c 軌跡**：7.3（08/07）→ 7.8（08/12）→ **8.00（10/01）**；涵蓋 alpelisib 暴露期，無法拆分藥物與基礎 T2DM 的貢獻，但 08/12 已顯示「基礎控制本就未達標」。
3. **處方不一致（再度出現）**：Qtern 已含 dapagliflozin；Xigduo 亦含 dapagliflozin＋metformin。若並存 → dapagliflozin 重複、metformin 總量不明。須核對 MAR。
4. **安全警訊**：HR 107＋感染（鼻竇炎）＋IV 輸液＋SGLT2i 在用；08 月曾有血酮 0.9＋代謝性酸中毒。血糖不高不能排除酮酸中毒【L3／L4：PROTOCOL §3.4】。

---

## 3. 能否再試 alpelisib

### 3-1. 腫瘤端：符合適應症，但這不是瓶頸

HR+/HER2−、PIK3CA 突變、內分泌治療後進展、搭配 fulvestrant，且已核准。

### 3-2. 血糖端：**不建議再用**（以下以「確為同一病人」為前提）

| 項目 | 依據 |
|---|---|
| 已確診 T2DM、**HbA1c 8.0%** | HbA1c ≥6.5% 達標前不應起始；≥8.0% 未經內分泌照會即起始屬 inappropriate，且此族群無前瞻安全性資料【L3：Delphi；PROTOCOL §1.1】 |
| **08 月已兩次 Grade 3**（FPG 255、305）＋血酮 0.9 與代謝性酸中毒 | rechallenge 後高血糖來得極快（個案：24 小時內），須先問「該不該」復用【L4；§7.2 第 1–2 點】 |
| **150 mg 時已再度 G3** | 仿單減量階梯止於 200 mg，**<200 mg 即永久停藥**；37.5 mg 為仿單外劑量【L1；§4.1、§7.1】。能合規使用的最低劑量是 200 mg，而更低劑量已失敗 |
| 10/01 前後「持續高血糖」 | 08/21 後至 10/01 的劑量與 FPG 紀錄**本回顧未取得可驗證來源** |

**結論**：若腫瘤科仍堅持再試，須同時滿足：①補齊 08/21 後的劑量與血糖紀錄；②內分泌重整降糖並**穩定達標**（參考治療目標餐前 90–130、HbA1c <7.5%【L3，§8】；**既有 T2DM 且 HbA1c 8% 時復用前的具體門檻，本回顧未取得可驗證來源**）；③住院＋CGM、驗酮監測、降階（不可高於前次失敗劑量）；④病人與家屬知情同意（兩次 G3 加酮症史）。

### 3-3. 替代路徑：Truqap（capivasertib）

- 高血糖強度較低（G≥3 約 2.3% vs alpelisib 36.6%，**跨試驗間接比較，不可直接相減**）；4-on/3-off，監測落在**用藥週第 3–4 天**【L3：附錄 C】。
- **與目前處方衝突**：附錄 C 建議避免促泌劑與 GLP-1RA／**DPP-4i**，而 Qtern 含 saxagliptin（DPP-4i）【L3：Iyengar 2025】。此條**不適用 alpelisib**，不可互套。
- 既有 T2DM／HbA1c 8% 在 capivasertib 的資格與預防建議：**本回顧未取得可驗證來源**（附錄 C 僅涵蓋預防性 metformin 於高風險者）。

---

## 4. 降糖建議（交內分泌科決定）

1. **先釐清處方**：Qtern／Xigduo／Glucophage 去重，算出 metformin 與 dapagliflozin 的實際總量。
2. **補檢驗**：creatinine／eGFR（08/12 為 48–51，C-G 41）、**β-OHB**、電解質。eGFR 45–59 時 metformin 上限 ≤2000 mg/day；30–44 不得新起始【L3；§3.2】。
3. **SGLT2i 安全清單**（§3.4）：進食足夠、無嘔吐腹瀉脫水、血酮 <0.6；生病日（無法進食）當日停用。
4. **metformin**：eGFR 允許時優先 XR 並依耐受加至 ≤2000 mg/day。
5. **日間／晚餐後高血糖**：metformin 與 SGLT2i 調整後仍餐前 >180，考慮 basal insulin（§5.2–5.3）；若預計用 PI3Ki／AKTi，pioglitazone 起效需 6 週，不能用於急性期【L3】。避免 sulfonylurea。
6. **目標**：ECOG 0 → HbA1c <7.5%、餐前 90–130；若判定餘命有限 → HbA1c <8.5%、餐前 100–180【L3；§8】。
7. **監測**：每日晨間空腹 SMBG，>160 回報；改 capivasertib 時另依 4-on/3-off 加驗用藥週第 3–4 天。

---

## 5. 待補資料

- 08/21 以後 alpelisib 實際劑量、停藥日、期間最高 FPG 與是否驗酮
- creatinine／eGFR、血酮、電解質（10/01 之後）
- Glucophage 單位劑量、Qtern／Xigduo 實際處方
- 08 月案例與本例是否同一病人
- 腫瘤科對 PET 進展後的下一線決定（Truqap vs 再試 PIK3CA）

---

## 6. 教學重點

1. **失敗史決定再挑戰資格**：兩次 G3＋酮症史，比當下單日血糖更重要。
2. **仿單劑量下限**：alpelisib 200 mg 以下即終局，「更低劑量續用」屬仿單外且已有失敗證據。
3. **AKTi 不是 PI3Kαi 的複製**：降糖藥避免清單不同（DPP-4i），處方要跟著換。
4. **處方重複是反覆發生的系統問題**：複方（Qtern、Xigduo）與單方並存。
