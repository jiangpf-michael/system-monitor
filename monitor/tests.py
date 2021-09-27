# Create your tests here.
from django.test import Client
from django.test import TestCase

from monitor.const import CONST
from monitor.models import Job
from monitor.service import check_healthy_of_jobs, send_unhealthy_email
from monitor.utils import get_current_timestamp


class RegisterTest(TestCase):
    def setUp(self):
        Job.objects.create(task_id=100001,
                           job_name="test job report",
                           healthy=1,
                           next_trigger_time=get_current_timestamp(),
                           create_time=get_current_timestamp(),
                           update_time=get_current_timestamp(),
                           remark="test remark")

        Job.objects.create(task_id=100002,
                           job_name="test email send",
                           healthy=0,
                           next_trigger_time=get_current_timestamp(),
                           create_time=get_current_timestamp(),
                           update_time=get_current_timestamp(),
                           remark="test remark")

    def test_register(self):
        """
            test register api
        :return:
        """
        client = Client()
        params = {
            CONST.TASK_ID: 10000,
            CONST.JOB_NAME: "test job",
            CONST.NEXT_TRIGGER_TIME: get_current_timestamp(),
            CONST.REMARK: "test remark"
        }
        response = client.post("/butter/monitor/register", params, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CONST.SUCCESS, response.json().get(CONST.RESULT))
        self.assertIsNotNone(response.json().get(CONST.ID))

    def test_report(self):
        """
            test report api
        :return:
        """
        client = Client()
        params = {
            CONST.TASK_ID: 100001,
            CONST.NEXT_TRIGGER_TIME: get_current_timestamp(),
            CONST.DESCRIPTION: "test report description",
            CONST.STATUS: 0
        }
        response = client.put("/butter/monitor/report", params, content_type='application/json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(CONST.SUCCESS, response.json().get(CONST.RESULT))

    def test_jobs(self):
        """
            test job api
        :return:
        """
        client = Client()
        params = {
            CONST.PAGE_NUM: 1,
            CONST.PAGE_SIZE: 10
        }
        response = client.get("/butter/monitor/jobs", params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(CONST.SUCCESS, response.json().get(CONST.RESULT))

    def test_check_healthy_of_jobs(self):
        check_healthy_of_jobs()
        job = Job.objects.get(task_id=100001)
        self.assertEqual(job.healthy, 0)

    def test_send_unhealthy_email(self):
        result = send_unhealthy_email()
        self.assertIsNotNone(result)
