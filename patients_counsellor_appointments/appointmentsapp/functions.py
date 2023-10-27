import appapi.constants as constants
import math
import traceback
from .models import (Patient,Counsellor,Appointment)
from django.db.models import Q,Count,Max,Min,Avg

from appointmentsapp.serializers import (PatientSerializer, CounsellorSerializer, AppointmentSerializer, AppointmentListtSerializer)
def patient_email_exist(sel_email):
    if sel_email is not None:
        try:
            sel_patient=Patient.objects.get(is_active=True,patient_email=sel_email)
        except Patient.DoesNotExist:
            sel_patient=None
    else:
        sel_patient=None
    
    return sel_patient

def counsellor_email_exist(sel_email):
    if sel_email is not None:
        try:
            sel_counsellor=Counsellor.objects.get(is_active=True,counsellor_email=sel_email)
        except Counsellor.DoesNotExist:
            sel_counsellor=None
    else:
        sel_counsellor=None
    
    return sel_counsellor

def get_patient(sel_patient_id):
    if sel_patient_id is not None:
        try:
            sel_patient=Patient.objects.get(is_active=True,patient_id=sel_patient_id)
        except Patient.DoesNotExist:
            sel_patient=None
    else:
        sel_patient=None
    
    return sel_patient

def get_patients_list():
    try:
        data=[]
        queryset=Patient.objects.filter(patient_name__isnull=False).order_by('patient_id')
        data_list=queryset
        data = PatientSerializer(data_list, many=True).data
    except:
        data=[]
    
    return data

def get_counsellor(sel_counsellor_id):
    if sel_counsellor_id is not None:
        try:
            sel_counsellor=Counsellor.objects.get(is_active=True,counsellor_id=sel_counsellor_id)
        except Counsellor.DoesNotExist:
            sel_counsellor=None
    else:
        sel_counsellor=None
    
    return sel_counsellor

def get_counsellors_list():
    try:
        data=[]
        queryset=Counsellor.objects.filter(counsellor_name__isnull=False).order_by('counsellor_id')
        data_list=queryset
        data = CounsellorSerializer(data_list, many=True).data
    except:
        data=[]
    
    return data

def get_appointment(sel_appointment_id):
    if sel_appointment_id is not None:
        try:
            sel_appointment=Appointment.objects.get(is_active=True,appointment_id=sel_appointment_id)
        except Appointment.DoesNotExist:
            sel_appointment=None
    else:
        sel_counsellor=None
    
    return sel_appointment

def get_appointments_list():
    try:
        data=[]
        queryset=Appointment.objects.filter(appointment_patient__isnull=False,appointment_counsellor__isnull=False,appointment_date__isnull=False).order_by('appointment_id')
        data_list=queryset
        data = AppointmentListtSerializer(data_list, many=True).data
    except:
        data=[]
    
    return data

def get_summary():
    data={}
    try:
        patient_summary=Patient.objects.aggregate(total=Count('patient_id'),
                                                active=Count('patient_id',filter=Q(is_active=True)),
                                                inactive=Count('patient_id',filter=Q(is_active=False))
                                                )
        counsellor_summary=Counsellor.objects.aggregate(total=Count('counsellor_id'),
                                                active=Count('counsellor_id',filter=Q(is_active=True)),
                                                inactive=Count('counsellor_id',filter=Q(is_active=False))
                                                )
        appointments_summary=Appointment.objects.aggregate(total=Count('appointment_id'),
                                                active=Count('appointment_id',filter=Q(is_active=True)),
                                                inactive=Count('appointment_id',filter=Q(is_active=False))
                                                )
        data={
            'patients':patient_summary,
            'counsellors':counsellor_summary,
            'appointments':appointments_summary
        }
    except Exception as e:
        data={
            'error':traceback.format_exc(),
        } 
    return data