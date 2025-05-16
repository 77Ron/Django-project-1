from django.contrib import admin
from .models import Meal

class MealAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "available",)
    search_fields = ("name", "description", "price")


# Register your models here.

admin.site.register(Meal, MealAdmin)