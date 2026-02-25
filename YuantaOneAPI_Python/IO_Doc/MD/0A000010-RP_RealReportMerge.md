# 0A000010 - RP_RealReportMerge (即時回報彙總)

## 1. 基本資訊 (Metadata)
- **Service ID**: `0A000010` (10.0.0.16)
- **COM Name**: `RP_RealReportMerge`
- **設計描述**: 即時回報彙總
- **通訊模式**: `RQ/RP` (Request / Response)
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### 2.1 JSON 結構範例
```json
{
  "ParentStruct_In": {
    "abyConditionFlag": 0,
    "byMarketNo": 0,
    "abyCompanyNo": "",
    "uintCount": 1
  },
  "ChildStruct_In": [
    {
      "abyAccount": "12345678901"
    }
  ]
}
```

### 2.2 參數說明 (Parameter Details)

- `ParentStruct_In` : 母結構，定義查詢的巨觀主條件 (Object)
  - `abyConditionFlag` : 條件標記 (Byte, Size: 1)
    - `0`: Select All
    - `1`: 不列取消單
    - `2`: 不列成交單
    - `3`: 不列取消 & 成交單
    - `4`: 不列失敗單
    - `5`: 不列取消 & 失敗單
    - `6`: 不列成交 & 失敗單
    - `7`: 不列取消 & 成交 & 失敗
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
    - *說明*: 若市場代碼 `= 0` ，則查詢該委託的全部股票。
  - `abyCompanyNo` : 商品代碼 (TByte20, Size: 20)
    - *範例*: `2854`, `05311`, `FITX 200709`, `FIGTL7/C8`, `TXO09000T7`
  - `uintCount` : 記錄筆數 (Uint, Size: 4)
    - *說明*: 宣告後方 `ChildStruct_In` 將傳入多少個子結構陣列物件。

- `ChildStruct_In` : 子結構陣列，總長度需與母結構 `uintCount` 相同 (Array of Objects)
  - `abyAccount` : 帳號 (TByte22, Size: 22)
    - *說明*: 現貨、期貨帳號

---

## 3. 回傳結構 (Response Specification)

### 3.1 JSON 結構範例
```json
{
  "ParentStruct_Out": {
    "uintCount": 2
  },
  "ChildStruct_Out": [
    {
      "abyAccount": "12345678901",
      "bytRptFlag": 1,
      "abyCompanyNo": "2854",
      "shtOrderStatus": 20,
      "abyOrderNo": "0000A12345",
      "...": "..."
    },
    {
      "abyAccount": "12345678901",
      "bytRptFlag": 2,
      "abyCompanyNo": "FITX 200709",
      "shtOrderStatus": 8,
      "abyOrderNo": "0000B23456",
      "...": "..."
    }
  ]
}
```

### 3.2 參數說明 (Parameter Details)

- `ParentStruct_Out` : 輸出的母結構 (Object)
  - `uintCount` : 回報總筆數 (Uint, Size: 4)
    - *說明*: 代表本次 API 總共回傳了多少筆 `ChildStruct_Out` 明細。

