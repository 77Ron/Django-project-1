from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Meal

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
