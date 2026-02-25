# SendFutureCombined - OdrFutCombined (期貨複式單組合函數)

## 1. 基本資訊 (Metadata)
- **Service ID**: `期貨複式單組合函數` (SendFutureCombined)
- **COM Name**: `OdrFutCombined`
- **設計描述**: API SendFutureCombined
- **通訊模式**: `Odr`
- **更新日期**: 2025/01/03

---

## 2. 請求結構 (Request Specification)

### 2.1 JSON 結構範例
```json
{
  "LoginAcno": "FF021000P001234567",
  "lstDepositOptimum": [
    {
      "byStrategyID": 6,
      "struFutAccountInfo": "FF021000P001234567",
      "shtQty": 1,
      "abyBuySell1": "B",
      "abyBuySell2": "S",
      "intDealPrice1": 100,
      "intDealPrice2": 150,
      "shtDecimal1": 0,
      "intCurrentIM1": 1000,
      "intCurrentIM2": 1000,
      "intSaveIM": 500,
      "abyCommodityID1": "TXO",
      "abyCallPut1": "C",
      "intSettlementMonth1": 202502,
      "intStrikePrice1": 22800,
      "abyStkName1": "台指選 02 22800 P",
      "abyCommodityID2": "TXO",
      "abyCallPut2": "P",
      "intSettlementMonth2": 202502,
      "intStrikePrice2": 23000,
      "abyStkName2": "台指選 02 23000 P"
    }
  ]
}
```

### 2.2 參數說明 (Parameter Details)

- `LoginAcno` : 帳號 (string)
  - *說明*: 期貨帳號：FF021000P001234567
- `lstDepositOptimum` : 組合物件清單 (Array of Objects / `List<DepositOptimum>`)
  - *說明*: 建議由保證金最佳化查詢結果篩選代入。包含以下欄位：
  - `byStrategyID` : 策略ID (Byte)
    - `6`: 買賣權混合部位(跨式,勒式)
    - `7`: 多頭價差
    - `8`: Put空頭價差
    - `9`: 溫跌作莊
    - `10`: 溫漲作莊
    - `11`: Call時間價差
    - `12`: Put時間價差
  - `struFutAccountInfo` : 期貨帳號 (string)
  - `shtQty` : 口數 (Short)
  - `abyBuySell1` : 買賣別1 (string)
    - *備註*: B, S
  - `abyBuySell2` : 買賣別2 (string)
    - *備註*: B, S
  - `intDealPrice1` : 成交價1 (Int)
  - `intDealPrice2` : 成交價2 (Int)
  - `shtDecimal1` : 小數位數1 (Short)
    - *說明*: `+`為小數位數, `-`為分數分母, `0`為整數
  - `intCurrentIM1` : 商品一保證金 (Int)
  - `intCurrentIM2` : 商品二保證金 (Int)
  - `intSaveIM` : 可節省保證金 (Int)
  - `abyCommodityID1` : 商品ID1 (string)
    - *範例*: TXO
  - `abyCallPut1` : 買賣權1 (string)
    - *範例*: C/P
  - `intSettlementMonth1` : 商品年月1 (Int)
    - *範例*: 202502
  - `intStrikePrice1` : 履約價1 (Int)
  - `abyStkName1` : 商品名稱1 (string)
    - *範例*: 台指選 02 22800 P
  - `abyCommodityID2` : 商品ID2 (string)
    - *範例*: TXO
  - `abyCallPut2` : 買賣權2 (string)
    - *範例*: C/P
  - `intSettlementMonth2` : 商品年月2 (Int)
    - *範例*: 202502
  - `intStrikePrice2` : 履約價2 (Int)
  - `abyStkName2` : 商品名稱2 (string)
    - *範例*: 台指選 02 23000 P

---

## 3. 回傳結構 (Response Specification)

### 3.1 JSON 結構範例
```json
{
  "OrderStatus": {
    "OrderResultCount": {
      "MsgCode": "0000",
      "MsgContent": "成功",
      "Count": 1
    },
    "OrderResultMesgList": [
      {
        "Identify": 123,
        "ReplyCode": 0,
        "OrderNO": "Ord001",
        "TradeDate": "20250103",
        "ErrType": "",
        "ErrNO": "",
        "Advisory": ""
      }
    ]
  }
}
```

### 3.2 參數說明 (Parameter Details)

- `OrderStatus` : 下單結果物件 (Object)
  - `OrderResultCount` : 下單結果筆數 (Object)
    - `MsgCode` : 訊息代碼 (string)
    - `MsgContent` : 訊息內容 (string)
    - `Count` : 筆數 (Int)
  - `OrderResultMesgList` : 下單明細清單 (Array of Objects / `List<OrderResultMesg>`)
    - `Identify` : 識別碼 (int)
    - `ReplyCode` : 委託結果代碼 (int)
      - `0`: 委託成功
      - `others`: 委託失敗
    - `OrderNO` : 委託書編號 (string)
      - *備註*: 未使用
    - `TradeDate` : 交易日期 (string)
      - *備註*: 未使用
    - `ErrType` : 錯誤類別 (string)
    - `ErrNO` : 錯誤代號 (string)
    - `Advisory` : 錯誤說明 (string)
