# 1467140D - PolaStoFutStoreClassifyIII (期貨庫存總表III (含複式單明細))

## 1. 基本資訊 (Metadata)
- **Service ID**: `1467140D (20.103.20.13)`
- **COM Name**: `PolaStoFutStoreClassifyIII`
- **設計描述**: 期貨庫存總表III (含複式單明細)
- **通訊模式**: `RQ/RP`
- **更新日期**: 2024/08/14

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
      "struFutAccountInfo": ""
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_In` : 輸入的母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)
    - *說明*: #

- `ChildStruct_In` : 輸入的子結構 (Array of Objects)
  - `struFutAccountInfo` : 期貨帳號 (TPolaFutAccount, Size: 22)

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "uintCount": 1
  },
  "ChildStruct_Out": [
    {
      "struFutAccountInfo": "",
      "abyKind": "example",
      "abyTrid": "example",
      "abyBS": "example",
      "intQty": 0,
      "lngAmt": 0,
      "intFee": 0,
      "intTax": 0,
      "abyCurrencyType": "example",
      "abyDayTradeID": "example",
      "abyCommodityID1": "example",
      "abyCallPut1": "example",
      "intSettlementMonth1": 0,
      "intStrikePrice1": 0,
      "abyBS1": "example",
      "abyStkName1": "example",
      "byMarketNo1": "example",
      "abyStkCode1": "example",
      "abyCommodityID2": "example",
      "abyCallPut2": "example",
      "intSettlementMonth2": 0,
      "intStrikePrice2": 0,
      "abyBS2": "example",
      "abyStkName2": "example",
      "byMarketNo2": "example",
      "abyStkCode2": "example",
      "intBuyPrice1": 0,
      "intSellPrice1": 0,
      "intMarketPrice1": 0,
      "intBuyPrice2": 0,
      "intSellPrice2": 0,
      "intMarketPrice2": 0,
      "shtDecimal": 0,
      "abyProductType1": "example",
      "abyProductKind1": "example",
      "abyProductType2": "example",
      "abyProductKind2": "example",
      "intUpStopPrice1": 0,
      "intDownStopPrice1": 0,
      "intUpStopPrice2": 0,
      "intDownStopPrice2": 0,
      "abyStkCode1opp": "example",
      "abyStkCode2opp": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_Out` : 輸出的母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)
    - *說明*: #

- `ChildStruct_Out` : 輸出的子結構 (Array of Objects)
  - `struFutAccountInfo` : 期貨帳號 (TPolaFutAccount, Size: 22)
  - `abyKind` : 委託種類 (TByte, Size: 1)
    - *說明*: 期貨(F)/選擇權(O)/期貨+選擇權(C)
  - `abyTrid` : 商品代碼 (TByte21, Size: 21)
    - *說明*: TX109100E4/TXO09000E4
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - *說明*: 買(B)/賣(S)
  - `intQty` : 未平倉口數 (Int, Size: 4)
  - `lngAmt` : 總成交點數 (Long, Size: 8)
    - *說明*: 前端需除以10000
  - `intFee` : 手續費 (Int, Size: 4)
    - *說明*: 前端需除以100
  - `intTax` : 交易稅 (Int, Size: 4)
    - *說明*: 前端需除以100
  - `abyCurrencyType` : 幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
  - `abyDayTradeID` : 當沖註記 (TByte, Size: 1)
    - *說明*: "Y":當沖 " ":空白
  - `abyCommodityID1` : 商品名稱1 (TByte6, Size: 6)
    - *說明*: TXO
  - `abyCallPut1` : 買賣權1 (TByte, Size: 1)
    - *說明*: C/P
  - `intSettlementMonth1` : 交易月份1 (Int, Size: 4)
    - *說明*: 200712
  - `intStrikePrice1` : 履約價1 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyBS1` : 買賣別1 (TByte, Size: 1)
    - *說明*: 買(B)/賣(S)
  - `abyStkName1` : 股票名稱1 (TByte20, Size: 20)
    - `Ex`: '中鋼實 06 0030 C', '台指01', ' 櫃指選 03 00400 C'
  - `byMarketNo1` : 市場代碼1 (Byte, Size: 1)
    - *說明*: 3
  - `abyStkCode1` : 行情報價代碼1 (TByte12, Size: 12)
    - *說明*: 7799,TXO04600A9
  - `abyCommodityID2` : 商品名稱2 (TByte6, Size: 6)
    - *說明*: TXO
  - `abyCallPut2` : 買賣權2 (TByte, Size: 1)
    - *說明*: C/P
  - `intSettlementMonth2` : 交易月份2 (Int, Size: 4)
    - *說明*: 200712
  - `intStrikePrice2` : 履約價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyBS2` : 買賣別2 (TByte, Size: 1)
    - *說明*: 買(B)/賣(S)
  - `abyStkName2` : 股票名稱2 (TByte20, Size: 20)
    - `Ex`: '中鋼實 06 0030 C', '台指01', ' 櫃指選 03 00400 C'
  - `byMarketNo2` : 市場代碼2 (Byte, Size: 1)
    - *說明*: 3
  - `abyStkCode2` : 行情報價代碼2 (TByte12, Size: 12)
    - *說明*: 7799,TXO04700A9
  - `intBuyPrice1` : 買入價1 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intSellPrice1` : 賣出價1 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intMarketPrice1` : 市價1 (int, Size: 4)
    - *說明*: 盤前市價若為0 則給開盤參考價
  - `intBuyPrice2` : 買入價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intSellPrice2` : 賣出價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intMarketPrice2` : 市價2 (int, Size: 4)
    - *說明*: 盤前市價若為0 則給開盤參考價
  - `shtDecimal` : 小數位數 (Short, Size: 2)
    - *說明*: # +為小數位數,-為分數分母,  # 0為整數
  - `abyProductType1` : 商品類別1 (TByte, Size: 1)
    - *說明*: "F":期貨 "O":選擇權
  - `abyProductKind1` : 商品屬性1 (TByte, Size: 1)
    - *說明*: "I":指數 "R":利率 "B":債券  "C":商品 "S":股票
  - `abyProductType2` : 商品類別2 (TByte, Size: 1)
    - *說明*: "F":期貨 "O":選擇權
  - `abyProductKind2` : 商品屬性2 (TByte, Size: 1)
    - *說明*: "I":指數 "R":利率 "B":債券  "C":商品 "S":股票
  - `intUpStopPrice1` : 漲停價1 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intDownStopPrice1` : 跌停價1 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `intUpStopPrice2` : 漲停價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intDownStopPrice2` : 跌停價2 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyStkCode1opp` : 行情股票代碼1反向 (TByte12, Size: 12)
    - *說明*: \<第1支腳\>
  - `abyStkCode2opp` : 行情股票代碼2反向 (TByte12, Size: 12)
    - *說明*: \<第2支腳\>

---
