#### 上报job工作日志

> 说明：上报job工作日志

- **对应模块：system-monitor**

- **作者： 江鹏飞**

- **请求URL**

  > /butter/system_monitor/report

- **请求方式**

  > PUT

- **请求参数**

  | 请求参数          | 参数值                  | 参数说明     | 是否可选 |
    | :---------------- | :---------------------- | :----------- | -------- |
  | task_id           | int                     | 任务唯一标识 | 必选     |
  | next_trigger_time | int（13位时间戳）       | 下次上报时间 | 必选     |
  | status            | int（0：失败，1：成功） | 任务状态     | 必选     |
  | description       | string                  | 任务日志详情 | 可选     |

- **请求示例**

  > http://localhost:8000/butter/monitor/report

  ```json
  {
      "task_id": 10,
  	"next_trigger_time":1632664632000,
  	"status": 0,
      "description": "this is the error log"
  }
  ```

- **响应**

  | 正确返回参数 | 参数值 | 参数说明                                 |
    | :----------- | :----- | :--------------------------------------- |
  | result       | string | 请求结果（success：成功，failure：失败） |
  | code         | string | 响应码                                   |
  | message      | string | 错误信息                                 |

  ```json
  {
    "result": "success",
    "code": "00000"
  }	
  ```

