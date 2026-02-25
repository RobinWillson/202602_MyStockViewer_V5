# 620A460A - RR_WatclistAll (WatchList(報價表)行情資料)

## 1. 基本資訊 (Metadata)
- **Service ID**: `620A460A (98.10.70.10)`
- **COM Name**: `RR_WatclistAll`
- **設計描述**: WatchList(報價表)行情資料
- **通訊模式**: `SB/SP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SubscribeWatchlistAll  UnsubscribeWatchlistAll": "",
    "lstWatchlistAll": "",
    "WatchlistAll": "",
    "[MarketNo]{.mark}": "example",
    "[StockCode]{.mark}": "example",
    "return": ""
  }
}
```

### 參數說明 (Parameter Details)

  - `SubscribeWatchlistAll  UnsubscribeWatchlistAll` : 訂閱報價表  解訂閱報價表 (function)
  - `lstWatchlistAll` : 訂閱商品清單 (List\<WatchlistAll\>)
  - `WatchlistAll` : 報價表 (Class)
  - `[MarketNo]{.mark}` : 市場代碼 (byte, Size: )
    - *說明*: #
  - `[StockCode]{.mark}` : 商品代碼 (string, Size: )
    - *說明*: #
  - `return` : 結果 (bool)

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "abyKey": "example",
    "byMarketNo": "example",
    "abyStkCode": "example",
    "llSeqNo": 0,
    "byIndexFlag": "example",
    "struRecord": "",
    "intValue": 0,
    "intBuyPrice": 0,
    "intSellPrice": 0,
    "byHour": "example",
    "byMin": "example",
    "bySec": "example",
    "wMSec": 0,
    "dwTotalOutVol": 0,
    "dwTotalInVol": 0,
    "intDeal": 0,
    "dwVol": 0,
    "dwTotalVol": 0,
    "dwTotalAmt": 0,
    "dwBuyVol": 0,
    "dwSellVol": 0
  }
}
```

### 參數說明 (Parameter Details)

  - `abyKey` : 鍵值 (TByte22, Size: 22)
    - *說明*: byMarketNo+abyStkCode (不足補0x00)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyStkCode` : 股票代碼 (TByte12, Size: 12)
  - `llSeqNo` : 序號 (Long, Size: 8)
    - *說明*: 090000000000。  後八碼表序號，前四碼表時間
  - `byIndexFlag` : 索引值 (Byte, Size: 1)
  - `struRecord` :  
    - *說明*: byIndexFlag\>=0  and byIndexFlag\<=48
  - `intValue` : 資料值 (Integer, Size: 4)
    - *說明*: 索引值=0,代表值=開盤  索引值=1,代表值=最高  索引值=2,代表值=最低  索引值=11,代表值=定價量  索引值=12,代表值=未平倉量  索引值=13,代表值=結算價  索引值=14,代表值=合約高價  索引值=15,代表值=合約低價  索引值=16,代表值=委託買進總筆數  索引值=17,代表值=委託買進總口數  索引值=18,代表值=委託賣出總筆數  索引值=19,代表值=委託賣出總口數  索引值=20,代表值=累計買進成交筆數  索引值=21,代表值=累計賣出成交筆數  索引值=24,代表值=虛擬最佳一檔買進價  索引值=25,代表值=虛擬最佳一檔買進量  索引值=26,代表值=虛擬最佳一檔賣出價  索引值=27,代表值=虛擬最佳一檔賣出量  索引值=48,代表值=瞬間價格趨勢(
    - `10`: 一般揭示
    - `11`: 暫緩撮合且瞬間趨跌
    - `12`: 暫緩撮合且瞬間趨漲
    - `13`: 試算後延後收盤
    - `14`: 暫停交易
    - `15`: 恢復交易
    - `16`: 試算後延後開盤)  索引值=240,代表值=交易狀態(
    - `0x00`: 初始狀態
    - `0x01`: 收單階段
    - `0x02`: 不可刪單階段
    - `0x03`: 集合競價階段)  索引值=241,試撮成交價  索引值=242,試摱成交量(最高位元的Bit,表示內/外盤的旗標,0:內盤/1:外盤)  索引值=254,代表值=開盤參考價  索引值=255,代表值=開盤參考價(清盤用)
  - `struRecord` :  
    - *說明*: byIndexFlag=28
  - `intBuyPrice` : 買價 (Integer, Size: 4)
  - `intSellPrice` : 賣價 (Integer, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=29
  - `byHour` : 時 (Byte, Size: 1)
  - `byMin` : 分 (Byte, Size: 1)
  - `bySec` : 秒 (Byte, Size: 1)
  - `wMSec` : 毫秒 (usShort, Size: 2)
  - `dwTotalOutVol` : 累計外盤量 (Uint, Size: 4)
  - `dwTotalInVol` : 累計內盤量 (Uint, Size: 4)
  - `intDeal` : 成交價 (Integer, Size: 4)
    - *說明*: 前端需除以10000
  - `dwVol` : 單量 (Uint, Size: 4)
    - *說明*: 最高位元的Bit，  表示內/外盤的旗標，
    - `0`: 內盤/1:外盤
  - `dwTotalVol` : 總成交量 (Uint, Size: 4)
  - `dwTotalAmt` : 總成交金額 (Uint, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=22
  - `dwBuyVol` : 第一買量 (Uint, Size: 4)
  - `dwSellVol` : 第一賣量 (Uint, Size: 4)

---
