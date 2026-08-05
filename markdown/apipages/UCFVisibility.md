# UCFVisibility - 可视性管理

提供Actor显隐控制、流关卡加载与卸载等接口实现场景的可视性管理

## 接口一览

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFVisibility/SetActorVisibility](#ucfvisibilitysetactorvisibility) | 设置Actor可视性 |
| [UCFVisibility/GetLevelList](#ucfvisibilitygetlevellist) | 获取已加载的流关卡名称 |
| [UCFVisibility/ShowLevels](#ucfvisibilityshowlevels) | 显示流关卡 |
| [UCFVisibility/HideLevels](#ucfvisibilityhidelevels) | 隐藏流关卡 |

<a id="ucfvisibilitysetactorvisibility"></a>

[← 返回接口一览](#接口一览)

## 设置Actor可视性

**类型:** Sync

**Tips:**

- 同时拥有显示和隐藏标签的Actor，显示优先级高于隐藏
- 隐藏Actor后，该Actor将不可见、不可交互且不参与碰撞计算

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| Tags | `Array<String>` | 选填 | 显示标签数组，拥有其中任一标签的Actor会显示，与UnTags必选其一 |
| UnTags | `Array<String>` | 选填 | 隐藏标签数组，拥有其中任一标签的Actor会隐藏，与Tags必选其一 |
| bAffectAttached | Boolean | 选填 | 是否影响附加的Actor，默认 `false` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFVisibility/SetActorVisibility",
  "Params": {
    "Tags": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "UnTags": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "bAffectAttached": false
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
  "Interface": "UCFVisibility/SetActorVisibility",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfvisibilitygetlevellist"></a>

[← 返回接口一览](#接口一览)

## 获取已加载的流关卡名称

**类型:** Sync

**Tips:**

- 仅返回关卡列表中已加载的流关卡，不包括持久关卡
- 返回的关卡名称为短名称（不含路径前缀和PIE前缀）

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
  "Interface": "UCFVisibility/GetLevelList",
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
| LevelNames | `Array<String>` | 已加载的流关卡名称 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFVisibility/GetLevelList",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "LevelNames": [
      "xxx",
      "xxx",
      "xxx"
    ]
  }
}
```

<a id="ucfvisibilityshowlevels"></a>

[← 返回接口一览](#接口一览)

## 显示流关卡

**类型:** Async

**Tips:**

- 支持关卡列表中预配置的流关卡或指定全路径的关卡资源(.umap)
- 若流关卡未加载，需要先进行加载操作，超时未加载完成的关卡会被卸载

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| LevelNames | `Array<String>` | 必填 | 关卡名称，对于关卡列表中的流关卡直接为关卡名称；对于未加载的关卡资源(.umap)，使用全路径，例如"/Game/Maps/MyMapName" |
| Timeout | Float | 选填 | 超时（秒），默认 `30.0，超时未加载完成的关卡会被标记为失败并卸载` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFVisibility/ShowLevels",
  "Params": {
    "LevelNames": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "Timeout": 30.0
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
| ErrorLevels | `Array<String>` | 错误的关卡列表 |
| TimeoutLevels | `Array<String>` | 超时的关卡列表 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFVisibility/ShowLevels",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "ErrorLevels": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "TimeoutLevels": [
      "xxx",
      "xxx",
      "xxx"
    ]
  }
}
```

<a id="ucfvisibilityhidelevels"></a>

[← 返回接口一览](#接口一览)

## 隐藏流关卡

**类型:** Sync

**Tips:**

- 仅支持已加载的的流关卡

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| LevelNames | `Array<String>` | 必填 | 关卡名称，仅支持已加载的的流关卡，直接为关卡名称即可 |
| Unload | Boolean | 选填 | 是否彻底卸载，默认 `false。若为true，则可降低性能消耗，但再次显示时耗时较长` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFVisibility/HideLevels",
  "Params": {
    "LevelNames": [
      "xxx",
      "xxx",
      "xxx"
    ],
    "Unload": false
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
| FailedLevels | `Array<String>` | 隐藏失败的关卡列表 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFVisibility/HideLevels",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "FailedLevels": [
      "xxx",
      "xxx",
      "xxx"
    ]
  }
}
```
