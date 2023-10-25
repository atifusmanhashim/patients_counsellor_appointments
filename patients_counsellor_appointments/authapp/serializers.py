from rest_framework import serializers

#For Checking Unique Values
from rest_framework.validators import UniqueValidator

#For User Login Authentication
from django.contrib.auth import authenticate

#For Getting Random String
from django.utils.crypto import get_random_string

#For Using App Models
from .models import (UserRole, AppUser, LoginAnalytics)

import appapi.constants as constants

from appapi.functions import (display_date_time)

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)

# Email Check and Social ID Check
class EmailSocialSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    social_id=serializers.CharField(required=False)

# Anonymous User
class AnonymousSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=150, required=True)   
    
#User List
class UserList(serializers.ModelSerializer):
    user_city=serializers.CharField(read_only=True, source='userCity.name')
    user_country=serializers.CharField(read_only=True, source='userCountry.name')
    referral=serializers.CharField(read_only=True, source='referral_string')
    referral_counter=serializers.CharField(read_only=True, source='user_referral_counter')

    class Meta:
        model = AppUser
        fields = ('id',
                  'name',
                  'email', 
                  'username', 
                  'contact_no',
                  'delivery_address',
                  'delivery_area',
                  'device_id',
                  'provider_id',
                  'social_id',
                  'user_city',
                  'user_country',
                  'referral',
                  'referral_counter',
                  'is_auth')

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    
    user_city=serializers.CharField(read_only=True, source='userCity.name')
    user_country=serializers.CharField(read_only=True, source='userCountry.name')
    address=serializers.CharField(read_only=True, source='delivery_address')
    area=serializers.CharField(read_only=True, source='delivery_area')
    referral=serializers.CharField(read_only=True, source='referral_url')
    referral_counter=serializers.CharField(read_only=True, source='user_referral_counter')

    
    class Meta:
        model = AppUser
        fields = ('id',
                  'user_no',
                  'name',
                  'email', 
                  'contact_no',
                  'address',
                  'area',
                  'username', 
                  'user_city',
                  'user_country',
                  'is_auth',   
                  'date_joined',
                  'device_id',   
                  'app_version',
                  'platform',
                  'brand',
                  'device_model',          
                  'social_id',
                  'provider_id',
                  'referral',
                  'referral_counter',
                )
        
#Normal Signup
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=AppUser.objects.all())]
            )
    name=serializers.CharField(required=False,default='N/A')
    password = serializers.CharField(min_length=8,required=False)
    device_id = serializers.CharField(max_length=150)
    provider_id=serializers.IntegerField(default=0)
    social_id=serializers.CharField(max_length=150, required=False, default='N/A')
    social_email_chk=serializers.BooleanField(default=False, required=False)
    social_contact_chk=serializers.BooleanField(default=False, required=False)
    contact_no= serializers.CharField(max_length=150,
                                        required=False,
                                        validators=[UniqueValidator(queryset=AppUser.objects.all())])
    user_city=serializers.CharField(required=False, default="N/A")
    user_country=serializers.CharField(required=False, default="N/A")
    
    
    def create(self, validated_data):
        device_id= serializers.CharField()
        
        try:
            user_city=City.objects.get(name=validated_data['user_city'])
            if user_city:
                user_city_chk=True
            else:
                user_city_chk=False
        except:
            user_city_chk=False

        try:
            user_country=Country.objects.get(name=validated_data['user_country'])
            if user_country:
                user_country_chk=True
            else:
                user_country_chk=False
        except:
            user_country_chk=False
            
        if user_city_chk==True and user_country_chk==True:
            user = AppUser.objects.create_user(
                name=validated_data['name'],
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                contact_no=validated_data['contact_no'],
                device_id=validated_data['device_id'],
                provider_id=validated_data['provider_id'],
                social_id=validated_data['social_id'],
                social_email_chk=validated_data['social_email_chk'],
                social_contact_chk=validated_data['social_contact_chk'],
                userCity=user_city,
                userCountry=user_country
                )
        else:
            user = AppUser.objects.create_user(
                name=validated_data['name'],
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                contact_no=validated_data['contact_no'],
                device_id=validated_data['device_id'],
                provider_id=validated_data['provider_id'],
                social_id=validated_data['social_id'],
                social_email_chk=validated_data['social_email_chk'],
                social_contact_chk=validated_data['social_contact_chk']
                )
        return user

    class Meta:
        model = AppUser
        fields = ('__all__')

# Normal Login
class LoginSerializer(serializers.ModelSerializer):

    email=serializers.EmailField(required=True)
    username = serializers.CharField(required=False)
    password = serializers.CharField(min_length=8)

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}

    class Meta:
        model = AppUser
        fields=('__all__')
               

#Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    model=AppUser
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

#Reset Password Serializer
class ResetPasswordSerializer(serializers.Serializer):
    model=AppUser
    """
    Serializer for password reset endpoint.
    """
    email =  serializers.EmailField(required=True)
    new_password = serializers.CharField(min_length=8)