from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse

from .models import Meal

# Create your views here.

def index(request):
    #Do something.
    if request.method == 'GET':
        meals = Meal.objects.all()
        
        #return HttpResponse(meals)
        return render(request=request, template_name='restaurant/index.html')
        
    #return HttpResponse(200)
    #return HttpResponse(f"HTTP Response: {HTTPStatus.OK}")
    return HttpResponse(f"HTTP Response: {HTTPStatus.BAD_REQUEST}")