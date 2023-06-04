from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from MonaApps.models import Token
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def get_tokens(request):
    if request.method == 'POST':
        print(request.headers.get('Authorization'))
        print(settings.INFLUXDB_TOKEN)
        if request.headers.get('Authorization') == settings.INFLUXDB_TOKEN:

            users = Token.objects.all().values('user__username', 'token')
            users_tokens = {user['user__username'] : user['token'] for user in users}
            
            return JsonResponse(users_tokens)
        
        else: return JsonResponse({'error' : 'Unauthorized'}, status=401)
        
    else: return JsonResponse({'error': 'Invalid request method'}, status=405)