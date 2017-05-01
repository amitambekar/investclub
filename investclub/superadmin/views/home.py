# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
from libs.authentication import userLogin
from libs.helpers import mysql_connect,mysql_commit
# Create your views here.
@csrf_exempt
def login(request):
	username = None;
	if 'username' in request.POST:
		username = request.POST['username']
	password = None
	if 'password' in request.POST:
		password = request.POST['password']
	data = userLogin(request,username,password)
	return data

def index(request):
	return render(request, 'home/home.html',{'name':'Amit'})

def homepage(request):
	return render(request, 'home/home.html',{'name':'Amit'})