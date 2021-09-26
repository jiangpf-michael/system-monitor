import json
import logging

from django.http import JsonResponse
# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from monitor.code import CODE_CONST
from monitor.const import CONST
from monitor.params_check import check_post_params_of_register
from monitor.service import register_job


class Register(View):
    @csrf_exempt
    def post(self, request):
        try:
            params = json.loads(request.body)
            if not check_post_params_of_register(params):
                result = {
                    CONST.RESULT: CONST.FAILURE,
                    CONST.CODE: CODE_CONST.PARAM_ERROR,
                    CONST.MESSAGE: CODE_CONST.PARAM_ERROR_MESSAGE
                }
                return JsonResponse(result)

            result = register_job(params)
            return JsonResponse(result)
        except Exception as e:
            logging.error(f"ERROR received POST request from ip: {request.META.get(CONST.REMOTE_ADDR)}, "
                          f"params: {request.body}, error info: {str(e)}")
            result = {
                CONST.RESULT: CONST.FAILURE,
                CONST.CODE: CODE_CONST.SYSTEM_ERROR,
                CONST.MESSAGE: CODE_CONST.SYSTEM_ERROR_MESSAGE
            }
            return JsonResponse(result)
