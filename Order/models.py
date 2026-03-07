from django.db import models
from Tables.models import DiningTable
from django.contrib.auth.models import User

class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    item_picture=models.ImageField(upload_to='menuItems/')
    
    def __str__(self):
        return self.item_name

class Order_Tracker(models.Model):
    order_items=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    special_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"KOT {self.order_items.item_name} x {self.quantity}"

    
class Order(models.Model):
    table = models.ForeignKey(DiningTable, on_delete=models.CASCADE, related_name='orders')
    order_items=models.ForeignKey(Order_Tracker,on_delete=models.CASCADE,related_name='OrderItem')
    def __str__(self):
        return f"Order for Table {self.table.table_name}"
    

class Bill(models.Model):
    Order_ins = models.ForeignKey(Order, on_delete=models.CASCADE)
    Bill_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Billed_to = models.CharField(max_length=255)
    VAT = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    Discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    Billing_Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Bill for {self.Billed_to} - Rs . {self.Bill_Total}"