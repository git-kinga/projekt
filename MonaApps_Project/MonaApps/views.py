from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.http import JsonResponse
from MonaAppForm.models import MonitorRequest
from MonaApps.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
from django.http import FileResponse
from django.conf import settings
import os
import zipfile

def MonaApps(request):
    return HttpResponse(request,"Hello world!")

# def index(request):
#     return render(request, 'index.html')

# def form(request):
#     return render(request, 'Monitoring_form.html')


def login(request):
     # Process login form submission
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print("### User logged ###")
                return redirect('/dashboard')
            else:
                error_message = "Invalid username or password."
                return redirect('/',{'error_message': error_message})
    else:
        print("### User not logged ###")
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            print(form.errors)
        if form.is_valid() and request.POST['agree'] == 'on':
            user = form.save()
            print("### User created ###")
            auth_login(request, user)
            return redirect('/')
        return render(request, 'registration.html', {'form': form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/')

def dashboard(request):
    return render(request, 'dashboard.html')

def api_config_old(request):
    items = MonitorRequest.objects.all()
    return JsonResponse({ item.id : item.URL for item in items})

@csrf_exempt
def api_config(request, user):
    
    if request.method == 'POST':
        if request.headers.get('Authorization') == Token.objects.get(user__username=user).token:
        
            items = MonitorRequest.objects.all()
            return JsonResponse({ item.id : [item.user.username, item.URL] for item in items})

        else: return JsonResponse({'error' : 'Unauthorized'}, status=401)
    else: return JsonResponse({'error': 'Invalid request method'}, status=405)
    
@login_required
def regenerate_token(request):
    token = Token.objects.get(user=request.user)
    if token.generate_date <= timezone.now() - timedelta(minutes=5):
        token.save()
        return HttpResponse('<h1> New Token Generated </h1>')
    else: 
        return HttpResponse('<h1> Please Wait</h1>')


#                   NOT COMPLETED                       #
# @login_required
# def download_agent(request):
#     token_object = Token.objects.get(user=request.user)
#     agent = token_object.user.username
#     token = token_object.token
    
    
#     # Get the base directory name
#     base_dir = 'telegraf-container'
#     directory_path = os.path.join(settings.DOWNLOAD_PATH, base_dir)

#     # Create a temporary zip file to store the zipped directory
#     temp_zip_path = os.path.join(directory_path, 'temp.zip')

#     # Open the temporary zip file for writing
#     with zipfile.ZipFile(temp_zip_path, 'w') as zip_write:
#         # Iterate over all the files in the directory and its subdirectories
#         for root, _, files in os.walk(directory_path):
#             for file in files:
#                 # Get the absolute path of the file
#                 file_path = os.path.join(root, file)

#                 # Open the file for reading
#                 with open(file_path, 'r') as f:
#                     # Read the content of the file
#                     content = f.read()

#                     # Check if the current file is the desired file to modify
#                     if file == 'docker-compose.yml':
#                         # Modify the content by replacing the values
#                         modified_content = content.replace('|>agent<|', agent).replace('|>token<|', token)
#                     else:
#                         # No modification required for other files
#                         modified_content = content

#                     # Get the relative path of the file within the directory
#                     relative_path = os.path.relpath(file_path, directory_path)

#                     # Add the modified or original file to the zip with the same relative path
#                     zip_write.writestr(os.path.join(base_dir, relative_path), modified_content)

#     response = FileResponse(open(temp_zip_path, 'rb'), as_attachment=True, filename='agent-app.zip')
    

#     return response