from django.urls import path
from .views import api, login, dashboard


urlpatterns = [
    #path('', views.index, name='index'),
    #path('form/', views.form, name='form'),
    path('', login.login, name='login'),
    path('registration/', login.registration, name='registration'),
    path('logout/', login.sign_out, name='logout'),
    path('dashboard/', login.dashboard, name='dashboard'),
    path('dashboard/monitoring/', dashboard.monitoring, name='monitoring'),
    path('dashboard/plugin/', dashboard.download_plugin, name='plugin'),
    #api/config/ only for debug (it will be remover)
    path('api/config/<str:user>', api.api_config, name='api_config'),
    path('api/regenerate/', login.regenerate_token, name='regenerate_token'),
    path('api/download/', api.download_agent, name='download_agent'),
    
]