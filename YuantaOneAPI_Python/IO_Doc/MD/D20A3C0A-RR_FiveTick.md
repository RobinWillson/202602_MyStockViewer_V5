# D20A3C0A - [RR_FiveTick]{.mark} (最佳五檔行情資料)

## 1. 基本資訊 (Metadata)
- **Service ID**: `D20A3C0A (210.10.60.10)`
- **COM Name**: `[RR_FiveTick]{.mark}`
- **設計描述**: 最佳五檔行情資料
- **通訊模式**: `SB/SP`
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "SubscribeFiveTickA  UnsubscribeFiveTickA": "",
    "lstFiveTickA": "",
    "lng": "",
    "return": "",
    "FiveTickA": "",
    "[MarketNo]{.mark}": "example",
    "[StockCode]{.mark}": "example"
  }
}
```

### 參數說明 (Parameter Details)

  - `SubscribeFiveTickA  UnsubscribeFiveTickA` : 訂閱五檔  解訂閱五檔 (function)
  - `lstFiveTickA` : 訂閱商品清單 (List\<FiveTickA\>)
  - `lng` : 語系:預設為繁體中文 (enumLangType)
    - `Normal`: Big5
    - `UTF8`: UTF8
    - `SC`: 簡體中文
  - `return` : 結果 (bool)
  - `FiveTickA` : 五檔 (Class)
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
    "dwValue": 0,
    "intValue": 0,
    "intPrice1": 0,
    "intPrice2": 0,
    "intPrice3": 0,
    "intPrice4": 0,
    "intPrice5": 0,
    "dwVol1": 0,
    "dwVol2": 0,
    "dwVol3": 0,
    "dwVol4": 0,
    "dwVol5": 0
  }
}
```

