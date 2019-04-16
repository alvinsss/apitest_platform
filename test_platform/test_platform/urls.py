"""test_platform URL Configuration
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import xadmin

from users import views

urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^xadmin/', xadmin.site.urls),
	url(r'^captcha/', include('captcha.urls')),

	# """用户管理"""
	# http://127.0.0.1:8000/test/?name=alvin
	path('test/', views.qatest),
	path('/index/', views.index, name="index"),
	path('', views.index),
	path('logout/', views.logout),
	path('accounts/login/', views.index),
	path('jsqa/', views.jsqa),
	path('jsdemo/', views.demo),

	# """项目管理"""
	path('project', include('project.urls')),

	# """模块管理"""
	path('module', include('module.urls')),

]
