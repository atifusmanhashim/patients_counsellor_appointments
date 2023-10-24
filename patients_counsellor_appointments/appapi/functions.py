# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime
from datetime import datetime, date, timedelta

#Used for  Path (File Handling, Folders)
from pathlib import Path

import datetime
import math
import json
import os
import requests
import pandas as pd

import appapi.constants as constants
from django.conf import settings

#URLLibrary Parsing
import urllib.parse

from .models import (AppAnalytics)

#=========================================== Common Functions ====================================
#Merge 2 Dictionaries
def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

#Getting Dictionary
def getList(dict): 
    
    return dict

#Date Validation Function
def validate(date_text):
    
    isValidDate = True
    date_string = date_text
    format = "%Y-%m-%d"
    try :
        datetime.datetime.strptime(date_string, format)
        isValidDate = True
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        return True
    else :
       return False

def current_date():

    current_date=date.today()
    return current_date

def current_date_time():

    current_date_time=format(datetime.datetime.now(),constants.datetime_format)
    return current_date_time

def display_date_time(date_text):
    req_format = constants.datetime_format

    dt=format(date_text,req_format)
    return dt

def get_app_base_url(request):
    base_url_string=request.scheme+":"+request.get_host()
    return base_url_string

def get_client_ip(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    return ip_address

def format_epoch_dtime(sel_time):
    if sel_time is not None:
        if type(sel_time)==int:
            epoch_time = sel_time
            epoch_time_len=len(str(sel_time))
            if epoch_time_len > 10:
                epoch_time=epoch_time/1000
                dt = datetime.datetime.utcfromtimestamp(epoch_time).strftime(constants.datetime_format)
            else:
                epoch_time=epoch_time
                dt = datetime.datetime.utcfromtimestamp(epoch_time).strftime(constants.datetime_format)
        else:
            dt=None
    else:
        dt=None
    return dt

#=========================================== Pagination ====================================
#Used for Pagination
def pagination(request):

    
    if 'page' in request.data:
        page = int(request.data.get('page', 1))
    else:
        page = 1

    if 'reqRecs' in request.data:
        reqRecs=int(request.data.get('reqRecs',10))
    else:
        reqRecs=10

    startpage=(page-1)*reqRecs
    endpage=page*reqRecs
    #================================End of Pagination ===============================

    result={'start':startpage,'end':endpage,'page':page,'reqRecs':reqRecs}
    return result

#Getting Total Pages
def get_total_pages (sel_total_records, sel_req_records):

    if sel_total_records > 0 and sel_req_records > 0:
        total_pages=int(math.ceil(sel_total_records/sel_req_records))
        if total_pages==0:
            total_pages=1
    else:
        total_pages=0

    return total_pages

#=========================================== End of Pagination ====================================


#=========================================== Error Logs ===========================================
log_dir_path=os.path.join(Path().absolute().parent,'log/error_logs')

def write_log_file(sel_text):
    log_file_name=str(current_date()) + '.log'
    log_file_path=os.path.join(log_dir_path,log_file_name)
    sel_file = log_file_path

    if sel_file is not None:
        

        file=open(sel_file,"a+")
       
            
        if sel_text is not None:
            file.write('\n')
            file.write(sel_text)
            file.close()
    return True

#Download Path
def download_excel_path():
    excel_file_path=str(os.path.join(Path(__file__).absolute().parent.parent))+ "/excel_data"
    if not os.path.isdir(excel_file_path):
        print("false")
        os.makedirs(excel_file_path)
    return excel_file_path

#Delete existing csv files
def delete_existing_csv():
    try:
        excel_file_path=download_excel_path()
        excel_file_lst=list(os.listdir(excel_file_path))
        if len(excel_file_lst)>0:
            print(excel_file_lst)
            for file_name in excel_file_lst:
                file_path=os.path.join(excel_file_path,file_name)
                os.remove(file_path)
        return True
    except:
        return False
    

#=========================================== Error Logs ===========================================
#=========================================== End of Common Functions ==============================#=========================================== Analytics =====================================
#Saving Analytics
def save_analytics(sel_user,sel_action,request):

    data=request.data
    app_version = data.get('app_version', None)
    platform= data.get('platform', None)
    brand= data.get('brand', None)
    device= data.get('device_id', None)
    device_model= data.get('device_model', None)
    device_ip=get_client_ip(request)
    
    if sel_user is not None:
        analytics=AppAnalytics.objects.create(user=sel_user,
                                                       search_params=request.data, 
                                                       action=sel_action,
                                                       app_version=app_version,
                                                       platform=platform,
                                                       brand=brand,
                                                       device=device,
                                                       device_model=device_model,
                                                       device_ip=device_ip)


    else:
        analytics=AppAnalytics.objects.create(search_params=request.data, 
                                                       action=sel_action,
                                                       app_version=app_version,
                                                       platform=platform,
                                                       brand=brand,
                                                       device=device,
                                                       device_model=device_model,
                                                       device_ip=device_ip)

    return True

# ========================================== URL Parsing ==========================================
def get_url_query_params(sel_url):
    if sel_url is not None:
        parse_url=urllib.parse.urlparse(sel_url)
        parse_url_query=parse_url.query
        parse_url_query_params=urllib.parse.parse_qs(parse_url_query)
        query_params=parse_url_query_params
    else:
        query_params=[]
    return query_params
# ========================================== End of URL Parsing ==========================================


