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
	# """mock"""
	path( '', views.mokcmanage ),
	path('sdkPullAds.do/', views.sdkPullAds),

]
