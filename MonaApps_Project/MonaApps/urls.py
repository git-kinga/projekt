from django.urls import path
from . import views
from .views import api_config

urlpatterns = [
    path('', views.MonaApps, name='MonaApps'),
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/config/', views.api_config, name='api_config')
]