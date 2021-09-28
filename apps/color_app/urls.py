from django.conf.urls import url 
from django.urls import path 
from . import views           
urlpatterns = [
    # path('', views.api), #need to leave localhost for login/registration app
    path('index', views.index),   
    path('dashboard', views.profile),    
    path('check_name', views.check_name),
    path('logged_out', views.logout),
]