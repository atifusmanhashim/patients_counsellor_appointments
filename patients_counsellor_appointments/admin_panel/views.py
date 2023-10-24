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


from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth.models import update_last_login

# Create your views here.
@csrf_exempt
def index(request):
   if 'user_id' in request.session:
        return HttpResponseRedirect("dashboard")
   else:
        return HttpResponseRedirect("login")

@csrf_exempt
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
        return HttpResponseRedirect(reverse("login"))

@csrf_protect
def user_login(request):
    context={}
    template = loader.get_template('login.html') 
    if 'user_id' in request.session:
        return HttpResponseRedirect("dashboard")
    else:
        return HttpResponse(render(request, "login.html",context))

def logout(request):
    context={}
    if 'user_id' in request.session:
        del request.session['user_id']
    context['message_success']="You are logged out"
    return HttpResponseRedirect("login/")
       
    
