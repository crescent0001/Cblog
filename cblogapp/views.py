from django.shortcuts import render
from django.urls import path

# Create your views here.
def myView(request):
    return HttpResponse("hello, World!")