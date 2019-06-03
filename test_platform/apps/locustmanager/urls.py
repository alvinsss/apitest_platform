from django.urls import path
from locustmanager import views

urlpatterns = [
    # 任务管理
    path('', views.locustmanager),
]