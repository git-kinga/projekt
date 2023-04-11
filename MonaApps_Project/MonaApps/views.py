from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from .forms import MonitorForm

def MonaApps(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, 'index.html')

#@login_required
def form(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        print("after creating")
        if form.is_valid():
            print("Inside if")
            form.save(request.user)
            return redirect('/')
        else: 
            print("erorr views")
            for error in form.errors:
                messages.error(request, MonitorForm.errors[error])
            return redirect(request.path)
    else:
        form =MonitorForm()
    return render(request, 'Monitoring_form.html', {'form':form})