from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MonitorRequest(models.Model):
    URL = models.CharField(max_length=200)
    interval = models.SmallIntegerField(default="1")
    notification = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    date = models.DateTimeField()

    def __str__(self):
        return f'URL: {self.URL} User: {self.user}'