from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import date 
import datetime
import random

colors = ["red", "yellow", "blue", "green", "purple"]

def index(request):
    today = datetime.datetime.now()
    color = "yellow"
    recent_name = Name.objects.last() #grabs most recent name  
    rand_color = random.randint(0, len(colors)-1)
    context = {
        "today": today,
        "color": color,
        "recent": recent_name,
        "color": rand_color,
    }
    return render(request, "index.html", context)

def profile(request):
    number_of_names = Name.objects.count()
    context = {
        "number":number_of_names,
    }
    return render(request, "profile.html", context)

def check_name(request):
    if 'name' in request.POST:
        name = request.POST['name']
        new_name = Name.objects.create(name = name)
    else:
        name = False
    return redirect('/home')

