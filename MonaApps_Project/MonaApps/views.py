from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import MonitorForm

def MonaApps(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, 'index.html')

#@login_required
def form(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        try:
            print(form.is_valid())
            if form.is_valid():
                print("Inside if")
                form.save(request.user)
                return redirect('/')
        except forms.ValidationError as e:
            print("erorr views")
            form.add_error('websiteURL', e.get_messages()[0])
            return render(request, 'Monitoring_form.html', {'form':form})
        else:
            print("else")
            return redirect('/')

    else:
        form =MonitorForm()
    return render(request, 'Monitoring_form.html', {'form':form})