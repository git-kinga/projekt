from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'Main_dashboard.html')

@login_required
def download_plugin (request):
    return render(request, 'Monitoring_agent.html')

@login_required
def your_monitoring (request):
    return render(request, 'Your_monitoring.html')

@login_required
def renew_token (request):
    return render(request, 'Renew_your_token.html')