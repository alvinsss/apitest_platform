from django.db import models
from project.models import Project
# Create your models here.

class Module(models.Model):
	"""模块表"""
	project = models.ForeignKey( Project,on_delete=models.CASCADE )
	name = models.CharField("模块名称", max_length=50, null=False)
	describe = models.TextField("描述", default="")
	create_time = models.DateTimeField("创建时间", auto_now_add=True)
	del_status = models.BooleanField("是否删除，1是不删除，0是删除",default=1)

	class Meta:
		verbose_name = '模块管理'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
