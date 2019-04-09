#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: project_views.py
@time: 2019/04/09
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from personal.models.project import Project


# Create your views here.

# 管理页面
@login_required
def project_manage(request):
	project_all = Project.objects.all()
	return render(request, "project.html",
	              {"projects": project_all
		              , "type": "list"})


@login_required
def add_project(request):
	"""
	添加项目
	:param request:
	:return:
	"""
	if request.method == "GET":
		return render(request, "project.html", {"type": "add"})
	else:
		name = request.POST.get("name", "")
		describe = request.POST.get("describe", "")
		status = request.POST.get("status", "")
		print(name, describe, status)
		if name == "":
			return render(request, "project.html",
			              {"type": "add", "name_error": "项目名称不能为空！"})
		Project.objects.create(name=name, describe=describe, status=status)
		return HttpResponseRedirect("/project/")
