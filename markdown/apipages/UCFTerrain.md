# UCFTerrain - 地形分析

支持高程分析、坡度坡向分析

## 接口一览

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFTerrain/EnableTerrain](#ucfterrainenableterrain) | 启用地形分析 |
| [UCFTerrain/OnDoPoint](#ucfterrainondopoint) | 添加关键点操作通知 |
| [UCFTerrain/OnUndoPoint](#ucfterrainonundopoint) | 撤销关键点操作通知 |
| [UCFTerrain/OnFinishOnce](#ucfterrainonfinishonce) | 完成单次地形分析通知 |
| [UCFTerrain/SwitchType](#ucfterrainswitchtype) | 切换地形分析类别 |
| [UCFTerrain/SetShowMark](#ucfterrainsetshowmark) | 设置地形分析标识的可视性 |
| [UCFTerrain/SetOpacity](#ucfterrainsetopacity) | 设置地形分析效果透明度 |
| [UCFTerrain/SetInterval](#ucfterrainsetinterval) | 设置高程分析等高距 |
| [UCFTerrain/SetWidth](#ucfterrainsetwidth) | 设置高程分析等高线宽 |
| [UCFTerrain/SetStep](#ucfterrainsetstep) | 设置坡度分析的坡向步长 |
| [UCFTerrain/ClearOnce](#ucfterrainclearonce) | 清除单次地形分析 |
| [UCFTerrain/CancelTerrain](#ucfterraincancelterrain) | 取消地形分析 |

<a id="ucfterrainenableterrain"></a>

[← 返回接口一览](#接口一览)

## 启用地形分析

**类型:** Sync

**Tips:**

- 默认为高程分析
- 进行地形分析的区域必须接受贴花效果
- cesiumforunreal的3D Tiles加载策略限制，暂不支持cesium地形 

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Offset | Float | 选填 | 高程基准偏移值，单位cm，默认0，等于基准海平面 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/EnableTerrain",
  "Params": {
    "Offset": 0.0
  }
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
  "Interface": "UCFTerrain/EnableTerrain",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainondopoint"></a>

[← 返回接口一览](#接口一览)

## 添加关键点操作通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFTerrain/OnDoPoint"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFTerrain/OnDoPoint",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {}
}
```

<a id="ucfterrainonundopoint"></a>

[← 返回接口一览](#接口一览)

## 撤销关键点操作通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFTerrain/OnUndoPoint"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFTerrain/OnUndoPoint",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {}
}
```

<a id="ucfterrainonfinishonce"></a>

[← 返回接口一览](#接口一览)

## 完成单次地形分析通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFTerrain/OnFinishOnce"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| ID | Int | 本次地形分析对应的ID值 |
| MinHeight | Float | 本次地形分析得到的高程极小值，单位m，保留两位小数(仅高程分析时返回) |
| MaxHeight | Float | 本次地形分析得到的高程极大值，单位m，保留两位小数(仅高程分析时返回) |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFTerrain/OnFinishOnce",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {
    "ID": 0,
    "MinHeight": 0.0,
    "MaxHeight": 0.0
  }
}
```

<a id="ucfterrainswitchtype"></a>

[← 返回接口一览](#接口一览)

## 切换地形分析类别

**类型:** Sync

**Tips:**

- 默认为高程分析
- 单次地形分析进行时不允许操作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Type | Int | 必填 | 地形分析类别，0为高程分析，1为坡度分析 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SwitchType",
  "Params": {
    "Type": 0
  }
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
  "Interface": "UCFTerrain/SwitchType",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainsetshowmark"></a>

[← 返回接口一览](#接口一览)

## 设置地形分析标识的可视性

**类型:** Sync

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Status | Boolean | 必填 | 可视性，true即显示 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SetShowMark",
  "Params": {
    "Status": false
  }
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
  "Interface": "UCFTerrain/SetShowMark",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainsetopacity"></a>

[← 返回接口一览](#接口一览)

## 设置地形分析效果透明度

**类型:** Sync

**Tips:**

- 默认值为0.85
- 单次地形分析进行时不允许操作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Opacity | Int | 必填 | 透明度，取值范围[0,1] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SetOpacity",
  "Params": {
    "Opacity": 0
  }
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
  "Interface": "UCFTerrain/SetOpacity",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainsetinterval"></a>

[← 返回接口一览](#接口一览)

## 设置高程分析等高距

**类型:** Sync

**Tips:**

- 默认值为50m
- 单次地形分析进行时不允许操作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Interval | Float | 必填 | 等高距，单位cm |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SetInterval",
  "Params": {
    "Interval": 0.0
  }
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
  "Interface": "UCFTerrain/SetInterval",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainsetwidth"></a>

[← 返回接口一览](#接口一览)

## 设置高程分析等高线宽

**类型:** Sync

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Width | Float | 必填 | 等高线宽，单位像素 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SetWidth",
  "Params": {
    "Width": 0.0
  }
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
  "Interface": "UCFTerrain/SetWidth",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainsetstep"></a>

[← 返回接口一览](#接口一览)

## 设置坡度分析的坡向步长

**类型:** Sync

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Step | Float | 必填 | 坡向步长 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SetStep",
  "Params": {
    "Step": 0.0
  }
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
  "Interface": "UCFTerrain/SetStep",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainclearonce"></a>

[← 返回接口一览](#接口一览)

## 清除单次地形分析

**类型:** Sync

**Tips:**

- 单次地形分析进行时不允许操作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ID | Int | 必填 | 所要清除的地形分析ID |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/ClearOnce",
  "Params": {
    "ID": 0
  }
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
  "Interface": "UCFTerrain/ClearOnce",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterraincancelterrain"></a>

[← 返回接口一览](#接口一览)

## 取消地形分析

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
  "Interface": "UCFTerrain/CancelTerrain",
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
  "Interface": "UCFTerrain/CancelTerrain",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```