### 參數說明 (Parameter Details)

  - `abyKey` : 鍵值 (TByte22, Size: 22)
    - *說明*: byMarketNo+abyStkCode (不足補0x00)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyStkCode` : 股票代碼 (TByte12, Size: 12)
  - `byIndexFlag` : 索引值 (Byte, Size: 1)
  - `struRecord` :  
    - *說明*: byIndexFlag=0\~4,10\~14,22\~26,32\~36
  - `dwValue` : 量的資料值 (Uint, Size: 4)
    - *說明*: 索引值=0,代表值=第一買量  索引值=1,代表值=第二買量  索引值=2,代表值=第三買量  索引值=3,代表值=第四買量  索引值=4,代表值=第五買量  索引值=10,代表值=第一賣量  索引值=11,代表值=第二賣量  索引值=12,代表值=第三賣量  索引值=13,代表值=第四賣量  索引值=14,代表值=第五賣量  索引值=22,代表值=第六買量  索引值=23,代表值=第七買量  索引值=24,代表值=第八買量  索引值=25,代表值=第九買量  索引值=26,代表值=第十買量  索引值=32,代表值=第六賣量  索引值=33,代表值=第七賣量  索引值=34,代表值=第八賣量  索引值=35,代表值=第九賣量  索引值=36,代表值=第十賣量
  - `struRecord` :  
    - *說明*: byIndexFlag=5\~9,15\~19,27\~31,37\~41
  - `intValue` : 價的資料值 (Integer, Size: 4)
    - *說明*: 索引值=5,代表值=第一買價  索引值=6,代表值=第二買價  索引值=7,代表值=第三買價  索引值=8,代表值=第四買價  索引值=9,代表值=第五買價  索引值=15,代表值=第一賣價  索引值=16,代表值=第二賣價  索引值=17,代表值=第三賣價  索引值=18,代表值=第四賣價  索引值=19,代表值=第五賣價  索引值=27,代表值=第六買價  索引值=28,代表值=第七買價  索引值=29,代表值=第八買價  索引值=30,代表值=第九買價  索引值=31,代表值=第十買價  索引值=37,代表值=第六賣價  索引值=38,代表值=第七賣價  索引值=39,代表值=第八賣價  索引值=40,代表值=第九賣價  索引值=41,代表值=第十賣價
  - `struRecord` :  
    - *說明*: byIndexFlag=20
  - `intPrice1` : 第一買價 (Integer, Size: 4)
  - `intPrice2` : 第二買價 (Integer, Size: 4)
  - `intPrice3` : 第三買價 (Integer, Size: 4)
  - `intPrice4` : 第四買價 (Integer, Size: 4)
  - `intPrice5` : 第五買價 (Integer, Size: 4)
  - `dwVol1` : 第一買量 (Uint, Size: 4)
  - `dwVol2` : 第二買量 (Uint, Size: 4)
  - `dwVol3` : 第三買量 (Uint, Size: 4)
  - `dwVol4` : 第四買量 (Uint, Size: 4)
  - `dwVol5` : 第五買量 (Uint, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=21
  - `intPrice1` : 第一賣價 (Integer, Size: 4)
  - `intPrice2` : 第二賣價 (Integer, Size: 4)
  - `intPrice3` : 第三賣價 (Integer, Size: 4)
  - `intPrice4` : 第四賣價 (Integer, Size: 4)
  - `intPrice5` : 第五賣價 (Integer, Size: 4)
  - `dwVol1` : 第一賣量 (Uint, Size: 4)
  - `dwVol2` : 第二賣量 (Uint, Size: 4)
  - `dwVol3` : 第三賣量 (Uint, Size: 4)
  - `dwVol4` : 第四賣量 (Uint, Size: 4)
  - `dwVol5` : 第五賣量 (Uint, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=42
  - `intPrice1` : 第六買價 (Integer, Size: 4)
  - `intPrice2` : 第七買價 (Integer, Size: 4)
  - `intPrice3` : 第八買價 (Integer, Size: 4)
  - `intPrice4` : 第九買價 (Integer, Size: 4)
  - `intPrice5` : 第十買價 (Integer, Size: 4)
  - `dwVol1` : 第六買量 (Uint, Size: 4)
  - `dwVol2` : 第七買量 (Uint, Size: 4)
  - `dwVol3` : 第八買量 (Uint, Size: 4)
  - `dwVol4` : 第九買量 (Uint, Size: 4)
  - `dwVol5` : 第十買量 (Uint, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=43
  - `intPrice1` : 第六賣價 (Integer, Size: 4)
  - `intPrice2` : 第七賣價 (Integer, Size: 4)
  - `intPrice3` : 第八賣價 (Integer, Size: 4)
  - `intPrice4` : 第九賣價 (Integer, Size: 4)
  - `intPrice5` : 第十賣價 (Integer, Size: 4)
  - `dwVol1` : 第六賣量 (Uint, Size: 4)
  - `dwVol2` : 第七賣量 (Uint, Size: 4)
  - `dwVol3` : 第八賣量 (Uint, Size: 4)
  - `dwVol4` : 第九賣量 (Uint, Size: 4)
  - `dwVol5` : 第十賣量 (Uint, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=50
  - `intPrice1` : 第一買價 (Integer, Size: 4)
  - `intPrice2` : 第二買價 (Integer, Size: 4)
  - `intPrice3` : 第三買價 (Integer, Size: 4)
  - `intPrice4` : 第四買價 (Integer, Size: 4)
  - `intPrice5` : 第五買價 (Integer, Size: 4)
  - `dwVol1` : 第一買量 (Uint, Size: 4)
  - `dwVol2` : 第二買量 (Uint, Size: 4)
  - `dwVol3` : 第三買量 (Uint, Size: 4)
  - `dwVol4` : 第四買量 (Uint, Size: 4)
  - `dwVol5` : 第五買量 (Uint, Size: 4)
  - `intPrice1` : 第一賣價 (Integer, Size: 4)
  - `intPrice2` : 第二賣價 (Integer, Size: 4)
  - `intPrice3` : 第三賣價 (Integer, Size: 4)
  - `intPrice4` : 第四賣價 (Integer, Size: 4)
  - `intPrice5` : 第五賣價 (Integer, Size: 4)
  - `dwVol1` : 第一賣量 (Uint, Size: 4)
  - `dwVol2` : 第二賣量 (Uint, Size: 4)
  - `dwVol3` : 第三賣量 (Uint, Size: 4)
  - `dwVol4` : 第四賣量 (Uint, Size: 4)
  - `dwVol5` : 第五賣量 (Uint, Size: 4)
  - `struRecord` :  
    - *說明*: byIndexFlag=51
  - `intPrice1` : 第六買價 (Integer, Size: 4)
  - `intPrice2` : 第七買價 (Integer, Size: 4)
  - `intPrice3` : 第八買價 (Integer, Size: 4)
  - `intPrice4` : 第九買價 (Integer, Size: 4)
  - `intPrice5` : 第十買價 (Integer, Size: 4)
  - `dwVol1` : 第六買量 (Uint, Size: 4)
  - `dwVol2` : 第七買量 (Uint, Size: 4)
  - `dwVol3` : 第八買量 (Uint, Size: 4)
  - `dwVol4` : 第九買量 (Uint, Size: 4)
  - `dwVol5` : 第十買量 (Uint, Size: 4)
  - `intPrice1` : 第六賣價 (Integer, Size: 4)
  - `intPrice2` : 第七賣價 (Integer, Size: 4)
  - `intPrice3` : 第八賣價 (Integer, Size: 4)
  - `intPrice4` : 第九賣價 (Integer, Size: 4)
  - `intPrice5` : 第十賣價 (Integer, Size: 4)
  - `dwVol1` : 第六賣量 (Uint, Size: 4)
  - `dwVol2` : 第七賣量 (Uint, Size: 4)
  - `dwVol3` : 第八賣量 (Uint, Size: 4)
  - `dwVol4` : 第九賣量 (Uint, Size: 4)
  - `dwVol5` : 第十賣量 (Uint, Size: 4)

---
