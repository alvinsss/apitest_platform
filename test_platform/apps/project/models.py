# Create your models here.
from django.db import models


class Project(models.Model):
	name = models.CharField("项目名称", max_length=40, null=False)
	describe = models.TextField("描述", default="")
	status = models.BooleanField("状态", default=1)
	del_status = models.BooleanField("是否删除，1是不删除，0是删除",default=1)
	create_time = models.DateTimeField("创建时间", auto_now_add=True)
	update_time = models.DateTimeField("更新时间", auto_now=True)

	class Meta:
		verbose_name = '项目管理'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
