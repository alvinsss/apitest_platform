from django.shortcuts import render
from django.http import JsonResponse ,HttpResponseRedirect
from testtask.models import  TestTask
from project.models import Project
from module.models import  Module
from testcase.models import TestCase
from django.views.decorators.csrf import  csrf_exempt
import json


def testtask_manage(request):
	"""
	任务管理
	"""
	task_list = TestTask.objects.filter(del_status=False)

	return render(request, "task_list.html", {
		"type": "list",
		"tasks": task_list
	})


def add_task(request):
	"""
	返回创建任务页面
	"""
	return render(request, "task_add.html", {
		"type": "add"
	})


def edit_task(request, tid):
	"""
	返回编辑任务页面
	"""
	return render(request, "task_edit.html", {
		"type": "edit"
	})


def delete_task(request, tid):
	"""
	删除任务 	TestTask.objects.get(id=tid).delete()

	"""
	print("delete_task",tid)
	task = TestTask.objects.get(id=tid)
	task.del_status=True
	task.save()

	return HttpResponseRedirect("/testtask/")

@csrf_exempt
def save_task(request):
	"""
	创建/编辑任务
	"""
	if request.method == "POST":
		task_id = request.POST.get("task_id", "")
		name = request.POST.get("name", "")
		desc = request.POST.get("desc", "")
		cases = request.POST.get("cases", "")
		print("name", name, desc)
		print("用例", type(cases), cases)

		if name == "" or cases == "":
			return JsonResponse({"status": 10102, "message": "Parameter is null"})

		print("任务的id--->", task_id)
		if task_id == "0":
			TestTask.objects.create(name=name, describe=desc, cases=cases)
		else:
			task = TestTask.objects.get(id=task_id)
			task.name = name
			task.describe = desc
			task.cases = cases
			task.save()

		return JsonResponse({"status": 10200, "message": "success"})
	else:
		return JsonResponse({"status": 10101, "message": "请求方法错误"})

@csrf_exempt
def get_case_tree(request):
	"""
	获得用例树形结构
	"""
	if request.method == "GET":
		# 过滤项目状态是关闭和是否删除标致
		projects = Project.objects.filter(del_status=1,status=1)
		data_list = []
		for project in projects:
			print("GET get_case_tree  select project is ",project)
			project_dict = {
				"name": project.name,
				"isParent": True
			}

			modules = Module.objects.filter(project_id=project.id)
			module_list = []
			for module in modules:
				module_dict = {
					"name": module.name,
					"isParent": True
				}
				# 过滤逻辑删除状态数据
				cases = TestCase.objects.filter(module_id=module.id).filter(status=True)
				case_list = []
				for case in cases:
					case_dict = {
						"name": case.name,
						"isParent": False,
						"id": case.id,
					}
					case_list.append(case_dict)

				module_dict["children"] = case_list
				module_list.append(module_dict)

			project_dict["children"] = module_list
			data_list.append(project_dict)

		return JsonResponse({"status": 10200, "message": "success", "data": data_list})

	if request.method == "POST":
		tid = request.POST.get("tid", "")
		print("任务的id", tid)
		if tid == "":
			return JsonResponse({"status": 10200, "message": "任务id不能为空"})

		task = TestTask.objects.get(id=tid)
		casesList = json.loads(task.cases)
		task_data = {
			"name": task.name,
			"desc": task.describe
		}

		projects = Project.objects.filter(del_status=1,status=1)
		data_list = []
		for project in projects:
			print("POST get_case_tree  select project is ",project)
			project_dict = {
				"name": project.name,
				"isParent": True
			}

			modules = Module.objects.filter(project_id=project.id)
			module_list = []
			for module in modules:
				module_dict = {
					"name": module.name,
					"isParent": True
				}

				cases = TestCase.objects.filter(module_id=module.id)
				case_list = []
				for case in cases:
					if case.id in casesList:
						case_dict = {
							"name": case.name,
							"isParent": False,
							"id": case.id,
							"checked": True,
						}
					else:
						case_dict = {
							"name": case.name,
							"isParent": False,
							"id": case.id,
							"checked": False,
						}
					case_list.append(case_dict)

				module_dict["children"] = case_list
				module_list.append(module_dict)

			project_dict["children"] = module_list
			data_list.append(project_dict)
		task_data["cases"] = data_list
		return JsonResponse({"status": 10200, "message": "success", "data": task_data})
