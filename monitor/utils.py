#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpf@touchdata.io
@File       : utils.py
@Datetime   : 2021/9/26
@Site       :
@Software   : PyCharm

"""
import logging
import time

from jsonschema import validate


def get_current_timestamp():
    return int(1000 * time.time())


def validate_data(schema, data):
    try:
        validate(data, schema)
        return True
    except Exception as e:
        logging.exception(f"error validate data info, error info: {str(e)}")
        return False
