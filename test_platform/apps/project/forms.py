#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: forms.py
@time: 2019/04/09
"""
from django import forms
from project.models import Project


class ProjectForm(forms.ModelForm):
	"""label与前端代码的label一致"""

	# name = forms.CharField(label="名称",max_length=100)
	# describe = forms.CharField(label="描述",widget=forms.Textarea)
	# status = forms.BooleanField(label="状态",required=True)
	class Meta:
		model = Project
		fields = ['name', 'describe', 'status']
