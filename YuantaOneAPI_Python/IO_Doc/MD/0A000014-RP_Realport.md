# 0A000014 - RP_Realport (即時回報)

## 1. 基本資訊 (Metadata)
- **Service ID**: `0A000014` (10.0.0.20)
- **COM Name**: `RP_Realport`
- **設計描述**: 即時回報
- **通訊模式**: `RQ/RP` (Request / Response)
- **更新日期**: 2020/01/10

---

## 2. 請求結構 (Request Specification)

### 2.1 JSON 結構範例
```json
{
  "ParentStruct_In": {
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

- `ParentStruct_In` : 母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)
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
      "bytRptType": 50,
      "abyOrderNo": "0000A12345",
      "byMarketNo": 1,
      "abyCompanyNo": "2854",
      "...": "..."
    },
    {
      "abyAccount": "12345678901",
      "bytRptType": 2,
      "abyOrderNo": "0000B23456",
      "byMarketNo": 2,
      "abyCompanyNo": "FITX 200709",
      "...": "..."
    }
  ]
}
```

### 3.2 參數說明 (Parameter Details)

- `ParentStruct_Out` : 輸出的母結構 (Object)
  - `uintCount` : 筆數 (Uint, Size: 4)
    - *說明*: 代表本次 API 總共回傳了多少筆 `ChildStruct_Out` 明細。

- `ChildStruct_Out` : 明細陣列 (Array of Objects)
  - `abyAccount` : 帳號 (TByte22, Size: 22)
  - `bytRptType` : 回報類別 (byte, Size: 1)
    - `07`: 期貨改價回報
    - `10`: 選擇權委託回報
    - `11`: 單式成交回報
    - `12`: 複式成交回報
    - `13`: 選擇權減量取消回報
    - `17`: 選擇權改價回報
    - `21`: 組合拆解回報
    - `22`: 改變新/平倉回報
    - `30`: 海外期貨委託
    - `31`: 海外期貨成交
    - `32`: 海外期貨風控委託失敗單
    - `40`: 海外股票委託
    - `41`: 海外股票委託取消
    - `42`: 海外股票委託回覆
    - `43`: 海外股票委託取消回覆
    - `44`: 海外股票成交
    - `50`: 股票委託
    - `51`: 股票成交
    - `2`: 期貨委託
    - `3`: 期貨成交
    - `4`: 期貨價差成交回報
    - `5`: 期貨委託減量取消
  - `abyOrderNo` : 委託單號 (Tbyte20, Size: 20)
  - `byMarketNo` : 市場代碼 (Byte, Size: 1)
  - `abyCompanyNo` : 商品代碼 (TByte20, Size: 20)
    - *範例*: `2854`, `05311`, `FITX 200709`, `URO200709`, `FIGTL7/C8`, `TXO09000T7`, `TXO08000/08100U7`
  - `abyStkCName` : 股票名稱 (TByte20, Size: 20)
  - `struOrderDate` : 交易日 (TYuantaDate, Size: 4)
  - `struOrderTime` : 交易時間 (TYuantaTime, Size: 5)
    - *說明*: 委託時間 / 成交時間
  - `abyOrderType` : 委託種類 (TByte3, Size: 3)
    - **現貨**: `0`:普通, `1,3`:資, `2,4`:券, `5`:策略借券, `6`:避險借券, `7`:資沖, `8`:券沖
    - **期權**: `M`:市價, `L`:限價, `P`:範圍市價
    - **海外期**: `LMT`:限價單, `MKT`:市價單, `STP`:停損單, `SWL`:停損限價單, `CXL`:取消單
    - **海外股票**: `1`:Market, `2`:Limit 限價單
  - `abyBS` : 買賣別 (TByte, Size: 1)
    - `B`: 買
    - `S`: 賣
  - `abyPrice` : 價位 (TByte14, Size: 14)
    - *說明*: 委託價 / 成交價
    - *範例*: `23.50`, `1.0585`
    - *範例 (海外期)*: `0000125'23.5`
  - `abyTouchPrice` : 停損執行價 (TByte14, Size: 14)
    - *範例*: `000116'21.75`
  - `intBeforeQty` : 改量前數量 (Int, Size: 4)
  - `intOrderQty` : 數量 (Int, Size: 4)
    - *說明*: 委託股數 / 成交股數
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
    - *範例*: `P201`
    - *說明*: 證券錯誤碼改 5 碼，使用另一欄位
  - `bytTradeKind` : 交易性質 (byte, Size: 1)
    - **現貨**: `1`:B, `2`:S, `3`:改量, `4`:取消, `5`:查詢, `6`:改價, `9`:交易所主動刪單
    - **期權**: `1`:新增, `2`:減量, `3`:取消, `5`:查詢, `6`:改價
  - `byAPCode` : 委託類別 (byte, Size: 1)
    - **現貨**: `0`:現股, `2`:零股, `4`:盤中零股, `7`:盤後
    - **組合拆解回報**: `83`:拆解, `67`:組合
    - **改變新/平倉回報**: `83`:新轉平, `79`:平轉新
  - `abyBasketNo` : 一籃子下單編號 (TByte32, Size: 32)
  - `byOrderStatus` : 即回資料狀態 (Byte, Size: 1)
    - `0`: 委託成功
    - `1`: 委託失敗
    - `2`: 取消成功
    - `3`: 取消失敗
    - `4`: 減量成功
    - `5`: 減量失敗
    - `6`: 查詢成功
    - `7`: 查詢失敗
    - `8`: 已成交
    - `10`: 組合成功
    - `11`: 拆解成功
    - `12`: 平轉新
    - `13`: 新轉平
    - `18`: 委託收到
    - `19`: 取消收到(國外股票)
    - `20`: 改價成功
    - `21`: 改價失敗
    - `23`: 取消成交 (國外股票)
    - `24`: 委託失效
    - `25`: 價穩失效
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
  - `uintSeqNo` : 成交序號 (Uint, Size: 4)
    - *說明*: For 股票,期貨成交單 (複委託,國際期 -> 0)。若 `byOrderStatus` = 25 並且 `abyStkErrCode` = 13051、19351，此欄位會帶入成交數量。
  - `abyPriceType` : 價格型態 (TByte, Size: 1)
    - *說明*: 只有證券使用
    - `1`: 市價
    - `2`: 限價
    - `H`: 漲停
    - `L`: 跌停
    - `-`: 平盤
  - `abyStkErrCode` : 證券回報錯誤碼 (TByte5, Size: 5)
