from django.db import models


# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime

#For Getting Random String
from django.utils.crypto import get_random_string

#
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

class UserRole(BasicModel):
    def get_role_code():
        new_role_code="UR-"+get_random_string(12)
        return new_role_code  
 
    role_id=models.AutoField (primary_key=True)
    role_code=models.CharField(max_length=50, null=True,
                            blank=True,
                            default=get_role_code,
                            db_index=True)  

    
    role_name=models.CharField (max_length=50, null=True, default=None, blank=True)
    
    def __str__(self):
        return self.role_name

    class Meta:
      db_table = 'app_user_role'  
      ordering = ['role_id']
      constraints = [models.UniqueConstraint(fields=['role_code'], name='unique_role_code')]
      

#Custom Abstract Model 
class AppUser (AbstractUser):

    def get_user_no():
        new_user_no="U-"+get_random_string(12)
        return new_user_no   

    def get_referral_string():
        referral_string=get_random_string(24)
        return referral_string  

    user_no=models.CharField(max_length=50, null=True,
                            blank=True,
                            default=get_user_no,
                            db_index=True)
    name=models.CharField (max_length=50, null=True, default=None, blank=True)
    user_role=models.ForeignKey(UserRole,blank=True, null=True ,related_name='category', on_delete=models.SET_NULL)
    

    def __str__(self):
        if self.name is not None and self.email is not None:
            return self.name + " ("+self.email+")"
        elif self.first_name is not None and self.last_name is not None and self.email is not None:
            return self.first_name + " " + self.last_name +" ("+self.email+")"
        else:
            return self.username

    class Meta:
      db_table = 'app_user_mst'  
#       ordering = ['-id']
      constraints = [models.UniqueConstraint(fields=['user_no'], name='unique_user_no')]


class LoginAnalytics(BasicModel):

    action=models.CharField (max_length=50, null=True, default=None, blank=True)   
    user=models.ForeignKey(AppUser, null=True, on_delete=models.CASCADE)
    source=models.CharField (max_length=300, null=True, default=None, blank=True)

    device_ip=models.CharField (max_length=50, null=True, default=None, blank=True)


    class Meta:
      db_table = 'app_login_analytics'
      ordering = ['-id']

