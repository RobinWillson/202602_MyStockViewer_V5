# 30.100.40.12 - OdrOVFutOrder (國際期貨下單)

## 1. 基本資訊 (Metadata)
- **Service ID**: `30.100.40.12 (1E64280C)`
- **COM Name**: `OdrOVFutOrder`
- **設計描述**: 國際期貨下單
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SendOVFutureOrder": "",
    "LoginAcno": "example",
    "lstOVFutureOrder": "",
    "lng": "",
    "return": "",
    "OVFutureOrder": "",
    "Identity": 0,
    "Account": "example",
    "~~Channel~~": "example",
    "OrderNo": "example",
    "TradeDate": "example",
    "FunctionCode": 0,
    "ExhCode": "example",
    "MarketNo": "example",
    "CommodityID": "example",
    "CallPut": "example",
    "SettlementMonth": 0,
    "StrikePrice": 0,
    "UtPrice": 0,
    "UtPrice2": 0,
    "MinPrice2": 0,
    "UtPrice4": 0,
    "UtPrice5": 0,
    "UtPrice6": 0,
    "OrderQty": 0,
    "BuySell": "example",
    "Dtover": "example",
    "OrderType": "example",
    "~~SellerNo~~": 0
  }
}
```

### 參數說明 (Parameter Details)

  - `SendOVFutureOrder` : 國際期貨下單 (function)
  - `LoginAcno` : 欲下單帳號 (string)
  - `lstOVFutureOrder` : 下單物件 (List\<OVFutureOrder\>)
  - `lng` : 語系:預設為繁體中文 (enumLangType)
    - `Normal`: Big5
    - `UTF8`: UTF8
    - `SC`: 簡體中文
  - `return` : 下單結果 (bool)
  - `OVFutureOrder` : 下單物件 (Class)
  - `Identity` : 識別碼 (int)
  - `Account` : 下單帳號 (string)
    - *說明*: 完整帳號:  如FF021000P001234567
  - `~~Channel~~` : ~~通路種類~~ (~~string~~)
  - `OrderNo` : 委託書編號 (string)
  - `TradeDate` : 交易日期 (string)
    - *說明*: yyyy/MM/dd
  - `FunctionCode` : 功能別 (short)
    - `00`: 委託單
    - `04`: 取消
    - `07`: 改價
  - `ExhCode` : 交易所簡碼 (string)
    - *說明*: 請參考 FunctionList.xlsx  市場表及股名對照表
  - `MarketNo` : 市場代碼 (byte)
  - `CommodityID` : 商品代碼 (string)
  - `CallPut` : 買賣權 (byte)
  - `SettlementMonth` : 商品年月 (int)
  - `StrikePrice` : 屐約價格 (int)
    - *說明*: 請\*10000
  - `UtPrice` : 委託價格整數位 (long)
    - *說明*: 請\*10000  (市價或市價停損單填0)
  - `UtPrice2` : 委託價格分子 (int)
    - *說明*: 請\*10000
  - `MinPrice2` : 委託價格分母 (int)
  - `UtPrice4` : 停損執行價整數位 (long)
    - *說明*: 請\*10000  (非停損單填0)
  - `UtPrice5` : 停損執行價格分子 (int)
    - *說明*: 請\*10000
  - `UtPrice6` : 停損執行價格分母 (int)
  - `OrderQty` : 委託口數 (short)
  - `BuySell` : 買賣別 (string)
    - *說明*: \"B\":買  \"S\":賣
  - `Dtover` : 是否當沖 (string)
    - *說明*: Y  N
  - `OrderType` : 委託種類 (string)
    - `LMT`: 限價單
    - `MKT`: 市價單
    - `STP`: 停損單
    - `SWL`: 停損限價單
  - `~~SellerNo~~` : ~~營業員代碼~~ (~~short~~)

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "abyMsgCode": "example",
    "abyMsgContent": "example",
    "uintCount": 1
  },
  "ChildStruct_Out": [
    {
      "intIdentify": 0,
      "shtReplyCode": 0,
      "abyOrderNO": "example",
      "struTradeDate": "",
      "abyErrType": "example",
      "abyErrNO": "example",
      "abyAdvisory": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_Out` : 下單筆數Structure (Object)
  - `abyMsgCode` : 訊息代碼 (TByte4, Size: 4)
    - `0001`: 執行成功  其它:失敗
  - `abyMsgContent` : 訊息內容 (TByte50, Size: 50)
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_Out` : 下單結果Structure (Array of Objects)
  - `intIdentify` : 識別碼 (Int, Size: 4)
  - `shtReplyCode` : 委託結果代碼 (Short, Size: 2)
    - `0`: 委託成功
    - `others`: 委託失敗
  - `abyOrderNO` : 委託書編號 (TByte5, Size: 5)
  - `struTradeDate` : 交易日期 (TYuantaDate, Size: 4)
  - `abyErrType` : 錯誤類別 (TByte, Size: 1)
  - `abyErrNO` : 錯誤代號 (TByte3, Size: 3)
    - `A003`: 預約單不支援改價或無此委託單
    - `A004`: 委託已成交，無法改價
    - `A005`: 委託已取消，無法改價
  - `abyAdvisory` : 錯誤說明 (TByte74, Size: 74)

---
