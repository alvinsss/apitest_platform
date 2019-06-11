#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: urls.py
@time: 2019/04/16
"""
from django.urls import path
from mock import views

urlpatterns = [
	# """mock http://127.0.0.1:8000/mock/upload/ """
	path( '', views.mokcmanage ),
	path('sdkPullAds.do/', views.sdkPullAds),
	path( 'uploadhtml/',views.uploadhtml ),
	path( 'uploadfile/', views.uploadfile ),

]
