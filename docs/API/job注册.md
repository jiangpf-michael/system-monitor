#### job注册

> 说明： 注册job信息

- **对应模块：system-monitor**

- **作者： 江鹏飞**

- **请求URL**

  > /butter/system_monitor/register

- **请求方式**

  > POST

- **请求参数**

  | 请求参数          | 参数值                    | 参数说明        | 是否可选 |
    | :---------------- | :------------------------ | :-------------- | -------- |
  | job_name          | string（不超过128个字符） | 任务名称        | 必选     |
  | task_id           | int                       | 任务唯一标识    | 必选     |
  | next_trigger_time | int（13位时间戳）         | 下一次上报时间  | 必选     |
  | remark            | string                    | 不超过512个字符 | 可选     |

- **请求示例**

  > http://localhost:8000/butter/monitor/register

  ```json
  {
  	"job_name":"job1",
      "task_id": 10,
  	"next_trigger_time":1632664632000,
  	"remark":"Runs at 7 o'clock every day"
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

