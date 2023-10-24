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

#Used for Storing Analytics
class AppAnalytics(BasicModel):

    action=models.CharField (max_length=50, null=True, default=None, blank=True)   
    search_params=models.TextField(null=True, default=None, blank=True) 
    
    #Device Information
    app_version=models.CharField (max_length=50, null=True, default=None, blank=True)  
    platform=models.CharField (max_length=50, null=True, default=None, blank=True)  
    brand=models.CharField (max_length=50, null=True, default=None, blank=True)  
    device=models.CharField (max_length=250, null=True, default=None, blank=True)  
    device_model=models.CharField (max_length=50, null=True, default=None, blank=True)   
    device_ip=models.CharField (max_length=50, null=True, default=None, blank=True)  
    
    user=models.ForeignKey(AppUser, null=True, on_delete=models.CASCADE)
    
    def get_action(self):
        return self.action 
    class Meta:
      db_table = 'app_analytics'  
      ordering = ['id']