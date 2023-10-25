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
                        get_patient,
                        get_counsellor
                        )

from .models import (Patient,Counsellor,Appointment)
import json 
import math
import traceback

# ======================================= Start of Patients =============================================
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

# Patient Delete
class PatientDelete(APIView):
    def post(self,request, format='json'):
        try:
            action="Patient Delete"
            analytics=save_analytics(action,request)
            data=request.data
                
            if 'patient_id' in data:
                if str(data.get('patient_id')).isnumeric():
                    patient_id=data.get('patient_id')
                    patient_obj=get_patient(patient_id)
                        
                    if patient_obj is not None:
                        patient_obj.is_active=False
                        patient_obj.deleted_date=current_date_time()
                        patient_obj.save()
                        serializer=PatientSerializer(instance=patient_obj)
                        response={'msg':'success','status':200,'data':serializer.data}
                        return Response(response, status=status.HTTP_200_OK)
                    else:
                        response={'msg':'fail','status':400,'errors':'Invalid Patient ID'}
                        return Response(response, status=400)
                    
                else:
                    response={'msg':'fail','status':400,'errors':'Patient ID Not Provided'}
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

# Patient Details
class PatientDetails(APIView):
    def get(self,request, format='json'):
        try:
                action="Patient Details"
                analytics=save_analytics(action,request)
                data=request.data
                
                if 'patient_id' in data:
                    if str(data.get('patient_id')).isnumeric():
                        patient_id=data.get('patient_id')
                        patient_obj=get_patient(patient_id)
                        
                        if patient_obj is not None:
                            serializer=PatientSerializer(instance=patient_obj)
                            response={'msg':'success','status':200,'data':serializer.data}
                            return Response(response, status=status.HTTP_200_OK)
                        else:
                            response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                            return Response(response, status=400)
                    else:
                        response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                        return Response(response, status=400)
                else:
                    response={'msg':'fail','status':400,'errors':'Counsellor ID Not Provided'}
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

# Patient Update
class PatientUpdate(APIView):
    def post(self,request, format='json'):
        try:
                action="Patient Update"
                analytics=save_analytics(action,request)
                data=request.data
                
                if 'patient_id' in data:
                    if str(data.get('patient_id')).isnumeric():
                        patient_id=data.get('patient_id')
                        patient_obj=get_patient(patient_id)
                        
                        if patient_obj is not None:
                              
                            
                            serializer=PatientSerializer(instance=patient_obj,data=request.data, partial=True)
                            if serializer.is_valid():
                                serializer.save()
                                response={'msg':'success','status':200,'data':serializer.data}
                                return Response(response, status=status.HTTP_200_OK)
                            else:
                                response={'msg':'fail','status':400,'data':request.data,'errors':str(serializer.errors)}
                                return Response(response, status=400)   
                        else:
                            response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                            return Response(response, status=400)
                    else:
                        response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                        return Response(response, status=400)
                else:
                    response={'msg':'fail','status':400,'errors':'Counsellor ID Not Provided'}
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


