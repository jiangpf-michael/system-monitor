#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
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
        CONST.REQUIRED: [CONST.TASK_ID, CONST.JOB_NAME, CONST.NEXT_TRIGGER_TIME],
        CONST.PROPERTIES: {
            CONST.TASK_ID: {
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


def check_put_params_of_job(data):
    job_schema = {
        CONST.TYPE: CONST.OBJECT,
        CONST.ADDITIONAL_PROPERTIES: True,
        CONST.REQUIRED: [CONST.TASK_ID, CONST.STATUS, CONST.NEXT_TRIGGER_TIME],
        CONST.PROPERTIES: {
            CONST.TASK_ID: {
                CONST.TYPE: CONST.INTEGER,
                CONST.MINIMUM: 1
            },
            CONST.DESCRIPTION: {
                CONST.TYPE: CONST.STRING,
                CONST.MIN_LENGTH: 1,
            },
            CONST.NEXT_TRIGGER_TIME: {
                CONST.TYPE: CONST.INTEGER,
                CONST.MINIMUM: 1577808000000
            },
            CONST.STATUS: {
                CONST.TYPE: CONST.INTEGER,
                CONST.MINIMUM: 0,
                CONST.MAXIMUM: 1
            }
        }
    }
    return validate_data(job_schema, data)


def check_get_params_of_jobs(data):
    job_schema = {
        CONST.TYPE: CONST.OBJECT,
        CONST.ADDITIONAL_PROPERTIES: True,
        CONST.REQUIRED: [],
        CONST.PROPERTIES: {
            CONST.PAGE_NUM: {
                CONST.TYPE: CONST.STRING,
                CONST.MIN_LENGTH: 1
            },
            CONST.PAGE_SIZE: {
                CONST.TYPE: CONST.STRING,
                CONST.MIN_LENGTH: 1,
                CONST.MAX_LENGTH: 3
            },
        }
    }
    return validate_data(job_schema, data)
