import appapi.constants as constants
import math

from .models import (Patient,Counsellor,Appointment)


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

def get_counsellor(sel_counsellor_id):
    if sel_counsellor_id is not None:
        try:
            sel_counsellor=Counsellor.objects.get(is_active=True,counsellor_id=sel_counsellor_id)
        except Counsellor.DoesNotExist:
            sel_counsellor=None
    else:
        sel_counsellor=None
    
    return sel_counsellor

def get_appointment(sel_appointment_id):
    if sel_appointment_id is not None:
        try:
            sel_appointment=Appointment.objects.get(is_active=True,appointment_id=sel_appointment_id)
        except Appointment.DoesNotExist:
            sel_appointment=None
    else:
        sel_counsellor=None
    
    return sel_appointment