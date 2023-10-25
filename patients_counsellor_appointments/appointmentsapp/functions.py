import appapi.constants as constants

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

def appointment_exist(sel_dt_time, sel_obj, sel_obj_type):
    if sel_dt_time is not None and sel_obj is not None and sel_obj_type is not None:
        try:
            sel_counsellor=Counsellor.objects.get(is_active=True,counsellor_email=sel_email)
        except Counsellor.DoesNotExist:
            sel_counsellor=None
    else:
        sel_counsellor=None
    
    return sel_counsellor
        