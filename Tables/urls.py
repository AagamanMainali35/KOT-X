from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.get_all_tables, name='get_all_tables'),          # GET all tables
    path('tables/<int:pk>/', views.get_table_by_id, name='get_table_by_id'), # GET table by ID
    path('tables/<int:pk>/update/', views.update_table, name='update_table'), # PUT update table by ID
    path('tables/create/', views.create_table, name='create_table'),       # POST create new table
]