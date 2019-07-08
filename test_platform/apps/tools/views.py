#!usr/bin/env python
# -*- coding:utf-8
"""
M(操作数据)
T(模板) - view
V(视图) -Controller
"""
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from users.forms import   RegisterForm
from users.models import  UserProfile
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password


# Create your views here.

def toolslists(request):
    return  render(request,"tools_list.html")
