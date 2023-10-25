from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, views, generics, response, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken  #for Getting Neew Token
from rest_framework.parsers import JSONParser



from collections import namedtuple

from django.db import IntegrityError
from requests.exceptions import HTTPError
from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.http import HttpRequest
from django.contrib.auth.hashers import make_password

#Settings
from django.conf import settings

# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime, date, timedelta
import datetime


from appapi.functions import (save_analytics, 
                              validate,
                              current_date,
                              current_date_time,
                              display_date_time, 
                              get_client_ip, 
                              pagination,
                              get_total_pages,
                              write_log_file)

from .serializers import (PatientSerializer, CounsellorSerializer, AppointmentSerializer)

from .functions import (patient_email_exist, 
                        counsellor_email_exist,
                        appointment_exist
                        )

import json 
import traceback

#Create Patient API
class CreatePatient(APIView):
    def post(self,request, format='json'):
        try:
                action="Create Patient"
                analytics=save_analytics(action,request)
                data=request.data
                
                required_data={
			'patient_name':data.get('patient_name'),
			'patient_email':data.get('patient_email'),
			'patient_password':data.get('patient_password')
		}
                serializer = PatientSerializer(data=required_data)   
                if serializer.is_valid():
                      patient= serializer.save()
                      mydata=serializer.data
                      mydata.pop('patient_password')
                      response={'msg':'success','status':200,'data':mydata}
                      return Response(response, status=status.HTTP_200_OK)   
                else:
                      response={'msg':'fail','status':400,'data':required_data,'errors':str(serializer.errors)}
                      return Response(response, status=400)   


          
                
        except Exception as e:
            message=("Error Date/Time:{current_time}\nURL:{current_url}\nError:{current_error}\n\{tb}\nCuurent Inputs:{current_input}".format(
                current_time=current_date_time(),
                current_url=request.build_absolute_uri(),
                current_error=repr(e),
                tb=traceback.format_exc(),
                current_input=request.data
            ))
            
            write_log_file(message)
            response={'msg':'fail','status':400,'errors':str(e)}
            return Response(response, status=400)        
         
#Create Counsellor API
class CreateCounsellor(APIView):
    def post(self,request, format='json'):
        try:
                action="Create Counsellor"
                analytics=save_analytics(action,request)
                data=request.data
                
                required_data={
			'counsellor_name':data.get('counsellor_name'),
			'counsellor_email':data.get('counsellor_email'),
			'counsellor_password':data.get('counsellor_password')
		}
                serializer = CounsellorSerializer(data=required_data)   
                if serializer.is_valid():
                      counsellor= serializer.save()
                      mydata=serializer.data
                      mydata.pop('counsellor_password')
                      response={'msg':'success','status':200,'data':mydata}
                      return Response(response, status=status.HTTP_200_OK)   
                else:
                      response={'msg':'fail','status':400,'data':required_data,'errors':str(serializer.errors)}
                      return Response(response, status=400)   


          
                
        except Exception as e:
            message=("Error Date/Time:{current_time}\nURL:{current_url}\nError:{current_error}\n\{tb}\nCuurent Inputs:{current_input}".format(
                current_time=current_date_time(),
                current_url=request.build_absolute_uri(),
                current_error=repr(e),
                tb=traceback.format_exc(),
                current_input=request.data
            ))
            
            write_log_file(message)
            response={'msg':'fail','status':400,'errors':str(e)}
            return Response(response, status=400)        
