from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MonitorForm
from .models import MonitorRequest


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
    return render(request, 'New_monitoring_service.html', {'form':form})

@login_required
def terminate_url(request):
    if request.method == 'POST':
        url_id = request.POST.get('url_id')
        try:
            url_obj = MonitorRequest.objects.get(id=url_id)
            url_obj.terminated = True
            url_obj.save()
            return redirect('your_monitoring')
        except MonitorRequest.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'URL not found.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

       