# Active Patients
class PatientList(APIView):
    def get(self,request, format='json'):
        try:
                action="Patient List"
                analytics=save_analytics(action,request)
                data=request.data
                 #============================== Pagination ============================================
                req_pagination=pagination(request)
                startpage=req_pagination['start']
                endpage=req_pagination['end']
                page=req_pagination['page']
                reqRecs=req_pagination['reqRecs']
                #================================End of Pagination ===============================

                queryset=Patient.objects.filter(is_active=True).order_by('-patient_id')
                

                total_records=queryset.count()
                    
                data_list=queryset[startpage:endpage]
            
                serializer = PatientSerializer(data_list, many=True)
        
                if total_records > 0:
                    total_pages=int(math.ceil(total_records/reqRecs))
                    if total_pages==0:
                        total_pages=1
                else:
                    total_pages=0

                for val in serializer.data:
                    val.pop('patient_password')
                
                response={'msg':'success','status':200,'total_pages':total_pages,'total_records':total_records,'current_page':page,'records':data_list.count(),'data':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

 


          
                
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

# ======================================= End of Patients =============================================
# ======================================= Start of Counsellor =============================================
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

# Active Counsellors
class CounsellorList(APIView):
    def get(self,request, format='json'):
        try:
                action="Counsellors List"
                analytics=save_analytics(action,request)
                data=request.data
                 #============================== Pagination ============================================
                req_pagination=pagination(request)
                startpage=req_pagination['start']
                endpage=req_pagination['end']
                page=req_pagination['page']
                reqRecs=req_pagination['reqRecs']
                #================================End of Pagination ===============================

                queryset=Counsellor.objects.filter(is_active=True).order_by('-counsellor_id')
                

                total_records=queryset.count()
                    
                data_list=queryset[startpage:endpage]
            
                serializer = CounsellorSerializer(data_list, many=True)
        
                if total_records > 0:
                    total_pages=int(math.ceil(total_records/reqRecs))
                    if total_pages==0:
                        total_pages=1
                else:
                    total_pages=0

                for val in serializer.data:
                    val.pop('counsellor_password')
                
                response={'msg':'success','status':200,'total_pages':total_pages,'total_records':total_records,'current_page':page,'records':data_list.count(),'data':serializer.data}
                return Response(response, status=status.HTTP_200_OK)

 


          
                
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

# Counsellor Delete
class CounsellorDelete(APIView):
    def post(self,request, format='json'):
        try:
            action="Counsellor Delete"
            analytics=save_analytics(action,request)
            data=request.data
                
            if 'counsellor_id' in data:
                if str(data.get('counsellor_id')).isnumeric():
                    counsellor_id=data.get('counsellor_id')
                    counsellor_obj=get_counsellor(counsellor_id)
                        
                    if counsellor_obj is not None:
                        counsellor_obj.is_active=False
                        counsellor_obj.deleted_date=current_date_time()
                        counsellor_obj.save()
                        serializer=CounsellorSerializer(instance=counsellor_obj)
                        response={'msg':'success','status':200,'data':serializer.data}
                        return Response(response, status=status.HTTP_200_OK)
                    else:
                        response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                        return Response(response, status=400)
                    
                else:
                    response={'msg':'fail','status':400,'errors':'Counsellor ID Not Provided'}
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

# Counsellor Update
class CounsellorUpdate(APIView):
    def post(self,request, format='json'):
        try:
            action="Counsellor Update"
            analytics=save_analytics(action,request)
            data=request.data
                
            if 'counsellor_id' in data:
                if str(data.get('counsellor_id')).isnumeric():
                    counsellor_id=data.get('counsellor_id')
                    counsellor_obj=get_counsellor(counsellor_id)
                        
                    if counsellor_obj is not None:
                        
                        serializer=CounsellorSerializer(instance=counsellor_obj,data=request.data,partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            response={'msg':'success','status':200,'data':serializer.data}
                            return Response(response, status=status.HTTP_200_OK)
                        else:
                            response={'msg':'fail','status':400,'data':request.data,'errors':str(serializer.errors)}
                            return Response(response, status=400)
                    else:
                        response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                        return Response(response, status=400)
                    
                else:
                    response={'msg':'fail','status':400,'errors':'Counsellor ID Not Provided'}
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


# Counsellor Details
class CounsellorDetails(APIView):
    def get(self,request, format='json'):
        try:
                action="Counsellor Details"
                analytics=save_analytics(action,request)
                data=request.data
                
                if 'counsellor_id' in data:
                    if str(data.get('counsellor_id')).isnumeric():
                        counsellor_id=data.get('counsellor_id')
                        counsellor_obj=get_counsellor(counsellor_id)
                        
                        if counsellor_obj is not None:
                            serializer=CounsellorSerializer(instance=counsellor_obj)
                            response={'msg':'success','status':200,'data':serializer.data}
                            return Response(response, status=status.HTTP_200_OK)
                        else:
                            response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                            return Response(response, status=400)
                    else:
                        response={'msg':'fail','status':400,'errors':'Invalid Counsellor ID'}
                        return Response(response, status=400)
                else:
                    response={'msg':'fail','status':400,'errors':'Counsellor ID Not Provided'}
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


# ======================================= End of Counsellor =============================================

# ======================================= Start of Appointments =============================================

# Create Appointment for Patient
class CreateAppointment(APIView):
    def post(self,request, format='json'):
        try:
            data=request.data
            
            required_data={
                            'appointment_patient':data.get('patient_id'),
                            'appointment_counsellor':data.get('counsellor_id'),
                            'appointment_date':data.get('appointment_date')
                        }
            serializer=AppointmentSerializer(data=required_data)
                        
            if serializer.is_valid():
                appointment=serializer.save()
                response={'msg':'success','status':200,'data':serializer.data}
                return Response(response, status=200)
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
