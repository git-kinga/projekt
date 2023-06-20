from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('terminate/', views.terminate_url, name='terminate_url'),
]