#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: xadmin.py
@time: 2019/05/12
"""
import xadmin
from .models import Module


class ModuleAdmin(object):
	list_display = ['project', 'name', 'describe', 'create_time']
	search_fields = ['project', 'name', 'describe']
	list_filter = ['project', 'name', 'describe', 'create_time']


xadmin.site.register(Module, ModuleAdmin)
