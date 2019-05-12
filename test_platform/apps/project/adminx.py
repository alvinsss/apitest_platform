#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: adminx.py
@time: 2019/05/12
"""
import xadmin
from .models import Project


class ProjectAdmin(object):
	list_display = ['name', 'describe', 'status']
	search_fields = ['name', 'describe', 'status']
	list_filter = ['name', 'describe', 'status']


xadmin.site.register(Project, ProjectAdmin)
