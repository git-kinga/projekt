from django import forms
from django.core.validators import URLValidator
from django.utils import timezone
from .models import MonitorRequest

class MonitorForm(forms.ModelForm):    
    class Meta:
        model = MonitorRequest
        fields = ['URL']
        widgets = {'interval':forms.Select(choices=((1, 1), (2, 2), (3, 3)))}
        labels = {
            'URL':'Monitor to service',
            'interval':'Interval',
            'notification':'Get an email notification if the service is not available'
        }
        
    
    def clean_URL(self):
        url = self.cleaned_data['URL']
        print(url)
        new_url = None
        if not url.startswith('http'):
            print('here')
            new_url = 'http://' + url
            print(new_url)
        try:
            validate_url = URLValidator()
            if new_url: validate_url(new_url) 
            else: validate_url(url)
            print("Valid")
        except:
            print("Invalid")
            raise forms.ValidationError('Invalid URL')
        return url
    
    def save(self, user):
        url = self.cleaned_data['URL']
        current_time = timezone.now()
        url_obj = MonitorRequest(user=user, URL=url, date=current_time)
        url_obj.save()
        return url_obj