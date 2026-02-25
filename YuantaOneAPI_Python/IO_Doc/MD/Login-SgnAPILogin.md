# Login函數 - SgnAPILogin (API Login)

## 1. 基本資訊 (Metadata)
- **Service ID**: `Login函數`
- **COM Name**: `SgnAPILogin`
- **設計描述**: API Login
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "Account": "example",
    "PWD": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `Account` : 帳號 (string)
    - *說明*: 證券:S9875005091  期貨:FF021000P001234567
  - `PWD` : 密碼 (string)

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
      "abyAccount": "example",
      "abyName": "example",
      "abyInvestorID": "example",
      "shtSellerNo": 0
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_Out` : 輸出的母結構 (Object)
  - `abyMsgCode` : 訊息代碼 (TByte5, Size: 5)
    - `0000`: 執行失敗
    - `0001`: 執行成功
    - `0102`: 密碼凍結或未啟用
    - `0112`: 無此權限使用功能
  - `abyMsgContent` : 中文訊息 (TByte50, Size: 50)
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_Out` : 輸出的子結構 (Array of Objects)
  - `abyAccount` : 帳號 (TByte22, Size: 22)
    - *說明*: 證券:S9875005091  期貨: FF021000P001234567
  - `abyName` : 客戶姓名 (TByte12, Size: 12)
  - `abyInvestorID` : 身分證字號 (TByte14, Size: 14)
  - `shtSellerNo` : 營業員代碼 (Short, Size: 2)

---
