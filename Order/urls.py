from django.urls import path
from .views import *

urlpatterns = [
    path("all/", get_all_orders),
    path("Items/", get_all_ordersItems),
    path('AddItem/',addItem),
    path('create/',create_Order)
]