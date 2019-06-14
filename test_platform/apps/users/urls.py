"""test_platform URL Configuration
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from users import views

urlpatterns = [
	# http://127.0.0.1:8000/test/?name=alvin
	path('', views.index),
	path('test/', views.qatest),
	path('index/', views.index, name="index"),
	path('logout/', views.logout),
	# path( 'register/', views.register ),
    # path( 'registerfun/', views.registerfun ),
    path('accounts/login/', views.index),
]
