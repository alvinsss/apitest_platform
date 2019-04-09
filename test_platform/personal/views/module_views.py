#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: project_views.py
@time: 2019/04/09
"""
# !usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: project_views.py
@time: 2019/04/09
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from personal.models.project import Project


# Create your views here.


# 模块管理
@login_required
def module_manage(request):
	return render(request, "module.html")
