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
	path('', views.testcase_manage),
	path( 'add_case/', views.add_case ),
	path( 'edit_case/<int:cid>/', views.edit_case ),
	path('delete_case/<int:cid>/', views.delete_case),
	path( 'debug', views.testcase_debug ),
	path('assert', views.testcase_assert),
	path('save_case', views.testcase_save),
	path( 'get_case_info', views.get_case_info ),
	path('getselect_data',views.getselect_data),
	path( 'search_name/', views.search_name ),

]
