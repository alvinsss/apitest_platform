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

from personal.models.module import Module
from personal.forms import ModuleForm


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
def edit_module(request):
	"""
	编辑管理
	:param request:
	:return:
	"""


# if request.method == "GET":
# 	if pid:
# 		p = Project.objects.get(id=mid)
# 		print("编辑的id:", mid, p.name)
# 		# 把p对象的数据赋值给表单
# 		form = ProjectForm(instance=p)
# 		return render(request, "project.html", {"type": "edit",
# 		                                        "form": form, "id": pid})
# elif request.method == "POST":
# 	form = ProjectForm(request.POST)
# 	p = Project.objects.get(id=pid)
# 	print("编辑post的id:", pid, p.name)
# 	if form.is_valid():
# 		name = form.cleaned_data['name']
# 		describe = form.cleaned_data['describe']
# 		status = form.cleaned_data['status']
# 		p = Project.objects.get(id=pid)
# 		p.name = name
# 		p.describe = describe
# 		p.status = status
# 		p.save()
# 	return HttpResponseRedirect("/project/")


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
def delete_module(request):
	pass
