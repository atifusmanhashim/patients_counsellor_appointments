
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    
    # Patient
    path('create-patient/', views.CreatePatient.as_view(), name='create-patient'),       # For Adding New Patient
    path('patient-list/', views.PatientList.as_view(), name='patient-list'),            # For Patient Listing
    path('patient-details/', views.PatientDetails.as_view(), name='patient-details'),   # For Reading PAtient Details
    path('patient-delete/', views.PatientDelete.as_view(), name='patient-delete'),      # For Deletion of Selected Patient
    path('patient-update/', views.PatientUpdate.as_view(), name='patient-update'),      # For Update of Selected Patient
    
    # Counsellor
    path('create-counsellor/', views.CreateCounsellor.as_view(), name='create-counsellor'),       # For Adding New Counsellor  
    path('counsellor-list/', views.CounsellorList.as_view(), name='counsellor-list'),             # for getting active Counsellors
    path('counsellor-details/', views.CounsellorDetails.as_view(), name='counsellor-details'),    # for getting Counsellor Details
    path('counsellor-delete/', views.CounsellorDelete.as_view(), name='counsellor-delete'),       # For Removing Counsellor 
    path('counsellor-update/', views.CounsellorUpdate.as_view(), name='counsellor-update'),       # For Update Counsellor 

    # Appointments
    path('create-appointment/', views.CreateAppointment.as_view(), name='create-appointment'),       # For Adding New Patient Appointment 
    path('active-appointment-list/', views.ActiveAppointments.as_view(), name='active-appointment'),       # For Viewing Active Appointments 
# ============================================Versioning APIs===============================================================================================
    
    # Patients
    path('<str:version>/create-patient/', views.CreatePatient.as_view(), name='create-patient'),       # For Adding New Patient
    path('<str:version>/patient-list/', views.PatientList.as_view(), name='patient-list'),         #For Viewing Active Patients List
    path('<str:version>/patient-details/', views.PatientDetails.as_view(), name='patient-details'), #For Viewing Details of Selected Patient
    path('<str:version>/patient-delete/', views.PatientDelete.as_view(), name='patient-delete'),    #For Deletion of Selected Patient
    path('<str:version>/patient-update/', views.PatientUpdate.as_view(), name='patient-update'),      # For Update of Selected Patient
    
    
    # Counsellors
    path('<str:version>/create-counsellor/', views.CreateCounsellor.as_view(), name='create-counsellor'),       # For Adding New Counsellor
    path('<str:version>/counsellor-list/', views.CounsellorList.as_view(), name='counsellor-list'),         #For Viewing Active Counsellors List
    path('<str:version>/counsellor-details/', views.CounsellorDetails.as_view(), name='counsellor-details'),   #For Viewing Details of Selected Counseller
    path('<str:version>/counsellor-delete/', views.CounsellorDelete.as_view(), name='counsellor-delete'),       #For Deletion of Selected Counsellor
    path('<str:version>/counsellor-update/', views.CounsellorUpdate.as_view(), name='counsellor-update'),       # For Update Counsellor 
    
    # Appointments
    path('<str:version>/create-appointment/', views.CreateAppointment.as_view(), name='create-appointment'),       # For Adding New Patient Appointment 
    path('<str:version>/active-appointment-list/', views.ActiveAppointments.as_view(), name='active-appointment'),       # For Viewing Active Appointments 

# ============================================End of Versioning APIs====================================================== 
 

]
