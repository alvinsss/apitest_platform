from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.urls import path
from pyunitest import views
from django.conf import settings  # 这一行需要引入
from django.conf.urls.static import static  # 这一行需要引入
from django.conf import settings

urlpatterns = [
    # 任务管理
    path('', views.unittestmanager),
    path( 'add_unittesttfile/', views.add_unittesttfile ),
    path( 'save_unittesttfile/', views.save_unittesttfile ),
    path( 'edit_py_unittest/<int:pyfid>/', views.edit_py_unittest ),
    path( 'get_unittestlist_info/', views.get_unittestlist_info ),
    path( 'delete_py_unittest/<int:pyfid>/', views.delete_py_unittest ),
    path( 'run_unittest_task/', views.run_unittest_task ),
    path( 'upload_file/', views.uploadfile ),
]
static(settings.FILE_PYROOT, document_root=settings.FILE_PYROOT)# 这句话是用来指定和映射静态文件的路径

