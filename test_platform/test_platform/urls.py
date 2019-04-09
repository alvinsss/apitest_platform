"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import xadmin

from personal.views import login_views
from personal.views import project_views
from personal.views import module_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    # http://127.0.0.1:8000/test/?name=alvin
    path('test/', login_views.qatest),
    path('index/', login_views.index, name="index"),
    path('', login_views.index),
    path('logout/', login_views.logout),
    path('accounts/login/', login_views.index),

    # """项目管理"""
    path('project/', project_views.project_manage),
    path('project/add_project/', project_views.add_project),
    # """模块管理"""
    path('module/', module_views.module_manage),

]
