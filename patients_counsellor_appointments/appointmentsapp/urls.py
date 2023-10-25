
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    
    # Patient
    path('create-patient/', views.CreatePatient.as_view(), name='create-patient'),       # For Adding New Patient
    path('patient-list/', views.PatientList.as_view(), name='patient-list'),            # For Patient Listing
    path('patient-details/', views.PatientDetails.as_view(), name='patient-details'), 
    path('patient-delete/', views.PatientDelete.as_view(), name='patient-delete'), 
    
    # Counsellor
    path('create-counsellor/', views.CreateCounsellor.as_view(), name='create-counsellor'),       # For Adding New Counsellor  
    path('counsellor-list/', views.CounsellorList.as_view(), name='counsellor-list'), 
    path('counsellor-details/', views.CounsellorDetails.as_view(), name='counsellor-details'), 
    path('counsellor-delete/', views.CounsellorDelete.as_view(), name='counsellor-delete'), 
# ============================================Versioning APIs====================================================== 
    
    # Patients
    path('<str:version>/create-patient/', views.CreatePatient.as_view(), name='create-patient'),       # For Adding New Patient
    path('<str:version>/patient-list/', views.PatientList.as_view(), name='patient-list'), 
    path('<str:version>/patient-details/', views.PatientDetails.as_view(), name='patient-details'), 
    path('<str:version>/patient-delete/', views.PatientDelete.as_view(), name='patient-delete'), 
    
    
    # Counsellors
    path('<str:version>/create-counsellor/', views.CreateCounsellor.as_view(), name='create-counsellor'),       # For Adding New Counsellor
    path('<str:version>/counsellor-list/', views.CounsellorList.as_view(), name='counsellor-list'),
    path('<str:version>/counsellor-details/', views.CounsellorDetails.as_view(), name='counsellor-details'),  
    path('<str:version>/counsellor-delete/', views.CounsellorDelete.as_view(), name='counsellor-delete'), 
# ============================================End of Versioning APIs====================================================== 
 

]
