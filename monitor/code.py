#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : code.py
@Datetime   : 2021/9/27
@Site       :
@Software   : PyCharm

"""


class _CodeConst:
    def __setattr__(self, *_):
        raise SyntaxError("Trying to change a constant value")

    SUCCESS_CODE = "00000"
    SYSTEM_ERROR = "10000"
    SYSTEM_ERROR_MESSAGE = "SYSTEM ERROR"
    PARAM_ERROR = "10001"
    PARAM_ERROR_MESSAGE = "PARAM ERROR"
    OPERATION_ERROR = "10002"
    OPERATION_ERROR_MESSAGE = "RECORD EXISTED"



CODE_CONST = _CodeConst()
