from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.urls import path
from locustmanager import views
from django.conf import settings  # 这一行需要引入
from django.conf.urls.static import static  # 这一行需要引入
from django.conf import settings
urlpatterns = [
    # 任务管理
    path('', views.locustmanager),
    path( 'add_locustfile/', views.add_locustfile ),
    path( 'save_locustfile/', views.save_locustfile ),
    path( 'edit_locustlist/<int:locustfid>/', views.edit_locustlist ),
    path( 'delete_locustlist/<int:locustfid>/', views.delete_locustlist ),
    path( 'upload_file/', views.uploadfile ),
]
static(settings.FILE_ROOT, document_root=settings.FILE_ROOT)# 这句话是用来指定和映射静态文件的路径
