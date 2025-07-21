from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user

from .models import Meal
from .forms import UserLoginForm

# Create your tests here.

class MealModelTest(TestCase):
    @classmethod 
    def setUpTestData(cls):
        Meal.objects.create(
            name="Test Meal",
            description="This is a test meal.",
            price=20.23,
            available=True,
            stock=3
        )

    def test_meal_name(self):
        meal = Meal.objects.get(id=1)

        self.assertEqual(meal.name, 'Test Meal')
    
    def test_stock_count(self):
        meal = Meal.objects.get(id=1)

        self.assertEqual(meal.stock, 3)

class ViewsTest(TestCase):
    def test_index_view(self):
         response = self.client.get(reverse('index'))

         self.assertEqual(response.status_code, 200)

    def test_details_view(self):
        user = User.objects.create(username = "Test1")
        user.set_password('password')
        user.save()

        response = self.client.login(username = "Test1", password = 'password')

        self.assertTrue(response)

    def test_details_view_fails(self):
        user = User.objects.create(username = "Test1")
        user.set_password('password')
        user.save()

        response = self.client.login(username = "Test1", password = 'passwordfalse')

        self.assertFalse(response)

class FormsTest(TestCase):
    def test_login_form_user_name_is_required(self):
        form = UserLoginForm()

        self.assertTrue(form.fields['username'].required)

    def test_valid_login_form(self):
        User.objects.create(username = "Test3", password='password3')
        
        form = UserLoginForm(data={
            'username': "Test3", 
            'password':'password3'
        })

        self.assertTrue(form.is_valid())

        #self.assertEqual(User.objects.username, form.fields['username'])

class ClientTest(TestCase):
    def test_login(self):
        user = User.objects.create(username = "Test4")
        user.set_password('password4')
        user.save()

        c = Client()

        c.post('/login/',{
            'username': "Test4", 
            'password':'password4'
        })

        #self.assertTrue(get_user(c).is_authenticated)

        response = c.get(reverse('details'))
        self.assertEqual(response.status_code, 200)
