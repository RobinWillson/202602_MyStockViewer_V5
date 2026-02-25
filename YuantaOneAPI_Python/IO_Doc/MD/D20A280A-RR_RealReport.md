# > - Unknown (個股分時明細)

## 1. 基本資訊 (Metadata)
- **Service ID**: `> D20A280A (210.10.40.10)`
- **COM Name**: ``
- **設計描述**: 個股分時明細
- **通訊模式**: `SB/SP`
- **更新日期**: > 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SubscribeStocktick  UnsubscribeStocktick": "",
    "lstStocktick": "",
    "lng": "",
    "return": "",
    "Stocktick": "",
    "[MarketNo]{.mark}": "example",
    "[StockCode]{.mark}": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `SubscribeStocktick  UnsubscribeStocktick` : 訂閱個股分時明細  解訂閱個股分時明細 (function)
  - `lstStocktick` : 訂閱商品清單 (List\<Stocktick\>)
  - `lng` : 語系:預設為繁體中文 (enumLangType)
    - `Normal`: Big5
    - `UTF8`: UTF8
    - `SC`: 簡體中文
  - `return` : 結果 (bool)
  - `Stocktick` : 個股分時明細 (Class)
  - `[MarketNo]{.mark}` : 市場代碼 (byte, Size: )
    - *說明*: #
  - `[StockCode]{.mark}` : 商品代碼 (string, Size: )
    - *說明*: #

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "abyKey": "example",
    "byMarketNo": "example",
    "abyStkCode": "example",
    "dwSerialNo": 0,
    "struTime": "",
    "byHour": "example",
    "byMin": "example",
    "bySec": "example",
    "wMSec": 0,
    "intBuyPrice": 0,
    "intSellPrice": 0,
    "intDealPrice": 0,
    "dwDealVol": 0,
    "byInOutFlag": "example",
    "byType": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `abyKey` : 鍵值 (TByte22, Size: 22)
    - *說明*: byMarketNo+abyStkCode  (不足補0x00)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyStkCode` : 股票代碼 (TByte12, Size: 12)
  - `dwSerialNo` : 序號 (Uint, Size: 4)
    - *說明*: 以股票代碼個別編序號，  從1開始  (0xFFFFFFFF代表商品清盤)
  - `struTime` :  
  - `byHour` : 時 (Byte, Size: 1)
  - `byMin` : 分 (Byte, Size: 1)
  - `bySec` : 秒 (Byte, Size: 1)
  - `wMSec` : 毫秒 (usShort, Size: 2)
  - `intBuyPrice` : 買價 (Integer, Size: 4)
    - *說明*: 當dwSerialNo=0xFFFFFFFF時,此欄位代表漲停價  市價買:999999999  前端需除以10000
  - `intSellPrice` : 賣價 (Integer, Size: 4)
    - *說明*: 當dwSerialNo=0xFFFFFFFF時,此欄位代表跌停價  市價賣:-999999999  前端需除以10000
  - `intDealPrice` : 成交價 (Integer, Size: 4)
    - *說明*: 當dwSerialNo=0xFFFFFFFF時,此欄位代表開盤參考價  前端需除以10000
  - `dwDealVol` : 成交量 (Uint, Size: 4)
  - `byInOutFlag` : 內外盤註記 (Byte, Size: 1)
    - `0`: 內盤
    - `1`: 外盤
    - `2`: 定價內盤
    - `3`: 定價外盤
    - `10`: 一般揭示
    - `11`: 暫緩撮合且瞬間趨跌
    - `12`: 暫緩撮合且瞬間趨漲
    - `13`: 試算後延後收盤
    - `14`: 暫停交易
    - `15`: 恢復交易  註1：當是10,11,12,13時,只有市場碼與股票代碼有值,其餘的欄位皆是0  註2：當是14,15時,只有市場碼、股票代碼與時間有值,其餘的欄位皆是0
  - `byType` : 明細類別 (Byte, Size: 1)
    - `0`: Normal

---
