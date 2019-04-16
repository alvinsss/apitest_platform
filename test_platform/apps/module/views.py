"""
@author:alvin
@file: modulet_views.py
@time: 2019/04/09
"""
# !usr/bin/env python
# -*- coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
		module_all = Module.objects.all()
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
			return HttpResponseRedirect("/module")
		else:
			module.delete()
		return HttpResponseRedirect("/module")
	else:
		return HttpResponseRedirect("/module")
