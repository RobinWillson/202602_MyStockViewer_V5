# 1E640A1F - OdrStkSOrder (現貨下單)

## 1. 基本資訊 (Metadata)
- **Service ID**: `1E640A1F (30.100.10.31)`
- **COM Name**: `OdrStkSOrder`
- **設計描述**: 現貨下單
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SendStockOrder": "",
    "LoginAcno": "example",
    "lstStockOrder": "",
    "lng": "",
    "return": "",
    "StockOrder": "",
    "Identity": 0,
    "Account": "example",
    "OrderNo": "example",
    "TradeDate": "example",
    "APCode": 0,
    "TradeKind": 0,
    "OrderType": "example",
    "StkCode": "example",
    "BuySell": "example",
    "PriceFlag": "example",
    "Price": 0,
    "BasketNo": "example",
    "SellerNo": 0,
    "OrderQty": 0,
    "~~LotSize~~": 0,
    "Time_in_force": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `SendStockOrder` : 國內證券下單 (function)
  - `LoginAcno` : 欲下單帳號 (string)
  - `lstStockOrder` : 下單物件 (List\<StockOrder\>)
  - `lng` : 語系:預設為繁體中文 (enumLangType)
    - `Normal`: Big5
    - `UTF8`: UTF8
    - `SC`: 簡體中文
  - `return` : 結果 (bool)
  - `StockOrder` : 下單物件 (Class)
  - `Identity` : 識別碼 (int)
  - `Account` : 下單帳號 (string)
    - *說明*: 完整帳號:如S98875005091
  - `OrderNo` : 委託書編號 (string)
  - `TradeDate` : 交易日期 (string)
    - *說明*: yyyy/MM/dd
  - `APCode` : 交易單市場別 (short)
    - `0`: 一般
    - `2`: 零股
    - `4`: 盤中零股
    - `7`: 盤後
  - `TradeKind` : 交易性質 (short)
    - `00`: 委託單
    - `03`: 改量
    - `04`: 取消
    - `07`: 改價
  - `OrderType` : 委託種類 (string)
    - *說明*: \"0\":現貨  \"3\":融資  \"4\":融券  \"5\":策略借券(賣出)  \"6\":避險借券(賣出)  \"9\":現股當沖委託控管
  - `StkCode` : 股票代號 (string)
  - `BuySell` : 買賣記號 (string)
    - *說明*: \"B\":買  \"S\":賣
  - `PriceFlag` : 價格種類 (string)
    - `H`: 漲停
    - `-`: 平盤
    - `L`: 跌停  \" \":限價
    - `M`: 市價單
  - `Price` : 委託價格 (long)
    - *說明*: 請\*10000
  - `BasketNo` : 使用者自訂欄位 (string)
    - *說明*: (限32個英數字內)
  - `SellerNo` : 營業員代號 (short)
    - *說明*: 固定填0
  - `OrderQty` : 委託單位 (long)
  - `~~LotSize~~` : ~~每手股數~~ (~~uint~~)
  - `Time_in_force` : 委託時間效期 (string)
    - `0`: ROD
    - `3`: IOC
    - `4`: FOK

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
  - `abyMsgContent` : 訊息內容 (TByte75, Size: 75)
    - `Max`: 25中文
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_Out` : 下單結果Structure (Array of Objects)
  - `intIdentify` : 識別碼 (Int, Size: 4)
  - `shtReplyCode` : 委託結果代碼 (Short, Size: 2)
    - `0`: 委託成功
    - `others`: 委託失敗
  - `abyOrderNO` : 委託書編號 (Tbyte5, Size: 5)
  - `struTradeDate` : 交易日期 (TYuantaDate, Size: 4)
  - `abyErrType` : 錯誤類別 (TByte, Size: 1)
  - `abyErrNO` : 錯誤代號 (TByte3, Size: 3)
    - `A003`: 預約單不支援改價或無此委託單
    - `A004`: 委託已成交，無法改價
    - `A005`: 委託已取消，無法改價
  - `abyAdvisory` : 錯誤說明 (TByte120, Size: 120)
    - `Max`: 40中文

---
