#!usr/bin/env python
# -*- coding:utf-8
"""
M(操作数据)
T(模板) - view
V(视图) -Controller
"""
from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib import auth
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
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		print(username, password)
		if username == "" or password == "":
			return render(request, "index.html", {"error": "用户名或密码不能为空"})
		user = auth.authenticate(username=username, password=password)
		print(user)
		if user is None:
			return render(request, "index.html", {"error": "用户名或密码错误"})
		else:
			return HttpResponse("登录成功")