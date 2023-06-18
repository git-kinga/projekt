from django import forms
from django.core.validators import URLValidator
from django.utils import timezone
from .models import MonitorRequest

class MonitorForm(forms.ModelForm):    
    class Meta:
        model = MonitorRequest
        fields = ['URL', 'expire_date']
        widgets = {
            'interval':forms.Select(choices=((1, 1), (2, 2), (3, 3))),
            'expire_date':forms.DateTimeInput(attrs={'type': 'datetime-local'})
                   }
        labels = {
            'URL':'Monitor to service',
            'interval':'Interval',
            'notification':'Get an email notification if the service is not available',
            'expire_date': 'Monitoring due date'
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
    
    def clean_expire_date(self):
        expire_date = self.cleaned_data['expire_date']
        if expire_date <= timezone.now() + timezone.timedelta(days=1):
            raise forms.ValidationError('The date must be min 1 day future')
        return expire_date
            
    
    def save(self, user):
        url = self.cleaned_data['URL']
        expire_date = self.cleaned_data['expire_date']
        current_time = timezone.now()
        instance = MonitorRequest(user=user, URL=url, expire_date=expire_date, date=current_time)
        instance.save()
        return instance