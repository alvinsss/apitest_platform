from django.urls import path
from tools import views

urlpatterns = [
    # 任务管理
    path('', views.toolslists),
]