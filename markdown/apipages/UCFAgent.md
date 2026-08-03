# UCFAgent - Agent连接管理

提供与Agent端的连接、鉴权、断开等接口

## 接口一览

| 接口名称 | 功能描述 |
| :--- | :--- |
| [UCFAgent/ConnectAgent](#ucfagentconnectagent) | 连接Agent |
| [UCFAgent/AuthenticateAgent](#ucfagentauthenticateagent) | Agent鉴权 |
| [UCFAgent/DisconnectAgent](#ucfagentdisconnectagent) | 断开Agent |
| [UCFAgent/IsConnectAgent](#ucfagentisconnectagent) | 查询Agent连接状态 |
| [UCFAgent/OnDisconnected](#ucfagentondisconnected) | Agent被动断开通知 |

<a id="ucfagentconnectagent"></a>

[← 返回接口一览](#接口一览)

## 连接Agent

**类型:** Async

**Tips:**

- 不支持WebSocket方式调用
- 若传入地址与当前已连接地址相同且处于已连接状态，直接返回成功，与当前已连接地址不同，自动断开旧连接并连接到新地址

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ServerURL | String | 必填 | Agent端地址 |
| TimeOut | Float | 选填 | 超时时间（秒），默认 `5.0` |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFAgent/ConnectAgent",
  "Params": {
    "ServerURL": "xxx",
    "TimeOut": 5.0
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
  "Interface": "UCFAgent/ConnectAgent",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfagentauthenticateagent"></a>

[← 返回接口一览](#接口一览)

## Agent鉴权

**类型:** Sync

**Tips:**

- 不支持WebSocket方式调用
- 应在连接Agentc成功之后调用

#### 调用参数说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| ExecutionID | String | 必填 | 执行ID |
| Interface | String | 必填 | 接口名称 |
| Params | Object | 必填 | 参数对象 |

#### Params内参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|:----:|------|
| PairId | String | 必填 | 鉴权配对ID(自行生成) |
| Token | String | 必填 | 鉴权令牌(Agent端生成) |

#### 调用参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFAgent/AuthenticateAgent",
  "Params": {
    "PairId": "xxx",
    "Token": "xxx"
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
  "Interface": "UCFAgent/AuthenticateAgent",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfagentdisconnectagent"></a>

[← 返回接口一览](#接口一览)

## 断开Agent

**类型:** Sync

**Tips:**

- 不支持WebSocket方式调用

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
  "Interface": "UCFAgent/DisconnectAgent",
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
  "Interface": "UCFAgent/DisconnectAgent",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {}
}
```

<a id="ucfagentisconnectagent"></a>

[← 返回接口一览](#接口一览)

## 查询Agent连接状态

**类型:** Sync

**Tips:**

- 不支持WebSocket方式调用

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
  "Interface": "UCFAgent/IsConnectAgent",
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
| bConnected | Boolean | 是否连接 |

#### 回调参数示例

```json
{
  "ExecutionID": "测试ID",
  "Interface": "UCFAgent/IsConnectAgent",
  "Status": true,
  "DebugInfo": "成功",
  "Params": {
    "bConnected": false
  }
}
```

<a id="ucfagentondisconnected"></a>

[← 返回接口一览](#接口一览)

## Agent被动断开通知

**类型:** Trigger

**Tips:**

- 仅Agent端断开或网络异常导致连接断开时触发，主动断开不会触发

#### 回调参数说明

| 字段 | 类型 | 说明 |
|------|------|------|
| ExecutionID | String | 触发接口无执行ID，固定为 `"Null"` |
| Interface | String | 接口名称，固定为 `"UCFAgent/OnDisconnected"` |
| Status | Boolean | 固定为 `true` |
| DebugInfo | String | 调试信息 |
| Params | Object | 参数对象 |

#### 回调参数示例

```json
{
  "ExecutionID": "Null",
  "Interface": "UCFAgent/OnDisconnected",
  "Status": true,
  "DebugInfo": "调试信息",
  "Params": {}
}
```
