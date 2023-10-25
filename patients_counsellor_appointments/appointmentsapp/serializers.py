from rest_framework import serializers

#For Checking Unique Values
from rest_framework.validators import UniqueValidator

#For Getting Random String
from django.utils.crypto import get_random_string

#For Using User Model
from authapp.models import AppUser

#For Using Listing Model
from .models import (Patient,Counsellor,Appointment)



from datetime import datetime,date,timedelta

from django.utils import timezone

import appapi.constants as constants


class PatientSerializer(serializers.ModelSerializer):
    def increment_patient_code():

        new_patient_code='P-'+ get_random_string(12)
        return new_patient_code
    
    patient_code=serializers.CharField(default=increment_patient_code, 
                                     max_length=50, 
                                     validators=[UniqueValidator(queryset=Patient.objects.all())])

    patient_email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Patient.objects.all())]
            )

    patient_name=serializers.CharField(required=True)
    patient_password = serializers.CharField(required=True,min_length=8)

    class Meta:
        model = Patient
        fields = ('__all__')

# Counsellor
class CounsellorSerializer(serializers.ModelSerializer):

    def increment_counsellor_code():

        new_counsellor_code='C-'+ get_random_string(12)
        return new_counsellor_code
    
    counsellor_code=serializers.CharField(default=increment_counsellor_code, 
                                     max_length=50, 
                                     validators=[UniqueValidator(queryset=Counsellor.objects.all())])

    counsellor_email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Counsellor.objects.all())]
            )

    counsellor_name=serializers.CharField(required=True)
    counsellor_password = serializers.CharField(min_length=8)


    class Meta:
        model = Counsellor
        fields = ('__all__')

    def create(self, validated_data): 
        instance = Counsellor.objects.create(**validated_data) 
        return instance


#Serializer for Creating Request Object
class AppointmentSerializer(serializers.ModelSerializer):

    def increment_appointment_code():

        new_appointment_code='A-'+ get_random_string(12)
        return new_appointment_code
         
    appointment_code=serializers.CharField(default=increment_appointment_code, max_length=50) 
    appointment_date=serializers.DateField(required=True,validators=[UniqueValidator(queryset=Appointment.objects.all())])
    
    #Patient
    appointment_patient_name = serializers.CharField(source='appointment_patient.patient_name', read_only=True) 
    appointment_patient_email= serializers.CharField(source='appointment_patient.patient_email', read_only=True) 

    #Counsellor
    appointment_counsellor_name = serializers.CharField(source='appointment_counsellor.counsellor_name', read_only=True) 
    appointment_counsellor_email= serializers.CharField(source='appointment_counsellor.counsellor_email', read_only=True) 
 

    class Meta:
        model=Appointment
        fields = (
                  'appointment_id', 
                  'appointment_code', 
                  'appointment_date',
                  'appointment_patient',
                  'appointment_patient_name',
                  'appointment_patient_email',
                  'appointment_counsellor',
                  'appointment_counsellor_name',
                  'appointment_counsellor_email',
                  'is_active',
                  'create_date',
                  'modified_date',
                  'deleted_date') 

    def create(self, validated_data): 
        instance = Appointment.objects.create(**validated_data) 
        return instance
    
#Serializer for Creating Request Object
class AppointmentListtSerializer(serializers.ModelSerializer):

    
         
    
   
    #Patient
    appointment_patient_name = serializers.CharField(source='appointment_patient.patient_name', read_only=True) 
    appointment_patient_email= serializers.CharField(source='appointment_patient.patient_email', read_only=True) 

    #Counsellor
    appointment_counsellor_name = serializers.CharField(source='appointment_counsellor.counsellor_name', read_only=True) 
    appointment_counsellor_email= serializers.CharField(source='appointment_counsellor.counsellor_email', read_only=True) 
 

    class Meta:
        model=Appointment
        fields = (
                  'appointment_id', 
                  'appointment_code', 
                  'appointment_date',
                  'appointment_patient',
                  'appointment_patient_name',
                  'appointment_patient_email',
                  'appointment_counsellor',
                  'appointment_counsellor_name',
                  'appointment_counsellor_email',
                  'is_active',
                  'create_date',
                  'modified_date',
                  'deleted_date') 
