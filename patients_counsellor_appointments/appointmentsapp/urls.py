
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('create-patient/', views.CreatePatient.as_view(), name='create-patient'),       # For Adding New Patient
    path('create-counsellor/', views.CreateCounsellor.as_view(), name='create-counsellor'),       # For Adding New Counsellor  
# ============================================Versioning APIs====================================================== 
    path('<str:version>/create-patient/', views.CreatePatient.as_view(), name='create-patient'),       # For Adding New Patient
    path('<str:version>/create-counsellor/', views.CreateCounsellor.as_view(), name='create-counsellor'),       # For Adding New Counsellor
# ============================================End of Versioning APIs====================================================== 
 

]
