from django.shortcuts import render, redirect # redirect() import 해주어야함
from django.contrib.auth.models import User # 유저 추가 기능
from django.contrib import auth # 계정 추가 기능
from .forms import AccountLogIn
from .models import Account

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = AccountLogIn(request.POST)
        if form.is_valid:
            if request.POST['pw1'] == request.POST['pw2']:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['pw1'])
                auth.login(request, user)            
                return redirect('home')
            else:
                return render(request, 'signupResult.html', {'error': 'password1 and password2 is different.'})
    else:
        form = AccountLogIn()
        return render(request, 'signup.html', {'form': form})    

def login(request):
    if request.method == 'POST':
        form = AccountLogIn(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['pw1']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'loginResult.html', {'error': 'username or password is incorrect.'})
    else:
        form = AccountLogIn()
        return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)        
        return redirect('home')        
        
    else:
        
        auth.logout(request)
        return redirect('home')
        