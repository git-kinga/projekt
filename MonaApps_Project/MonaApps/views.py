from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import LoginForm, RegistrationForm
from django.http import JsonResponse
#from .models import URL
from MonaAppForm.models import MonitorRequest

def MonaApps(request):
    return HttpResponse(request,"Hello world!")

def index(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'Monitoring_form.html')


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
            return redirect('/login')
        return render(request, 'registration.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def api_config(request):
    
    items = MonitorRequest.objects.all()
    urls_dict = {}
    
    
    
    return JsonResponse({ item.id : item.URL for item in items})