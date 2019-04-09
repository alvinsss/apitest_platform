from django.db import models
from personal.models.project import Project

# Create your models here.


class Module(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, null=False)
	describe = models.TextField(default="")
	create_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '模块信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
