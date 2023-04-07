from django.shortcuts import render
from django.http import HttpResponse

def MonaApps(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, 'index.html')

def form(request):
    return render(request, 'Monitoring_form.html')