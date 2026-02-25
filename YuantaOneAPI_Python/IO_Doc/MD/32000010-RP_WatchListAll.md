# 32000010 - RP_WatchListAll (WatchList 完整版)

## 1. 基本資訊 (Metadata)
- **Service ID**: `32000010 (50.0.0.16)`
- **COM Name**: `RP_WatchListAll`
- **設計描述**: WatchList 完整版
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/01/10

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
      "byMarketNo": "example",
      "abyStkCode": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_In` : 輸入的母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_In` : 輸入的子結構 (Array of Objects)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyStkCode` : 股票代碼 (TByte12, Size: 12)

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
      "byMarketNo": "example",
      "abyStkCode": "example",
      "abyStkName": "example",
      "intYstPrice": 0,
      "intOpenRefPrice": 0,
      "intUpStopPrice": 0,
      "intDownStopPrice": 0,
      "uintYstVol": 0,
      "abyExtName": "example",
      "shtDecimal": 0,
      "byCreditPercent": "example",
      "byLenBondPercent": "example",
      "intOpenPrice": 0,
      "intHighPrice": 0,
      "intLowPrice": 0,
      "intBuyPrice": 0,
      "uintTotalOutVol": 0,
      "intSellPrice": 0,
      "uintTotalInVol": 0,
      "intDealPrice": 0,
      "uintTotalDealAmt": 0,
      "bytVolFlag": "example",
      "uintVol": 0,
      "uintTotalVol": 0,
      "uintFixedPriceVol": 0,
      "uintReserveVol": 0,
      "intSettlementPrice": 0,
      "intHiContractPrice": 0,
      "intLoContractPrice": 0,
      "uintOrderBuyCount": 0,
      "uintOrderBuyQty": 0,
      "uintOrderSellCount": 0,
      "uintOrderSellQty": 0,
      "uintDealBuyCount": 0,
      "uintDealSellCount": 0,
      "uintVolatility": 0,
      "struTime": "",
      "sbytTimeDiff": "example",
      "byStkType2": "example",
      "uintReserveVolDiff": 0,
      "abyBelongCode": "example",
      "abyIndustryName": "example",
      "intPrincipalPercent": 0,
      "shtUpDownDay": 0,
      "uintBidQty": 0,
      "uintAskQty": 0,
      "byPriceTrends": "example",
      "intEstDealPrice": 0,
      "uintEstDealVol": 0,
      "byEstDealVolFlag": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_Out` : 輸出的母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_Out` : 輸出的子結構 (Array of Objects)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
    - *說明*: #
    - `0`: TSE  #
    - `1`: OTC  #
    - `2`: TAIFEX
  - `abyStkCode` : 股票代碼 (TByte12, Size: 12)
    - *說明*: #
  - `abyStkName` : 股票名稱 (TByte20, Size: 20)
    - *說明*: #
  - `intYstPrice` : 昨收價 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intOpenRefPrice` : 開盤參考價 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intUpStopPrice` : 漲停價 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intDownStopPrice` : 跌停價 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `uintYstVol` : 昨量 (Uint, Size: 4)
    - *說明*: #
  - `abyExtName` : 擴充名 (TByte20, Size: 20)
    - *說明*: #
  - `shtDecimal` : 小數位數 (short, Size: 2)
    - *說明*: #
  - `byCreditPercent` : 融資成數 (Byte, Size: 1)
    - *說明*: #
  - `byLenBondPercent` : 融券成數 (Byte, Size: 1)
    - *說明*: #
  - `intOpenPrice` : 開盤 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intHighPrice` : 最高 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intLowPrice` : 最低 (int, Size: 4)
    - *說明*: # 前端需除以10000
  - `intBuyPrice` : 買價 (int, Size: 4)
    - *說明*: # 市價買:999999999  前端需除以10000
  - `uintTotalOutVol` : 累計外盤量 (Uint, Size: 4)
    - *說明*: #
  - `intSellPrice` : 賣價 (int, Size: 4)
    - *說明*: # 市價賣:-999999999  前端需除以10000
  - `uintTotalInVol` : 累計內盤量 (Uint, Size: 4)
    - *說明*: #
  - `intDealPrice` : 成交價 (int, Size: 4)
    - *說明*: # \[註1\]  前端需除以10000
  - `uintTotalDealAmt` : 總成交金額 (Uint, Size: 4)
    - *說明*: #
  - `bytVolFlag` : 單量內外盤標記 (Byte, Size: 1)
    - *說明*: #
    - `0`: 內盤  #
    - `1`: 外盤
  - `uintVol` : 單量 (Uint, Size: 4)
    - *說明*: # (最高位元的Bit，表示內/外盤的旗標，0:內盤/1:外盤)
  - `uintTotalVol` : 總成交量 (Uint, Size: 4)
    - *說明*: #
  - `uintFixedPriceVol` : 定價量 (Uint, Size: 4)
    - *說明*: #
  - `uintReserveVol` : 未平倉量 (Uint, Size: 4)
    - *說明*: #
  - `intSettlementPrice` : 結算價 (int, Size: 4)
    - *說明*: #
  - `intHiContractPrice` : 合約高價 (int, Size: 4)
    - *說明*: #
  - `intLoContractPrice` : 合約低價 (int, Size: 4)
    - *說明*: #
  - `uintOrderBuyCount` : 委託買進總筆數 (Uint, Size: 4)
    - *說明*: #
  - `uintOrderBuyQty` : 委託買進總口數 (Uint, Size: 4)
    - *說明*: #
  - `uintOrderSellCount` : 委託賣出總筆數 (Uint, Size: 4)
    - *說明*: #
  - `uintOrderSellQty` : 委託賣出總口數 (Uint, Size: 4)
    - *說明*: #
  - `uintDealBuyCount` : 累計買進成交筆數 (Uint, Size: 4)
    - *說明*: #
  - `uintDealSellCount` : 累計賣出成交筆數 (Uint, Size: 4)
    - *說明*: #
  - `uintVolatility` : 波動率 (Uint, Size: 4)
    - *說明*: #
  - `struTime` : 時間 (TYuantaTime, Size: 5)
    - *說明*: #
  - `sbytTimeDiff` : 時差 (SByte, Size: 1)
    - *說明*: # 台股為0，（晚＝正值，早＝負值）。日本比台灣早一小時，時差就是等於-1
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
  - `uintReserveVolDiff` : 未平倉量增減 (int, Size: 4)
    - *說明*: #
  - `abyBelongCode` : 所屬產業分類碼 (TByte2, Size: 2)
    - *說明*: # 01 水泥工業  # 02 食品工業  # 03 塑膠工業
  - `abyIndustryName` : 產業類股名稱 (TByte20, Size: 20)
    - *說明*: #
  - `intPrincipalPercent` : 市值(%) (int, Size: 4)
    - *說明*: # /100 (單位％)
  - `shtUpDownDay` : 連續漲跌(天) (short, Size: 2)
    - *說明*: # + : 連續漲天數 - : 連續跌天數
  - `uintBidQty` : 第一買量 (Uint, Size: 4)
    - *說明*: #
  - `uintAskQty` : 第一賣量 (Uint, Size: 4)
    - *說明*: #
  - `byPriceTrends` : 瞬間價格趨勢 (Byte, Size: 1)
    - *說明*: #
    - `10`: 一般揭示  #
    - `11`: 暫緩撮合且瞬間趨跌  #
    - `12`: 暫緩撮合且瞬間趨漲  #
    - `13`: 試算後延後收盤  #
    - `14`: 暫停交易  #
    - `15`: 恢復交易
  - `intEstDealPrice` : 盤前揭露價 (Int, Size: 4)
    - *說明*: #
  - `uintEstDealVol` : 盤前揭露量 (Uint, Size: 4)
    - *說明*: #
  - `byEstDealVolFlag` : 盤前揭露量內外盤標記 (Byte, Size: 1)
    - *說明*: #
    - `0`: 內盤  #
    - `1`: 外盤

---
