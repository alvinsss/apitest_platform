#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: urls.py
@time: 2019/04/16
"""

from django.urls import path
from module import views

urlpatterns = [

	# """模块管理"""
	path('/', views.module_manage),
	path('/add_module/', views.add_module),
	path('/edit_module/<int:mid>/', views.edit_module),
	path('/delete_module/<int:mid>/', views.delete_module),

]
