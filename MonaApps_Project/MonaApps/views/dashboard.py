from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'Dashboard.html')

@login_required
def download_plugin (request):
    return render(request, 'Monitoring_agent.html')

@login_required
def monitoring (request):
    return render(request, 'Monitoring.html')

