from django.contrib import admin

# Register your models here.
from authapp.models import (AppUser,LoginAnalytics)

admin.site.register(AppUser)
admin.site.register(LoginAnalytics)

from appointmentsapp.models import (Patient,Counsellor,Appointment)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'patient_code','patient_name','patient_email', 'is_active','create_date','modified_date','deleted_date')

    search_fields = ['patient_id', 'patient_code','patient_name','patient_email']

admin.site.register(Patient,PatientAdmin)

class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('counsellor_id', 'counsellor_code','counsellor_name','counsellor_email', 'is_active','create_date','modified_date','deleted_date')

    search_fields = ['counsellor_id', 'counsellor_code','counsellor_name','counsellor_email']
admin.site.register(Counsellor,CounsellorAdmin)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'appointment_code','appointment_patient','appointment_counsellor', 'appointment_date','is_active','create_date','modified_date','deleted_date')

    search_fields = ['appointment_id', 'appointment_code','appointment_patient__patient_name','appointment_counsellor__counsellor_name']



admin.site.register(Appointment,AppointmentAdmin)

from appapi.models import (AppAnalytics)

admin.site.register(AppAnalytics)