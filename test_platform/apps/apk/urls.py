#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: urls.py
@time: 2019/7/8
"""
from django.urls import path
from apk import views

urlpatterns = [
	# """项目管理"""
	path('', views.apk_list),
	path('add_apk/', views.add_apk),
	path( 'save_uploadapkfile/', views.save_uploadapkfile ),
	# path('edit_apk/<int:pid>/', views.edit_apk),
	path('detail_result/<int:resultid>/', views.detail_result),
	path('result/<int:apkid>/', views.result),
	path( 'get_detail_result/', views.get_detail_result ),
	path( 'run_apk_task/', views.run_apk_task ),

]
