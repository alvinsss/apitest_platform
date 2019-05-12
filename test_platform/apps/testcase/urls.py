#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: urls.py
@time: 2019/04/16
"""
from django.urls import path
from testcase import views

urlpatterns = [
	# """用例管理"""
	path('/', views.testcase_manage),
	path('/debug', views.debug),
	path('/tc_assert', views.testcase_assert),
	path('/save_case', views.testcase_save),
]