from django.urls import path
from .views  import index, order

urlpatterns = [
    path('', index, name='index'),
    path('order/<int:pk>', order, name='order'),
]
