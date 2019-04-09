#!usr/bin/env python
# -*- coding:utf-8
"""
@author:alvin
@file: UserProfile.py
@time: 2019/04/09
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserProfile(AbstractUser):
	'''UserProfile表增加字段内容，继承默认user表,'''
	# 默认user表字段
	nick_name = models.CharField(max_length=50, verbose_name="昵称", default='')
	birday = models.DateField(verbose_name="生日", null=True, blank=True)
	gender = models.CharField(max_length=10, choices=(("make", "男"), ("female", "女")), default="female")
	address = models.CharField(max_length=100, default="")
	mobile = models.CharField(max_length=11, null=True, blank=True)

	class Meta:
		'''verbose_name的意思很简单，就是给你的模型类起一个更可读的名字一般定义为中文'''
		verbose_name = "用户信息"
		# '''如果不指定Django会自动在模型名称后加一个s'''
		verbose_name_plural = verbose_name

	def __unicode__(self):
		'''打印自定义字符串'''
		return self.username


class EmailVerifyRecord(models.Model):
	code = models.CharField(max_length=20, verbose_name="验证码")
	email = models.EmailField(max_length=50, verbose_name="邮箱")
	send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")), max_length=10, verbose_name="验证码类型")
	send_time = models.DateField(default=datetime.now, verbose_name="发送时间")

	class Meta:
		verbose_name = "邮箱验证码"
