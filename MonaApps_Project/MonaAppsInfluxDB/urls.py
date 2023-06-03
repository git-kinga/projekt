from django.urls import path
from . import views

urlpatterns = [
    path('get_tokens/', views.get_tokens, name='get_tokens'),
]