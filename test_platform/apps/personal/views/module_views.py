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
		print("module_all:", module_all)
		print("we are in %s" % __name__)
		return render(request, "module.html", {"type": "list", "modules": module_all})


def test_getdata():
	m = Module.objects.all()
	print(m)


if __name__ == '__main__':
	print("test")
	test_getdata()
