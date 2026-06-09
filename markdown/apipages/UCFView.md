# UCFView API

UCFView 提供 DefaultPawn 的位置控制、视角操作、漫游管理、输入配置和功能开关等完整接口，用于三维数字孪生场景中的视口控制与漫游交互。

## 接口一览

### 位置与视角

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/SetDPPosition](#ucfviewsetdpposition) | 设置DefaultPawn的位置和视角 |
| [UCFView/SetDPLocation](#ucfviewsetdplocation) | 设置DefaultPawn的位置 |
| [UCFView/SetDPRotation](#ucfviewsetdprotation) | 设置DefaultPawn的视角 |
| [UCFView/GetDPPosition](#ucfviewgetdpposition) | 获取DefaultPawn的位置和视角 |
| [UCFView/FocusToActorByTag](#ucfviewfocustoactorbytag) | 聚焦到指定Tag的对象 |

### 漫游控制

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/StartRoamUniformTime](#ucfviewstartroamuniformtime) | 开始漫游（均匀时间模式） |
| [UCFView/StartRoamUniformSpeed](#ucfviewstartroamuniformspeed) | 开始漫游（均匀速度模式） |
| [UCFView/StartRoamCustomTime](#ucfviewstartroamcustomtime) | 开始漫游（自定义时间模式） |
| [UCFView/PauseRoam](#ucfviewpauseroam) | 暂停漫游 |
| [UCFView/ResumeRoam](#ucfviewresumeroam) | 继续漫游 |
| [UCFView/StopRoam](#ucfviewstoproam) | 停止漫游 |
| [UCFView/RestartRoam](#ucfviewrestartroam) | 重新开始漫游 |
| [UCFView/OnRoamFinished](#ucfviewonroamfinished) | 漫游结束通知 |

### 输入配置

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/ModifyDPInputConfig](#ucfviewmodifydpinputconfig) | 修改DefaultPawn输入配置 |
| [UCFView/ResetDPInputToDefault](#ucfviewresetdpinputtodefault) | 恢复DefaultPawn默认输入方式 |

### 功能控制

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/SetDPFeatureSwitch](#ucfviewsetdpfeatureswitch) | 设置DefaultPawn功能开关 |
| [UCFView/SetDPSpeedParams](#ucfviewsetdpspeedparams) | 设置DefaultPawn速度参数 |

### 系统

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFView/Reset](#ucfviewreset) | 重置UCFView类的所有状态 |

<a id="ucfviewsetdpposition"></a>

[← 返回接口一览](#接口一览)

## 设置DefaultPawn的位置和视角

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- OffestDistance 为相对目标位置的反向偏移距离，单位为厘米
- bIgnoreLag 为 false 时会启用平滑移动效果

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirLocation | Object | 必填 | 目标位置，世界坐标系下的三维坐标 |
| DesirLocation.X | Float | 必填 | X坐标，单位：厘米 |
| DesirLocation.Y | Float | 必填 | Y坐标，单位：厘米 |
| DesirLocation.Z | Float | 必填 | Z坐标，单位：厘米 |
| DesirRotation | Object | 必填 | 目标视角，欧拉角表示的旋转值 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角，单位：度，取值 [-90,90] |
| DesirRotation.Yaw | Float | 必填 | 偏航角，单位：度，取值 [-180,180] |
| DesirRotation.Roll | Float | 必填 | 翻滚角，单位：度，取值 [-180,180] |
| OffestDistance | Float | 选填 | 相对目标位置的反向偏移距离（厘米），默认 `0` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "123456789",
  "Interface": "UCFView/SetDPPosition",
  "Params": {
    "DesirLocation": { "X": 1000.0, "Y": 2000.0, "Z": 500.0 },
    "DesirRotation": { "Pitch": 0.0, "Yaw": 90.0, "Roll": 0.0 },
    "OffestDistance": 100.0,
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
  "ExecutionID": "123456789",
  "Interface": "UCFView/SetDPPosition",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdplocation"></a>

[← 返回接口一览](#接口一览)

## 设置DefaultPawn的位置

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 该接口仅修改位置，不改变当前视角
- OffestDistance 为相对目标位置的反向偏移距离，单位为厘米
- bIgnoreLag 为 false 时会启用平滑移动效果

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirLocation | Object | 必填 | 目标位置，世界坐标系下的三维坐标 |
| DesirLocation.X | Float | 必填 | X坐标，单位：厘米 |
| DesirLocation.Y | Float | 必填 | Y坐标，单位：厘米 |
| DesirLocation.Z | Float | 必填 | Z坐标，单位：厘米 |
| OffestDistance | Float | 选填 | 相对目标位置的反向偏移距离（厘米），默认 `0` |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "223456789",
  "Interface": "UCFView/SetDPLocation",
  "Params": {
    "DesirLocation": { "X": 1000.0, "Y": 2000.0, "Z": 500.0 },
    "OffestDistance": 100.0,
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
  "ExecutionID": "223456789",
  "Interface": "UCFView/SetDPLocation",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdprotation"></a>

[← 返回接口一览](#接口一览)

## 设置DefaultPawn的视角

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 该接口仅修改视角，不改变当前位置
- bIgnoreLag 为 false 时会启用平滑旋转效果

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| DesirRotation | Object | 必填 | 目标视角，欧拉角表示的旋转值 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角，单位：度，取值 [-90,90] |
| DesirRotation.Yaw | Float | 必填 | 偏航角，单位：度，取值 [-180,180] |
| DesirRotation.Roll | Float | 必填 | 翻滚角，单位：度，取值 [-180,180] |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "323456789",
  "Interface": "UCFView/SetDPRotation",
  "Params": {
    "DesirRotation": { "Pitch": -30.0, "Yaw": 180.0, "Roll": 0.0 },
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
  "ExecutionID": "323456789",
  "Interface": "UCFView/SetDPRotation",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewgetdpposition"></a>

[← 返回接口一览](#接口一览)

## 获取DefaultPawn的位置和视角

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 返回的位置和旋转值均保留两位小数
- 位置坐标为世界坐标系下的三维坐标
- 旋转值为欧拉角表示

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "423456789",
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

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| PawnLocation | Object | 必填 | 当前位置，世界坐标系下的三维坐标，保留两位小数 |
| PawnLocation.X | Float | 必填 | X坐标（厘米） |
| PawnLocation.Y | Float | 必填 | Y坐标（厘米） |
| PawnLocation.Z | Float | 必填 | Z坐标（厘米） |
| PawnRotation | Object | 必填 | 当前视角，欧拉角表示的旋转值，保留两位小数 |
| PawnRotation.Pitch | Float | 必填 | 俯仰角（度） |
| PawnRotation.Yaw | Float | 必填 | 偏航角（度） |
| PawnRotation.Roll | Float | 必填 | 翻滚角（度） |

#### 回调参数示例

```json
{
  "ExecutionID": "423456789",
  "Interface": "UCFView/GetDPPosition",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "PawnLocation": { "X": 1000.50, "Y": 2000.75, "Z": 500.25 },
    "PawnRotation": { "Pitch": -30.50, "Yaw": 180.00, "Roll": 0.00 }
  }
}
```

<a id="ucfviewfocustoactorbytag"></a>

[← 返回接口一览](#接口一览)

## 聚焦到指定Tag的对象

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 通过 Tag 查找对象，如果找到多个对象则使用第一个
- 计算包围盒时会包含目标对象及其所有挂载的子对象
- 若未传入 OffestDistance 或小于 0，则使用包围盒最大边长的 2 倍作为偏移距离
- 若未传入 DesirRotation，则保持当前视角不变
- bIgnoreLag 为 false 时会启用平滑移动效果

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| TargetTag | String | 必填 | 目标对象的 Tag 标识 |
| OffestDistance | Float | 选填 | 相对包围盒中心的反向偏移距离（厘米）。小于 0 则自动计算 |
| DesirRotation | Object | 选填 | 目标视角。不传入则保持当前视角 |
| DesirRotation.Pitch | Float | 必填 | 俯仰角（度），取值 [-90,90] |
| DesirRotation.Yaw | Float | 必填 | 偏航角（度），取值 [-180,180] |
| DesirRotation.Roll | Float | 必填 | 翻滚角（度），取值 [-180,180] |
| bIgnoreLag | Boolean | 选填 | 是否忽略平滑移动效果，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "1123456789",
  "Interface": "UCFView/FocusToActorByTag",
  "Params": {
    "TargetTag": "Building_01",
    "OffestDistance": 500.0,
    "DesirRotation": { "Pitch": -30.0, "Yaw": 45.0, "Roll": 0.0 },
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
  "ExecutionID": "1123456789",
  "Interface": "UCFView/FocusToActorByTag",
  "Status": false,
  "DebugInfo": "未找到Tag为[Building_01]的对象",
  "Params": {}
}
```

#### 功能演示

[![B站视频](https://img.shields.io/badge/点击查看-BiliBili功能演示-ff69b4?style=flat-square)](https://www.bilibili.com/video/BV1wvVh6oEKM/)

<a id="ucfviewstartroamuniformtime"></a>

[← 返回接口一览](#接口一览)

## 开始漫游（均匀时间模式）

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 关键帧数组至少需要包含 2 个关键帧
- 漫游总时长必须大于 0
- 相邻关键帧之间耗时相同，距离长则速度快，距离短则速度慢
- 漫游完成后会自动停止并触发 OnRoamFinished 接口

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Keyframes | Array | 必填 | 关键帧数组，至少包含 2 个元素 |
| Keyframes[].Location | Object | 必填 | 关键帧位置（世界坐标） |
| Keyframes[].Location.X | Float | 必填 | X坐标（厘米） |
| Keyframes[].Location.Y | Float | 必填 | Y坐标（厘米） |
| Keyframes[].Location.Z | Float | 必填 | Z坐标（厘米） |
| Keyframes[].Rotation | Object | 必填 | 关键帧视角（欧拉角） |
| Keyframes[].Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Keyframes[].Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Keyframes[].Rotation.Roll | Float | 必填 | 翻滚角（度） |
| Duration | Float | 必填 | 漫游总时长（秒） |

#### 调用参数示例

```json
{
  "ExecutionID": "523456789",
  "Interface": "UCFView/StartRoamUniformTime",
  "Params": {
    "Keyframes": [
      { "Location": {"X":0,"Y":0,"Z":500}, "Rotation": {"Pitch":-30,"Yaw":0,"Roll":0} },
      { "Location": {"X":1000,"Y":0,"Z":500}, "Rotation": {"Pitch":-30,"Yaw":90,"Roll":0} },
      { "Location": {"X":1000,"Y":1000,"Z":500}, "Rotation": {"Pitch":-30,"Yaw":180,"Roll":0} }
    ],
    "Duration": 15.0
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
  "ExecutionID": "523456789",
  "Interface": "UCFView/StartRoamUniformTime",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewstartroamuniformspeed"></a>

[← 返回接口一览](#接口一览)

## 开始漫游（均匀速度模式）

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 关键帧数组至少需要包含 2 个关键帧
- 漫游总时长必须大于 0
- 整个过程保持匀速运动，每帧移动的实际距离相同
- 各段耗时根据实际路径长度自动分配
- 漫游完成后会自动停止并触发 OnRoamFinished 接口

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Keyframes | Array | 必填 | 关键帧数组，至少包含 2 个元素 |
| Keyframes[].Location | Object | 必填 | 关键帧位置（世界坐标） |
| Keyframes[].Location.X | Float | 必填 | X坐标（厘米） |
| Keyframes[].Location.Y | Float | 必填 | Y坐标（厘米） |
| Keyframes[].Location.Z | Float | 必填 | Z坐标（厘米） |
| Keyframes[].Rotation | Object | 必填 | 关键帧视角（欧拉角） |
| Keyframes[].Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Keyframes[].Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Keyframes[].Rotation.Roll | Float | 必填 | 翻滚角（度） |
| Duration | Float | 必填 | 漫游总时长（秒） |

#### 调用参数示例

```json
{
  "ExecutionID": "623456789",
  "Interface": "UCFView/StartRoamUniformSpeed",
  "Params": {
    "Keyframes": [
      { "Location": {"X":1000,"Y":2000,"Z":500}, "Rotation": {"Pitch":-30,"Yaw":0,"Roll":0} },
      { "Location": {"X":1500,"Y":2500,"Z":600}, "Rotation": {"Pitch":-20,"Yaw":90,"Roll":0} },
      { "Location": {"X":2000,"Y":3000,"Z":700}, "Rotation": {"Pitch":-10,"Yaw":180,"Roll":0} }
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
  "ExecutionID": "623456789",
  "Interface": "UCFView/StartRoamUniformSpeed",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewstartroamcustomtime"></a>

[← 返回接口一览](#接口一览)

## 开始漫游（自定义时间模式）

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 关键帧数组至少需要包含 2 个关键帧
- 每个关键帧的 Duration 参数表示从上一个关键帧到达该关键帧所需的时间（段时长）
- 第一个关键帧的 Duration 可以忽略（设为 0），因为它是起点
- 后续关键帧的 Duration 必须大于 0
- 漫游总时长由各段 Duration 累加得到
- 漫游完成后会自动停止并触发 OnRoamFinished 接口

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Keyframes | Array | 必填 | 关键帧数组，每个元素含 Location、Rotation、Duration |
| Keyframes[].Location | Object | 必填 | 关键帧位置（世界坐标） |
| Keyframes[].Location.X | Float | 必填 | X坐标（厘米） |
| Keyframes[].Location.Y | Float | 必填 | Y坐标（厘米） |
| Keyframes[].Location.Z | Float | 必填 | Z坐标（厘米） |
| Keyframes[].Rotation | Object | 必填 | 关键帧视角（欧拉角） |
| Keyframes[].Rotation.Pitch | Float | 必填 | 俯仰角（度） |
| Keyframes[].Rotation.Yaw | Float | 必填 | 偏航角（度） |
| Keyframes[].Rotation.Roll | Float | 必填 | 翻滚角（度） |
| Keyframes[].Duration | Float | 必填 | 到达该帧用时（秒），首帧可设 0 |

#### 调用参数示例

```json
{
  "ExecutionID": "1023456789",
  "Interface": "UCFView/StartRoamCustomTime",
  "Params": {
    "Keyframes": [
      { "Location": {"X":0,"Y":0,"Z":500}, "Rotation": {"Pitch":-30,"Yaw":0,"Roll":0}, "Duration": 0 },
      { "Location": {"X":1000,"Y":0,"Z":500}, "Rotation": {"Pitch":-30,"Yaw":90,"Roll":0}, "Duration": 3 },
      { "Location": {"X":1000,"Y":1000,"Z":600}, "Rotation": {"Pitch":-20,"Yaw":180,"Roll":0}, "Duration": 5 },
      { "Location": {"X":0,"Y":1000,"Z":700}, "Rotation": {"Pitch":-10,"Yaw":270,"Roll":0}, "Duration": 2 }
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
  "ExecutionID": "1023456789",
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

- 必须在漫游进行中才能暂停
- 暂停后可以通过 ResumeRoam 继续漫游
- 适用于所有漫游模式（均匀时间、均匀速度、自定义时间）

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "623456789",
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
  "ExecutionID": "623456789",
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

- 必须在漫游已暂停的状态下才能继续
- 继续后会从暂停的时间点继续漫游
- 适用于所有漫游模式（均匀时间、均匀速度、自定义时间）

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "723456789",
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
  "ExecutionID": "723456789",
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

- 停止后漫游状态会被清除
- 停止后如需再次漫游，需要重新调用 StartRoamXXX 接口
- 适用于所有漫游模式（均匀时间、均匀速度、自定义时间）

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "823456789",
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
  "ExecutionID": "823456789",
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

- 必须已经调用过 StartRoamXXX 接口初始化漫游数据
- 重新开始会将漫游进度重置为 0
- 如果漫游已暂停，重新开始后会自动恢复运行状态
- 以上一次开始漫游时的模式（均匀时间/均匀速度/自定义时间）重新开始
- 适用于所有漫游模式（均匀时间、均匀速度、自定义时间）

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "923456789",
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
  "ExecutionID": "923456789",
  "Interface": "UCFView/RestartRoam",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewonroamfinished"></a>

[← 返回接口一览](#接口一览)

## 漫游结束通知

**类型:** Trigger

**Tips:**

- 漫游时间达到总时长，自动完成时触发，手动调用 StopRoam 不会触发此接口
- 仅在漫游自然完成时触发，手动调用 StopRoam 不会触发
- 适用于所有三种漫游模式（均匀时间、均匀速度、自定义时间）
- 可用于在漫游结束后执行后续操作，如开始下一段漫游、显示提示信息等

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 "Null" |
| Interface | String | 接口名称，固定为 "UCFView/OnRoamFinished" |
| Status | Boolean | 固定为 true |
| DebugInfo | String | 调试信息，固定为 "漫游已完成" |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFView/OnRoamFinished",
  "Status": true,
  "DebugInfo": "漫游已完成",
  "Params": {}
}
```

<a id="ucfviewmodifydpinputconfig"></a>

[← 返回接口一览](#接口一览)

## 修改DefaultPawn输入配置

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 所有参数均为必填，需要同时配置所有输入方式
- 所有输入方式必须唯一，不能有重复的输入绑定
- 修改后立即生效，影响后续的所有 Pawn 操作
- 可通过 ResetDPInputToDefault 接口恢复默认设置

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| HMoveInput | String | 必填 | 水平移动输入，可选值："UCFInputTagBase.LeftMouseDown", "UCFInputTagBase.RightMouseDown", "UCFInputTagBase.MiddleMouseDown" |
| VUPInput | String | 必填 | 垂直向上移动输入，可选值："UCFInputTagDefaultPawn.QDown", "UCFInputTagDefaultPawn.EDown" |
| VDownInput | String | 必填 | 垂直向下移动输入，可选值："UCFInputTagDefaultPawn.QDown", "UCFInputTagDefaultPawn.EDown" |
| RotateAnchorInput | String | 必填 | 固定锚点旋转输入，可选值："UCFInputTagBase.LeftMouseDown", "UCFInputTagBase.RightMouseDown", "UCFInputTagBase.MiddleMouseDown" |
| RotateSelfInput | String | 必填 | 绕自身旋转输入，可选值："UCFInputTagBase.LeftMouseDown", "UCFInputTagBase.RightMouseDown", "UCFInputTagBase.MiddleMouseDown" |
| ZoomInput | String | 必填 | 缩放输入，可选值："UCFInputTagBase.MiddleMouseRoll", "UCFInputTagBase.LeftMouseDown", "UCFInputTagBase.RightMouseDown", "UCFInputTagBase.MiddleMouseDown" |
| FocusInput | String | 必填 | 快速聚焦输入，可选值："LeftMouseDoubleTap", "RightMouseDoubleTap", "MiddleMouseDoubleTap" |

#### 调用参数示例

```json
{
  "ExecutionID": "1023456789",
  "Interface": "UCFView/ModifyDPInputConfig",
  "Params": {
    "HMoveInput": "UCFInputTagBase.RightMouseDown",
    "VUPInput": "UCFInputTagDefaultPawn.EDown",
    "VDownInput": "UCFInputTagDefaultPawn.QDown",
    "RotateAnchorInput": "UCFInputTagBase.LeftMouseDown",
    "RotateSelfInput": "UCFInputTagBase.MiddleMouseDown",
    "ZoomInput": "UCFInputTagBase.MiddleMouseRoll",
    "FocusInput": "RightMouseDoubleTap"
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
  "ExecutionID": "1023456789",
  "Interface": "UCFView/ModifyDPInputConfig",
  "Status": false,
  "DebugInfo": "输入动作冲突",
  "Params": {}
}
```

<a id="ucfviewresetdpinputtodefault"></a>

[← 返回接口一览](#接口一览)

## 恢复DefaultPawn默认输入方式

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 恢复所有输入方式到默认设置
- 恢复后立即生效

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### 调用参数示例

```json
{
  "ExecutionID": "1723456789",
  "Interface": "UCFView/ResetDPInputToDefault",
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
  "ExecutionID": "1723456789",
  "Interface": "UCFView/ResetDPInputToDefault",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdpfeatureswitch"></a>

[← 返回接口一览](#接口一览)

## 设置DefaultPawn功能开关

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 所有参数均为可选，不传入则保持当前状态不变
- 修改后立即生效，影响后续的 Pawn 操作
- 可用于动态控制 Pawn 的各项功能开关

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| bEnableCollision | Boolean | 选填 | 碰撞开关 |
| bEnableHMove | Boolean | 选填 | 固定锚点水平移动 |
| bEnableVMove | Boolean | 选填 | 竖直移动 |
| bEnableRotateWithAnchor | Boolean | 选填 | 固定锚点旋转 |
| bEnableRotateWithSelf | Boolean | 选填 | 绕自身旋转 |
| bEnableZoom | Boolean | 选填 | 缩放 |
| bEnableFastFocus | Boolean | 选填 | 快速聚焦 |

#### 调用参数示例

```json
{
  "ExecutionID": "1823456789",
  "Interface": "UCFView/SetDPFeatureSwitch",
  "Params": {
    "bEnableCollision": true,
    "bEnableHMove": true,
    "bEnableVMove": true,
    "bEnableRotateWithAnchor": true,
    "bEnableRotateWithSelf": true,
    "bEnableZoom": true,
    "bEnableFastFocus": true
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
  "ExecutionID": "1823456789",
  "Interface": "UCFView/SetDPFeatureSwitch",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewsetdpspeedparams"></a>

[← 返回接口一览](#接口一览)

## 设置DefaultPawn速度参数

**类型:** Sync

**Tips:**

- 当前 Player0 必须是 DefaultPawn 类型，否则操作失败
- 所有参数均为可选，不传入则保持当前值不变
- ZoomPercent 会自动限制在 [0.1, 0.8] 范围内
- LagSpeed 会自动限制在 [0.0, 8.0] 范围内，值为 0 时关闭平滑效果
- 参数修改后立即生效，影响后续的 Pawn 操作

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| RotateSpeed | Float | 选填 | 旋转角速度，默认值：3.0 |
| VerticalMoveSpeed | Float | 选填 | 竖直移动速度，单位：米/秒，默认值：3.0 |
| ZoomPercent | Float | 选填 | 单次缩放距离相对于当前位置与参考锚点距离的百分比，取值范围：[0.1, 0.8]，默认值：0.4 |
| LagSpeed | Float | 选填 | 滞后平滑速度，值越小滞后效果越明显，值为0即关闭，取值范围：[0.0, 8.0]，默认值：5.0 |

#### 调用参数示例

```json
{
  "ExecutionID": "1323456789",
  "Interface": "UCFView/SetDPSpeedParams",
  "Params": {
    "RotateSpeed": 4.0,
    "VerticalMoveSpeed": 5.0,
    "ZoomPercent": 0.5,
    "LagSpeed": 6.0
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
  "ExecutionID": "1323456789",
  "Interface": "UCFView/SetDPSpeedParams",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfviewreset"></a>

[← 返回接口一览](#接口一览)

## 重置UCFView类的所有状态

**类型:** Sync

**Tips:**

- UCFView必须重写ResetInterface()方法
- 该操作不可逆，重置后需要重新调用相关接口才能恢复

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
  "Interface": "UCFView/Reset",
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
  "Interface": "UCFView/Reset",
  "Status": true,
  "DebugInfo": "success",
  "Params": {}
}
```