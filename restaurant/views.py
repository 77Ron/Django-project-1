from http import HTTPStatus
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Meal, OrderTransaction

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

@login_required
def order(request, pk=None):
    if pk:
        got_meal=Meal.objects.filter(id=pk).last()
        if got_meal and got_meal.stock > 0:
            OrderTransaction.objects.create(
                meal=got_meal, customer=request.user, amount=got_meal.price)
            got_meal.stock -= 1
            got_meal.save()
            # return HttpResponse(f"HTTP Response: {HTTPStatus.CREATED}")
            return redirect('index')
        
    return HttpResponse(f"HTTP Response: {HTTPStatus.BAD_REQUEST}")

@login_required
def details(request):
    transactions = OrderTransaction.objects.filter(customer=request.user)

    context = {
        'transactions': transactions,
    }

    return render(request=request, template_name='restaurant/details.html', context=context)