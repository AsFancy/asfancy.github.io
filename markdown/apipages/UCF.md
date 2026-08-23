# UCF - 接口管理

接口管理，提供全局重置，接口类重置等接口。UCF定义为接口管理类UCFIManager对外的简称、区分于派生自UCFIBase的接口类，不会被重置。

## 接口一览

### 重置接口

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCF/ResetInterface](#ucfresetinterface) | 重置指定接口类状态 |
| [UCF/ResetAll](#ucfresetall) | 重置所有接口类状态 |

<a id="ucfresetinterface"></a>

[← 返回接口一览](#接口一览)

## 重置指定接口类状态

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
| Interface | String | 必填 | 需要重置的接口类名（如 "UCFView"） |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCF/ResetInterface",
  "Params": {
    "Interface": "UCFView"
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
  "Interface": "UCF/ResetInterface",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfresetall"></a>

[← 返回接口一览](#接口一览)

## 重置所有接口类状态

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
  "Interface": "UCF/ResetAll",
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
  "Interface": "UCF/ResetAll",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```
