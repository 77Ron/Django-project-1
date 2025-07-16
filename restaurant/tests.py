from django.test import TestCase

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
