from django.db import models
# Create your models here.


class Project(models.Model):
	name = models.CharField(max_length=40, null=False)
	describe = models.TextField(default="")
	status = models.BooleanField(default=1)
	create_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = '项目信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
