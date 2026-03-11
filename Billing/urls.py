from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/',getOrders),
    path('create_bill', create_bill, name='create-bill'),           # POST

]