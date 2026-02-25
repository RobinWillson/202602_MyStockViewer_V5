# 14681414 - PriFutInterestStore (期貨簡易權益數庫存查詢)

## 1. 基本資訊 (Metadata)
- **Service ID**: `14681414 (20.104.20.20)`
- **COM Name**: `PriFutInterestStore`
- **設計描述**: 期貨簡易權益數庫存查詢
- **通訊模式**: `RQ/RP`
- **更新日期**: 2024/09/13

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "struFutAccountInfo": "",
    "abyType": "example",
    "abyCurrency": "example"
  }
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_In` : 帳號筆數Structure (Object)
  - `struFutAccountInfo` : 期貨帳號Structure (TPolaFut  Account, Size: 22)
    - *說明*: 總帳 / 總帳+子帳
  - `abyType` : 型態 (TByte, Size: 1)
    - *說明*: "1" : 基本幣別  "2" : 明細幣別
  - `abyCurrency` : 幣別 (TByte3, Size: 3)
    - `TWD`: 台幣
    - `USA`: 美金
    - `CNA`: 人民幣
    - `JPA`: 日圓

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "shtReplyCode": 0,
    "abyAdvisory": "example",
    "abyType": "example",
    "abyCurrency": "example",
    "lngEquity": 0,
    "lngAllFullIm": 0,
    "lngCanuseMargin": 0,
    "abyRiskRate": "example",
    "abyDaytradeRisk": "example",
    "abyAllRiskRate": "example",
    "lngCashForward": 0,
    "lngOpenGlYes": 0,
    "strucUpdateTime": "",
    "lngAccounting": 0,
    "lngFloatMargin": 0,
    "lngFloatPremium": 0,
    "lngCommissionAll": 0,
    "lngTotalValue": 0,
    "lngTaxRate": 0,
    "lngAllIm": 0,
    "lngCallMargin": 0,
    "lngGrantal": 0,
    "lngAllMm": 0,
    "lngOrderIm": 0,
    "lngPremium": 0,
    "lngOrderPremium": 0,
    "lngBalance": 0,
    "lngCanusePremium": 0,
    "lngCoveredOim": 0,
    "lngBondAmt": 0,
    "lngNobondAmt": 0,
    "lngBondMargin": 0,
    "lngCoveredIm": 0,
    "lngReduceIm": 0,
    "lngIncreaseIm": 0,
    "lngYTotalValue": 0,
    "lngRate": 0,
    "abyBestFlag": "",
    "lngGlToday": 0,
    "lngDspEquity": 0,
    "lngDspFloatmargin": 0,
    "lngDspFloatpremium": 0,
    "lngDspIM": 0,
    "lngDspRiskRate": 0,
    "uintCount": 1
  },
  "ChildStruct_Out": [
    {
      "struFutAccountInfo": "",
      "abyKind": "example",
      "abyTrid": "example",
      "abyID1": "example",
      "abyCommodity1": "example",
      "intSettlementMonth1": 0,
      "abyCP1": "example",
      "intStrikePrice1": 0,
      "intNetLotsB1": 0,
      "intNetLotsS1": 0,
      "byMarketNo1": "example",
      "abyStkCode1": "example",
      "abyStkName1": "example",
      "shtDecimal1": 0,
      "intBuyPrice1": 0,
      "intSellPrice1": 0,
      "intMarketPrice1": 0,
      "abyID2": "example",
      "abyCommodity2": "example",
      "intSettlementMonth2": 0,
      "abyCP2": "example",
      "intStrikePrice2": 0,
      "intNetLotsB2": 0,
      "intNetLotsS2": 0,
      "byMarketNo2": "example",
      "abyStkCode2": "example",
      "abyStkName2": "example",
      "shtDecimal2": 0,
      "intBuyPrice2": 0,
      "intSellPrice2": 0,
      "intMarketPrice2": 0
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_Out1` : 帳號權益Structure (Object)
  - `shtReplyCode` : 委託結果代碼 (Short, Size: 2)
    - `0`: 委託成功
    - `others`: 委託失敗
  - `abyAdvisory` : 錯誤說明 (TByte78
TByte120, Size: 78  120)
    - *說明*: 一般版:78
    - *說明*: UTF8版:120
  - `abyType` : 型態 (TByte, Size: 1)
    - *說明*: "1" : 基本幣別  "2" : 明細幣別
  - `abyCurrency` : 幣別 (TByte3, Size: 3)
    - `TWD`: 台幣
    - `USA`: 美金
    - `CNA`: 人民幣
    - `JPA`: 日圓
  - `lngEquity` : 權益數 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngAllFullIm` : 全額原始保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngCanuseMargin` : 可運用保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `abyRiskRate` : 權益比率 (Tbyte9, Size: 9)
  - `abyDaytradeRisk` : 當沖風險指標 (Tbyte9, Size: 9)
  - `abyAllRiskRate` : 風險指標 (Tbyte9, Size: 9)
  - `lngCashForward` : 前日餘額 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngOpenGlYes` : 昨日未平倉損益 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `strucUpdateTime` : 風險更新時間 (TPolaDateTime, Size: 9)
  - `lngAccounting` : 存/提 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngFloatMargin` : 未沖銷期貨浮動損益 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngFloatPremium` : 未沖銷買方選擇權市值 + 未沖銷賣方選擇權市值 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngCommissionAll` : 手續費 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngTotalValue` : 權益總值 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngTaxRate` : 期交稅 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngAllIm` : 原始保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngCallMargin` : 追繳保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngGrantal` : 本日期貨平倉損益淨額 + 到期履約損益 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngAllMm` : 維持保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngOrderIm` : 委託保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngPremium` : 權利金收入與支出 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngOrderPremium` : 委託權利金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngBalance` : 本日餘額 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngCanusePremium` : 可動用(出金)保證金(含抵委) (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngCoveredOim` : 委託抵繳保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngBondAmt` : 債券實物交割款 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngNobondAmt` : 債券實物不足交割款 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngBondMargin` : 債券待交割保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngCoveredIm` : 有價證券抵繳總額 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngReduceIm` : 期貨多空減收保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngIncreaseIm` : 加收保證金 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngYTotalValue` : 昨日權益總值 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngRate` : 匯率 (Long, Size: 8)
    - *說明*: 前端須除以1000000
  - `abyBestFlag` : 客戶保證金計收方式 (TBye, Size: 1)
    - *說明*: ' ': 傳統(策略)
    - *說明*: 'S':整戶風險(SPAN)  'Y':保證金最佳化
  - `lngGlToday` : 本日損益 (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngDspEquity` : [風險權益總值]{.mark} (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngDspFloatmargin` : [未沖銷期貨風險浮動損益]{.mark} (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngDspFloatpremium` : [未沖銷買方選擇權風險市值+未沖銷賣方選擇權風險市值]{.mark} (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngDspIM` : [風險原始保證金]{.mark} (Long, Size: 8)
    - *說明*: 前端須除以100
  - `lngDspRiskRate` : [盤後風險指標]{.mark} (Long, Size: 8)
    - *說明*: 前端須除以100
- `ParentStruct_Out2` : 帳號庫存Structure (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_Out2` : 帳號庫存Structure (Array of Objects)
  - `struFutAccountInfo` : 期貨帳號Structure (TPolaFut  Account, Size: 22)
    - *說明*: 總帳 / 總帳+子帳
  - `abyKind` : 期權別 (TByte3, Size: 3)
    - `F`: 期貨  O : 單式選擇權  OF : 期權組合  OO : 複式選擇權
  - `abyTrid` : 商品代碼 (TByte21, Size: 21)
    - *說明*: TX109100E4/TXO09000E4
  - `abyID1` : 商品組合代碼-單腳1 (TByte12, Size: 12)
    - *說明*: TXO09600I6  或TXO08600I6
  - `abyCommodity1` : 商品代碼1 (TByte6, Size: 6)
    - *說明*: 例：FITX
  - `intSettlementMonth1` : 商品月份1 (Int, Size: 4)
    - *說明*: 例：201612
  - `abyCP1` : 買賣權 (TByte, Size: 1)
    - `F`: 期貨  C : CALL  P : PUT
  - `intStrikePrice1` : 履約價1 (Int, Size: 4)
    - *說明*: 前端需除以10000
  - `intNetLotsB1` : 留倉總買1 (Int, Size: 4)
  - `intNetLotsS1` : 留倉總賣1 (Int, Size: 4)
  - `byMarketNo1` : 市場代碼1 (byte)
  - `abyStkCode1` : 行情報價代碼1 (TByte12)
    - `Ex`: 7799
  - `abyStkName1` : 股票名稱1 (TByte20
TByte30, Size: 20
30)
    - `Ex`: '中鋼實 06 0030 C', '台指01', ' 櫃指選 03 00400 C'  一般版 : 20
    - `UTF8`: 30
  - `shtDecimal1` : 小數位數1 (Short, Size: 2)
    - *說明*: +為小數位數,-為分數分母, 0為整數
  - `intBuyPrice1` : 買入價1 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `intSellPrice1` : 賣出價1 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `intMarketPrice1` : 市價1 (int, Size: 4)
    - *說明*: 盤前市價若為0 則給開盤參考價  前端需除以1000
  - `abyID2` : 商品組合代碼-單腳2 (TByte12, Size: 12)
    - *說明*: TXO09600I6  或TXO08600I6
  - `abyCommodity2` : 商品代碼2 (TByte6, Size: 6)
    - *說明*: 例：FITX
  - `intSettlementMonth2` : 商品月份2 (Int, Size: 4)
    - *說明*: 例：201612
  - `abyCP2` : 買賣權2 (TByte, Size: 1)
    - `F`: 期貨  C : CALL  P : PUT
  - `intStrikePrice2` : 履約價2 (Int, Size: 4)
    - *說明*: 前端需除以10000
  - `intNetLotsB2` : 留倉總買2 (Int, Size: 4)
  - `intNetLotsS2` : 留倉總賣2 (Int, Size: 4)
  - `byMarketNo2` : 市場代碼2 (byte)
  - `abyStkCode2` : 行情報價代碼2 (TByte12)
    - `Ex`: 7799
  - `abyStkName2` : 股票名稱2 (TByte20
TByte30, Size: 20
30)
    - `Ex`: '中鋼實 06 0030 C', '台指01', ' 櫃指選 03 00400 C'
    - *說明*: 一般版 : 20
    - `UTF8`: 30
  - `shtDecimal2` : 小數位數2 (Short, Size: 2)
    - *說明*: +為小數位數,-為分數分母, 0為整數
  - `intBuyPrice2` : 買入價2 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `intSellPrice2` : 賣出價2 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `intMarketPrice2` : 市價2 (int, Size: 4)
    - *說明*: 盤前市價若為0 則給開盤參考價  前端需除以1000

---
