from django.shortcuts import render, HttpResponse, redirect
from datetime import date 

def index(request):
    today = date.today()
    context = {
        "today": today,
    }
    return render(request, "index.html", context)

def profile(request):
    return render(request, "profile.html")

