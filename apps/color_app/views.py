from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response="This is the first message"
    return HttpResponse(response)
