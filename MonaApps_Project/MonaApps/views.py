from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages

def MonaApps(request):
    return HttpResponse("Hello world!")

def index(request):
    return render(request, 'index.html')
