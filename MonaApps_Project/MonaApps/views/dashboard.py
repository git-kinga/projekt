from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def download_plugin (request):
    return render(request, 'Telegraf_plugin.html')

@login_required
def monitoring (request):
    return render(request, 'Monitoring.html')

