#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: forms.py
@time: 2019/04/09
"""
from django import forms
from module.models import Module


# 定义前端展示form字段
class ModuleForm(forms.ModelForm):
	class Meta:
		model = Module
		fields = ['project', 'name', 'describe']
