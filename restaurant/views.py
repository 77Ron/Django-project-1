from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse

from .models import Meal

# Create your views here.

def index(request):
    #Do something.
    if request.method == 'GET':
        cnt = 0
        # To store the meals.
        meals = []
        # To control the meals.
        temp_list =[]
        # Collect all the meals from the database.
        all_meals = Meal.objects.all()

        for cnt in range(all_meals.count()):
            # Append the meal to the temp list.
            temp_list.append(all_meals[cnt])

            # Append temp list to meals and reset it for every third meal/
            if (cnt + 1) % 3 == 0 and (cnt + 1)  > 2:
                meals.append(temp_list)
                temp_list = []
                
        # If we have lagging mmeals, just append tthem to meals.     
        if temp_list:
            meals.append(temp_list)

        context ={
            'meals' : meals,
        }
        
        #return HttpResponse(meals)
        return render(request=request, template_name='restaurant/index.html', 
                      context=context)
        
    #return HttpResponse(200)
    #return HttpResponse(f"HTTP Response: {HTTPStatus.OK}")
    return HttpResponse(f"HTTP Response: {HTTPStatus.BAD_REQUEST}")