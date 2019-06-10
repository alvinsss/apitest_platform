from django.shortcuts import render
from django.http import JsonResponse ,HttpResponseRedirect
from testtask.models import  TestTask
from project.models import Project
from module.models import  Module
from testcase.models import TestCase
from django.views.decorators.csrf import  csrf_exempt
import json


def locustmanager(request):
	"""
	locust管理
	"""
	task_list = TestTask.objects.filter(del_status=False)

	return render(request, "locust_list.html", {
		"type": "list",
		"tasks": task_list
	})