from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from ..forms import LoginForm, RegistrationForm
from MonaApps.models import Token
from django.utils import timezone
from datetime import timedelta



def login(request):
     # Process login form submission
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print("### User logged ###")
                return redirect('/dashboard')
            else:
                error_message = "Invalid username or password."
                return redirect('/',{'error_message': error_message})
    else:
        print("### User not logged ###")
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            print(form.errors)
        if form.is_valid() and request.POST['agree'] == 'on':
            user = form.save()
            print("### User created ###")
            auth_login(request, user)
            return redirect('/')
        return render(request, 'registration.html', {'form': form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/')

@login_required
def regenerate_token(request):
    token = Token.objects.get(user=request.user)
    if token.generate_date <= timezone.now() - timedelta(minutes=5):
        token.save()
        return HttpResponse('<h1> New Token Generated </h1>')
    else: 
        return HttpResponse('<h1> Please Wait</h1>')

def dashboard(request):
    return render(request, 'dashboard.html')