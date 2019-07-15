#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: urls.py
@time: 2019/04/16
"""
from django.urls import path
from project import views

urlpatterns = [
	# """项目管理"""
	path('', views.project_manage),
	path('add_project/', views.add_project),
	path('edit_project/<int:pid>', views.edit_project),
	path('delete_project/<int:pid>', views.delete_project),
	path('get_project_list/', views.get_project_list),

]
