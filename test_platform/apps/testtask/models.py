from django.db import models

# Create your models here.
class TestTask(models.Model):
    """
    任务表
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.IntegerField("状态", default=0)  # 未执行、执行中、执行完成、排队中
    cases = models.TextField("关联用例", default="")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    del_status = models.BooleanField("是否删除",default=False)

    class Meta:
        verbose_name="任务管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name