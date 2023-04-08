from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MonitorForm

def MonaApps(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, 'index.html')

@login_required
def form(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('/')
    else:
        form =MonitorForm()
    return render(request, 'Monitoring_form.html')