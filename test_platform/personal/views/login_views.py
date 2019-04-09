#!usr/bin/env python
# -*- coding:utf-8
"""
M(操作数据)
T(模板) - view
V(视图) -Controller
"""
from django.shortcuts import render
from django.http import  HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from personal.forms import LoginForm
from personal.models.project import Project
# Create your views here.

def test(request):
	name = request.GET.get("name", "")
	info = []
	for n in range(3):
		info.append("qatest:" + name + "<br>")
	return HttpResponse(info)

def qatest(request):
	input_name = request.GET.get("name", "")
	if input_name == "":
		return HttpResponse("请输入？name=name")
	return render(request, "qatest.html", {"name": input_name})


def index(request):
	if request.method == "GET":
		return render(request, "index.html")
	else:
		login_form = LoginForm(request.POST)
		# 判断提交数据,密码至少6位长度
		if login_form.is_valid():
			username = request.POST.get("username", "")
			password = request.POST.get("password", "")
			print(username, password)
			# if username == "" or password == "":
			# 	return render(request, "index.html", {"msg": "用户名或密码不能为空"})
			user = auth.authenticate(username=username, password=password)
			print(user)
			if user is None:
				return render(request, "index.html", {"msg": "用户名或密码不正确"})
			else:
				auth.login(request, user)  # 记录用户的登录状态
				return HttpResponseRedirect("/project/")
		else:
			return render(request, 'index.html', {'form_errors': login_form.errors})

# 用户的退出操作
@login_required
def logout(request):
	auth.logout(request)
	# 删除数据库的的session记录
	return HttpResponseRedirect("/index/")
