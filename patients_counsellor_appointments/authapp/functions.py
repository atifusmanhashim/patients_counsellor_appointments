#Getting Random String
from django.utils.crypto import get_random_string

# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime, date, timedelta
import datetime

#Oauth2 Provider
from oauth2_provider.models import AccessToken, Application, RefreshToken
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.generators import generate_client_id, generate_client_secret

#For Getting Access Token
from oauth2_provider.views import TokenView

#Using Models
from .models import (GroceryAppCustomer, AppUser, AppUserLocation, AppUserDeliveryAddress,AppUserDevice,AppUserReferral)

from appapi.models import (GroceryStoreNotificationPreferences)
from appapi.functions import (save_analytics, 
                              current_date,
                              current_date_time,
                              display_date_time, 
                              get_client_ip, 
                              pagination,
                              get_total_pages,
                              write_log_file,
                              get_url_query_params)
#Using Constant Values
import appapi.constants as constants

#Types for Checking DataTypes
import types

from django.db.models import Q
from django.conf import settings
#==================================================Oauth2 ====================================
#Getting Application Oauth2 Credentials
def get_application_credentials():
    
    application_chk = Application.objects.filter(name=constants.app_name)
    if application_chk.count()==0:
        application=Application(
                                user= AppUser.objects.filter(is_superuser=True)[0],
                                client_type="confidential",
                                authorization_grant_type="password",
                                name=constants.app_name,
                                client_id=generate_client_id(),
                                client_secret=generate_client_secret(),
                                )   
        application.save()                        
    else:
        application=application_chk[0] 
            
    result=application
        
    return result

#Getting User using ID
def get_user(sel_id):
    if sel_id.isnumeric():
        try:
            sel_user=AppUser.objects.get(pk=sel_id)
        except AppUser.DoesNotExist:
            sel_user=None
    else:
       sel_user=None 
    return sel_user
