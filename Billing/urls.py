from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/',getOrders),
    path('create-bill', create_bill, name='create-bill'),           # POST

]