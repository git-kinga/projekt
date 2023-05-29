from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MonitorForm


@login_required
def form(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)
        print("after creating")
        if form.is_valid():
            print("Inside if")
            form.save(request.user)
            return redirect('../dashboard')
        else: 
            print("error views")
            for field in form.errors:
                print('errorField')
                for error in form.errors[field]:
                    messages.error(request, f'{field.capitalize()}: {error}', extra_tags='alert alert-danger')
                    print("Error css")
            return redirect(request.path)
    else:
        form =MonitorForm()
    return render(request, 'Monitoring_form.html', {'form':form})