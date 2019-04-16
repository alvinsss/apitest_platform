#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: forms.py
@time: 2019/04/09
"""
from django import forms
from personal.models import Project
from personal.models import Module
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, min_length=6)
	captcha = CaptchaField(error_messages={"invalid": "验证码错误,请F5刷新页面"})

class ProjectForm(forms.ModelForm):
	"""label与前端代码的label一致"""
	# name = forms.CharField(label="名称",max_length=100)
	# describe = forms.CharField(label="描述",widget=forms.Textarea)
	# status = forms.BooleanField(label="状态",required=True)
	class Meta:
		model = Project
		fields = ['name', 'describe', 'status']


# 定义前端展示form字段
class ModuleForm(forms.ModelForm):
	class Meta:
		model = Module
		fields = ['name', 'describe', 'project']
