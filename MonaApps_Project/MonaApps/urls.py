from django.urls import path
from . import views
from .views import api_config

urlpatterns = [
    path('MonaApps/', views.MonaApps, name='MonaApps'),
    #path('', views.index, name='index'),
    #path('form/', views.form, name='form'),
    path('', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.sign_out, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #api/config/ only for debug (it will be remover)
    path('api/config/', views.api_config_old, name='api_config_old'),
    path('api/config/<str:user>', views.api_config, name='api_config'),
    path('api/regenerate/', views.regenerate_token, name='regenerate_token'),
    path('api/download/', views.download_agent, name='download_agent')
]