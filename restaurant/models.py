from django.db import models

# Create your models here.
class Meal(models.Model):
    # Name of the meal.
    name = models.CharField("Name of the Meal", max_length=100)
    # Description of the meal.
    description = models.TextField("Description of the Meal", blank=True, null=True)
    # Store the meal price.
    price = models.DecimalField("Price (£)", max_digits=10, decimal_places=2)
    # Availability of the meal.
    available = models.BooleanField("Online Availability", default=False)
    # Stock count.
    stock = models.IntegerField("Stock Count", default=0)

    def __str__(self):
        return f'{self.description}'