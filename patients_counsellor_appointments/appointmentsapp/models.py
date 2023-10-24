from django.db import models


# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime

#For Getting Random String
from django.utils.crypto import get_random_string

from authapp.models import (AppUser,UserRole,LoginAnalytics)
from django.contrib.auth.models import AbstractUser

from django.conf import settings

import appapi.constants as constants

#Common Basic Model
class BasicModel(models.Model):
    is_active = models.BooleanField (null=True, default=True, blank=True) 
    create_date = models.DateTimeField(default=timezone.now, blank=True)
    modified_date = models.DateTimeField(default=timezone.now, blank=True) 

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
    patient_name=models.CharField (max_length=300, null=True, default=None, blank=False,db_index=True) 
    patient_email=models.CharField (max_length=300, null=True, default=None, blank=False,db_index=True,unique=True) 
    patient_user=models.ForeignKey(AppUser, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.patient_name is not None and self.user.email is not None:
            return self.patient_name + " ("+self.user.email+")"
	
    def (self):
        return self.action 
    class Meta:
      db_table = 'app_patient'  
      ordering = ['-patient_id']

#Used for Patient Information
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
    counsellor_name=models.CharField (max_length=300, null=True, default=None, blank=False,db_index=True) 
    counsellor_email=models.CharField (max_length=300, null=True, default=None, blank=False,db_index=True,unique=True) 
    counsellor_user=models.ForeignKey(AppUser, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.counsellor_name is not None and self.counsellor_user.email is not None:
            return self.counsellor_name + " ("+self.counsellor_user.email+")"
	

    class Meta:
      db_table = 'app_counsellor'  
      ordering = ['-counsellor_id']

