#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: forms.py
@time: 2019/04/09
"""
from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, min_length=6)
