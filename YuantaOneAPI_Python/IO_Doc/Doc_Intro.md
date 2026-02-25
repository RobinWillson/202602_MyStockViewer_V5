# 元大 API 規格文件導讀 (Document Introduction)

本專案的 `IO_Doc` 目錄下存放了 API 規格文件（`.md` 檔）。為了正確解讀並實作這些 API，請參考以下的觀念說明。

## 1. 文件的基本概念

每一份規格文件（例如 `0A000010_10.0.0.16_IO_Spec.md`）實際上代表了 **一隻單獨的 API / 函式 (Function)**。
* **文件頭部的資訊：**
  * `COM Name`：這是函式或請求封包的名稱（例如 `RP_RealReportMerge`）。實際呼叫或實作時，通常就是呼叫這個物件。
  * `Service ID`：這隻 API 的唯一識別碼（例如 `0A000010`）。
  * `Service Desc`：這隻 API 的功能描述（例如「即時回報彙總」）。

## 2. Input Spec（輸入規格）與 Output Spec（輸出規格）

文件會被劃分為 Input Spec 和 Output Spec 兩大區塊。

### **Input Spec Table (輸入/請求欄位)**
這裡列出的所有欄位，代表了在使用這隻 API 時，所需要準備並送出的**封包結構 (Request Payload)**。您可以將它想像成在呼叫這隻函式時，準備好的一大包字典（Dict）、結構體（Struct）或物件（Object）參數。

### **Output Spec Table (輸出/回傳欄位)**
這裡列出的所有欄位，代表了 API 處理完畢後，回傳給您的**資料內容結構 (Response Payload)**。您需要依照這些欄位定義來解析收到的結果。

## 3. 母結構、子結構與 `uintCount` (陣列與迴圈觀念)

在底層結構（如 C/C++ Struct、Socket 封包）的 API 中，常會有「一對多」的情況。在文件中通常透過以下三個項目來表達這種 Array（陣列）或 List（清單）的關聯：
* **`ParentStruct` (母結構)**：放置共用的主要條件或單一欄位（例如：查詢日期、主要的市場代碼、單號）。
* **`uintCount` (數量 / 長度)**：代表緊接著的陣列長度或迴圈的執行次數。
* **`ChildStruct` (子結構)**：備註通常會寫著 `Loop(uintCount)`，代表這是一個存放多筆明細資料的陣列（Array）。

### **以 `uintCount` 為例的實際運用：**

* **在 Input Spec 時 (準備送出 Request)：**
  `uintCount` 是您需要填寫的參數，用來明確告訴 API 接下來會在 `ChildStruct` 結構中傳入「幾筆」明細（例如幾個不同帳號）。如果您塞了 4 個帳號，`uintCount` 的值就必須帶 `4`。

* **在 Output Spec 時 (接收並解析 Response)：**
  `uintCount` 是 API 回傳給您的值。API 在這裡告訴您，這次回傳的 `ChildStruct` 資料中總共有「幾筆」明細紀錄。您的程式在解析時，就會先讀取 `uintCount` 的值，接著寫一個 `for 迴圈` 依照該次數讀取對應的明細資料。

---

## 4. 程式碼概念轉換範例

以 `RP_RealReportMerge` (即時回報彙總) 單一 API 為例，當您要將文件轉換為程式碼思維時：

```python
# [Input Spec 概念呈現]：組成 Request 封包
request_payload = {
    # ---------- 以下為屬於 母結構 (ParentStruct_In) 的欄位 ----------
    "abyConditionFlag": 0,    
    "byMarketNo": 0,          
    "abyCompanyNo": "",       
    
    # 宣告底下的子結構陣列有幾筆
    "uintCount": 4,           
    
    # ---------- 以下為屬於 子結構 (ChildStruct_In) 的陣列 ----------
    "ChildStruct_In": [
        {"abyAccount": "Account_A"}, # 第 1 筆
        {"abyAccount": "Account_B"}, # 第 2 筆
        {"abyAccount": "Account_C"}, # 第 3 筆
        {"abyAccount": "Account_D"}  # 第 4 筆
    ]
}

# 送出請求，呼叫名為 RP_RealReportMerge 的功能
response_payload = call_api("RP_RealReportMerge", request_payload)


# [Output Spec 概念呈現]：解析 Response 封包
# (假設 API 回傳上面的 response_payload)

# 讀取回傳的筆數
received_count = response_payload["uintCount"]

# 迴圈讀取收到的明細
for i in range(received_count):
    detail = response_payload["ChildStruct_Out"][i]
    print(f"委託單號: {detail['abyOrderNo']}, 狀態: {detail['shtOrderStatus']}")
```
