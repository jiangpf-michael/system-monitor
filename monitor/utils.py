#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : utils.py
@Datetime   : 2021/9/26
@Site       :
@Software   : PyCharm

"""
import logging
import time

from jsonschema import validate

from monitor.const import CONST


def get_current_timestamp():
    return int(1000 * time.time())


def get_dict(*args, **kwargs):
    if not args and not kwargs:
        return {}
    if len(args) == 1 and not kwargs and isinstance(args[0], dict):
        return args[0]
    if kwargs and not args:
        return kwargs

    raise ValueError('neither a dict nor a **kwargs')


def validate_data(schema, data):
    try:
        validate(data, schema)
        return True
    except Exception as e:
        logging.exception(f"error validate data info, error info: {str(e)}")
        return False


def get_params_of_get_request(request):
    params = {}
    for key, value in request.GET.items():
        params[key] = value
    return params


def get_page_param(data):
    try:
        page_size = int(data.get(CONST.PAGE_SIZE, 10))
        page_num = int(data.get(CONST.PAGE_NUM, 1))
    except Exception as e:
        logging.exception('ERROR get page param, error info: {}'.format(str(e)))
        page_size = 10
        page_num = 1
    return page_size, page_num
