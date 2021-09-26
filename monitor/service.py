#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author     : jiangpf
@Contact    : jiangpf@touchdata.io
@File       : service.py
@Datetime   : 2021/9/27
@Site       :
@Software   : PyCharm

"""
from monitor.code import CODE_CONST
from monitor.const import CONST
from monitor.models import Job


def register_job(params):
    job_id = params.get(CONST.JOB_ID)
    job_name = params.get(CONST.JOB_NAME)
    next_trigger_time = params.get(CONST.NEXT_TRIGGER_TIME)
    remark = params.get(CONST.REMARK) or "",
    job = Job.objects.filter(job_id=job_id)
    if not job:
        job = Job(job_id=job_id, job_name=job_name, next_trigger_time=next_trigger_time, remark=remark)
    else:
        job.job_id = job_id
        job.job_name = job_name
        job.next_trigger_time = next_trigger_time
        job.remark = remark
    job.save()
    return {CONST.RESULT: CONST.SUCCESS, CONST.CODE: CODE_CONST.SUCCESS_CODE}
