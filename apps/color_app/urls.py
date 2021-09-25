from django.conf.urls import url 
from django.urls import path 
from . import views           
urlpatterns = [
    # path('', views.api), #need to leave localhost for login/registration app
    path('home', views.index),    
]