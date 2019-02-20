from django.shortcuts import render, redirect # redirect() import 해주어야함
from django.contrib.auth.models import User # 유저 추가 기능
from django.contrib import auth # 계정 추가 기능
from accounts import views

def basehtml(request):    
    loginUserName = auth.get_user(request)
    loginUserName = loginUserName.get_username    
    
    return {'loginUserName': loginUserName}
    