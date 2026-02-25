# 14650012 - RptOrderTradeReportGroupIV (委託成交綜合回報IV)

## 1. 基本資訊 (Metadata)
- **Service ID**: `14650012 (20.101.0.18)`
- **COM Name**: `RptOrderTradeReportGroupIV`
- **設計描述**: 委託成交綜合回報IV
- **通訊模式**: `RQ/RP`
- **更新日期**: 2020/9/22

---

## 2. 請求結構 (Request Specification)

### JSON 結構範例
```json
{
  "ParentStruct_In": {
    "abyNoListCancel": "example",
    "uintCount": 1
  },
  "ChildStruct_In": [
    {
      "abyAccount": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct_In` : 輸入的母結構 (Object)
  - `abyNoListCancel` : 是否不列出取消單 (TByte, Size: 1)
    - `Y`: 不列
    - `N`: 列
  - `uintCount` : 筆數 (Uint, Size: 4)

- `ChildStruct_In` : 輸入的子結構 (Array of Objects)
  - `abyAccount` : 帳號 (TByte22, Size: 22)
    - *說明*: 第一個Byte為帳號種類  如:  S98875005091  FF021919F00000001X

---

## 3. 回傳結構 (Response Specification)

### JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "uintCount1": 0,
    "uintCount2": 0,
    "uintCount3": 0,
    "uintCount4": 0,
    "uintCount5": 0,
    "uintCount6": 0,
    "uintCount7": 0,
    "uintCount8": 0
  },
  "ChildStruct_Out": [
    {
      "struStkAccountInfo": "example",
      "struTradeYMD": "",
      "byMarketNo": "example",
      "abyMarketName": "example",
      "abyCompanyNo": "example",
      "abyStkName": "example",
      "shtOrderType": 0,
      "abyBS": "example",
      "lngPrice": 0,
      "abyPriceFlag": "example",
      "intBeforeQty": 0,
      "intAfterQty": 0,
      "intOkQty": 0,
      "shtOrderStatus": 0,
      "struAcceptDate": "",
      "struAcceptTime": "",
      "abyOrderNo": "example",
      "abyOrderErrorNo": "example",
      "abyEmError": "example",
      "shtSeller": 0,
      "abyChannel": "example",
      "shtAPCode": 0,
      "intOTax": 0,
      "intOCharge": 0,
      "intODueAmt": 0,
      "abyCancelFlag": "example",
      "abyReduceFlag": "example",
      "abyTraditionFlag": "example",
      "abyBasketNo": "example",
      "abyTradeCurrency": "example",
      "abyTime_in_Force": "example",
      "abyOrder_Success": "example",
      "abyReduce_Flag": "example",
      "abyChg_Prz_Flag": "example",
      "abyTSE_Cancel": "example",
      "intCancelQty": 0,
      "intOR_QTY": 0,
      "struUpdateDate": "",
      "struUpdateTime": "",
      "abyAccount": "example",
      "intOkStockNos": 0,
      "lngOPrice": 0,
      "lngSPrice": 0,
      "struDateTime": "",
      "abyPrice_Flag": "example",
      "shtExchange_Code": 0,
      "struTradeDate": "",
      "abyCommodityID1": "example",
      "intSettlementMonth1": 0,
      "intStrikePrice1": 0,
      "abyBuySellKind1": "example",
      "abyCommodityID2": "example",
      "intSettlementMonth2": 0,
      "intStrikePrice2": 0,
      "abyBuySellKind2": "example",
      "abyOpenOffsetKind": "example",
      "abyOrderCondition": "example",
      "abyOrderPrice": "example",
      "intAferQty": 0,
      "intOKQty": 0,
      "shtStatus": 0,
      "abyErrorNo": "example",
      "abyErrorMessage": "example",
      "abyOrderNO": "example",
      "abyProductType": "example",
      "ushtSeller": 0,
      "lngTotalMatFee": 0,
      "lngTotalMatExchTax": 0,
      "lngTotalMatPremium": 0,
      "abyDayTradeID": "example",
      "abyStkName1": "example",
      "abyStkName2": "example",
      "abyTRID": "example",
      "abyCurrencyType": "example",
      "abyCurrencyType2": "example",
      "byMarketNo1": "example",
      "abyStkCode1": "example",
      "byMarketNo2": "example",
      "abyStkCode2": "example",
      "intMatchQty": 0,
      "lngMatchPrice1": 0,
      "lngMatchPrice2": 0,
      "struMatchTime": "",
      "struMatchDate": "",
      "abyRecType": "example",
      "lngOrderPrice": 0,
      "lng SprMatchPrice": 0,
      "abySubNo": "example",
      "abyPriceType": "example",
      "intOrderQty": 0,
      "struOrderTime": "",
      "abyOrderType": "example",
      "intFee": 0,
      "lngPolarisAMT": 0,
      "abySettleType": "example",
      "lngMatchPrice": 0,
      "lngSettlementAMT": 0,
      "abyCommodityID": "example",
      "intSettlementMonth": 0,
      "abyBuySell": "example",
      "abyOdrPrice": "example",
      "abyTouchPrice": "example",
      "lngUtPrice": 0,
      "intUtPrice2": 0,
      "intMinPrice2": 0,
      "lngUtPrice4": 0,
      "intUtPrice5": 0,
      "intUtPrice6": 0,
      "shtMatchQty": 0,
      "abyMatchPrice": "example"
    }
  ]
}
```

### 參數說明 (Parameter Details)

- `ParentStruct1_Out` : 輸出的母結構1 (Object)
  - `uintCount1` : 現貨委託筆數 (Uint, Size: 4)
    - *說明*: # 現貨委託回報

- `ChildStruct1_Out` : 輸出的子結構1 (Array of Objects)
  - `struStkAccountInfo` : 現貨帳號 (TByte22, Size: 22)
  - `struTradeYMD` : 交易日 (TYuantaDate, Size: 4)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
    - *說明*: 上市/上櫃
  - `abyCompanyNo` : 股票代碼 (TByte12, Size: 12)
  - `abyStkName` : 股票名稱 (TByte30, Size: 30)
  - `shtOrderType` : 委託種類 (Short, Size: 2)
    - `0`: 現貨
    - `3`: 融資
    - `4`: 融券
    - `5`: 策略借券
    - `6`: 避險借券
    - `7`: 資沖
    - `8`: 券沖
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - `S`: 賣
    - `B`: 買
  - `lngPrice` : 價位 (Long, Size: 8)
    - *說明*: 前端需除以10000  (現貨小數4位,興櫃小數4位)
  - `abyPriceFlag` : 價格種類 (TByte, Size: 1)
    - `H`: 漲停
    - `L`: 跌停
    - *說明*: "-":平盤  1-市價  2-限價
  - `intBeforeQty` : 前一次委託量 (Int, Size: 4)
    - *說明*: For 委託狀態=取消成功
  - `intAfterQty` : 目前委託量 (Int, Size: 4)
    - *說明*: 委託狀態=取消成功時,委託口數為0, 前端要改讀前一次委託量  委託狀態=10or24，COM改給OR_QTY原委託量
  - `intOkQty` : 成交量 (Int, Size: 4)
  - `shtOrderStatus` : 委託狀態 (Short, Size: 2)
    - `0`: 傳輸中
    - `5`: 預約單
    - `10`: 委託失敗
    - `20`: 委託成功
    - `24`: 委託失效
    - `25`: 價穩失效
    - `30`: 取消成功
  - `struAcceptDate` : 委託日期 (TYuantaDate, Size: 4)
    - *說明*: 年月日
  - `struAcceptTime` : 委託時間 (TYuantaTime, Size: 5)
    - *說明*: 時分秒毫秒
  - `abyOrderNo` : 委託單號 (TByte5, Size: 5)
    - *說明*: "H00001"
  - `abyOrderErrorNo` : 錯誤碼 (TByte5, Size: 5)
  - `abyEmError` : 錯誤原因 (TByte120, Size: 120)
    - `Max`: 40中文
  - `shtSeller` : 營業員代碼 (Short, Size: 2)
  - `abyChannel` : Channel (TByte3, Size: 3)
  - `shtAPCode` : APCode (Short, Size: 2)
    - `0`: 現貨
    - `2`: 盤後零股
    - `7`: 盤後
    - `4`: 盤中零股
    - `99`: 盤中零股
  - `intOTax` : 證交稅 (Int, Size: 4)
  - `intOCharge` : 手續費 (Int, Size: 4)
  - `intODueAmt` : 應收付 (Int, Size: 4)
  - `abyCancelFlag` : 可取消Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'  盤中or 預約單才可取消
  - `abyReduceFlag` : 可減量Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'  盤中or 預約單才可減量
  - `abyTraditionFlag` : 傳統單Flag (TByte, Size: 1)
    - *說明*: 'Y" :傳統單
  - `abyBasketNo` : BasketNo (TByte10, Size: 10)
    - *說明*: 無值
  - `abyTradeCurrency` : 報價幣別 (TByte3, Size: 3)
    - *說明*: TWD  CNY  HKD  USD
  - `abyTime_in_Force` : 委託效期 (TByte, Size: 1)
    - `0`: 當日有效
    - `3`: IOC
    - `4`: FOK
  - `abyOrder_Success` : 委託成功旗標 (TByte, Size: 1)
  - `abyReduce_Flag` : 本委託下單是否被減量 (TByte, Size: 1)
  - `abyChg_Prz_Flag` : 本委託下單是否進行改價 (TByte, Size: 1)
  - `abyTSE_Cancel` : 本委託下單是否被交易所主動刪單 (TByte, Size: 1)
  - `intCancelQty` : 取消數量 (Int, Size: 4)
  - `intOR_QTY` : 原委託量 (Int, Size: 4)
  - `struUpdateDate` : 更新日期 (TYuantaDate, Size: 4)
    - *說明*: 年月日
  - `struUpdateTime` : 更新時間 (TYuantaTime, Size: 5)
    - *說明*: 時分秒毫秒
- `ParentStruct2_Out` : 輸出的母結構2 (Object)
  - `uintCount2` : 現貨成交筆數 (Uint, Size: 4)
    - *說明*: 現貨成交回報

- `ChildStruct2_Out` : 輸出的子結構2 (Array of Objects)
  - `abyAccount` : 現貨帳號 (TByte22, Size: 22)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCompanyNo` : 股票代碼 (TByte12, Size: 12)
  - `abyStkName` : 股票名稱 (TByte30, Size: 30)
  - `shtOrderType` : 委託種類 (Short, Size: 2)
    - `0`: 現貨
    - `3`: 融資
    - `4`: 融券
    - `5`: 策略借券
    - `6`: 避險借券
    - `7`: 資沖
    - `8`: 券沖
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - `S`: 賣
    - `B`: 買
  - `intOkStockNos` : 成交量 (Int, Size: 4)
  - `lngOPrice` : 委託價 (Long, Size: 8)
    - *說明*: 前端需除以10000  (現貨小數4位,興櫃小數4位)
  - `lngSPrice` : 成交價 (Long, Size: 8)
    - *說明*: 前端需除以10000  (現貨小數4位,興櫃小數4位)
  - `struDateTime` : 交易日 (TYuantaDateTime, Size: 9)
    - *說明*: 年月日時分秒毫秒
  - `abyOrderNo` : 委託單號 (TByte5, Size: 5)
    - *說明*: "H0001"
  - `abyTradeCurrency` : 報價幣別 (TByte3, Size: 3)
    - *說明*: TWD  CNY  HKD  USD
  - `abyPrice_Flag` : 價位Flag (TByte, Size: 1)
    - *說明*: 1-市價  2-限價
  - `shtExchange_Code` : 委託別 (Short, Size: 2)
    - *說明*: 0-一般委託  1-鉅額  2-零股  4-盤後定價  5 盤中零股
