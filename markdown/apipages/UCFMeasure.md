# UCFMeasure - 测量

支持长度、面积、经纬度、高度测量

## 接口一览

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFMeasure/Length](#ucfmeasurelength) | 长度测量 |
| [UCFMeasure/Area](#ucfmeasurearea) | 面积测量 |
| [UCFMeasure/GeoCoord](#ucfmeasuregeocoord) | 经纬度测量 |
| [UCFMeasure/Height](#ucfmeasureheight) | 高度测量 |
| [UCFMeasure/Cancel](#ucfmeasurecancel) | 取消测量 |
| [UCFMeasure/OnFinishOnce](#ucfmeasureonfinishonce) | 完成单次测量通知 |

<a id="ucfmeasurelength"></a>

[← 返回接口一览](#接口一览)

## 长度测量

**类型:** Sync

**Tips:**

- 支持多段连续测量，支持多次测量
- 重复激活无效，非重复激活时会清除之前的所有分析结果
- 交互逻辑：左键单击确定关键点，右键单击撤销最后一个关键点，中键单击完成单次测量(单击时的位置作为最后一个关键点)

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Length",
  "Params": {}
}
```

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 执行ID |
| Interface | String | 接口名称 |
| Status | Boolean | 操作是否成功 |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Length",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmeasurearea"></a>

[← 返回接口一览](#接口一览)

## 面积测量

**类型:** Sync

**Tips:**

- 支持多次测量
- 重复激活无效，非重复激活时会清除之前的所有分析结果
- 交互逻辑：左键单击确定关键点，右键单击撤销最后一个关键点，中键单击完成单次测量(单击时的位置作为最后一个关键点)

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Area",
  "Params": {}
}
```

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 执行ID |
| Interface | String | 接口名称 |
| Status | Boolean | 操作是否成功 |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Area",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmeasuregeocoord"></a>

[← 返回接口一览](#接口一览)

## 经纬度测量

**类型:** Sync

**Tips:**

- 支持多次测量
- 重复激活无效，非重复激活时会清除之前的所有分析结果
- 交互逻辑：左键单击确定关键点，右键单击撤销最后一个关键点

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/GeoCoord",
  "Params": {}
}
```

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 执行ID |
| Interface | String | 接口名称 |
| Status | Boolean | 操作是否成功 |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/GeoCoord",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmeasureheight"></a>

[← 返回接口一览](#接口一览)

## 高度测量

**类型:** Sync

**Tips:**

- 支持多次测量
- 重复激活无效，非重复激活时会清除之前的所有分析结果
- 交互逻辑：首次左键单击确定关键点，第二次左键单击完成单次测量，右键单击撤销首个关键点

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Height",
  "Params": {}
}
```

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 执行ID |
| Interface | String | 接口名称 |
| Status | Boolean | 操作是否成功 |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Height",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmeasurecancel"></a>

[← 返回接口一览](#接口一览)

## 取消测量

**类型:** Sync

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Cancel",
  "Params": {}
}
```

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 执行ID |
| Interface | String | 接口名称 |
| Status | Boolean | 操作是否成功 |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMeasure/Cancel",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmeasureonfinishonce"></a>

[← 返回接口一览](#接口一览)

## 完成单次测量通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFMeasure/OnFinishOnce"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| Area | Float | 仅测量类型为Area时返回, 多边形面积（m²） |
| TotalLength | Float | 仅测量类型为Length时返回, 总长度（m） |
| VerticalHeight | Float | 仅测量类型为Height时返回, 垂直高度（m） |
| Latitude | Float | 仅测量类型为GeoCoord时返回, 纬度（度） |
| Longitude | Float | 仅测量类型为GeoCoord时返回, 经度（度） |
| Altitude | Float | 仅测量类型为GeoCoord时返回, 高程（m） |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFMeasure/OnFinishOnce",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {
    "Area": 0.0,
    "TotalLength": 0.0,
    "VerticalHeight": 0.0,
    "Latitude": 0.0,
    "Longitude": 0.0,
    "Altitude": 0.0
  }
}
```
