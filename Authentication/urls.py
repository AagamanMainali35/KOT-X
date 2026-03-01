from django.urls import path
from .views import get_user_byID, get_all_users,login_view

urlpatterns = [
    path('login/',login_view,name='login_view'), # Login for Staff
    path('users/', get_all_users, name='get_all_users'),           # GET all users
    path('users/<int:pk>/', get_user_byID, name='get_user_byID'),  # GET single user by ID
]