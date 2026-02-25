# D20A460B - RR_Watchlist (WatchList  (報價表指定欄位)  行情資料)

## 1. 基本資訊 (Metadata)
- **Service ID**: `D20A460B (210.10.70.11)`
- **COM Name**: `RR_Watchlist`
- **設計描述**: WatchList  (報價表指定欄位)  行情資料
- **通訊模式**: `SB/SP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SubscribeWatchlist  UnsubscribeWatchlist": "",
    "lstWatchlist": "",
    "lng": "",
    "return": "",
    "Watchlist": "",
    "IndexFlag": "example",
    "[MarketNo]{.mark}": "example",
    "[StockCode]{.mark}": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `SubscribeWatchlist  UnsubscribeWatchlist` : 訂閱報價表指定欄位  解訂閱報價表指定欄位 (function)
  - `lstWatchlist` : 訂閱商品清單 (List\<Watchlist\>)
  - `lng` : 語系:預設為繁體中文 (enumLangType)
    - `Normal`: Big5
    - `UTF8`: UTF8
    - `SC`: 簡體中文
  - `return` : 結果 (bool)
  - `Watchlist` : 報價表指定欄位 (Class)
  - `IndexFlag` : 訂閱索引值 (byte, Size: )
  - `[MarketNo]{.mark}` : 市場代碼 (byte, Size: )
  - `[StockCode]{.mark}` : 商品代碼 (string, Size: )

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "abyKey": "example",
    "byMarketNo": "example",
    "abyStkCode": "example",
    "byIndexFlag": "example",
    "struRecord": "",
    "intValue": 0
  }
}
```

### 參數說明 (Parameter Details)

  - `abyKey` : 鍵值 (TByte22, Size: 22)
    - *說明*: byIndexFlag+byMarketNo+  abyStkCode (不足補0x00)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyStkCode` : 股票代碼 (TByte12, Size: 12)
  - `byIndexFlag` : 索引值 (Byte, Size: 1)
  - `struRecord` :  
  - `intValue` : 資料值 (Integer, Size: 4)
    - *說明*: 索引值=0,代表值=開盤  索引值=1,代表值=最高  索引值=2,代表值=最低  索引值=3,代表值=買價  索引值=4,代表值=累計外盤量  索引值=5,代表值=賣價  索引值=6,代表值=累計內盤量  索引值=7,代表值=成交價  索引值=8,代表值=總成交金額  索引值=9,代表值=單量  (最高位元的Bit,表示內/外盤的旗標,0-內盤/1-外盤)  索引值=10,代表值=總成交量  索引值=11,代表值=定價量  索引值=12,代表值=未平倉量  索引值=13,代表值=結算價  索引值=14,代表值=合約高價  索引值=15,代表值=合約低價  索引值=16,代表值=委託買進總筆數  索引值=17,代表值=委託買進總口數  索引值=18,代表值=委託賣出總筆數  索引值=19,代表值=委託賣出總口數  索引值=20,代表值=累計買進成交筆數  索引值=21,代表值=累計賣出成交筆數  索引值=23,代表值=波動率  索引值=24,代表值=虛擬最佳一檔買進價  索引值=25,代表值=虛擬最佳一檔買進量  索引值=26,代表值=虛擬最佳一檔賣出價  索引值=27,代表值=虛擬最佳一檔賣出量  索引值=42,代表值=第一買量  索引值=43,代表值=第一賣量  索引值=45,代表值=delay一秒的成交價(海外股無此資料,請使用索引值=7的成交價)  索引值=48,代表值=瞬間價格趨勢(
    - `10`: 一般揭示
    - `11`: 暫緩撮合且瞬間趨跌
    - `12`: 暫緩撮合且瞬間趨漲
    - `13`: 試算後延後收盤
    - `14`: 暫停交易
    - `15`: 恢復交易
    - `16`: 試算後延後開盤)  索引值=201,代表值=昨收價  索引值=202,代表值=漲停價  索引值=203,代表值=跌停價  索引值=240,代表值=交易狀態
    - `0x00`: 初始狀態
    - `0x01`: 收單階段
    - `0x02`: 不可刪單階段
    - `0x03`: 集合競價階段  索引值=241,代表值=試撮價  索引值=242,代表值=試撮量  (最高位元的Bit,表示內/外盤的旗標,0:內盤/1:外盤)  索引值=254,代表值=開盤參考價  索引值=255,代表值=開盤參考價(清盤用)

---
