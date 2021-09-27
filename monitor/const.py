#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : const.py
@Datetime   : 2021/9/27
@Site       :
@Software   : PyCharm

"""


class _CommonConst:
    def __setattr__(self, *_):
        raise SyntaxError("Trying to change a constant value")

    SUCCESS = "success"
    FAILURE = "failure"
    RESULT = "result"
    CODE = "code"
    MESSAGE = "message"
    REMOTE_ADDR = "REMOTE_ADDR"

    # jsonshema
    REQUIRED = 'required'
    ADDITIONAL_PROPERTIES = 'additionalProperties'
    OBJECT = 'object'
    PROPERTIES = 'properties'
    TYPE = 'type'
    ENUM = 'enum'
    ANYOF = 'anyOf'
    INTEGER = 'integer'
    STRING = 'string'
    BOOLEAN = "boolean"
    ITEMS = 'items'
    MINITEMS = 'minItems'
    MAXITEMS = 'maxItems'
    ARRAY = 'array'
    DESCRIPTION = 'description'
    PATTERN = 'pattern'
    MINIMUM = 'minimum'
    MAXIMUM = 'maximum'
    NUMBER = 'number'
    TIMESTAMP = 'timestamp'
    MIN_LENGTH = 'minLength'
    MAX_LENGTH = 'maxLength'
    GROUP_LIST = "group_list"
    GROUP_ID_LIST = "group_id_list"
    EXCLUSIVE_MINIMUM = "exclusiveMinimum"

    JOB_NAME = "job_name"
    JOB_ID = "job_id"
    NEXT_TRIGGER_TIME = "next_trigger_time"
    STATUS = "status"
    REMARK = "remark"
    HEALTHY = "healthy"
    IP_ADDRESS = "ip_address"
    PAGE_SIZE = "page_size"
    PAGE_NUM = "page_num"
    TASK_ID = "task_id"
    ID = "id"

    INTERVAL = "interval"


CONST = _CommonConst()
