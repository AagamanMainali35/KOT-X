from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('owner', 'Owner'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('chef', 'Chef'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} ({self.role})"
    
class DiningTable(models.Model):
    
    table_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_name

class Order(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('billed', 'Billed'),
        ('closed', 'Closed'),
    ]

    table = models.ForeignKey(DiningTable, on_delete=models.CASCADE, related_name='orders')
    opened_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='opened_orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - Table {self.table.table_name}"
    
class Order_Tracker(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('served', 'Served'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='kots')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_kots')
    special_note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='sent')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"KOT {self.id} for Order {self.order.id}"
    

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name