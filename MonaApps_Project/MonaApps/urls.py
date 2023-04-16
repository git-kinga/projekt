from django.urls import path
from . import views

urlpatterns = [
    path('MonaApps/', views.MonaApps, name='MonaApps'),
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('login/', views.login, name='login')
]