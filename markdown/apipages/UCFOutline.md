# UCFOutline - 高亮管理

支持按Tag区分多个对象高亮，支持区域高亮

## 接口一览

### 对象高亮

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFOutline/OutlineActor](#ucfoutlineoutlineactor) | 高亮Actor |
| [UCFOutline/ApplyOutlineDefault](#ucfoutlineapplyoutlinedefault) | 应用默认高亮Actor效果 |
| [UCFOutline/SetOutlineFill](#ucfoutlinesetoutlinefill) | 设置高亮填充 |
| [UCFOutline/SetOutlineBeat](#ucfoutlinesetoutlinebeat) | 设置高亮频闪 |
| [UCFOutline/SetOutlineWidth](#ucfoutlinesetoutlinewidth) | 设置高亮描边线宽 |
| [UCFOutline/SetOutlineWidthRef](#ucfoutlinesetoutlinewidthref) | 设置高亮描边线宽距离基准 |
| [UCFOutline/SetOutlineEmissive](#ucfoutlinesetoutlineemissive) | 设置高亮自发光 |
| [UCFOutline/SetOutlineOpacity](#ucfoutlinesetoutlineopacity) | 设置高亮透明度 |
| [UCFOutline/UnOutlineActor](#ucfoutlineunoutlineactor) | 取消Actor高亮 |
| [UCFOutline/UnOutlineAllActor](#ucfoutlineunoutlineallactor) | 取消所有Actor高亮 |

### 区域高亮

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFOutline/OutlineArea](#ucfoutlineoutlinearea) | 高亮多边形区域 |
| [UCFOutline/ApplyAreaDefault](#ucfoutlineapplyareadefault) | 应用默认多边形区域效果 |
| [UCFOutline/SetOutGray](#ucfoutlinesetoutgray) | 设置多边形外区域的去色强度 |
| [UCFOutline/SetOutColor](#ucfoutlinesetoutcolor) | 设置多边形外区域的颜色 |
| [UCFOutline/SetAreaFill](#ucfoutlinesetareafill) | 设置多边形区域填充 |
| [UCFOutline/SetAreaOpacity](#ucfoutlinesetareaopacity) | 设置多边形区域填充透明度 |
| [UCFOutline/SetAreaColor](#ucfoutlinesetareacolor) | 设置多边形区域填充颜色 |
| [UCFOutline/SetAreaEmissive](#ucfoutlinesetareaemissive) | 设置多边形区域填充自发光强度 |
| [UCFOutline/UnOutlineArea](#ucfoutlineunoutlinearea) | 取消高亮多边形区域 |

<a id="ucfoutlineoutlineactor"></a>

[← 返回接口一览](#接口一览)

## 高亮Actor

**类型:** Sync

**Tips:**

- 可重复调用更新高亮颜色，累计高亮颜色值不得超过256种
- 若该Actor上有多个Tag符合，按第一个符合的Tag对应颜色值高亮
- 若同时启用高亮Area，高亮Actor优先

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ColorTag | `Array<Object>` | 必填 | 高亮颜色与对应的Tag |
| {}.Color | Object | 必填 | 高亮颜色 |
| Color.R | Int | 必填 | R通道值，取值范围[0,255] |
| Color.G | Int | 必填 | G通道值，取值范围[0,255] |
| Color.B | Int | 必填 | B通道值，取值范围[0,255] |
| {}.Tag | `Array<String>` | 必填 | 高亮颜色对应的Tag |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/OutlineActor",
  "Params": {
    "ColorTag": [
      {
        "Color": {
          "R": 0,
          "G": 0,
          "B": 0
        },
        "Tag": [
          "xxx",
          "xxx",
          "xxx"
        ]
      },
      {
        "Color": {
          "R": 0,
          "G": 0,
          "B": 0
        },
        "Tag": [
          "xxx",
          "xxx",
          "xxx"
        ]
      },
      {
        "Color": {
          "R": 0,
          "G": 0,
          "B": 0
        },
        "Tag": [
          "xxx",
          "xxx",
          "xxx"
        ]
      }
    ]
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
  "Interface": "UCFOutline/OutlineActor",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1z2GK6EEQ4/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlineapplyoutlinedefault"></a>

[← 返回接口一览](#接口一览)

## 应用默认高亮Actor效果

**类型:** Sync

**Tips:**

- OutlineOpacity：1
- OutlineEmissive：1
- OutlineFill：false
- OutlineBeat：false
- OutlineWidth：1.5
- OutlineWidthRef：5000

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
  "Interface": "UCFOutline/ApplyOutlineDefault",
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
  "Interface": "UCFOutline/ApplyOutlineDefault",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetoutlinefill"></a>

[← 返回接口一览](#接口一览)

## 设置高亮填充

**类型:** Sync

**Tips:**

- 启用高亮填充后整个Actor被高亮，无单独描边效果

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| OutlineFill | Boolean | 必填 | 高亮填充开关 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutlineFill",
  "Params": {
    "OutlineFill": false
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
  "Interface": "UCFOutline/SetOutlineFill",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1FyGK6DEqh/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlinesetoutlinebeat"></a>

[← 返回接口一览](#接口一览)

## 设置高亮频闪

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
| OutlineBeat | Boolean | 必填 | 高亮频闪开关 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutlineBeat",
  "Params": {
    "OutlineBeat": false
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
  "Interface": "UCFOutline/SetOutlineBeat",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1z2GK6EExh/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlinesetoutlinewidth"></a>

[← 返回接口一览](#接口一览)

## 设置高亮描边线宽

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
| OutlineWidth | Float | 必填 | 高亮描边线宽（像素），取值范围[0.5,5] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutlineWidth",
  "Params": {
    "OutlineWidth": 0.0
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
  "Interface": "UCFOutline/SetOutlineWidth",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetoutlinewidthref"></a>

[← 返回接口一览](#接口一览)

## 设置高亮描边线宽距离基准

**类型:** Sync

**Tips:**

- 高亮描边线宽为像素单位，由于透视投影的存在，物体离相机越远，其在屏幕上占据的总像素就越少，会导致固定像素宽度的描边占比越来越大

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| OutlineWidthRef | Float | 必填 | 高亮描边线宽距离基准（cm） |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutlineWidthRef",
  "Params": {
    "OutlineWidthRef": 0.0
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
  "Interface": "UCFOutline/SetOutlineWidthRef",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetoutlineemissive"></a>

[← 返回接口一览](#接口一览)

## 设置高亮自发光

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
| OutlineEmissive | Float | 必填 | 高亮自发光，取值范围[1,10] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutlineEmissive",
  "Params": {
    "OutlineEmissive": 0.0
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
  "Interface": "UCFOutline/SetOutlineEmissive",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetoutlineopacity"></a>

[← 返回接口一览](#接口一览)

## 设置高亮透明度

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
| OutlineOpacity | Float | 必填 | 高亮透明度，取值范围[0,1] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutlineOpacity",
  "Params": {
    "OutlineOpacity": 0.0
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
  "Interface": "UCFOutline/SetOutlineOpacity",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlineunoutlineactor"></a>

[← 返回接口一览](#接口一览)

## 取消Actor高亮

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
| Tags | `Array<String>` | 必填 | 需要取消高亮的Actor的标签数组 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/UnOutlineActor",
  "Params": {
    "Tags": [
      "xxx",
      "xxx",
      "xxx"
    ]
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
  "Interface": "UCFOutline/UnOutlineActor",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlineunoutlineallactor"></a>

[← 返回接口一览](#接口一览)

## 取消所有Actor高亮

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
  "Interface": "UCFOutline/UnOutlineAllActor",
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
  "Interface": "UCFOutline/UnOutlineAllActor",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlineoutlinearea"></a>

[← 返回接口一览](#接口一览)

## 高亮多边形区域

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
| PolygonsList | `Array<Array<Object>>` | 必填 | 多边形顶点列表数组，支持多个多边形 |
| [].[] | `Array<Object>` | 必填 | 单个多边形的顶点数组 |
| {}.X | Float | 必填 | 顶点X坐标 |
| {}.Y | Float | 必填 | 顶点Y坐标 |
| AreaMinZ | Float | 必填 | 多边形区域竖向最小值 |
| AreaMaxZ | Float | 必填 | 多边形区域竖向最大值 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/OutlineArea",
  "Params": {
    "PolygonsList": [
      [
        {
          "X": 1000.0,
          "Y": 2000.0
        },
        {
          "X": 1000.0,
          "Y": 2000.0
        },
        {
          "X": 1000.0,
          "Y": 2000.0
        }
      ],
      [
        {
          "X": 1000.0,
          "Y": 2000.0
        },
        {
          "X": 1000.0,
          "Y": 2000.0
        },
        {
          "X": 1000.0,
          "Y": 2000.0
        }
      ],
      [
        {
          "X": 1000.0,
          "Y": 2000.0
        },
        {
          "X": 1000.0,
          "Y": 2000.0
        },
        {
          "X": 1000.0,
          "Y": 2000.0
        }
      ]
    ],
    "AreaMinZ": 0.0,
    "AreaMaxZ": 0.0
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
  "Interface": "UCFOutline/OutlineArea",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1z2GK6EEq3/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlineapplyareadefault"></a>

[← 返回接口一览](#接口一览)

## 应用默认多边形区域效果

**类型:** Sync

**Tips:**

- OutGray：0.1
- OutColor：FLinearColor(0.227451f, 0.227451f, 0.227451f)
- AreaFill：false
- AreaColor：FLinearColor(0.104136f, 0.030858f, 1.0f)
- AreaOpacity：1
- AreaEmissive：1

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
  "Interface": "UCFOutline/ApplyAreaDefault",
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
  "Interface": "UCFOutline/ApplyAreaDefault",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetoutgray"></a>

[← 返回接口一览](#接口一览)

## 设置多边形外区域的去色强度

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
| OutGray | Float | 必填 | 多边形外区域的去色强度,取值范围[0,1]，值为1时完全去色 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutGray",
  "Params": {
    "OutGray": 0.0
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
  "Interface": "UCFOutline/SetOutGray",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1ZSGK6jE9h/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlinesetoutcolor"></a>

[← 返回接口一览](#接口一览)

## 设置多边形外区域的颜色

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
| OutColor | Object | 必填 | 遮罩区域颜色 |
| OutColor.R | Float | 必填 | R通道值，取值范围[0,1] |
| OutColor.G | Float | 必填 | G通道值，取值范围[0,1] |
| OutColor.B | Float | 必填 | B通道值，取值范围[0,1] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetOutColor",
  "Params": {
    "OutColor": {
      "R": 0.0,
      "G": 0.0,
      "B": 0.0
    }
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
  "Interface": "UCFOutline/SetOutColor",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1BSGK6jEij/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlinesetareafill"></a>

[← 返回接口一览](#接口一览)

## 设置多边形区域填充

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
| AreaFill | Boolean | 必填 | 是否填充多边形区域 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetAreaFill",
  "Params": {
    "AreaFill": false
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
  "Interface": "UCFOutline/SetAreaFill",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetareaopacity"></a>

[← 返回接口一览](#接口一览)

## 设置多边形区域填充透明度

**类型:** Sync

**Tips:**

- 仅启用多边形区域填充时生效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| AreaOpacity | Float | 必填 | 多边形区域填充透明度,取值范围[0,1] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetAreaOpacity",
  "Params": {
    "AreaOpacity": 0.0
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
  "Interface": "UCFOutline/SetAreaOpacity",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlinesetareacolor"></a>

[← 返回接口一览](#接口一览)

## 设置多边形区域填充颜色

**类型:** Sync

**Tips:**

- 仅启用多边形区域填充时生效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| AreaColor | Object | 必填 | 多边形区域填充颜色 |
| AreaColor.R | Float | 必填 | R通道值，取值范围[0,1] |
| AreaColor.G | Float | 必填 | G通道值，取值范围[0,1] |
| AreaColor.B | Float | 必填 | B通道值，取值范围[0,1] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetAreaColor",
  "Params": {
    "AreaColor": {
      "R": 0.0,
      "G": 0.0,
      "B": 0.0
    }
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
  "Interface": "UCFOutline/SetAreaColor",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1nyGK6DEhn/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfoutlinesetareaemissive"></a>

[← 返回接口一览](#接口一览)

## 设置多边形区域填充自发光强度

**类型:** Sync

**Tips:**

- 仅启用多边形区域填充时生效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| AreaEmissive | Float | 必填 | 多边形区域填充自发光强度,取值范围[1,10] |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFOutline/SetAreaEmissive",
  "Params": {
    "AreaEmissive": 0.0
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
  "Interface": "UCFOutline/SetAreaEmissive",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfoutlineunoutlinearea"></a>

[← 返回接口一览](#接口一览)

## 取消高亮多边形区域

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
  "Interface": "UCFOutline/UnOutlineArea",
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
  "Interface": "UCFOutline/UnOutlineArea",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```
