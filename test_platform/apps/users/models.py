from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 模型一旦发生改变，要重新迁移
class UserProfile(AbstractUser):
    # user = models.ForeignKey( User )
    unickname = models.CharField(max_length=20,verbose_name='昵称',null=True,blank=True)
    ubirthday = models.DateField(auto_now_add=True,verbose_name='生日',null=True)
    uaddress = models.CharField(max_length=200,verbose_name='地址')

    class Meta:
        '''verbose_name的意思很简单，就是给你的模型类起一个更可读的名字一般定义为中文'''
        verbose_name = "用户信息"
        ''' 如果不指定Django会自动在模型名称后加一个s '''
        verbose_name_plural = verbose_name

    def __unicode__(self):
        '''打印自定义字符串'''
        return self.username
