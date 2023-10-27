from django.urls import path
from . import views
app_name="admin_panel"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    
    path('dashboard', views.dashboard, name = 'dashboard'),  
    path('patients', views.patients, name = 'patients'),  
    path('counsellors', views.counsellors, name = 'counsellors'),  
    path('appointments', views.appointments, name = 'appointments'),  
    
]
