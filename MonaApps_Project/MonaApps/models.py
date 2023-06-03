from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from .token_generator import token_generator

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=32, validators=[MinLengthValidator(32)])
    old_tokens = models.TextField(blank=True)
    
    def __str__(self):
        return self.token
    
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = token_generator(32)
        else:
            self.old_tokens = ','.join([old_tokens, self.token])
            
        all_old_tokens = Token.objects.values_list('old_tokens', flat=True)
        old_tokens = set(','.join(all_old_tokens).split(',')) if all_old_tokens else set()    
            
        while Token.objects.filter(token=self.token).exists() or self.token in old_tokens:
            self.token = token_generator(32)
        
        super().save(*args, **kwargs)
        
        
        
        