- `ParentStruct3_Out` : 輸出的母結構3 (Object)
  - `uintCount3` : 期貨委託筆數 (Uint, Size: 4)
    - *說明*: 期貨委託回報

- `ChildStruct3_Out` : 輸出的子結構3 (Array of Objects)
  - `abyAccount` : 期貨帳號 (TByte22, Size: 22)
  - `struTradeDate` : 交易日期 (TPolaDate, Size: 4)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCommodityID1` : 商品名稱1 (TByte7, Size: 7)
    - *說明*: 選擇權第7碼是C或P
  - `intSettlementMonth1` : 商品月份1 (Int, Size: 4)
  - `intStrikePrice1` : 履約價1 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyBuySellKind1` : 買賣別1 (TByte, Size: 1)
  - `abyCommodityID2` : 商品名稱2 (TByte7, Size: 7)
    - *說明*: 選擇權第7碼是C或P
  - `intSettlementMonth2` : 商品月份2 (Int, Size: 4)
  - `intStrikePrice2` : 履約價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyBuySellKind2` : 買賣別2 (TByte, Size: 1)
  - `abyOpenOffsetKind` : 新/平倉 (TByte, Size: 1)
    - `0`: 新倉
    - `1`: 平倉  2系統
  - `abyOrderCondition` : 委託條件 (TByte, Size: 1)
    - *說明*: " ":ROD  "1":FOK  "2":IOC
  - `abyOrderPrice` : 委託價 (TByte10, Size: 10)
    - `M`: 市價
    - `P`: 範圍市價
  - `intBeforeQty` : 前一次委託量 (Int, Size: 4)
    - *說明*: For 委託狀態=取消成功
  - `intAferQty` : 目前委託量 (Int, Size: 4)
    - *說明*: 委託狀態=取消成功時,委託口數為0, 前端要改讀前一次委託量
  - `intOKQty` : 成交口數 (Int, Size: 4)
  - `shtStatus` : 委託狀態 (short, Size: 2)
    - `0`: 傳輸中
    - `5`: 預約單
    - `10`: 委託失敗
    - `20`: 委託成功
    - `30`: 取消成功
  - `struAcceptDate` : 委託日期 (TYuantaDate, Size: 4)
  - `struAcceptTime` : 委託時間 (TYuantaTime, Size: 5)
  - `abyErrorNo` : 錯誤代碼 (TByte10, Size: 10)
  - `abyErrorMessage` : 錯誤訊息 (TByte120, Size: 120)
    - `Max`: 40中文
  - `abyOrderNO` : 委託單號 (TByte5, Size: 5)
  - `abyProductType` : 商品種類 (TByte, Size: 1)
    - `O`: 選擇權
    - `F`: 期貨
  - `ushtSeller` : 營業員代碼 (UShort, Size: 2)
  - `lngTotalMatFee` : 手續費總和 (Long, Size: 8)
    - *說明*: 前端除以1000
  - `lngTotalMatExchTax` : 交易稅總和 (Long, Size: 8)
    - *說明*: 前端除以1000
  - `lngTotalMatPremium` : 應收付 (Long, Size: 8)
    - *說明*: 前端除以1000
  - `abyDayTradeID` : 當沖註記 (TByte, Size: 1)
    - `Y`: 當沖
  - `abyCancelFlag` : 可取消Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'  盤中or 預約單才可取消
  - `abyReduceFlag` : 可減量Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'  盤中or 預約單才可減量
  - `abyStkName1` : 商品名稱1 (TByte30, Size: 30)
    - `Ex`: '中鋼實 06 0030 C', '台指01',' 櫃指選 03 00400 C'
  - `abyStkName2` : 商品名稱2 (TByte30, Size: 30)
    - `Ex`: '中鋼實 06 0030 C', '台指01',' 櫃指選 03 00400 C'
  - `abyTraditionFlag` : 傳統單Flag (TByte, Size: 1)
    - *說明*: 'Y" :傳統單
  - `abyTRID` : 商品代碼 (TByte20, Size: 20)
    - *說明*: FITX 200709,
    - *說明*: URO200709,  FIGTL7/C8,
    - *說明*: TXO09000T7,
    - *說明*: TXO08000/08100U7
  - `abyCurrencyType` : 交易幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
    - `USD`: 美元
  - `abyCurrencyType2` : 交割幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
    - `USD`: 美元
  - `abyBasketNo` : BasketNo (Tbyte10, Size: 10)
  - `byMarketNo1` : 市場代碼1 (Byte, Size: 1)
    - *說明*: \<第1支腳\>
  - `abyStkCode1` : 行情股票代碼1 (TByte12, Size: 12)
    - *說明*: \<第1支腳\>
  - `byMarketNo2` : 市場代碼2 (Byte, Size: 1)
    - *說明*: \<第2支腳\>
  - `abyStkCode2` : 行情股票代碼2 (TByte12, Size: 12)
    - *說明*: \<第2支腳\>
- `ParentStruct4_Out` : 輸出的母結構4 (Object)
  - `uintCount4` : 期貨成交筆數 (Uint, Size: 4)
    - *說明*: # 期貨成交回報

- `ChildStruct4_Out` : 輸出的子結構4 (Array of Objects)
  - `abyAccount` : 期貨帳號 (TByte22, Size: 22)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCommodityID1` : 商品名稱1 (TByte7, Size: 7)
    - *說明*: 選擇權第7碼是C或P
  - `intSettlementMonth1` : 商品月份1 (Int, Size: 4)
  - `abyBuySellKind1` : 買賣別1 (TByte, Size: 1)
  - `intMatchQty` : 成交口數 (Int, Size: 4)
  - `lngMatchPrice1` : 成交價1 (Long, Size: 8)
    - *說明*: 前端需除以10000
  - `lngMatchPrice2` : 成交價2 (Long, Size: 8)
    - *說明*: 前端需除以10000
  - `struMatchTime` : 成交時間 (TYuantaTime, Size: 5)
  - `struMatchDate` : 成交日期 (TYuantaDate, Size: 4)
  - `abyOrderNO` : 委託單號 (TByte5, Size: 5)
  - `intStrikePrice1` : 履約價1 (int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyCommodityID2` : 商品名稱2 (TByte7, Size: 7)
    - *說明*: 選擇權第7碼是C或P
  - `intSettlementMonth2` : 商品月份2 (Int, Size: 4)
  - `abyBuySellKind2` : 買賣別2 (TByte, Size: 1)
  - `intStrikePrice2` : 履約價2 (Int, Size: 4)
    - *說明*: 前端需除以1000
  - `abyRecType` : 單式單/複式單 (TByte, Size: 1)
    - *說明*: "1":單式  "2":複式
  - `abyProductType` : 商品種類 (TByte, Size: 1)
  - `lngOrderPrice` : 委託價 (Long, Size: 8)
    - *說明*: 前端需除以10000
  - `abyStkName1` : 商品名稱1 (TByte30, Size: 30)
    - `Ex`: '中鋼實 06 0030 C', '台指01',' 櫃指選 03 00400 C'
  - `abyStkName2` : 商品名稱2 (TByte30, Size: 30)
    - `Ex`: '中鋼實 06 0030 C', '台指01',' 櫃指選 03 00400 C'
  - `abyDayTradeID` : 當沖註記 (TByte, Size: 1)
  - `lng SprMatchPrice` : 複式單成交價 (Long, Size: 8)
    - *說明*: 前端需除以10000
  - `abyTRID` : 商品代碼 (TByte20, Size: 20)
    - *說明*: 2854, 05311
    - *說明*: FITX 200709,
    - *說明*: URO200709,  FIGTL7/C8,
    - *說明*: TXO09000T7,
    - *說明*: TXO08000/08100U7
  - `abyCurrencyType` : 交易幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
    - `USD`: 美元
  - `abyCurrencyType2` : 交割幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
    - `USD`: 美元
  - `abySubNo` : 子成交序號 (TByte, Size: 1)
    - *說明*: 0(單式)  1(複式腳1)  2(複式腳2)
- `ParentStruct5_Out` : 輸出的母結構5 (Object)
  - `uintCount5` : 國外股票委託筆數 (Uint, Size: 4)
    - *說明*: # 國外股票回報

- `ChildStruct5_Out` : 輸出的子結構5 (Array of Objects)
  - `abyAccount` : 證券帳號 (TByte22, Size: 22)
  - `struTradeYMD` : 交易日 (TYuantaDate, Size: 4)
    - *說明*: 西元年
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCompanyNo` : 股票代碼 (TByte12, Size: 12)
  - `abyStkName` : 股票名稱 (TByte30, Size: 30)
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - `S`: 賣
    - `B`: 買
  - `abyCurrencyType` : 交易幣別 (TByte3, Size: 3)
    - `USD`: 美元
    - `HDK`: 港幣
  - `lngPrice` : 委託價 (Long, Size: 8)
    - *說明*: 前端需除以10000
    - *說明*: (港股小數3位,美股小數4位)
  - `abyPriceType` : 價格型態 (TByte3, Size: 3)
    - *說明*: 'LMT':限價單
  - `intOrderQty` : 委託量 (Int, Size: 4)
    - *說明*: 股數
  - `intMatchQty` : 成交量 (Int, Size: 4)
  - `shtOrderStatus` : 狀態碼 (short, Size: 2)
    - `0`: 傳輸中
    - `5`: 預約單
    - `10`: 委託失敗
    - `20`: 委託成功
    - `30`: 取消成功
  - `struOrderTime` : 委託時間 (TYuantaDateTime, Size: 9)
  - `abyOrderType` : 委託單型態 (TByte3, Size: 3)
    - `DAY`: 當日有效單
    - `GTD`: 指定日期單
  - `abyOrderNo` : 委託書編號 (TByte7, Size: 7)
  - `intFee` : 手續費 (Int, Size: 4)
    - *說明*: 前端需除以10000
  - `lngPolarisAMT` : 應收付金額 (Long, Size: 8)
    - *說明*: 前端需除以10000
  - `abyOrderErrorNo` : 錯誤碼 (TByte8, Size: 8)
  - `abyEmError` : 錯誤原因 (TByte180, Size: 180)
    - `Max`: 60中文
  - `abyCurrencyType2` : 交割幣別 (TByte3, Size: 3)
    - `USD`: 美元
    - `HDK`: 港幣
  - `abyCancelFlag` : 可取消Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'  盤中or 預約單才可取消
  - `abyReduceFlag` : 可減量Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'
    - *說明*: ＊美股不提供改量改價功能,由元件固定回N
  - `abyTraditionFlag` : 傳統單Flag (TByte, Size: 1)
    - *說明*: 'Y" :傳統單
  - `abySettleType` : 交割方式 (TByte, Size: 1)
    - `0`: 外幣
    - `1`: 台幣
  - `abyBasketNo` : BasketNo (Tbyte10, Size: 10)
- `ParentStruct6_Out` : 輸出的母結構6 (Object)
  - `uintCount6` : 國外股票成交筆數 (Uint, Size: 4)
    - *說明*: # 國外股票成交回報

- `ChildStruct6_Out` : 輸出的子結構6 (Array of Objects)
  - `abyAccount` : 現貨帳號 (TByte22, Size: 22)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCompanyNo` : 股票代碼 (TByte12, Size: 12)
  - `abyStkName` : 股票名稱 (TByte30, Size: 30)
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - `S`: 賣
    - `B`: 買
  - `abyCurrencyType` : 交易幣別 (TByte3, Size: 3)
    - `USD`: 美元
    - `HDK`: 港幣
  - `intMatchQty` : 成交量 (Int, Size: 4)
  - `lngOrderPrice` : 委託價 (Long, Size: 8)
    - *說明*: 前端需除以10000
    - *說明*: (港股小數3位,美股小數4位)
  - `lngMatchPrice` : 成交價 (Long, Size: 8)
    - *說明*: 前端需除以10000
    - *說明*: (港股小數3位,美股小數4位)
  - `struDateTime` : 成交時間 (TYuantaDateTime, Size: 9)
  - `intFee` : 手續費 (Int, Size: 4)
    - *說明*: 前端需除以10000
  - `abyOrderNo` : 委託單號 (TByte7, Size: 7)
  - `lngSettlementAMT` : 成交金額 (Long, Size: 8)
    - *說明*: 前端需除以10000 (含手續費)
  - `abyCurrencyType2` : 交割幣別 (TByte3, Size: 3)
    - `USD`: 美元
    - `HDK`: 港幣
- `ParentStruct7_Out` : 輸出的母結構7 (Object)
  - `uintCount7` : 國際期貨委託筆數 (Uint, Size: 4)
    - *說明*: # 國際期貨委託回報

- `ChildStruct7_Out` : 輸出的子結構7 (Array of Objects)
  - `abyAccount` : 期貨帳號 (TByte22, Size: 22)
  - `struTradeYMD` : 交易日 (TYuantaDate, Size: 4)
    - *說明*: 西元年
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCommodityID` : 商品代碼 (TByte7, Size: 7)
    - *說明*: URO,JGL
  - `intSettlementMonth` : 商品年月 (Int, Size: 4)
    - *說明*: 200909
  - `abyStkName` : 商品名稱 (TByte30, Size: 30)
  - `abyBuySell` : 買賣別 (TByte, Size: 1)
    - *說明*: "B":買  "S":賣
  - `abyOrderType` : 委託方式 (TByte3, Size: 3)
    - `LMT`: 限價單
    - `MKT`: 市價單
    - `STP`: 停損市價單
    - `SWL`: 停損限價單
  - `abyOdrPrice` : 委託價 (TByte14, Size: 14)
    - *說明*: 000116'21.75
  - `abyTouchPrice` : 停損執行價 (TByte14, Size: 14)
    - *說明*: 000116'21.75
  - `intOrderQty` : 委託口數 (int, Size: 4)
  - `intMatchQty` : 成交口數 (int, Size: 4)
  - `shtOrderStatus` : 狀態碼 (short, Size: 2)
    - `0`: 傳輸中
    - `5`: 預約單
    - `10`: 委託失敗
    - `20`: 委託成功
    - `30`: 取消成功
  - `struAcceptDate` : 委託日期 (TYuantaDate, Size: 4)
  - `struAcceptTime` : 委託時間 (TYuantaTime, Size: 5)
  - `abyErrorNo` : 錯誤代碼 (TByte10, Size: 10)
  - `abyErrorMessage` : 錯誤訊息 (TByte120, Size: 120)
    - `Max`: 40中文
  - `abyOrderNo` : 委託書編號 (TByte8, Size: 8)
    - *說明*: AA0484
  - `abyDayTradeID` : 當沖註記 (TByte, Size: 1)
    - `Y`: 當沖
  - `abyCancelFlag` : 可取消Flag (TByte, Size: 1)
    - *說明*: 'Y'/'N'  盤中or 預約單才可取消
  - `abyReduceFlag` : 可減量Flag (TByte, Size: 1)
    - *說明*: 國際期貨目前無提供減量  'P':可改價
  - `lngUtPrice` : 委託價格整數位 (Long, Size: 8)
    - *說明*: /10000  市價或市價停損單= 0  \<For 取消下單時使用\>
  - `intUtPrice2` : 委託價格分子 (Int, Size: 4)
    - *說明*: /10000  \<For 取消下單時使用\>
  - `intMinPrice2` : 委託價格分母 (Int, Size: 4)
    - *說明*: \<For 取消下單時使用\>
  - `lngUtPrice4` : 停損執行價整數位 (Long, Size: 8)
    - *說明*: /10000  非停損單=0  \<For 取消下單時使用\>
  - `intUtPrice5` : 停損執行價格分子 (Int, Size: 4)
    - *說明*: /10000  \<For 取消下單時使用\>
  - `intUtPrice6` : 停損執行價格分母 (Int, Size: 4)
    - *說明*: \<For 取消下單時使用\>
  - `abyTraditionFlag` : 傳統單Flag (TByte, Size: 1)
    - *說明*: 'Y" :傳統單
  - `abyBasketNo` : BasketNo (Tbyte10, Size: 10)
  - `byMarketNo1` : 市場代碼1 (Byte, Size: 1)
  - `abyStkCode1` : 行情股票代碼1 (TByte12, Size: 12)
  - `abyCurrencyType` : 交易幣別 (TByte3, Size: 3)
  - `abyCurrencyType2` : 交割幣別 (TByte3, Size: 3)
- `ParentStruct8_Out` : 輸出的母結構8 (Object)
  - `uintCount8` : 國際期貨成交筆數 (Uint, Size: 4)
    - *說明*: # 國際期貨成交回報

- `ChildStruct8_Out` : 輸出的子結構8 (Array of Objects)
  - `abyAccount` : 期貨帳號 (TByte22, Size: 22)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyMarketName` : 市場名稱 (TByte30, Size: 30)
  - `abyCommodityID` : 商品代碼 (TByte7, Size: 7)
    - *說明*: URO,JGL
  - `intSettlementMonth` : 商品年月 (Int, Size: 4)
    - *說明*: 200909
  - `abyStkName` : 商品名稱 (TByte30, Size: 30)
  - `abyBuySell` : 買賣別 (TByte, Size: 1)
    - *說明*: "B":買  "S":賣
  - `shtMatchQty` : 成交口數 (int, Size: 4)
  - `abyOdrPrice` : 委託價 (TByte14, Size: 14)
    - *說明*: 000116'21.75
  - `abyMatchPrice` : 成交價 (TByte14, Size: 14)
    - *說明*: 000116'21.75
  - `struMatchDate` : 成交日期 (TYuantaDate, Size: 4)
  - `struMatchTime` : 成交時間 (TYuantaTime, Size: 5)
  - `abyOrderNo` : 委託書編號 (TByte8, Size: 8)
    - *說明*: AA0484
  - `abyCurrencyType` : 交易幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
    - `USD`: 美元
  - `abyCurrencyType2` : 交割幣別 (TByte3, Size: 3)
    - `NTD`: 台幣
    - `USD`: 美元

---
