import json
import logging

from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from monitor.code import CODE_CONST
from monitor.const import CONST
from monitor.models import Job, JobInfo
from monitor.params_check import check_post_params_of_register, check_put_params_of_job, check_get_params_of_jobs
from monitor.utils import get_dict, get_params_of_get_request, get_page_param, get_current_timestamp


class BaseView(View):
    @classmethod
    def success(cls, *args, **kwargs):
        result = {
            CONST.RESULT: CONST.SUCCESS,
            CONST.CODE: CODE_CONST.SUCCESS_CODE
        }
        result.update(get_dict(*args, **kwargs))
        return JsonResponse(result)

    @classmethod
    def failure(cls, error_code=-1, reason=None, *args, **kwargs):
        result = {
            CONST.RESULT: CONST.FAILURE,
            CONST.CODE: error_code,
            CONST.MESSAGE: reason
        }
        result.update(get_dict(*args, **kwargs))
        return JsonResponse(result)


class Register(BaseView):
    @csrf_exempt
    def post(self, request):
        try:
            params = json.loads(request.body)
            if not check_post_params_of_register(params):
                return self.failure(error_code=CODE_CONST.PARAM_ERROR, reason=CODE_CONST.PARAM_ERROR_MESSAGE)
            task_id = params.get(CONST.TASK_ID)
            job_name = params.get(CONST.JOB_NAME)
            next_trigger_time = params.get(CONST.NEXT_TRIGGER_TIME)
            remark = params.get(CONST.REMARK)
            job_list = Job.objects.filter(task_id=task_id)
            if job_list:
                return self.failure(error_code=CODE_CONST.OPERATION_ERROR, reason=CODE_CONST.OPERATION_ERROR_MESSAGE)
            healthy = 0
            if next_trigger_time >= get_current_timestamp():
                healthy = 1
            job = Job(task_id=task_id, job_name=job_name, next_trigger_time=next_trigger_time, remark=remark,
                      healthy=healthy)

            job.save()
            return self.success(id=job.id)
        except Exception as e:
            logging.error(f"ERROR received POST request of register from ip: {request.META.get(CONST.REMOTE_ADDR)}, "
                          f"params: {request.body}, error info: {str(e)}")
            return self.failure(error_code=CODE_CONST.SYSTEM_ERROR, reason=CODE_CONST.SYSTEM_ERROR_MESSAGE)


class Report(BaseView):
    @csrf_exempt
    def put(self, request):
        try:
            params = json.loads(request.body)
            if not check_put_params_of_job(params):
                return self.failure(error_code=CODE_CONST.PARAM_ERROR, reason=CODE_CONST.PARAM_ERROR_MESSAGE)

            task_id = params.get(CONST.TASK_ID)
            description = params.get(CONST.DESCRIPTION)
            next_trigger_time = params.get(CONST.NEXT_TRIGGER_TIME)
            status = params.get(CONST.STATUS) or 0
            job = Job.objects.get(task_id=task_id)
            if not job:
                return self.failure(error_code=CODE_CONST.PARAM_ERROR, reason=CODE_CONST.PARAM_ERROR_MESSAGE)
            job.next_trigger_time = next_trigger_time
            job.update_time = get_current_timestamp()
            job.healthy = status
            job.save()
            job_id = job.id
            job_info = JobInfo(**{
                CONST.JOB_ID: job_id,
                CONST.DESCRIPTION: description,
                CONST.STATUS: status,
                CONST.IP_ADDRESS: request.META.get(CONST.REMOTE_ADDR)
            })
            job_info.save()
            return self.success(id=job_info.id)
        except Exception as e:
            logging.error(f"ERROR received PUT request of report from ip: {request.META.get(CONST.REMOTE_ADDR)}, "
                          f"params: {request.body}, error info: {str(e)}")
            return self.failure(error_code=CODE_CONST.SYSTEM_ERROR, reason=CODE_CONST.SYSTEM_ERROR_MESSAGE)


class Jobs(BaseView):
    def get(self, request):
        try:
            params = get_params_of_get_request(request)
            if not check_get_params_of_jobs(params):
                return self.failure(error_code=CODE_CONST.PARAM_ERROR, reason=CODE_CONST.PARAM_ERROR_MESSAGE)
            page_size, page_num = get_page_param(params)
            jobs = Job.objects.all().order_by("-create_time")
            paginator = Paginator(jobs, page_size)  # Show 25 contacts per page.
            job_list = paginator.get_page(page_num)
            result = []
            for job in job_list:
                result.append({
                    CONST.ID: job.id,
                    CONST.JOB_NAME: job.job_name,
                    CONST.HEALTHY: job.healthy,
                    CONST.REMARK: job.remark
                })
            return self.success(count=paginator.count, data=result)
        except Exception as e:
            logging.error(f"ERROR received GET request of JOBS from ip: {request.META.get(CONST.REMOTE_ADDR)}, "
                          f"params: {request.GET}, error info: {str(e)}")
            return self.failure(error_code=CODE_CONST.SYSTEM_ERROR, reason=CODE_CONST.SYSTEM_ERROR_MESSAGE)
