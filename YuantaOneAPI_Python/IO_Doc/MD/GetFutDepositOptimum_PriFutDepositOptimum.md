# GetFutDepositOptimum - PriFutDepositOptimum (查詢期貨保證金最佳化函數)

## 1. 基本資訊 (Metadata)
- **Service ID**: `查詢期貨保證金最佳化函數`
- **COM Name**: `PriFutDepositOptimum`
- **設計描述**: API GetFutDepositOptimum
- **通訊模式**: `RQ/RP` (Request / Response)
- **更新日期**: 2025/01/03

---

## 2. 請求結構 (Request Specification)

### 2.1 JSON 結構範例
```json
{
  "Account": "FF021000P001234567"
}
```

### 2.2 參數說明 (Parameter Details)

- `Account` : 帳號 (string)
  - *說明*: 期貨帳號：FF021000P001234567

---

## 3. 回傳結構 (Response Specification)

*說明：本 API 直接回傳 `List<DepositOptimum>` 陣列，而非區分 ParentStruct 與 ChildStruct。*

### 3.1 JSON 結構範例
```json
[
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
```

### 3.2 參數說明 (Parameter Details)

- `DepositOptimum` : 期貨保證金最佳化物件 (Array of Objects)
  - `byStrategyID` : 策略ID (Byte)
    - `6`: 買賣權混合部位 (跨式,勒式)
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
