# authapi/urls.py
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    #Normal Signup
    path('register/', views.UserCreate.as_view(), name='register'),          # For Sign-up
    
    #Normal Login
    path('login/', views.UserLogin.as_view(), name='login'),                 # For Normal Login

    #Email Check
    path('emailcheck/',views.EmailCheck.as_view(),name='emailcheck'),                          # For Checking Email Address / Social ID (Used For Reset Password also)
    
    #Change Password
    path('changepassword/', views.changepassword.as_view(), name='changepassword'),    # For Change Password
    
    #Reset Password
    path('resetpassword/',views.ResetPassword.as_view(), name='resetpassword'),        # For Password Saving

    #Account Deactivation
    path('account-deletion/', views.UserAccountDeletion.as_view(), name='account-deletion'),                            # Account Deletion

    #Logout
    path('logout/', views.logout, name='logout'),                            # For Logout

# ====================================== Versioning APIs ======================================================================
    #Normal Signup
    path('<str:version>/register/', views.UserCreate.as_view(), name='register'),          # For Sign-up
    
    #Normal Login
    path('<str:version>/login/', views.UserLogin.as_view(), name='login'),                 # For Normal Login

    #Email Check
    path('<str:version>/emailcheck/',views.EmailCheck.as_view(),name='emailcheck'),                          # For Checking Email Address / Social ID (Used For Reset Password also)
    
    #Change Password
    path('<str:version>/changepassword/', views.changepassword.as_view(), name='changepassword'),    # For Change Password
    
    #Reset Password
    path('<str:version>/resetpassword/',views.ResetPassword.as_view(), name='resetpassword'),        # For Password Saving

    #Account Deactivation
    path('<str:version>/account-deletion/', views.UserAccountDeletion.as_view(), name='account-deletion'),                            # Account Deletion

    #Logout
    path('<str:version>/logout/', views.logout, name='logout'),                            # For Logout

# ====================================== End of Versioning APIs ======================================================================
]