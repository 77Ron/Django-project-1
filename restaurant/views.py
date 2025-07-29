from http import HTTPStatus
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Meal, OrderTransaction

from .forms import UserLoginForm

# Create your views here.

class IndexView(View):
    def get(self, request):
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
    

"""def index(request):
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
"""

class OrderView(View):
    def get(self, request, pk=None):
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

"""@login_required
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
"""

class DetailsView(ListView):
    context_object_name = 'transactions'
    #template_name = 'restaurant/details.html'

    def get_queryset(self):
        return OrderTransaction.objects.filter(customer=self.request.user)


"""class DetailsView(View):
    def get(self, request):
        transactions = OrderTransaction.objects.filter(customer=request.user)

        context = {
            'transactions': transactions,
        }

        return render(request=request, template_name='restaurant/details.html', context=context)
"""
"""@login_required
def details(request):
    transactions = OrderTransaction.objects.filter(customer=request.user)

    context = {
        'transactions': transactions,
    }

    return render(request=request, template_name='restaurant/details.html', context=context)
"""

class CustomLoginView(View):
    form_class = UserLoginForm
    template_name = 'restaurant/login.html'

    def get(self, request):
        form = self.form_class()
        form.fields['password'].widget.attrs['placeholder'] = 'Your Password'
        form.fields['password'].widget.attrs['Id'] = 'password_id'

        context = {
            'login_form': form,
         }
        return render(request=request, template_name=self.template_name, context = context)

    def post(self, request):
        form = self.form_class(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            authenticateUser = authenticate(request, username=username, password=password)

            if authenticateUser is not None:
                login(request, authenticateUser)

                return redirect('details')
            
            form.add_error('username', 'Wrong Username and Password!')
            form.add_error('password', 'Wrong Username and Password!')
            
            context = {
            'login_form': form,
            }

            return render(request=request, template_name=self.template_name, context = context)

"""class CustomLoginView(View):
    form_class = UserLoginForm
    template_name = 'restaurant/login.html'

    def get(self, request):
        form = self.form_class()
        form.fields['password'].widget.attrs['placeholder'] = 'Your Password'
        context = {
            'login_form': form,
         }
        return render(request=request, template_name=self.template_name, context = context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            authenticateUser = authenticate(request, username=username, password=password)

            if authenticateUser is not None:
                login(request, authenticateUser)

                return redirect('details')
            
            form.add_error('username', 'Wrong Username and Password!')
            form.add_error('password', 'Wrong Username and Password!')
            
            context = {
            'login_form': form,
            }

            return render(request=request, template_name=self.template_name, context = context)
"""

"""def login_user(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST, request.FILES)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            authenticateUser = authenticate(request, username=username, password=password)

            if authenticateUser is not None:
                login(request, authenticateUser)

                return redirect('details')
            
            login_form.add_error('username', 'Wrong Username and Password!')
            login_form.add_error('password', 'Wrong Username and Password!')
            
    else:
        login_form = UserLoginForm()
        login_form.fields['password'].widget.attrs['placeholder'] = 'Your Password'

    context = {
        'login_form': login_form,
    }
    return render(request=request, template_name='restaurant/login.html', context = context)
"""

def logout_user(request):
    logout(request)
    return redirect('index')
    
