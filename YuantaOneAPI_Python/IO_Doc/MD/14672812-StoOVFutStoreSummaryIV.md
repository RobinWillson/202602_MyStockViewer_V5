# 14672812 - StoOVFutStoreSummaryIV (國際期貨庫存總表IV)

## 1. 基本資訊 (Metadata)
- **Service ID**: `14672812 (20.103.40.18)`
- **COM Name**: `StoOVFutStoreSummaryIV`
- **設計描述**: 國際期貨庫存總表IV
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
      "abyCommodityID1": "example",
      "abyCallPut1": "example",
      "intSettlementMonth1": 0,
      "abyProductCName1": "example",
      "intStrikePrice1": 0,
      "abyCommodityID2": "example",
      "abyCallPut2": "example",
      "intSettlementMonth2": 0,
      "abyProductCName2": "example",
      "intStrikePrice2": 0,
      "intFee": 0,
      "abyCurrencyType": "example",
      "abyDayTradeID": "example",
      "abyBS1": "example",
      "abyBS2": "example",
      "abyOptProdKind1": "example",
      "abyOptProdKind2": "example",
      "byMarketNo1": "example",
      "abyStkCode1": "example",
      "byMarketNo2": "example",
      "abyStkCode2": "example",
      "intBuyPrice1": 0,
      "intSellPrice1": 0,
      "intMarketPrice1": 0,
      "intBuyPrice2": 0,
      "intSellPrice2": 0,
      "intMarketPrice2": 0,
      "shtDecimal": 0,
      "uintTickDiff": ""
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
    - *說明*: 期貨(F)/選擇權(O)
  - `abyTrid` : 商品代碼 (TByte20, Size: 20)
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - *說明*: 買(B)/賣(S)
  - `intQty` : 未平倉口數 (Int, Size: 4)
  - `lngAmt` : 總成交點數 (Long, Size: 8)
    - *說明*: 前端需除以100000000
  - `abyCommodityID1` : 商品名稱1 (TByte6, Size: 6)
    - *說明*: EC, URO
  - `abyCallPut1` : 買賣權1 (TByte, Size: 1)
    - *說明*: C/P
  - `intSettlementMonth1` : 交易月份1 (Int, Size: 4)
    - *說明*: 201101
  - `abyProductCName1` : 商品中文名稱1 (TByte18, Size: 18)
    - `Max`: 6個中文  歐元,
  - `intStrikePrice1` : 履約價1 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyCommodityID2` : 商品名稱2 (TByte6, Size: 6)
    - *說明*: EC
  - `abyCallPut2` : 買賣權2 (TByte, Size: 1)
    - *說明*: C/P
  - `intSettlementMonth2` : 交易月份2 (Int, Size: 4)
    - *說明*: 201101
  - `abyProductCName2` : 商品中文名稱2 (TByte18, Size: 18)
    - `Max`: 6個中文  歐元,
  - `intStrikePrice2` : 履約價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `intFee` : 手續費 (Int, Size: 4)
    - *說明*: 前端需除以100
  - `abyCurrencyType` : 幣別 (TByte3, Size: 3)
    - *說明*: AUD澳幣,EUR歐元,GBP英鎊,HKD港幣,JPY日幣,NTD新台幣,SGD新加坡幣,USD美金
  - `abyDayTradeID` : 當沖註記 (TByte, Size: 1)
    - *說明*: "Y":當沖 " ":空白
  - `abyBS1` : 買賣別1 (TByte, Size: 1)
    - *說明*: 買(B)/賣(S)
  - `abyBS2` : 買賣別2 (TByte, Size: 1)
    - *說明*: 買(B)/賣(S)
  - `abyOptProdKind1` : 選擇權商品種類1 (TByte, Size: 1)
    - *說明*: \<第1支腳\>
    - *說明*: \"0\":期貨選擇權  \"1\":現貨選擇權
  - `abyOptProdKind2` : 選擇權商品種類2 (TByte, Size: 1)
    - *說明*: \<第2支腳\>
    - *說明*: "0":期貨選擇權  "1":現貨選擇權
  - `byMarketNo1` : 市場代碼1 (Byte, Size: 1)
    - *說明*: \<第1支腳\>
  - `abyStkCode1` : 行情股票代碼1 (TByte12, Size: 12)
    - *說明*: \<第1支腳\>
  - `byMarketNo2` : 市場代碼2 (Byte, Size: 1)
    - *說明*: \<第2支腳\>
  - `abyStkCode2` : 行情股票代碼2 (TByte12, Size: 12)
    - *說明*: \<第2支腳\>
  - `intBuyPrice1` : 買入價1 (Int, Size: 4)
    - *說明*: \<第1支腳\>
  - `intSellPrice1` : 賣出價1 (Int, Size: 4)
    - *說明*: \<第1支腳\>
  - `intMarketPrice1` : 市價1 (int, Size: 4)
    - *說明*: \<第1支腳\>
    - *說明*: 盤前市價若為0 則給開盤參考價
  - `intBuyPrice2` : 買入價2 (Int, Size: 4)
    - *說明*: \<第2支腳\>
  - `intSellPrice2` : 賣出價2 (Int, Size: 4)
    - *說明*: \<第2支腳\>
  - `intMarketPrice2` : 市價2 (int, Size: 4)
    - *說明*: \<第2支腳\>
    - *說明*: 盤前市價若為0 則給開盤參考價
  - `shtDecimal` : 小數位數 (Short, Size: 2)
    - *說明*: # +為小數位數,-為分數分母,  # 0為整數
  - `uintTickDiff` : 檔差 (unit, Size: 4)
    - *說明*: # 檔差不是固定的就為0，例如台股都為0；海外股票跟海外期貨預留用的；若檔差是0.05，且他的小數位是3位，檔差就是50

---
