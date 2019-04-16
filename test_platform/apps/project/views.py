#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: project_views.py
@time: 2019/04/09
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project.models import Project
from project.forms import ProjectForm


# Create your views here.

# 管理页面
@login_required
def project_manage(request):
	print("project_manage")
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


@login_required
def edit_project(request, pid):
	"""
	编辑项目
	:param request:
	:return:
	"""
	if request.method == "GET":
		if pid:
			p = Project.objects.get(id=pid)
			print("编辑的id:", pid, p.name)
			# 把p对象的数据赋值给表单
			form = ProjectForm(instance=p)
			return render(request, "project.html", {"type": "edit", "form": form, "id": pid})
	elif request.method == "POST":
		form = ProjectForm(request.POST)
		p = Project.objects.get(id=pid)
		print("编辑post的id:", pid, p.name)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']
			p = Project.objects.get(id=pid)
			p.name = name
			p.describe = describe
			p.status = status
			p.save()
		return HttpResponseRedirect("/project/")


@login_required
def delete_project(request, pid):
	"""
	删除项目
	:param request:
	:return:
	"""
	print("delete_project", pid)
	if request.method == "GET":
		if pid:
			try:
				p = Project.objects.get(id=pid)
			except Project.DoesNotExist:
				return HttpResponseRedirect("/project")
			else:
				p.delete()
				return HttpResponseRedirect("/project")
	elif request.method == "POST":
		return HttpResponseRedirect("/project/")
