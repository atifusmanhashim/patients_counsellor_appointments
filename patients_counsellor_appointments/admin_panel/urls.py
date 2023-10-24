from django.urls import include, path, re_path as url
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name="user"

urlpatterns = [
    path('', views.index, name = 'index'),   
    path('dashboard/', views.dashboard, name = 'dashboard'),  
    path('login', views.user_login, name = 'login'),   
    path('logout', views.logout, name = 'logout'),   
]
