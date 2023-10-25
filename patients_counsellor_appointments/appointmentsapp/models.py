from django.db import models


# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime,datetime

#For Getting Random String
from django.utils.crypto import get_random_string

from authapp.models import (AppUser,UserRole,LoginAnalytics)
from django.contrib.auth.models import AbstractUser

from django.conf import settings

import appapi.constants as constants

#Common Basic Model
class BasicModel(models.Model):
    is_active = models.BooleanField (null=True, default=True, blank=True) 
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True) 
    deleted_date = models.DateTimeField(default=None,null=True, blank=True) 
    
    class Meta:
        abstract = True

#Used for Patient Information
class Patient(BasicModel):

    def get_patient_code():
        new_patient_code="P-"+get_random_string(12)
        return new_patient_code 
    
    patient_id=models.AutoField (primary_key=True)
    patient_code=models.CharField(max_length=50, null=True,
                            blank=True,
                            default=get_patient_code,
                            unique=True,
                            db_index=True)  
    patient_name=models.CharField (max_length=250, null=True, default=None, blank=False,db_index=True) 
    patient_email=models.CharField (max_length=250, null=False, default=None, blank=False,db_index=True,unique=True) 
    patient_password=models.CharField (max_length=15, null=False, default=None, blank=False) 
    
    def __str__(self):
        return self.patient_name + " ("+self.patient_email+")"
	
    class Meta:
      db_table = 'app_patient'  
      ordering = ['-patient_id']

#Used for Counsellor Information
class Counsellor(BasicModel):

    def get_counsellor_code():
        new_counsellor_code="C-"+get_random_string(12)
        return new_counsellor_code 
    
    counsellor_id=models.AutoField (primary_key=True)
    counsellor_code=models.CharField(max_length=50, null=True,
                            blank=True,
                            default=get_counsellor_code,
                            unique=True,
                            db_index=True)  
    counsellor_name=models.CharField (max_length=250, null=True, default=None, blank=False,db_index=True) 
    counsellor_email=models.CharField (max_length=250, null=False, default=None, blank=False,db_index=True,unique=True) 
    counsellor_password=models.CharField (max_length=15, null=False, default=None, blank=False) 
   
    
    def __str__(self):
        return self.counsellor_name + " ("+self.counsellor_email+")"
	

    class Meta:
      db_table = 'app_counsellor'  
      ordering = ['-counsellor_id']

#Used for Counsellor Information
class Appointment(BasicModel):

    def get_appointment_code():
        new_appointment_code="A-"+get_random_string(12)
        return new_appointment_code 
    
    appointment_id=models.AutoField (primary_key=True)
    appointment_code=models.CharField(max_length=50, null=True,
                            blank=True,
                            default=get_appointment_code,
                            unique=True,
                            db_index=True)  
    
    appointment_date=models.DateTimeField(default=None, blank=True, null=True)
    appointment_patient=models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    appointment_counsellor=models.ForeignKey(Counsellor, null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.appointment_id

    def counsellor_name(self):
        
        if self.appointment_counsellor is not None:
            return self.appointment_counsellor.counsellor_name + " ("+self.appointment_counsellor.counsellor_email+")"
        else:
           return "Nil"     
          

    def patient_name(self):
        
        if self.appointment_patient is not None:
           return self.appointment_patient.patient_name + " ("+self.appointment_counsellor.counsellor_email+")"	
        else:
           return "Nil"     

	

    class Meta:
      db_table = 'app_appointments'  
      ordering = ['-appointment_id']
