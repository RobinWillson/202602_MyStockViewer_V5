# 1E641418 - OdrFutOrder (期貨下單)

## 1. 基本資訊 (Metadata)
- **Service ID**: `1E641418 (30.100.20.24)`
- **COM Name**: `OdrFutOrder`
- **設計描述**: 期貨下單
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SendFutureOrder": "",
    "LoginAcno": "example",
    "lstFutureOrder": "",
    "lng": "",
    "return": "",
    "FutureOrder": "",
    "Identity": 0,
    "Account": "example",
    "~~Channel~~": "example",
    "OrderNo": "example",
    "TradeDate": "example",
    "FunctionCode": 0,
    "CommodityID1": "example",
    "CallPut1": "example",
    "SettlementMonth1": 0,
    "Price": 0,
    "StrikePrice1": 0,
    "OrderQty1": 0,
    "BuySell1": "example",
    "CommodityID2": "example",
    "CallPut2": "example",
    "SettlementMonth2": 0,
    "StrikePrice2": 0,
    "OrderQty2": 0,
    "BuySell2": "example",
    "OpenOffsetKind": "example",
    "DayTradeID": "example",
    "OrderType": "example",
    "OrderCond": "example",
    "SellerNo": 0,
    "BasketNo": "example",
    "Session": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `SendFutureOrder` : 國內期貨下單 (function)
  - `LoginAcno` : 欲下單帳號 (string)
  - `lstFutureOrder` : 下單物件 (List\<FutureOrder\>)
  - `lng` : 語系:預設為繁體中文 (enumLangType)
    - `Normal`: Big5
    - `UTF8`: UTF8
    - `SC`: 簡體中文
  - `return` : 下單結果 (bool)
  - `FutureOrder` : 下單物件 (Class)
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
    - `05`: 改量
    - `07`: 改價  (Opt複式單沒有改價)
  - `CommodityID1` : 商品名稱1 (string)
    - *說明*: 請參考 FunctionList.xlsx  股名對照表的下單代碼  如:台指🡪FITX  如:台指選🡪TXO
  - `CallPut1` : 買賣權1 (string)
    - *說明*: \"C\":Call  \"P\":Put
    - *說明*: (選擇權才需填值)
  - `SettlementMonth1` : 商品月份1 (int)
    - *說明*: 如:201912
  - `Price` : 委託價格 (int)
    - *說明*: 請\*10000
  - `StrikePrice1` : 履約價1 (int)
    - *說明*: 請\*1000
  - `OrderQty1` : 委託口數1 (short)
  - `BuySell1` : 買賣別1 (string)
    - *說明*: \"B\":買  \"S\":賣
  - `CommodityID2` : 商品名稱2 (string)
  - `CallPut2` : 買賣權2 (string)
    - *說明*: \"C\":Call  \"P\":Put
    - *說明*: (選擇權才需填值)
  - `SettlementMonth2` : 商品月份2 (int)
    - *說明*: 如:201912
  - `StrikePrice2` : 履約價2 (int)
    - *說明*: 請\*1000
  - `OrderQty2` : 委託口數2 (short)
  - `BuySell2` : 買賣別2 (string)
    - *說明*: \"B\":買  \"S\":賣
  - `OpenOffsetKind` : 新平倉 (string)
    - `0`: 新倉
    - `1`: 平倉
    - `2`: 自動
  - `DayTradeID` : 當沖註記 (string)
    - *說明*: \"Y\":當沖  \" \":空白
  - `OrderType` : 委託方式 (string)
    - `1`: 市價
    - `2`: 限價
    - `3`: 範圍市價
  - `OrderCond` : 委託條件 (string)
    - *說明*: \" \":ROD
    - `I`: FOK
    - `2`: IOC
  - `SellerNo` : 營業員代碼 (short)
    - *說明*: 請填0
  - `BasketNo` : BasketNo (string)
    - *說明*: 目前無作用
  - `Session` : 盤別 (string)
    - `1`: 預約  其他:盤中單

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
      "abyErrKind": "example",
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
  - `abyErrKind` : 錯誤種類 (TByte, Size: 1)
  - `abyErrNO` : 錯誤代號 (TByte3, Size: 3)
  - `abyAdvisory` : 錯誤說明 (TByte74, Size: 74)

---
