from django.urls import path
from .views import api, login, dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('form/', views.form, name='form'),
    path('', login.login, name='login'),
    path('registration/', login.registration, name='registration'),
    path('logout/', login.sign_out, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('dashboard/', dashboard.dashboard, name='dashboard'),
    path('dashboard/monitoring/', dashboard.your_monitoring, name='your_monitoring'),
    path('dashboard/plugin/', dashboard.download_plugin, name='plugin'),
    path('dashboard/renew/', dashboard.renew_token, name='renew_token'),

    path('api/config/<str:user>', api.api_config, name='api_config'),
    path('api/regenerate/', login.regenerate_token, name='regenerate_token'),
    path('api/download/', api.download_agent, name='download_agent'),
    
]