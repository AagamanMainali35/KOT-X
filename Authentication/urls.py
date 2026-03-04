from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login_view'), # GET:  Login for Staff
    path('list/', views.get_all_users, name='get_all_users'), # GET:  all users
    path('get/<int:pk>/', views.get_user_byID, name='get_user_byID'), # GET:  Single user by ID
    path('update/<int:pk>',views.update_user,name='update_user') ,   # PATCH: update user data partially
    path('tables/', views.get_all_tables, name='get_all_tables'), # GET all tables
    path('tables/<int:pk>/', views.get_table_by_id, name='get_table_by_id'), # GET table by ID
    path('tables/<int:pk>/update/', views.update_table, name='update_table'), # PUT update table by ID
    path('tables/create/', views.create_table, name='create_table'),       # POST create new table# PATCH: User data and his/her profile      
]