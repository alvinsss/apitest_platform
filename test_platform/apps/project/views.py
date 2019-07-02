#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: project_views.py
@time: 2019/04/09
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from project.models import Project
from project.forms import ProjectForm


# Create your views here.

# 管理页面
@login_required
def project_manage(request):
	print("project_manage")
	# project_all = Project.objects.all()
	project_all = Project.objects.filter(del_status=1)
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
		del_status ="1" # 1不删除，0删除
		print(name, describe, status)
		if name == "":
			return render(request, "project.html",
			              {"type": "add", "name_error": "项目名称不能为空！"})
		Project.objects.create(name=name, describe=describe, status=status,del_status=del_status)
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
				return HttpResponseRedirect("/project/")
			else:
				# p.delete()
				p.del_status=0
				p.save()
				return HttpResponseRedirect("/project/")
	elif request.method == "POST":
		return HttpResponseRedirect("/project/")


@csrf_exempt
def get_project_list(request):
	"""
	接口：获取项目列表
	"""
	print("get_project_list")
	if request.method == "GET":
		# projects = Project.objects.all()
		projects = Project.objects.filter(del_status=1)
		project_list = []
		for pro in projects:
			project_dict = {
				"id": pro.id,
				"name": pro.name
			}
			project_list.append(project_dict)

		return JsonResponse({"status": 10200,
		                     "message": "请求成功",
		                     "data": project_list})

	else:
		return JsonResponse({"status": 10101, "message": "请求方法错误"})

#
# {1: "测试平台", 2: "新项目BBB"}
#
# [
# {"id":1, "name":"测试平台"},
# {"id":2, "name":"新项目BBB"},
#  ]
