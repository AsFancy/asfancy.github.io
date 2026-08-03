# UCFMark - 标记管理

提供POI标绘、二维标绘、三维标绘等接口

## 接口一览

### POI标绘

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFMark/CreatePOI](#ucfmarkcreatepoi) | 创建POI(UE坐标系) |
| [UCFMark/CreatePOIGeo](#ucfmarkcreatepoigeo) | 创建POI(WGS84坐标系) |
| [UCFMark/SetGroupVisibility](#ucfmarksetgroupvisibility) | 按Group设置POI可视性 |
| [UCFMark/SetIDVisibility](#ucfmarksetidvisibility) | 按ID设置POI可视性 |
| [UCFMark/UpdatePOIGroup](#ucfmarkupdatepoigroup) | 按ID更新POI的Group |
| [UCFMark/UpdatePOIStyle](#ucfmarkupdatepoistyle) | 按ID更新POI样式 |
| [UCFMark/SetGroupAutoFocus](#ucfmarksetgroupautofocus) | 按Group设置POI自动聚焦功能开关 |
| [UCFMark/FocusPOI](#ucfmarkfocuspoi) | 按ID聚焦到指定POI实例 |
| [UCFMark/EnableAdaptiveScale](#ucfmarkenableadaptivescale) | 启用POI尺寸自适应 |
| [UCFMark/DisableAdaptiveScale](#ucfmarkdisableadaptivescale) | 关闭POI尺寸自适应 |
| [UCFMark/EnableGroupClustering](#ucfmarkenablegroupclustering) | 按Group启用POI聚合 |
| [UCFMark/DisableGroupClustering](#ucfmarkdisablegroupclustering) | 按Group关闭POI聚合 |
| [UCFMark/DebugClustering](#ucfmarkdebugclustering) | 调试指定Group的聚合功能 |
| [UCFMark/ClearGroup](#ucfmarkcleargroup) | 按Group删除POI |
| [UCFMark/ClearID](#ucfmarkclearid) | 按ID删除POI |
| [UCFMark/ClearAll](#ucfmarkclearall) | 清除所有POI |
| [UCFMark/OnPOIClicked](#ucfmarkonpoiclicked) | 光标点击POI实例通知 |
| [UCFMark/OnPOIHovered](#ucfmarkonpoihovered) | 光标悬停POI实例通知 |
| [UCFMark/OnPOIUnhovered](#ucfmarkonpoiunhovered) | 光标取消悬停POI实例通知 |

<a id="ucfmarkcreatepoi"></a>

[← 返回接口一览](#接口一览)

## 创建POI(UE坐标系)

**类型:** Sync

**Tips:**

- StyleConfig和POIData[].config必须适配所指定的StyleRef，否则配置项都不会被应用
- StyleRef对应的UMG类可选重写SetStyleConfig，用于解析并应用StyleConfig
- StyleRef对应的UMG类可选重写SetInstanceData，用于解析并应用POIData[].config
- 与POI聚合功能无先后调用顺序要求

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Group | String | 必填 | POI分组 |
| StyleRef | String | 必填 | POI样式引用路径，即派生自UCFPOIbase的UMG资产，例如/Game/POI/BP_MyPOI.BP_MyPOI_C |
| StyleConfig | Object | 选填 | POI样式配置，必须适配所指定的StyleRef，是对StyleRef中子控件的统一参数配置，对所有POI实例生效 |
| POIData | `Array<Object>` | 必填 | POI数据 |
| {}.id | String | 必填 | POI唯一标识 |
| {}.vec | Object | 必填 | POI世界坐标位置 |
| vec.X | Float | 必填 | X坐标（厘米） |
| vec.Y | Float | 必填 | Y坐标（厘米） |
| vec.Z | Float | 必填 | Z坐标（厘米） |
| {}.config | Object | 选填 | POI实例配置，必须适配所指定的StyleRef，是对StyleRef中子控件的特定参数配置，仅对该POI实例生效，例如需要额外显示的文本信息 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/CreatePOI",
  "Params": {
    "Group": "xxx",
    "StyleRef": "xxx",
    "StyleConfig": {},
    "POIData": [
      {
        "id": "xxx",
        "vec": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "config": {}
      },
      {
        "id": "xxx",
        "vec": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "config": {}
      },
      {
        "id": "xxx",
        "vec": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "config": {}
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
  "Interface": "UCFMark/CreatePOI",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkcreatepoigeo"></a>

[← 返回接口一览](#接口一览)

## 创建POI(WGS84坐标系)

**类型:** Sync

**Tips:**

- WGS84坐标会按照项目配置的坐标参考转为UE坐标，对于Z坐标则按照转换后的UE坐标进行竖向射线检测获取到碰撞位置的Z值，否则默认为100厘米
- StyleConfig和POIData[].config必须适配所指定的StyleRef，否则配置项都不会被应用
- StyleRef对应的UMG类可选重写SetStyleConfig，用于解析并应用StyleConfig
- StyleRef对应的UMG类可选重写SetInstanceData，用于解析并应用POIData[].config
- 与POI聚合功能无先后调用顺序要求

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Group | String | 必填 | POI分组 |
| StyleRef | String | 必填 | POI样式引用路径，即派生自UCFPOIbase的UMG资产，例如/Game/POI/BP_MyPOI.BP_MyPOI_C |
| StyleConfig | Object | 选填 | POI样式配置，必须适配所指定的StyleRef，是对StyleRef中子控件的统一参数配置，对所有POI实例生效 |
| POIData | `Array<Object>` | 必填 | POI数据 |
| {}.id | String | 必填 | POI唯一标识 |
| {}.lon | Float | 必填 | POI经度坐标（度） |
| {}.lat | Float | 必填 | POI纬度坐标（度） |
| {}.config | Object | 选填 | POI实例配置，必须适配所指定的StyleRef，是对StyleRef中子控件的特定参数配置，仅对该POI实例生效，例如需要额外显示的文本信息 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/CreatePOIGeo",
  "Params": {
    "Group": "xxx",
    "StyleRef": "xxx",
    "StyleConfig": {},
    "POIData": [
      {
        "id": "xxx",
        "lon": 0.0,
        "lat": 0.0,
        "config": {}
      },
      {
        "id": "xxx",
        "lon": 0.0,
        "lat": 0.0,
        "config": {}
      },
      {
        "id": "xxx",
        "lon": 0.0,
        "lat": 0.0,
        "config": {}
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

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| MaxHeight | Float | 所创建的POI实例中Z值的最大值（厘米） |
| MinHeight | Float | 所创建的POI实例中Z值的最小值（厘米） |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/CreatePOIGeo",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "MaxHeight": 0.0,
    "MinHeight": 0.0
  }
}
```

<a id="ucfmarksetgroupvisibility"></a>

[← 返回接口一览](#接口一览)

## 按Group设置POI可视性

**类型:** Sync

**Tips:**

- Group必须有效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Groups | `Array<String>` | 必填 | POI分组名称 |
| bVisible | Boolean | 必填 | true为显示，false为隐藏 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/SetGroupVisibility",
  "Params": {
    "Groups": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "bVisible": false
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
  "Interface": "UCFMark/SetGroupVisibility",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarksetidvisibility"></a>

[← 返回接口一览](#接口一览)

## 按ID设置POI可视性

**类型:** Sync

**Tips:**

- POIID必须有效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| POIIDs | `Array<String>` | 必填 | POI唯一标识 |
| bVisible | Boolean | 必填 | true为显示，false为隐藏 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/SetIDVisibility",
  "Params": {
    "POIIDs": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "bVisible": false
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
  "Interface": "UCFMark/SetIDVisibility",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkupdatepoigroup"></a>

[← 返回接口一览](#接口一览)

## 按ID更新POI的Group

**类型:** Sync

**Tips:**

- POIID必须有效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| POIIDs | `Array<String>` | 必填 | POI唯一标识 |
| NewGroup | String | 必填 | 新Group名称 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/UpdatePOIGroup",
  "Params": {
    "POIIDs": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "NewGroup": "xxx"
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
  "Interface": "UCFMark/UpdatePOIGroup",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkupdatepoistyle"></a>

[← 返回接口一览](#接口一览)

## 按ID更新POI样式

**类型:** Sync

**Tips:**

- POIID必须有效
- StyleConfig必须适配所指定的StyleRef或POI实例的实际StyleRef，否则配置项都不会被应用
- StyleRef对应的UMG类可选重写SetStyleConfig，用于解析并应用StyleConfig

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| POIIDs | `Array<String>` | 必填 | POI唯一标识 |
| StyleRef | String | 选填 | POI样式引用路径，即派生自UCFPOIbase的UMG资产，例如/Game/POI/BP_MyPOI.BP_MyPOI_C |
| StyleConfig | Object | 选填 | POI样式配置，必须适配所传入的StyleRef或POI实例的实际StyleRef，是对StyleRef中子控件的统一参数配置，对所有POI实例生效 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/UpdatePOIStyle",
  "Params": {
    "POIIDs": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "StyleRef": "xxx",
    "StyleConfig": {}
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
  "Interface": "UCFMark/UpdatePOIStyle",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarksetgroupautofocus"></a>

[← 返回接口一览](#接口一览)

## 按Group设置POI自动聚焦功能开关

**类型:** Sync

**Tips:**

- Group必须有效
- 仅当 autofocus=true 时，光标点击POI实例后才会自动聚焦到该POI的世界坐标位置

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Group | String | 必填 | POI分组名称 |
| autofocus | Boolean | 必填 | 是否开启自动聚焦 |
| offset | Float | 选填 | 聚焦时视点相对于世界坐标的反向偏移距离（厘米），默认 `5000` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/SetGroupAutoFocus",
  "Params": {
    "Group": "xxx",
    "autofocus": false,
    "offset": 5000
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
  "Interface": "UCFMark/SetGroupAutoFocus",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkfocuspoi"></a>

[← 返回接口一览](#接口一览)

## 按ID聚焦到指定POI实例

**类型:** Sync

**Tips:**

- POIID必须有效
- POI实例被用户手动隐藏时拒绝聚焦
- POI实例所在Group启用了聚合且该POI当前被聚合隐藏时拒绝聚焦

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| POIID | String | 必填 | POI唯一标识 |
| Rotation | Object | 选填 | 目标角度，不传则保持当前Pawn角度 |
| Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Rotation.Roll | Float | 必填 | 翻滚角（度）（该值会被忽略） |
| Offset | Float | 选填 | 相对WorldLocation的反向偏移距离（厘米），不传则使用POI实例自身的offset值 |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/FocusPOI",
  "Params": {
    "POIID": "xxx",
    "Rotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
    },
    "Offset": 0.0,
    "bIgnoreLag": false
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
  "Interface": "UCFMark/FocusPOI",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkenableadaptivescale"></a>

[← 返回接口一览](#接口一览)

## 启用POI尺寸自适应

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
| MinHeight | Float | 必填 | POI原始尺寸对应的高度值，小于等于此值时保持正常尺寸 |
| MaxHeight | Float | 必填 | POI按MinScale的尺寸对应的高度值，大于等于此值时按MinScale缩放尺寸 |
| MinScale | Float | 必填 | 最小缩放比例，取值范围(0,1) |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/EnableAdaptiveScale",
  "Params": {
    "MinHeight": 0.0,
    "MaxHeight": 0.0,
    "MinScale": 0.0
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
  "Interface": "UCFMark/EnableAdaptiveScale",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkdisableadaptivescale"></a>

[← 返回接口一览](#接口一览)

## 关闭POI尺寸自适应

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
  "Interface": "UCFMark/DisableAdaptiveScale",
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
  "Interface": "UCFMark/DisableAdaptiveScale",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkenablegroupclustering"></a>

[← 返回接口一览](#接口一览)

## 按Group启用POI聚合

**类型:** Sync

**Tips:**

- 每个Group拥有独立的聚合配置，互不干扰
- 聚合功能基于四叉树实现，非叶子节点对应的聚合POI位置以所有子节点POI位置的平均值计算，非四叉树中心点
- 以参数MaxHeight对应四叉树的最小深度0，参数MinHeight对应四叉树的最大深度MaxDepth，视点的Z值作为动态变量映射得到目标深度
- 以视点二维坐标为中心、目标深度对应节点尺寸大小的详情窗口，从FullImpactDepth层起与各深度下的节点的包围盒做相交判定：节点包围盒与详情窗口相交的继续分裂以提供更细粒度，不相交的在当前深度聚合，自然形成近处精细、远处粗粒度的渐变聚合梯度
- StyleRef对应的UMG类可选重写SetAggregateCount，可用于设置显示聚合数量
- 与POI创建功能无先后调用顺序要求

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Group | String | 必填 | POI分组名称 |
| StyleRef | String | 选填 | 聚合POI样式引用路径，即派生自UCFPOIbase的UMG资产，默认值/UCFPlugin/UCFPlugin/UCFMark/UCFPOI/ClusterStyle/Cluster_Style2.Cluster_Style2_C |
| MaxDepth | Int | 选填 | 四叉树最大深度，默认值4，取值范围[2,8] |
| MinHeight | Float | 选填 | 四叉树最大深度对应的高度值，默认值0，视点高度≤该值时目标深度达MaxDepth，详情窗口内相交的节点将递归划分到叶子层级 |
| MaxHeight | Float | 选填 | 四叉树深度0对应的高度值，默认值10000，视点高度≥该值时目标深度为0，详情窗口覆盖全域，所有节点聚合为1个根节点 |
| FullImpactDepth | Int | 选填 | 无相交判定的全局覆盖深度，默认值1，深度小于该值的节点不做详情窗口相交判定，统一随TargetDepth分裂 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/EnableGroupClustering",
  "Params": {
    "Group": "xxx",
    "StyleRef": "xxx",
    "MaxDepth": 0,
    "MinHeight": 0.0,
    "MaxHeight": 0.0,
    "FullImpactDepth": 0
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
  "Interface": "UCFMark/EnableGroupClustering",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1a5KM64EJq/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfmarkdisablegroupclustering"></a>

[← 返回接口一览](#接口一览)

## 按Group关闭POI聚合

**类型:** Sync

**Tips:**

- Group必须有效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Group | String | 必填 | Group名称 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/DisableGroupClustering",
  "Params": {
    "Group": "xxx"
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
  "Interface": "UCFMark/DisableGroupClustering",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkdebugclustering"></a>

[← 返回接口一览](#接口一览)

## 调试指定Group的聚合功能

**类型:** Sync

**Tips:**

- Group必须有效
- 必须指定目标Group，用于查看对应的四叉树效果
- Shipping版本禁用

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Group | String | 必填 | 目标Group名称 |
| bEnable | Boolean | 必填 | 是否启用调试绘制 |
| NodeRange | Float | 选填 | 受影响节点的绘制线宽，默认 `20.0` |
| ViewRange | Float | 选填 | 详情窗口范围线的绘制线宽，默认 `30.0` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/DebugClustering",
  "Params": {
    "Group": "xxx",
    "bEnable": false,
    "NodeRange": 20.0,
    "ViewRange": 30.0
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
  "Interface": "UCFMark/DebugClustering",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkcleargroup"></a>

[← 返回接口一览](#接口一览)

## 按Group删除POI

**类型:** Sync

**Tips:**

- Group必须有效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Groups | `Array<String>` | 必填 | POI分组名称 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/ClearGroup",
  "Params": {
    "Groups": [
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
  "Interface": "UCFMark/ClearGroup",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkclearid"></a>

[← 返回接口一览](#接口一览)

## 按ID删除POI

**类型:** Sync

**Tips:**

- POIID必须有效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| POIIDs | `Array<String>` | 必填 | POI唯一标识 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFMark/ClearID",
  "Params": {
    "POIIDs": [
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
  "Interface": "UCFMark/ClearID",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkclearall"></a>

[← 返回接口一览](#接口一览)

## 清除所有POI

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
  "Interface": "UCFMark/ClearAll",
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
  "Interface": "UCFMark/ClearAll",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfmarkonpoiclicked"></a>

[← 返回接口一览](#接口一览)

## 光标点击POI实例通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFMark/OnPOIClicked"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| PID | String | POI实例ID |
| Group | String | POI实例所属组别 |
| Location | Object | POI实例的三维世界坐标 |
| Location.X | Float | X坐标（厘米） |
| Location.Y | Float | Y坐标（厘米） |
| Location.Z | Float | Z坐标（厘米） |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFMark/OnPOIClicked",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {
    "PID": "xxx",
    "Group": "xxx",
    "Location": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    }
  }
}
```

<a id="ucfmarkonpoihovered"></a>

[← 返回接口一览](#接口一览)

## 光标悬停POI实例通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFMark/OnPOIHovered"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| PID | String | POI实例ID |
| Group | String | POI实例所属组别 |
| Location | Object | POI实例的三维世界坐标 |
| Location.X | Float | X坐标（厘米） |
| Location.Y | Float | Y坐标（厘米） |
| Location.Z | Float | Z坐标（厘米） |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFMark/OnPOIHovered",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {
    "PID": "xxx",
    "Group": "xxx",
    "Location": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    }
  }
}
```

<a id="ucfmarkonpoiunhovered"></a>

[← 返回接口一览](#接口一览)

## 光标取消悬停POI实例通知

**类型:** Trigger

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFMark/OnPOIUnhovered"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| PID | String | POI实例ID |
| Group | String | POI实例所属组别 |
| Location | Object | POI实例的三维世界坐标 |
| Location.X | Float | X坐标（厘米） |
| Location.Y | Float | Y坐标（厘米） |
| Location.Z | Float | Z坐标（厘米） |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFMark/OnPOIUnhovered",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {
    "PID": "xxx",
    "Group": "xxx",
    "Location": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    }
  }
}
```
