from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages,sessions
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect,HttpResponse,HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt

import logging
import re
import json

import appapi.constants as constants

from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth.models import update_last_login
from authapp.serializers import (AnonymousSerializer, RegisterSerializer, LoginSerializer,
                        UserSerializer, ChangePasswordSerializer, ResetPasswordSerializer)


# Create your views here.

@csrf_exempt
def index(request):
   if 'user_id' in request.session:
        return HttpResponseRedirect("dashboard")
   else:
        return HttpResponseRedirect("login")

@csrf_protect
def dashboard(request):
    context={}
    template = loader.get_template('dashboard.html')
    if 'user_id' in request.session:
        global userId
        userId = str(request.session['user_id'])
        context={
    		'user_id':userId
    	}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("login")

@csrf_protect
def user_login(request):
    context={}
    template = loader.get_template('login.html') 
    if request.method == 'GET':
        if 'user_id' in request.session:
            return HttpResponseRedirect("dashboard")

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username is not None and password is not None:
            user=authenticate(username=username,password=password)
            
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session.set_expiry(constants.session_expiry_time) #sets the exp. value of the session 
                    update_last_login(None, user)
                    username=user.username
                    user_id=user.id
                    if user.name is not None:
                        name=user.name
                    elif user.first_name is not None and user.last_name is not None:
                        name=user.first_name + " " + user.last_name
                    else:
                        name=user.username
                    email=user.email
                    request.session["user_id"]=user_id
                    request.session["user_name"]=name
                    request.session["username"]=username
                    request.session["user_email"]=email

                    context={
                            'user_name':name,
                            'user_email':email
                        }
                    return HttpResponseRedirect("dashboard")
               
                else:
                    context['message_error']="User is not active"
                    # messages.error(request, "User is not active") 
                    return HttpResponseRedirect(reverse("login"))
            else:
                context['message_error']="Wrong Username or Password!"
                # messages.error(request, "Wrong Username or Password!") 
                return HttpResponseRedirect(reverse("login"))
        else:
            context['message_error']="Username or Password not provided for login!"
            # messages.info(request, "Username or Password not provided for login!") 
            return HttpResponseRedirect(reverse("login"))
    context = {
        'user_id':'', 
    }
    return HttpResponse(render(request, "login.html",context))

            
            
            

@csrf_exempt
def patients(request):
    try:
        context={}
        template = loader.get_template('patients.html')
        if 'user_id' in request.session:
            global userId
            userId = str(request.session['user_id'])
            context={
                'user_id':userId
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse("login"))
  
    except Exception as e:
        message=("Error Date/Time:{current_time}\nURL:{current_url}\nError:{current_error}\n\{tb}\nCuurent Inputs:{current_input}\nUser:{current_user}".format(
                    current_time=current_date_time(),
                    current_url=request.build_absolute_uri(),
                    current_error=repr(e),
                    tb=traceback.format_exc(),
                    current_input=request,
                    current_user=None

        ))

        write_log_file(message)
        context['error_msg']="Something Went Wrong"
        # context['error_msg']=traceback.format_exc()
        return(render(request, 'error.html',context))


@csrf_exempt
def counsellors(request):
    try:
        context={}
        template = loader.get_template('counsellors.html')
        if 'user_id' in request.session:
            global userId
            userId = str(request.session['user_id'])
            context={
                'user_id':userId
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse("login"))
  
    except Exception as e:
        message=("Error Date/Time:{current_time}\nURL:{current_url}\nError:{current_error}\n\{tb}\nCuurent Inputs:{current_input}\nUser:{current_user}".format(
                    current_time=current_date_time(),
                    current_url=request.build_absolute_uri(),
                    current_error=repr(e),
                    tb=traceback.format_exc(),
                    current_input=request,
                    current_user=None

        ))

        write_log_file(message)
        context['error_msg']="Something Went Wrong"
        # context['error_msg']=traceback.format_exc()
        return(render(request, 'error.html',context))

@csrf_exempt
def appointments(request):
    try:
        context={}
        template = loader.get_template('appointments.html')
        if 'user_id' in request.session:
            global userId
            userId = str(request.session['user_id'])
            context={
                'user_id':userId
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse("login"))
  
    except Exception as e:
        message=("Error Date/Time:{current_time}\nURL:{current_url}\nError:{current_error}\n\{tb}\nCuurent Inputs:{current_input}\nUser:{current_user}".format(
                    current_time=current_date_time(),
                    current_url=request.build_absolute_uri(),
                    current_error=repr(e),
                    tb=traceback.format_exc(),
                    current_input=request,
                    current_user=None

        ))

        write_log_file(message)
        context['error_msg']="Something Went Wrong"
        # context['error_msg']=traceback.format_exc()
        return(render(request, 'error.html',context))    
          
# Logout    
def logout(request):
    try:
        context={}
        if 'user_id' in request.session:
            del request.session['user_id']
        context['message_success']="You are logged out"
        return HttpResponseRedirect("admin_panel:login")
    except Exception as e:
        message=("Error Date/Time:{current_time}\nURL:{current_url}\nError:{current_error}\n\{tb}\nCuurent Inputs:{current_input}\nUser:{current_user}".format(
                    current_time=current_date_time(),
                    current_url=request.build_absolute_uri(),
                    current_error=repr(e),
                    tb=traceback.format_exc(),
                    current_input=request,
                    current_user=None

        ))

        write_log_file(message)
        context['error_msg']="Something Went Wrong"
        # context['error_msg']=traceback.format_exc()
        return(render(request, 'error.html',context))  
    
