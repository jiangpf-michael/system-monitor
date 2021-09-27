#### 查看job状态列表

> 说明： 查看job状态列表

- **对应模块：system-monitor**

- **作者： 江鹏飞**

- **请求URL**

  > /butter/system_monitor/jobs

- **请求方式**

  > GET

- **请求参数**

  | 请求参数  | 参数值                              | 参数说明       | 是否可选       |
    | :-------- | :---------------------------------- | :------------- | -------------- |
  | page_num  | string                              | 第几页         | 可选，默认为1  |
  | page_size | string（长度不超过3的数字型字符串） | 每页展示数据量 | 可选，默认为10 |

- **请求示例**

  > http://localhost:8000/butter/monitor/jobs?page_size=10&page_num=1

- **响应**

  | 正确返回参数 | 参数值 | 参数说明                                 |
    | :----------- | :----- | :--------------------------------------- |
  | result       | string | 请求结果（success：成功，failure：失败） |
  | code         | string | 响应码                                   |
  | message      | string | 错误信息                                 |

  ```json
  {
      "result": "success",
      "code": "00000",
      "count": 1,
      "data": [
          {
              "id": 2,
              "job_name": "job1",
              "healthy": 0,
              "remark": ""
          }
      ]
  }
  ```

