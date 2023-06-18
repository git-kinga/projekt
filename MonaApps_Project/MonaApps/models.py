from django.db import models

class URL(models.Model):
    url = models.URLField(max_length=1000)
    class Meta:
        app_label = 'MonaApps'
