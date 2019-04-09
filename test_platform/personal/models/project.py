from django.db import models
# Create your models here.


class Project(models.Model):
	name = models.CharField("项目名称", max_length=40, null=False)
	describe = models.TextField("描述", default="")
	status = models.BooleanField("状态", default=1)
	create_time = models.DateTimeField("创建时间", auto_now_add=True)

	class Meta:
		verbose_name = '项目信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
