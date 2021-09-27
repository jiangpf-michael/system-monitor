#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : urls.py
@Datetime   : 2021/9/26
@Site       :
@Software   : PyCharm

"""
from django.urls import path

# from monitor.views import Register
from monitor.views import Register, Report, Jobs

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('report', Report.as_view(), name='report'),
    path('jobs', Jobs.as_view(), name='jobs'),
    # path('register', views.register, name='register')
]
