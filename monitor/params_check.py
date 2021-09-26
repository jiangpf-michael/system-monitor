#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpf@touchdata.io
@File       : params_check.py
@Datetime   : 2021/9/27
@Site       :
@Software   : PyCharm

"""
from monitor.const import CONST
from monitor.utils import validate_data


def check_post_params_of_register(data):
    register_schema = {
        CONST.TYPE: CONST.OBJECT,
        CONST.ADDITIONAL_PROPERTIES: True,
        CONST.REQUIRED: [CONST.JOB_ID, CONST.JOB_NAME, CONST.NEXT_TRIGGER_TIME],
        CONST.PROPERTIES: {
            CONST.JOB_ID: {
                CONST.TYPE: CONST.INTEGER,
                CONST.MINIMUM: 1
            },
            CONST.JOB_NAME: {
                CONST.TYPE: CONST.STRING,
                CONST.MIN_LENGTH: 1,
                CONST.MAX_LENGTH: 128
            },
            CONST.NEXT_TRIGGER_TIME: {
                CONST.TYPE: CONST.INTEGER,
                CONST.MINIMUM: 1577808000000
            }
        }
    }
    return validate_data(register_schema, data)
