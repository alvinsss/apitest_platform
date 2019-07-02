"""
@author:alvin
@file: modulet_views.py
@time: 2019/04/09
"""
# !usr/bin/env python
# -*- coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from module.models import Module
from module.forms import ModuleForm


# Create your views here.


# 模块管理
@login_required
def module_manage(request):
	"""
	模块管理
	:param request:
	:return:
	"""
	print("module_manage")
	if request.method == "GET":
		module_all = Module.objects.filter(del_status=1)
		print(type(module_all))
		return render(request, "module.html", {"type": "list", "modules": module_all})


@login_required
def edit_module(request, mid):
	"""
	编辑管理，GET展示
	:param request:
	:return:
	"""
	if request.method == "GET":
		module = Module.objects.get(id=mid)
		module_form = ModuleForm(instance=module)
		print(module.id)
		return render(request, "module.html",
		              {"form": module_form, "id": module.id, "type": "edit"})

	if request.method == "POST":
		print("POST")
		form = ModuleForm(request.POST)
		if form.is_valid():
			project = form.cleaned_data['project']
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			print(name, describe, project)

			m = Module.objects.get(id=mid)
			m.name = name
			m.describe = describe
			m.project = project
			m.save()
			return HttpResponseRedirect("/module/")


@login_required()
def add_module(request):
	if request.method == "GET":
		form = ModuleForm()
		return render(request, "module.html",
		              {"form": form, "type": "add"})
	else:
		form = ModuleForm(request.POST)
		request.user.username
		if form.is_valid():
			project = form.cleaned_data['project']
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			print(name, describe, project)
			if name == "":
				return render(request, "module.html",
				              {"type": "add", "name_error": "模块名称不能为空！"})
			Module.objects.create(name=name, describe=describe, project=project)
		return HttpResponseRedirect("/module/")


@login_required()
def delete_module(request, mid):
	"""删除模块
	"""
	if request.method == "GET":
		try:
			module = Module.objects.get(id=mid)
		except Module.DoesNotExist:
			return HttpResponseRedirect("/module/")
		else:
			module.del_status=0
			module.save()
			# module.delete()
		return HttpResponseRedirect("/module/")
	else:
		return HttpResponseRedirect("/module/")


@csrf_exempt
def get_searchmodule_info(request):
	print("get_searchmodule_info")
	if request.method == "POST":
		search_info = request.POST.get("search_info", "")
		if search_info == "":
			return JsonResponse({"status": 10102,
			                     "message": "搜索内容不能空"})

		modules = Module.objects.filter(name=search_info)

		module_list = []
		for mod in modules:
			module_dict = {
				"id": mod.id,
				"name": mod.name,
				"describe": mod.describe,
				"create_time": mod.create_time,
				"project_id": mod.project_id,
			}
			module_list.append(module_dict)
		return JsonResponse({"status": 10200, "message": "请求成功",
		                     "data": module_list})
	else:
		return JsonResponse({"status": 10101, "message": "请求方法错误"})


@csrf_exempt
def get_module_list(request):
	"""
	接口：根据项目id,返回对应的模块列表,用于js的调用
	"""
	if request.method == "POST":
		pid = request.POST.get("pid", "")
		if pid == "":
			return JsonResponse({"status": 10102,
			                     "message": "项目id不能空"})

		modules = Module.objects.filter(project=pid)
		module_list = []
		for mod in modules:
			module_dict = {
				"id": mod.id,
				"name": mod.name
			}
			module_list.append(module_dict)
		return JsonResponse({"status": 10200, "message": "请求成功",
		                     "data": module_list})
	else:
		return JsonResponse({"status": 10101, "message": "请求方法错误"})
