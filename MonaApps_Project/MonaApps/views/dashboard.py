from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from MonaAppForm.models import MonitorRequest
from django.utils import timezone
from django.db.models import Q

percent_encode = {
    # ':' :'%3A',
    # '/'	:'%2F',
    # '?'	:'%3F',
    # '#'	:'%23',
    # '['	:'%5B',
    # ']'	:'%5D',
    # '@'	:'%40',
    # '!'	:'%21',
    # '$'	:'%24',
    '&'	:'%26',
    # "'"	:'%27',
    # '('	:'%28',
    # ')'	:'%29',
    # '*'	:'%2A',
    '+'	:'%2B',
    # ','	:'%2C',
    # ';'	:'%3B',
    '='	:'%3D',
    # '%'	:'%25',
    # ' '	:'%20',
}

def format_url(string:str) -> str:
    for old, new in percent_encode.items():
        string = string.replace(old, new)
    print(string)
    return string 

@login_required
def dashboard(request):
    return render(request, 'Main_dashboard.html', {'user' : request.user.get_username()})

@login_required
def download_plugin (request):
    return render(request, 'Monitoring_agent.html')


@login_required
def renew_token (request):
    return render(request, 'Renew_your_token.html')

@login_required
def your_monitoring (request):
    urls = MonitorRequest.objects.filter(user__username = request.user.get_username())
    
    active_urls = urls.filter(expire_date__gte=timezone.now()).filter(terminated=False)
    finished_urls = urls.filter(Q(expire_date__lt=timezone.now()) | Q(terminated=True))
    
    active_urls_pair = [(x, format_url(x.URL)) for x in active_urls]  
    finished_urls_pair = [(x, format_url(x.URL)) for x in finished_urls]
    
    return render(request, 'Your_monitoring.html', {'user': request.user.get_username(), 'active_urls_pair':active_urls_pair, 'finished_urls_pair':finished_urls_pair})
