from django.urls import path
from .views import*

urlpatterns = [
    path('login/',login_view,name='login_view'),                 # GET:  Login for Staff
    path('list/', get_all_users, name='get_all_users'),          # GET:  all users
    path('get/<int:pk>/', get_user_byID, name='get_user_byID'),  # GET:  Single user by ID
    path('update/<int:pk>',update_user,name='update_user')       # PATCH: User data and his/her profile      
]