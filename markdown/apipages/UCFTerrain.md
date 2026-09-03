# UCFTerrain - 地形分析

支持高程分析、坡度坡向分析

## 接口一览

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFTerrain/Elevation](#ucfterrainelevation) | 启用高程分析 |
| [UCFTerrain/Slope](#ucfterrainslope) | 启用坡度分析 |
| [UCFTerrain/SetShowMark](#ucfterrainsetshowmark) | 设置地形分析标识的可视性 |
| [UCFTerrain/SetOpacity](#ucfterrainsetopacity) | 设置地形分析效果透明度 |
| [UCFTerrain/SetInterval](#ucfterrainsetinterval) | 设置高程分析等高距 |
| [UCFTerrain/SetWidth](#ucfterrainsetwidth) | 设置高程分析等高线宽 |
| [UCFTerrain/SetStep](#ucfterrainsetstep) | 设置坡度分析的坡向步长 |
| [UCFTerrain/Clear](#ucfterrainclear) | 清除所有地形分析内容 |
| [UCFTerrain/Cancel](#ucfterraincancel) | 取消地形分析 |
| [UCFTerrain/OnFinishOnce](#ucfterrainonfinishonce) | 完成单次地形分析通知 |

<a id="ucfterrainelevation"></a>

[← 返回接口一览](#接口一览)

## 启用高程分析

**类型:** Sync

**Tips:**

- 重复激活无效，非重复激活时会清除之前的所有分析结果
- 交互逻辑：左键单击确定关键点，右键单击撤销最后一个关键点，中键单击完成单次分析(单击时的位置作为最后一个关键点)
- 进行高程分析的区域必须接受贴花效果
- 垂直面、反斜面等不适用，因为正交俯视深度采样，这些区域的深度值退化为阶跃函数

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
  "Interface": "UCFTerrain/Elevation",
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
  "Interface": "UCFTerrain/Elevation",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainslope"></a>

[← 返回接口一览](#接口一览)

## 启用坡度分析

**类型:** Sync

**Tips:**

- 重复激活无效，非重复激活时会清除之前的所有分析结果
- 交互逻辑：左键单击确定关键点，右键单击撤销最后一个关键点，中键单击完成单次分析(单击时的位置作为最后一个关键点)
- 进行地形分析的区域必须接受贴花效果
- 垂直面、反斜面等不适用

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
  "Interface": "UCFTerrain/Slope",
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
  "Interface": "UCFTerrain/Slope",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterrainsetshowmark"></a>

[← 返回接口一览](#接口一览)

## 设置地形分析标识的可视性

**类型:** Sync

**Tips:**

- 默认显示地形分析标识
- 高程分析时的标识即等高线与标高
- 坡度分析时的标识即坡向
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
| ShowMark | Boolean | 必填 | 地形分析标识的可视性，true即显示 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFTerrain/SetShowMark",
  "Params": {
    "ShowMark": false
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

**Tips:**

- 默认值为1像素
- 首曲线宽即设定的等高线宽，计曲线宽是首曲线宽的2倍
- 计曲线表现为自发光效果
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

**Tips:**

- 默认值为2000
- 步长越大,坡向越稀疏
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

<a id="ucfterrainclear"></a>

[← 返回接口一览](#接口一览)

## 清除所有地形分析内容

**类型:** Sync

**Tips:**

- 仅清除当前已完成的分析内容(贴花、遮罩纹理、计曲线标高等)
- 之前进行的相关属性设置会被保留
- 跟随鼠标的提示点继续显示
- 未启用地形分析时该接口无效

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
  "Interface": "UCFTerrain/Clear",
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
  "Interface": "UCFTerrain/Clear",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfterraincancel"></a>

[← 返回接口一览](#接口一览)

## 取消地形分析

**类型:** Sync

**Tips:**

- 取消后跟随鼠标的提示点会清除
- 所有与地形分析相关的资源(贴花、遮罩纹理、Widget、深度RT等)都会清除
- 之前设置的属性会重置为默认值

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
  "Interface": "UCFTerrain/Cancel",
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
  "Interface": "UCFTerrain/Cancel",
  "Status": true,
  "DebugInfo": "成功",
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
    "MinHeight": 0.0,
    "MaxHeight": 0.0
  }
}
```
