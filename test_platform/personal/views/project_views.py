#!usr/bin/env python
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

# 管理页面
@login_required
def project_manage(request):
	project_all = Project.objects.all()
	return render(request, "project.html", {"projects": project_all})
