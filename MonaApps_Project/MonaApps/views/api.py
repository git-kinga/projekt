from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from MonaAppForm.models import MonitorRequest
from MonaApps.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.conf import settings
from django.utils import timezone
import os
import zipfile
from io import BytesIO
from django.core.files import File


@csrf_exempt
def api_config(request, user):
    
    if request.method == 'POST':
        print(request.headers.get('Authorization'))
        print(Token.objects.get(user__username=user).token)
        if request.headers.get('Authorization') == Token.objects.get(user__username=user).token:
        
            items = MonitorRequest.objects.all().filter(expire_date__gte=timezone.now()).filter(terminated=False)
            print(type(items))
            print(len(items))
            print(timezone.now())

        try:
            return JsonResponse({ item.id : [item.user.username, item.URL] for item in items})
        except:
            return JsonResponse({'error' : 'Unauthorized'}, status=401)

    else: return JsonResponse({'error': 'Invalid request method'}, status=405)
    

@login_required
def download_agent(request):
    token_object = Token.objects.get(user=request.user)
    agent = token_object.user.username
    token = token_object.token
    
    # Get the base directory name
    base_dir = 'telegraf-container'
    directory_path = os.path.join(settings.DOWNLOAD_PATH, base_dir)

    # Create a BytesIO object to hold the ZIP file in memory
    zip_buffer = BytesIO()

    # Create the ZIP file in memory
    with zipfile.ZipFile(zip_buffer, 'w') as zip_write:
        # Iterate over all the files in the directory and its subdirectories
        for root, _, files in os.walk(directory_path):
            for file in files:
                # Get the absolute path of the file
                file_path = os.path.join(root, file)

                # Open the file for reading
                with open(file_path, 'r') as f:
                    # Read the content of the file
                    content = f.read()

                    # Check if the current file is the desired file to modify
                    if file == 'docker-compose.yml':
                        # Modify the content by replacing the values
                        modified_content = content.replace('|>agent<|', agent).replace('|>token<|', token)
                    else:
                        # No modification required for other files
                        modified_content = content

                    # Get the relative path of the file within the directory
                    relative_path = os.path.relpath(file_path, directory_path)

                    # Add the modified or original file to the ZIP with the same relative path
                    zip_write.writestr(os.path.join(base_dir, relative_path), modified_content)

    # Set the position of the BytesIO object to the beginning
    zip_buffer.seek(0)

    # Prepare the response with the ZIP file
    file = File(zip_buffer, name='agent-app.zip')

    # Create the FileResponse with the wrapped file
    response = FileResponse(file, as_attachment=True)

    return response