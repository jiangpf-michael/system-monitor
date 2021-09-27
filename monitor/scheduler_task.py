#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : scheduler_task.py
@Datetime   : 2021/9/27
@Site       :
@Software   : PyCharm

"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore

from monitor.service import send_unhealthy_email, check_healthy_of_jobs


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(send_unhealthy_email, trigger=CronTrigger(minute="*/1"))
    scheduler.add_job(check_healthy_of_jobs, trigger=CronTrigger(minute="*/1"))
    try:
        logging.info('scheduler start success...')
        scheduler.start()
    except Exception as e:
        logging.info(f'scheduler start failure..., error info: {str(e)}')
        scheduler.shutdown()
