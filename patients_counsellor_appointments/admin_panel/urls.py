from django.urls import path
from . import views
app_name="admin_panel"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    
    path('dashboard', views.dashboard, name = 'dashboard'),  
    path('patients', views.dashboard, name = 'patients'),  
    path('counsellors', views.dashboard, name = 'counsellors'),  
    path('appointments', views.dashboard, name = 'appointments'),  
    
]
