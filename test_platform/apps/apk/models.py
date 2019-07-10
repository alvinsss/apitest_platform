from django.db import models
from module.models import  Module
# from apk.models import  APK_UPLOADFILE
# Create your models here.
class APK_UPLOADFILE(models.Model):
    """
    apk_upload表
    """
    module = models.ForeignKey( Module, on_delete=models.CASCADE )
    userid = models.IntegerField("用户id",default=None)
    username = models.CharField("用户名",max_length=10,null=False,default=None)
    name_des = models.CharField("名称描述", max_length=50, null=False)
    apk_testtype = models.CharField("测试类型", max_length=200,null=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    upfilepath = models.FileField(upload_to = "",storage = None )
    sum_status = models.IntegerField("运行状态", default=0)  # 0未执行、1执行中、2执行完成、3 排队中
    sum_result = models.IntegerField("运行结果", default=0,null=False) # 0 未知、1成功、2失败
    del_status = models.IntegerField("是否删除",default=0)
    # locustfile = models.FileField( upload_to=user_directory_path, verbose_name="文件" )

    class Meta:
        verbose_name = 'apk管理_文件上传'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name_des


class APK_RESULTS(models.Model):
    """
    APK_RESULTS表
    """
    module = models.ForeignKey( Module, on_delete=models.CASCADE )
    batch_id = models.ForeignKey(APK_UPLOADFILE,on_delete=models.CASCADE)
    userid = models.IntegerField("用户id",default=None)
    username = models.CharField("用户名",max_length=10,null=False,default=None)
    name_des = models.CharField("名称描述", max_length=50, null=False)
    apk_testtype = models.CharField("测试类型", max_length=200,null=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    upfilepath = models.FileField("上传zip和apk文件路徑",upload_to = "",storage = None )
    apkfile_path = models.FileField("apk文件路徑",upload_to = "",storage = None )
    run_status = models.IntegerField("运行状态", default=0)  # 0未执行、1执行中、2执行完成、3 排队中
    run_result = models.IntegerField("运行结果", default=0)  # 0 未知、1成功、2失败
    del_status = models.IntegerField("是否删除",default=0)
    detail     = models.CharField("运行结果", null=False,max_length=1000)

    class Meta:
        verbose_name = 'apk管理_运行结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name_des
