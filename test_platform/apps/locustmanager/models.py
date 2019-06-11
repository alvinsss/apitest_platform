from django.db import models
from module.models import Module
from users.models import UserProfile
import  os
import uuid


def user_directory_path(instance,filename):
	ext = filename.split('.')[-1]
	filename = '{}.{}'.format( uuid.uuid4().hex[:10], ext )
	print(filename)
	return os.path.join( instance.user.id, "avatar", filename )


class LocustScript(models.Model):
	"""
	LOCUST表
	"""
	module = models.ForeignKey( Module, on_delete=models.CASCADE )
	userid = models.IntegerField("用户id")
	slave_num=models.IntegerField("slave数量",default=0)
	username = models.CharField("用户名",max_length=10,null=False,default=None)
	scriptname = models.CharField("脚本名称", max_length=50, null=False)
	host = models.CharField("host", max_length=200,null=False)
	encryption = models.IntegerField("是否加密",null=False)
	create_time = models.DateTimeField("创建时间", auto_now_add=True)
	locustfile = models.FileField(upload_to = "",storage = None )
	del_status = models.IntegerField("是否删除",default=0)
	# locustfile = models.FileField( upload_to=user_directory_path, verbose_name="文件" )

	class Meta:
		verbose_name = 'LOCUST管理'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.scriptname
