#!usr/bin/env python
# -*- coding:utf-8
"""
M(操作数据)
T(模板) - view
V(视图) -Controller
"""
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from users.forms import LoginForm


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


# 登录的首页
def index(request):
	if request.method == "GET":
		return render(request, "index.html")

	else:
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		if username == "" or password == "":
			return render(request, "index.html", {"error": "用户名或密码为空"})
		user = auth.authenticate(username=username, password=password)
		print("user-->", user)
		if user is None:
			return render(request, "index.html", {
				"error": "用户名或密码错误"})
		else:
			auth.login(request, user)  # 记录用户的登录状态
			return HttpResponseRedirect("/project/")


# 用户的退出操作
@login_required
def logout(request):
	auth.logout(request)
	# 删除数据库的的session记录
	return HttpResponseRedirect("/index/")


def demo(request):
	return render(request, "js_demo.html")


# 测试的接口
@csrf_exempt
def jsqa(request):
	if request.method == "POST":
		n1 = request.POST.get("num1", "")
		n2 = request.POST.get("num2", "")
		if n1 == "" or n2 == "":
			return JsonResponse({"status_code": 10011, "message": "参数不能为空"})
		try:
			n1 = int(n1)
			n2 = int(n2)
		except ValueError:
			return JsonResponse({"status_code": 10012, "message": "参数类型错误"})

		return JsonResponse({"status_code": 10200, "message": "成功", "data": n1 + n2})
	else:
		return JsonResponse({"status_code": 10010, "message": "请求方法错误"})


def debug(request):
	print("debug")
	pass
