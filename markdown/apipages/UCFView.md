# UCFView - 视点管理

提供视点控制，视点参数、功能配置，视点切换，漫游操作等相关的接口

## 接口一览

### 视点操作

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/SetDPPosition](#ucfviewsetdpposition) | 设置视点方位 |
| [UCFView/SetDPPositionGeo](#ucfviewsetdppositiongeo) | 设置视点方位（WGS84坐标系） |
| [UCFView/SetDPLocation](#ucfviewsetdplocation) | 设置视点位置 |
| [UCFView/SetDPRotation](#ucfviewsetdprotation) | 设置视点角度 |
| [UCFView/GetDPPosition](#ucfviewgetdpposition) | 获取视点方位 |
| [UCFView/GetDPPositionGeo](#ucfviewgetdppositiongeo) | 获取视点地理方位 |
| [UCFView/FocusActor](#ucfviewfocusactor) | 设置视点聚焦对象 |
| [UCFView/FocusArea](#ucfviewfocusarea) | 设置视点聚焦圆柱体区域 |
| [UCFView/FocusAreaGeo](#ucfviewfocusareageo) | 设置视点聚焦圆柱体区域（WGS84坐标系） |
| [UCFView/SwitchDPInput](#ucfviewswitchdpinput) | 开启或关闭视点的特定操作 |
| [UCFView/SetDPInputParams](#ucfviewsetdpinputparams) | 配置视点操作的参数 |
| [UCFView/SetDPHMoveInput](#ucfviewsetdphmoveinput) | 设置定点平移的输入动作 |
| [UCFView/SetDPRotateWithAnchorInput](#ucfviewsetdprotatewithanchorinput) | 设置定点旋转的输入动作 |
| [UCFView/SetDPRotateWithSelfInput](#ucfviewsetdprotatewithselfinput) | 设置自旋转的输入动作 |
| [UCFView/SetDPFastFocusInput](#ucfviewsetdpfastfocusinput) | 设置快速聚焦的输入动作 |
| [UCFView/SwitchViewType](#ucfviewswitchviewtype) | 切换视点类型 |

### 漫游操作

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/StartRoamUniformTime](#ucfviewstartroamuniformtime) | 开始漫游(均匀时间) |
| [UCFView/StartRoamUniformSpeed](#ucfviewstartroamuniformspeed) | 开始漫游(均匀速度) |
| [UCFView/StartRoamCustomTime](#ucfviewstartroamcustomtime) | 开始漫游(自定义时间) |
| [UCFView/PauseRoam](#ucfviewpauseroam) | 暂停漫游 |
| [UCFView/ResumeRoam](#ucfviewresumeroam) | 继续漫游 |
| [UCFView/StopRoam](#ucfviewstoproam) | 停止漫游 |
| [UCFView/RestartRoam](#ucfviewrestartroam) | 重新开始漫游 |
| [UCFView/OnRoamFinished](#ucfviewonroamfinished) | 漫游自动结束通知 |

<a id="ucfviewsetdpposition"></a>

[← 返回接口一览](#接口一览)

## 设置视点方位

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 视点位置严格限制在为UCFDefaultPawn配置的直棱柱区域内，传入值超出该范围时，会被设置到该直棱柱区域内最接近目标位置处
- 视点角度严格限制在为UCFDefaultPawn配置的角度范围内，传入值超出该范围时，会被设置为最该范围内最接近目标角度的值
- 目标视点的角度的翻滚角(roll)值忽略，UCFDefaultPawn不允许有翻滚角度

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirLocation | Object | 必填 | 目标位置 |
| DesirLocation.X | Float | 必填 | X坐标（厘米） |
| DesirLocation.Y | Float | 必填 | Y坐标（厘米） |
| DesirLocation.Z | Float | 必填 | Z坐标（厘米） |
| DesirRotation | Object | 必填 | 目标角度 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角（度） |
| DesirRotation.Yaw | Float | 必填 | 偏航角（度） |
| DesirRotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| OffsetDistance | Float | 选填 | 相对目标位置的反向偏移距离（厘米），默认 `0` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPPosition",
  "Params": {
    "DesirLocation": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "DesirRotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
    },
    "OffsetDistance": 0,
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
  "Interface": "UCFView/SetDPPosition",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1Kwjq6sEtZ/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfviewsetdppositiongeo"></a>

[← 返回接口一览](#接口一览)

## 设置视点方位（WGS84坐标系）

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 视点位置严格限制在为UCFDefaultPawn配置的直棱柱区域内，传入值超出该范围时，会被设置到该直棱柱区域内最接近目标位置处
- 视点角度严格限制在为UCFDefaultPawn配置的角度范围内，传入值超出该范围时，会被设置为最该范围内最接近目标角度的值
- 目标视点的角度的翻滚角(roll)值忽略，UCFDefaultPawn不允许有翻滚角度

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirLocation | Object | 必填 | 目标位置 |
| DesirLocation.X | Float | 必填 | 经度（度） |
| DesirLocation.Y | Float | 必填 | 纬度（度） |
| DesirLocation.Z | Float | 必填 | 海拔（米） |
| DesirRotation | Object | 必填 | 目标角度 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角（度） |
| DesirRotation.Yaw | Float | 必填 | 偏航角（度） |
| DesirRotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| OffsetDistance | Float | 选填 | 相对目标位置的反向偏移距离（厘米），默认 `0` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPPositionGeo",
  "Params": {
    "DesirLocation": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "DesirRotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
    },
    "OffsetDistance": 0,
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
  "Interface": "UCFView/SetDPPositionGeo",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdplocation"></a>

[← 返回接口一览](#接口一览)

## 设置视点位置

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 视点位置严格限制在为UCFDefaultPawn配置的直棱柱区域内，传入值超出该范围时，会被设置到该直棱柱区域内最接近目标位置处

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirLocation | Object | 必填 | 目标位置 |
| DesirLocation.X | Float | 必填 | X坐标（厘米） |
| DesirLocation.Y | Float | 必填 | Y坐标（厘米） |
| DesirLocation.Z | Float | 必填 | Z坐标（厘米） |
| OffsetDistance | Float | 选填 | 相对目标位置的反向偏移距离（厘米），默认 `0` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPLocation",
  "Params": {
    "DesirLocation": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "OffsetDistance": 0,
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
  "Interface": "UCFView/SetDPLocation",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdprotation"></a>

[← 返回接口一览](#接口一览)

## 设置视点角度

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 视点角度严格限制在为UCFDefaultPawn配置的角度范围内，传入值超出该范围时，会被设置为最该范围内最接近目标角度的值
- 目标视点的角度的翻滚角(roll)值忽略，UCFDefaultPawn不允许有翻滚角度

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirRotation | Object | 必填 | 目标角度 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角（度） |
| DesirRotation.Yaw | Float | 必填 | 偏航角（度） |
| DesirRotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPRotation",
  "Params": {
    "DesirRotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
    },
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
  "Interface": "UCFView/SetDPRotation",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewgetdpposition"></a>

[← 返回接口一览](#接口一览)

## 获取视点方位

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn

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
  "Interface": "UCFView/GetDPPosition",
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

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| PawnLocation | Object | 当前位置 |
| PawnLocation.X | Float | X坐标（厘米） |
| PawnLocation.Y | Float | Y坐标（厘米） |
| PawnLocation.Z | Float | Z坐标（厘米） |
| PawnRotation | Object | 当前角度 |
| PawnRotation.Pitch | Float | 俯仰角（度） |
| PawnRotation.Yaw | Float | 偏航角（度） |
| PawnRotation.Roll | Float | 翻滚角（度） |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/GetDPPosition",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "PawnLocation": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "PawnRotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
    }
  }
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1FEjz6HEAB/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfviewgetdppositiongeo"></a>

[← 返回接口一览](#接口一览)

## 获取视点地理方位

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn

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
  "Interface": "UCFView/GetDPPositionGeo",
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

#### Params内参数

| 字段 | 类型 | 说明 |
|------|------|------|
| Longitude | Float | 经度（度） |
| Latitude | Float | 纬度（度） |
| Altitude | Float | 海拔（米） |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/GetDPPositionGeo",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "Longitude": 0.0,
    "Latitude": 0.0,
    "Altitude": 0.0
  }
}
```

<a id="ucfviewfocusactor"></a>

[← 返回接口一览](#接口一览)

## 设置视点聚焦对象

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 找到多个匹配 Tag 的对象时仅聚焦第一个
- 视点聚焦中心为目标对象及其所有挂载对象的包围盒中心
- 视点角度严格限制在为UCFDefaultPawn配置的角度范围内，传入值超出该范围时，会被设置为最该范围内最接近目标角度的值
- 目标视点的角度的翻滚角(roll)值忽略，UCFDefaultPawn不允许有翻滚角度

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| TargetTag | String | 必填 | 目标对象的Tag标识 |
| FocusOffset | Float | 选填 | 相对包围盒中心的反向偏移距离（厘米）。若不传入或小于0，则使用包围盒最大边长的2倍 |
| DesirRotation | Object | 选填 | 目标角度，欧拉角表示的旋转值。若不传入则保持当前视点的角度不变 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角（度） |
| DesirRotation.Yaw | Float | 必填 | 偏航角（度） |
| DesirRotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/FocusActor",
  "Params": {
    "TargetTag": "xxx",
    "FocusOffset": 0.0,
    "DesirRotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
    },
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
  "Interface": "UCFView/FocusActor",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1FEjz6HEgn/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfviewfocusarea"></a>

[← 返回接口一览](#接口一览)

## 设置视点聚焦圆柱体区域

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 圆柱体半高为0时退化为纯2D圆盘

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Center | Object | 必填 | 圆柱体几何中心 |
| Center.X | Float | 必填 | X坐标（厘米） |
| Center.Y | Float | 必填 | Y坐标（厘米） |
| Center.Z | Float | 必填 | Z坐标（厘米） |
| Radius | Float | 必填 | 圆柱体半径（厘米） |
| HalfHeight | Float | 必填 | 圆柱体半高（厘米），0=纯2D圆盘 |
| Pitch | Float | 必填 | 视角俯仰角（度），取值范围[-85,85]，负=俯视，正=仰视，0=平视 |
| Margin | Float | 选填 | 视野余量系数，默认 `1.1` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/FocusArea",
  "Params": {
    "Center": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "Radius": 0.0,
    "HalfHeight": 0.0,
    "Pitch": 0.0,
    "Margin": 1.1,
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
  "Interface": "UCFView/FocusArea",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewfocusareageo"></a>

[← 返回接口一览](#接口一览)

## 设置视点聚焦圆柱体区域（WGS84坐标系）

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 圆柱体半高为0时退化为纯2D圆盘

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Center | Object | 必填 | 圆柱体几何中心（WGS84坐标系） |
| Center.X | Float | 必填 | 经度（度） |
| Center.Y | Float | 必填 | 纬度（度） |
| Center.Z | Float | 必填 | 海拔（米） |
| Radius | Float | 必填 | 圆柱体半径（米） |
| HalfHeight | Float | 必填 | 圆柱体半高（米），0=纯2D圆盘 |
| Pitch | Float | 必填 | 视角俯仰角（度），取值范围[-85,85]，负=俯视，正=仰视，0=平视 |
| Margin | Float | 选填 | 视野余量系数，默认 `1.1` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/FocusAreaGeo",
  "Params": {
    "Center": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "Radius": 0.0,
    "HalfHeight": 0.0,
    "Pitch": 0.0,
    "Margin": 1.1,
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
  "Interface": "UCFView/FocusAreaGeo",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewswitchdpinput"></a>

[← 返回接口一览](#接口一览)

## 开启或关闭视点的特定操作

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| bEnableCollision | Boolean | 选填 | Pawn的碰撞开关 |
| bEnableHMove | Boolean | 选填 | 固定锚点水平移动开关 |
| bEnableVMove | Boolean | 选填 | 竖直移动开关 |
| bEnableRotateWithAnchor | Boolean | 选填 | 固定锚点旋转开关 |
| bEnableRotateWithSelf | Boolean | 选填 | 绕自身位置旋转开关 |
| bEnableZoom | Boolean | 选填 | 缩放开关 |
| bEnableFastFocus | Boolean | 选填 | 快速聚焦开关 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SwitchDPInput",
  "Params": {
    "bEnableCollision": false,
    "bEnableHMove": false,
    "bEnableVMove": false,
    "bEnableRotateWithAnchor": false,
    "bEnableRotateWithSelf": false,
    "bEnableZoom": false,
    "bEnableFastFocus": false
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
  "Interface": "UCFView/SwitchDPInput",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdpinputparams"></a>

[← 返回接口一览](#接口一览)

## 配置视点操作的参数

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| RotateSpeed | Float | 选填 | 旋转角速度，默认 `3.0` |
| VerticalMoveSpeed | Float | 选填 | 单帧竖直移动距离（cm），默认 `1000.0` |
| ZoomPercent | Float | 选填 | 单次缩放距离相对于当前位置与参考锚点距离的百分比，取值范围：[0.1, 0.8]，默认 `0.4` |
| LagSpeed | Float | 选填 | 滞后平滑速度，值越小滞后效果越明显，值为0即关闭，取值范围：[0.0, 8.0]，默认 `5.0` |
| FocusOffset | Float | 选填 | 快速聚焦到中键双击位置时的相对偏移距离（cm），默认 `1000.0` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPInputParams",
  "Params": {
    "RotateSpeed": 3.0,
    "VerticalMoveSpeed": 1000.0,
    "ZoomPercent": 0.4,
    "LagSpeed": 5.0,
    "FocusOffset": 1000.0
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
  "Interface": "UCFView/SetDPInputParams",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdphmoveinput"></a>

[← 返回接口一览](#接口一览)

## 设置定点平移的输入动作

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 设置成功后,使用该输入动作的其他行为会被置空动作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Input | String | 必填 | 输入动作,可选值:"LeftMouseDown"、"RightMouseDown"、"MiddleMouseDown" |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPHMoveInput",
  "Params": {
    "Input": "xxx"
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
  "Interface": "UCFView/SetDPHMoveInput",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdprotatewithanchorinput"></a>

[← 返回接口一览](#接口一览)

## 设置定点旋转的输入动作

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 设置成功后,使用该输入动作的其他行为会被置空动作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Input | String | 必填 | 输入动作,可选值:"LeftMouseDown"、"RightMouseDown"、"MiddleMouseDown" |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPRotateWithAnchorInput",
  "Params": {
    "Input": "xxx"
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
  "Interface": "UCFView/SetDPRotateWithAnchorInput",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdprotatewithselfinput"></a>

[← 返回接口一览](#接口一览)

## 设置自旋转的输入动作

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 设置成功后,使用该输入动作的其他行为会被置空动作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Input | String | 必填 | 输入动作,可选值:"LeftMouseDown"、"RightMouseDown"、"MiddleMouseDown" |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPRotateWithSelfInput",
  "Params": {
    "Input": "xxx"
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
  "Interface": "UCFView/SetDPRotateWithSelfInput",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdpfastfocusinput"></a>

[← 返回接口一览](#接口一览)

## 设置快速聚焦的输入动作

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Input | String | 必填 | 输入动作,可选值:"LeftMouseDoubleTap"、"MiddleMouseDoubleTap"、"RightMouseDoubleTap" |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SetDPFastFocusInput",
  "Params": {
    "Input": "xxx"
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
  "Interface": "UCFView/SetDPFastFocusInput",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewswitchviewtype"></a>

[← 返回接口一览](#接口一览)

## 切换视点类型

**类型:** Sync

**Tips:**

- 若传入类型与当前类型相同，则操作无效
- 切换到 Default 类型时，若不传入 Location/Rotation，则使用之前离开Default时保存的位置和角度
- 从 Default 切换到 Male/Vehicle 时，若不传入Location，则通过鼠标点击确定生成位置
- 从 Male/Vehicle 互相切换时，若不传入 Location/Rotation，直接在指定方位生成，否则使用当前的位置和角度直接切换

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ViewType | String | 必填 | 视点类型，可选值："Default"、"Male"、"Vehicle" |
| Location | Object | 选填 | 目标生成位置 |
| Location.X | Float | 必填 | X坐标（厘米） |
| Location.Y | Float | 必填 | Y坐标（厘米） |
| Location.Z | Float | 必填 | Z坐标（厘米） |
| Rotation | Object | 选填 | 目标生成角度 |
| Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Rotation.Roll | Float | 必填 | 翻滚角（度） |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/SwitchViewType",
  "Params": {
    "ViewType": "xxx",
    "Location": {
      "X": 1000.0,
      "Y": 2000.0,
      "Z": 500.0
    },
    "Rotation": {
      "Pitch": 0.0,
      "Yaw": 90.0,
      "Roll": 0.0
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
  "Interface": "UCFView/SwitchViewType",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1NKjz68Eb2/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfviewstartroamuniformtime"></a>

[← 返回接口一览](#接口一览)

## 开始漫游(均匀时间)

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 路径关键帧数量需大于等于2
- 漫游总时长必须大于0
- 相邻关键帧之间耗时相同，速度则根据距离间隔动态变化
- 漫游自动完成后触发 UCFView/OnRoamFinished

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Keyframes | `Array<Object>` | 必填 | 关键帧数组 |
| {}.Location | Object | 必填 | 关键帧位置 |
| Location.X | Float | 必填 | X坐标（厘米） |
| Location.Y | Float | 必填 | Y坐标（厘米） |
| Location.Z | Float | 必填 | Z坐标（厘米） |
| {}.Rotation | Object | 必填 | 关键帧角度 |
| Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Rotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| Duration | Float | 必填 | 漫游总时长（秒） |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/StartRoamUniformTime",
  "Params": {
    "Keyframes": [
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        }
      },
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        }
      },
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        }
      }
    ],
    "Duration": 10.0
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
  "Interface": "UCFView/StartRoamUniformTime",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1h5KM64ED6/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfviewstartroamuniformspeed"></a>

[← 返回接口一览](#接口一览)

## 开始漫游(均匀速度)

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 路径关键帧数量需大于等于2
- 漫游总时长必须大于0
- 整个漫游过程保持匀速运动
- 漫游自动完成后触发 UCFView/OnRoamFinished

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Keyframes | `Array<Object>` | 必填 | 关键帧数组 |
| {}.Location | Object | 必填 | 关键帧位置 |
| Location.X | Float | 必填 | X坐标（厘米） |
| Location.Y | Float | 必填 | Y坐标（厘米） |
| Location.Z | Float | 必填 | Z坐标（厘米） |
| {}.Rotation | Object | 必填 | 关键帧角度 |
| Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Rotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| Duration | Float | 必填 | 漫游总时长（秒） |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/StartRoamUniformSpeed",
  "Params": {
    "Keyframes": [
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        }
      },
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        }
      },
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        }
      }
    ],
    "Duration": 10.0
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
  "Interface": "UCFView/StartRoamUniformSpeed",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1bEKM69Ekv/?share_source=copy_web&vd_source=a88925a690dc55b6a7d0a333e107e2eb)

<a id="ucfviewstartroamcustomtime"></a>

[← 返回接口一览](#接口一览)

## 开始漫游(自定义时间)

**类型:** Sync

**Tips:**

- 仅支持UCFDefaultPawn
- 路径关键帧数量需大于等于2
- 每个关键帧可自定义到达该关键帧的用时,首个关键帧的Duration可设为0，后续关键帧的Duration必须大于0
- 漫游总时长由各段Duration累加得到
- 漫游自动完成后触发 UCFView/OnRoamFinished

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Keyframes | `Array<Object>` | 必填 | 关键帧数组 |
| {}.Location | Object | 必填 | 关键帧位置 |
| Location.X | Float | 必填 | X坐标（厘米） |
| Location.Y | Float | 必填 | Y坐标（厘米） |
| Location.Z | Float | 必填 | Z坐标（厘米） |
| {}.Rotation | Object | 必填 | 关键帧角度 |
| Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Rotation.Roll | Float | 必填 | 翻滚角（度），该值会被忽略 |
| {}.Duration | Float | 必填 | 到达该关键帧的耗时（秒）。第一个关键帧可设为0，后续关键帧必须大于0 |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFView/StartRoamCustomTime",
  "Params": {
    "Keyframes": [
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        },
        "Duration": 10.0
      },
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        },
        "Duration": 10.0
      },
      {
        "Location": {
          "X": 1000.0,
          "Y": 2000.0,
          "Z": 500.0
        },
        "Rotation": {
          "Pitch": 0.0,
          "Yaw": 90.0,
          "Roll": 0.0
        },
        "Duration": 10.0
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
  "Interface": "UCFView/StartRoamCustomTime",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewpauseroam"></a>

[← 返回接口一览](#接口一览)

## 暂停漫游

**类型:** Sync

**Tips:**

- 仅在漫游进行中生效

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
  "Interface": "UCFView/PauseRoam",
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
  "Interface": "UCFView/PauseRoam",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewresumeroam"></a>

[← 返回接口一览](#接口一览)

## 继续漫游

**类型:** Sync

**Tips:**

- 仅在漫游过程中暂停后生效
- 从漫游路径中暂停位置继续

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
  "Interface": "UCFView/ResumeRoam",
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
  "Interface": "UCFView/ResumeRoam",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewstoproam"></a>

[← 返回接口一览](#接口一览)

## 停止漫游

**类型:** Sync

**Tips:**

- 不会触发 UCFView/OnRoamFinished

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
  "Interface": "UCFView/StopRoam",
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
  "Interface": "UCFView/StopRoam",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewrestartroam"></a>

[← 返回接口一览](#接口一览)

## 重新开始漫游

**类型:** Sync

**Tips:**

- 以上一次开始漫游时的模式和参数重新开始

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
  "Interface": "UCFView/RestartRoam",
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
  "Interface": "UCFView/RestartRoam",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewonroamfinished"></a>

[← 返回接口一览](#接口一览)

## 漫游自动结束通知

**类型:** Trigger

**Tips:**

- 仅漫游时间达到总时长、自动完成时触发
- 手动调用 StopRoam 不会触发该接口

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFView/OnRoamFinished"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFView/OnRoamFinished",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {}
}
```
