from django import forms
from django.core.validators import URLValidator
from django.utils import timezone
from .models import MonitorRequest

class MonitorForm(forms.Form):
    websiteURL = forms.CharField(label='Website URL', max_length=200)

    def clean_url(self):
        url = self.cleaned_data['url']
        validate_url = URLValidator()
        try:
            validate_url(url)
        except:
            raise forms.ValidationError('Invalid URL')
        return url
    
    def save(self, user):
        url = self.cleaned_data['url']
        current_time = timezone.now()
        url_obj = MonitorRequest(user=user, url=url, date=current_time)
        url_obj.save()
        return url_obj