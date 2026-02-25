# 14670016 - StoStoreSummaryGroupIX (股票庫存綜合總表IX)

## 1. 基本資訊 (Metadata)
- **Service ID**: `14670016 (20.103.0.22)`
- **COM Name**: `StoStoreSummaryGroupIX`
- **設計描述**: 股票庫存綜合總表IX
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/09/22

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "uintCount": 1
  },
  "ChildStruct_In": [
    {
      "abyAccount": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_In` : 輸入的母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)
    - *說明*: #

- `ChildStruct_In` : 輸入的子結構 (Array of Objects)
  - `abyAccount` : 現貨帳號 (TByte22, Size: 22)

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "uintCount1": 0,
    "uintCount2": 0
  },
  "ChildStruct_Out": [
    {
      "abyAccount": "example",
      "shtTradeKind": 0,
      "byMarketNo": "example",
      "abyMarketName": "example",
      "abyStkCode": "example",
      "abyStkName": "example",
      "lngStockNos": 0,
      "lngPrice": 0,
      "lngCost": 0,
      "lngInterest": 0,
      "intBuyNotInNos": 0,
      "intSellNotInNos": 0,
      "lngCanOrderQty": 0,
      "lngLoan": 0,
      "intTaxRate": 0,
      "uintLotSize": 0,
      "intMarketPrice": 0,
      "shtDecimal": 0,
      "byStkType1": "example",
      "byStkType2": "example",
      "intBuyPrice": 0,
      "intSellPrice": 0,
      "intUpStopPrice": 0,
      "intDownStopPrice": 0,
      "uintPriceMultiplier": 0,
      "abyTradeCurrency": "example",
      "lngCDQTY": 0,
      "lngCanOrderOddQty": 0,
      "abyCurrencyType": "example",
      "abyStkFullName": "example",
      "lngStockQty": 0,
      "lngTradingQty": 0,
      "intCloseRate": 0,
      "byRateKind": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct1_Out` : 輸出的母結構1 (Object)
  - `uintCount1` : 現貨庫存筆數 (Uint, Size: 4)
    - *說明*: # 現貨庫存總表

- `ChildStruct1_Out` : 輸出的子結構1 (Array of Objects)
  - `abyAccount` : 現貨帳號 (TByte22, Size: 22)
    - *說明*: #
  - `shtTradeKind` : 交易種類 (short, Size: 2)
    - *說明*: #
    - `0`: 現股  #
    - `3`: 資買  #
    - `4`: 券賣  #
    - `6`: 借券
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
    - *說明*: #
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
    - *說明*: # 上市/上櫃  #
    - `Max`: 10個中文
  - `abyStkCode` : 股票代號 (TByte12, Size: 12)
    - *說明*: #
  - `abyStkName` : 股票名稱 (TByte30, Size: 30)
    - *說明*: #
    - `Max`: 10個中文
  - `lngStockNos` : 股數 (Long, Size: 8)
    - *說明*: #
  - `lngPrice` : 成交均價 (Long, Size: 8)
    - *說明*: # 前端需除以10000
  - `lngCost` : 持有成本 (Long, Size: 8)
    - *說明*: #
  - `lngInterest` : 預估利息 (Long, Size: 8)
    - *說明*: #
  - `intBuyNotInNos` : 買進未入帳股數 (Int, Size: 4)
    - *說明*: #
  - `intSellNotInNos` : 賣出未入帳股數 (Int, Size: 4)
    - *說明*: #
  - `lngCanOrderQty` : 今日可下單股數 (Long, Size: 8)
    - *說明*: #
  - `lngLoan` : 資保證金/券擔保價品 (Long, Size: 8)
    - *說明*: #
  - `intTaxRate` : 交易稅率 (Int, Size: 4)
    - *說明*: # 前端需除以1000  #
    - `0`: Reits 股票  #
    - `1`: 基金,認股權證,債券,存託憑證  #
    - `3`: 一般股票 (單位千分之一)
  - `uintLotSize` : 交易單位 (uint, Size: 4)
    - *說明*: # 每手股數
  - `intMarketPrice` : 市價 (int, Size: 4)
    - *說明*: # 盤前市價若為0則給開盤參考價  前端需除以10000
  - `shtDecimal` : 小數位數 (Short, Size: 2)
    - *說明*: # +為小數位數  # -為分數分母  # 0為整數
  - `byStkType1` : 屬性1 (Byte, Size: 1)
    - *說明*: # Bit
    - `1`: 管理商品  # Bit
    - `2`: 交易記號  # Bit
    - `3`: 受益憑證  # Bit
    - `4`: ETF商品  # Bit
    - `5`: 權證記號  # Bit
    - `6`: 特別股  # Bit
    - `7`: 存託憑證  # Bit
    - `8`: 外國股票
  - `byStkType2` : 屬性2 (Byte, Size: 1)
    - *說明*: # Bit
    - `1`: 可轉換公司債  # Bit
    - `2`: 附認股權公司債  # Bit
    - `3`: 警示股  # Bit
    - `4`: 指數記號  # Bit
    - `5`: 期貨  # Bit
    - `6`: 個股選擇權  # Bit
    - `7`: 指數選擇權  # Bit
    - `8`: 保留
  - `intBuyPrice` : 買價 (Int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intSellPrice` : 賣價 (Int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intUpStopPrice` : 漲停價 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intDownStopPrice` : 跌停價 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `uintPriceMultiplier` : 計價倍數 (uint, Size: 4)
    - *說明*: # 1，乘1倍  # 10，乘10倍
  - `abyTradeCurrency` : 報價幣別 (TByte3, Size: 3)
    - *說明*: # TWD  # CNY  # HKD  # USD
  - `lngCDQTY` : 借貸股數 (Long, Size: 8)
    - *說明*: #
  - `lngCanOrderOddQty` : 零股可下單股數 (Long, Size: 8)
    - *說明*: #
- `ParentStruct2_Out` : 輸出的母結構2 (Object)
  - `uintCount2` : 國外股票庫存筆數 (Uint, Size: 4)
    - *說明*: # 國外股票庫存總表

- `ChildStruct2_Out` : 輸出的子結構2 (Array of Objects)
  - `abyAccount` : 現貨帳號 (TByte22, Size: 22)
    - *說明*: #
  - `abyCurrencyType` : 幣別 (TByte3, Size: 3)
    - *說明*: #
    - `USD`: 美元  #
    - `HKD`: 港幣
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
    - *說明*: #
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
    - *說明*: #
    - `Max`: 10個中文
  - `abyStkCode` : 股票代號 (TByte12, Size: 12)
    - *說明*: #
  - `abyStkName` : 股票名稱 (TByte30, Size: 30)
    - *說明*: #
    - `Max`: 10個中文
  - `abyStkFullName` : 股票全名 (TByte60, Size: 60)
    - *說明*: #
    - `Max`: 20個中文
  - `lngStockQty` : 庫存股數 (Long, Size: 8)
    - *說明*: #
  - `lngTradingQty` : 可交易股數 (Long, Size: 8)
    - *說明*: #
  - `lngPrice` : 成交均價 (Long, Size: 8)
    - *說明*: # 前端需除以1000
  - `lngCost` : 持有成本 (Long, Size: 8)
    - *說明*: # 前端需除以1000
  - `intCloseRate` : 匯率 (Int, Size: 4)
    - *說明*: # 前端需除以10000
  - `byRateKind` : 匯率運算模式 (Byte, Size: 1)
    - *說明*: #
    - `1`: 除以匯率  #
    - `2`: 乘以匯率
  - `uintLotSize` : 交易單位 (uint, Size: 4)
    - *說明*: # 每手股數
  - `intMarketPrice` : 市價 (int, Size: 4)
    - *說明*: # 固定為0,前端自行根據登入權限查詢
  - `shtDecimal` : 小數位數 (Short, Size: 2)
    - *說明*: # +為小數位數  # -為分數分母  # 0為整數
  - `intBuyPrice` : 買價 (Int, Size: 4)
    - *說明*: #
  - `intSellPrice` : 賣價 (Int, Size: 4)
    - *說明*: #

---
