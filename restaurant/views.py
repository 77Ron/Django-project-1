from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    #Do something.
    #return HttpResponse(200)
    return HttpResponse(f"HTTP Response: {HTTPStatus.OK}")