from django.urls import path
from . import views

urlpatterns = [
    path('MonaApps/', views.MonaApps, name='MonaApps'),
]