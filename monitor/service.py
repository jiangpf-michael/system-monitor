#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpengfei573@163.com
@File       : service.py
@Datetime   : 2021/9/27
@Site       :
@Software   : PyCharm

"""
import logging

from django.conf import settings
from django.core.mail import send_mail

from monitor.models import Job
from monitor.utils import get_current_timestamp


def check_healthy_of_jobs():
    logging.info('START check healthy of jobs')
    try:
        current_timestamp = get_current_timestamp()
        jobs = Job.objects.filter(next_trigger_time__lt=current_timestamp)
        for job in jobs:
            job.healthy = 0
            job.update_time = get_current_timestamp()
            job.save()
    except Exception as e:
        logging.error('ERROR check healthy of jobs, error info: {}'.format(str(e)))
    logging.info('FINISH check healthy of jobs')


def send_unhealthy_email():
    logging.info('START send unhealthy email')
    try:
        jobs = Job.objects.filter(healthy=0)
        if not jobs:
            return
        subject = 'Unhealthy job notify'
        message = "The following jobs are unhealthy, please check: \n"
        for job in jobs:
            message += "job_id: {}, job_name: {} \n".format(job.id, job.job_name)
        send_mail(subject, message, settings.EMAIL_FROM, settings.EMAIL_RECEIVER)
    except Exception as e:
        logging.error('ERROR send unhealthy email, error info: {}'.format(str(e)))
    logging.info('FINISH send unhealthy email')
