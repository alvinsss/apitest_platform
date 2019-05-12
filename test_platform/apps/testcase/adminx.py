#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: adminx.py
@time: 2019/05/12
"""
import xadmin
from .models import TestCase


class TestCaseAdmin(object):
	list_display = ['module', 'name', 'url', 'method', 'header', 'parameter_type', 'parameter_body', 'result',
	                'assert_type', 'assert_text', 'create_time']
	search_fields = ['module', 'name', 'url', 'method', 'header', 'parameter_type', 'parameter_body', 'result',
	                 'assert_type', 'assert_text']
	list_filter = ['module', 'name', 'url', 'method', 'header', 'parameter_type', 'parameter_body', 'result',
	               'assert_type', 'assert_text', 'create_time']


xadmin.site.register(TestCase, TestCaseAdmin)
