from django.db import models

# Create your models here.
from django.db import models
from module.models import Module
from users.models import UserProfile
import  os
import uuid


class UnittestScript(models.Model):
	"""
	pyunittest表
	"""
	module = models.ForeignKey( Module, on_delete=models.CASCADE )
	userid = models.IntegerField("用户id")
	username = models.CharField("用户名",max_length=10,null=False,default=None)
	scriptname = models.CharField("脚本名称", max_length=50, null=False)
	create_time = models.DateTimeField("创建时间", auto_now_add=True)
	py_file = models.FileField(upload_to = "",storage = None )
	uploadfilename = models.FileField(upload_to="",storage=None)
	del_status = models.IntegerField("是否删除",default=0)
	test_result = models.BooleanField("测试结果",default=True)
	class Meta:
		verbose_name = 'py_unittest管理'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.scriptname
