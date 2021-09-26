# auth0login\urls.py
from django.conf.urls import url, include
from django.urls import path 
from . import views     

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]