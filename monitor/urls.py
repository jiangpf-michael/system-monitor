#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpf@touchdata.io
@File       : urls.py
@Datetime   : 2021/9/26
@Site       :
@Software   : PyCharm

"""
from django.urls import path

from monitor import views
# from monitor.views import Register
from monitor.views import Register

urlpatterns = [path('index', views.index, name='index'),
               path('register', Register.as_view(), name='register'),
               # path('register', views.register, name='register')
               ]