- `ChildStruct_Out` : 明細陣列 (Array of Objects)
  - `abyAccount` : 帳號 (TByte22, Size: 22)
  - `bytRptFlag` : 回報標記 (Byte, Size: 1)
    - `1`: 股票
    - `2`: 期貨
    - `3`: 選擇權
    - `4`: 海外期貨
    - `5`: 海外股票
  - `abyOrderNo` : 委託單號 (TByte20, Size: 20)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyCompanyNo` : 商品代碼 (TByte20, Size: 20)
    - *範例*: `2854`, `FITX 200709`
  - `struOrderDate` : 交易日 (TYuantaDate, Size: 4)
  - `struOrderTime` : 委託時間 (TYuantaTime, Size: 5)
  - `abyOrderType` : 委託種類 (TByte3, Size: 3)
    - **現貨**: `0`:普通, `1,3`:資, `2,4`:券, `5`:策略借券, `6`:避險借券, `7`:資沖, `8`:券沖
    - **期權**: `M`:市價, `L`:限價, `P`:範圍市價
    - **海外期**: `LMT`:限價單, `MKT`:市價單, `STP`:停損單, `SWL`:停損限價單, `CXL`:取消單
    - **海外股票**: `1`:Market, `2`:Limit 限價單
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - `B`: 買
    - `S`: 賣
  - `abyOrderPrice` : 委託價 (TByte14, Size: 14)
    - *範例*: `23.50`, `1.0585`
    - *範例 (海外期)*: `0000125'23.5`
  - `abyTouchPrice` : 停損執行價 (TByte14, Size: 14)
    - *範例*: `000116'21.75`
  - `abyLastDealPrice` : 最新成交價 (TByte14, Size: 14)
  - `abyAvgDealPrice` : 成交均價 (TByte14, Size: 14)
  - `intBeforeQty` : 改量前數量 (Int, Size: 4)
  - `intOrderQty` : 委託股/口數 (Int, Size: 4)
    - *說明*: 此為有效數量(含成交)。
  - `intOkQty` : 成交股/口數 (Int, Size: 4)
  - `abyOpenOffsetKind` : 新增/沖銷別 (TByte, Size: 1)
    - **期貨**: `0`:新增, `1`:沖銷, `2`:新倉且當日沖銷單
    - **選擇權**: `0`:新增, `1`:沖銷
    - **海外股票 (SettleType)**: `0`:外幣, `1`:台幣
  - `abyDayTrade` : 當沖記號 (TByte, Size: 1)
    - **證券**: ` ` (空白) 或 `X`
    - **期權**: ` ` (空白) 或 `Y`
  - `abyOrderCond` : 委託條件 (TByte, Size: 1)
    - **證券**: `0`:ROD, `3`:IOC, `4`:FOK
    - **期權**: `R`:ROD, `I`:IOC, `F`:FOK
    - **海外期**: `0`:DAY, `1`:FOK, `2`:IOC, `N`:非GTC單
    - **海外股票**: `0`:DAY, `3`:IOC, `4`:FOK
  - `abyOrderErrorNo` : 錯誤碼 (TByte4, Size: 4)
    - *說明*: 證券以外的錯誤碼。
  - `byAPCode` : 委託類別 (Byte, Size: 1)
    - **現貨**: `0`:現股, `2`:零股, `4`:盤中零股, `7`:盤後, `99`:興櫃
  - `shtOrderStatus` : 狀態碼 (Short, Size: 2)
    - `0`: 傳輸中
    - `5`: 預約單
    - `10`: 委託失敗
    - `20`: 委託成功
    - `24`: 委託失效
    - `25`: 價穩失效
    - `30`: 取消
  - `byLastOrderStatus` : 最新一筆即回資料狀態 (Byte, Size: 1)
    - `0`: 委託成功
    - `1`: 委託失敗
    - `2`: 取消成功
    - `3`: 取消失敗
    - `4`: 減量成功
    - `5`: 減量失敗
    - `6`: 查詢成功
    - `7`: 查詢失敗
    - `8`: 已成交
    - `10`: 組合成功 (1:0 組合成功)
    - `11`: 拆解成功
    - `12`: 平轉新
    - `13`: 新轉平
    - `18`: 委託收到
    - `19`: 取消收到 (國外股票)
    - `20`: 改價成功
    - `21`: 改價失敗
    - `23`: 取消成交 (國外股票)
    - `24`: 委託失效
    - `25`: 價穩失效
  - `abyStkCName` : 商品名稱 (TByte20, Size: 20)
  - `abyTradeCode` : 實體交易代號 (TByte20, Size: 20)
    - *說明*: TradeCode 放下單格式。
    - *台股證券*: `"2854"`, `"03038"`, `"03152P"`
    - *台股期權*: `"FITX 200903"`, `"XIO C200811"` (商品名稱[6] + 買賣權[1] + 商品年月[6])
    - *港股證券*: `"0001"`, `"14200"`
    - *港股期權*: `"HSIK8"`, `"HSI19800K8"`, `"HSI198I8/194U8"`
    - *美股*: `"A"`, `"MSFT"`
  - `uintStrikePrice` : 履約價 (uInt, Size: 4)
    - *備註*: 前端接數須除以 `10000`。
  - `abyBasketNo` : 一籃子下單編號 (TByte32, Size: 32)
  - `byStkType1` : 屬性 1 (Byte, Size: 1)
    - `Bit 1`: 管理商品
    - `Bit 2`: 交易記號
    - `Bit 3`: 受益憑證
    - `Bit 4`: ETF商品
    - `Bit 5`: 權證記號
    - `Bit 6`: 特別股
    - `Bit 7`: 存託憑證
    - `Bit 8`: 外國股票
  - `byStkType2` : 屬性 2 (Byte, Size: 1)
    - `Bit 1`: 可轉換公司債
    - `Bit 2`: 附認股權公司債
    - `Bit 3`: 警示股
    - `Bit 4`: 指數記號
    - `Bit 5`: 期貨
    - `Bit 6`: 個股選擇權
    - `Bit 7`: 指數選擇權
    - `Bit 8`: 保留
  - `byBelongMarketNo` : 所屬市場代碼 (Byte, Size: 1)
  - `abyBelongStkCode` : 所屬股票代碼 (TByte12, Size: 12)
  - `abyStkOrderType` : 委託價格種類 (證券使用) (TByte, Size: 1)
    - `1`: 市價
    - `2`: 限價
    - `H`: 漲停
    - `L`: 跌停
    - `-`: 平盤
  - `abyStkOrderErrorNo` : 證券回報錯誤碼 (TByte5, Size: 5)
    - *說明*: 證券專用的錯誤碼。
