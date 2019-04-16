"""test_platform URL Configuration
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import xadmin

from personal.views import login_views
from personal.views import module_views
from personal.views import qatest_views

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
	path('project', include('project.urls')),

	# """模块管理"""
	path('module/', module_views.module_manage),
	path('module/add_module/', module_views.add_module),
	path('module/edit_module/<int:mid>/', module_views.edit_module),
	path('module/delete_module/<int:mid>/', module_views.delete_module),

	path('jsqa/', qatest_views.jsqa),
	path('jsdemo/', qatest_views.demo),

]
