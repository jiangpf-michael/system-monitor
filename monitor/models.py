from django.db import models

# Create your models here.
from monitor.utils import get_current_timestamp


class Job(models.Model):
    task_id = models.IntegerField(unique=True)
    job_name = models.CharField(max_length=128)
    healthy = models.IntegerField(default=0)
    next_trigger_time = models.BigIntegerField()
    create_time = models.BigIntegerField(default=get_current_timestamp())
    update_time = models.BigIntegerField(default=get_current_timestamp())
    remark = models.CharField(max_length=512)


class JobInfo(models.Model):
    job_id = models.IntegerField()
    description = models.TextField()
    ip_address = models.CharField(max_length=15)
    status = models.IntegerField(default=0)
    create_time = models.BigIntegerField(default=get_current_timestamp())
