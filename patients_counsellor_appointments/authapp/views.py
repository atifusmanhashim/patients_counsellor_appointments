from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, views, generics, response, permissions, authentication
from rest_framework.authtoken.views import ObtainAuthToken  #for Getting Neew Token
from rest_framework.parsers import JSONParser

from django.contrib.auth import get_user_model  # Using for user default model
from django.contrib.auth import authenticate    #Using for Login
from rest_framework.permissions import IsAuthenticated  #for using Authenication of User
from rest_framework.decorators import api_view, permission_classes
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth.models import update_last_login

from collections import namedtuple

from django.db import IntegrityError
from requests.exceptions import HTTPError
from django.shortcuts import render, HttpResponse
from django.db.models import Q
from django.http import HttpRequest

Settings
from django.conf import settings

# Used for Timezone / Datetime
from django.utils import timezone
from datetime import datetime, date, timedelta
import datetime

import base64

#Used for Math Functions
import math

from .models import (AppUser, UserRole, LoginAnalytics)


