#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: qatest_views.py
@time: 2019/04/10
"""
from django.http import HttpResponse
from django.shortcuts import render


def demo(request):
	return render(request, "js_demo.html")


def jsqa(request):
	if request.method == "POST":
		n1 = request.POST.get("num1")
		print(n1)
		n2 = request.POST.get("num2")
		sum = int(n1) + int(n2)
		return HttpResponse(sum)
	else:
		print("GET")
		return HttpResponse({"status_code": "1001", "message": "请求方法错误！"})
