import os
import django
import random
from decimal import Decimal
from faker import Faker

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KOT.settings")
django.setup()

from Order.models import Menu, Order, Order_Tracker, Bill
from Tables.models import DiningTable

fake = Faker()

# 1️⃣ Create Menu items
dishes = [
    "Margherita Pizza", "Veggie Burger", "Chicken Burger", "Pasta Carbonara",
    "Caesar Salad", "Sushi Roll", "Tacos", "Grilled Sandwich",
    "Tomato Soup", "Chocolate Cake"
]

menu_items = []
for _ in range(10):
    item = Menu.objects.create(
        item_name=random.choice(dishes),  # pick from manual list
        price=round(random.uniform(50, 500), 2),
        is_available=random.choice([True, True, True, False]),
        item_picture="menuItems/placeholder.jpg"
    )
    menu_items.append(item)

print("Menu items created:", len(menu_items))

# 2️⃣ Create DiningTables if not existing
tables = DiningTable.objects.all()
if not tables.exists():
    for i in range(1, 6):
        DiningTable.objects.create(table_name=f"Table {i}")
    tables = DiningTable.objects.all()

# 3️⃣ Create Orders + Order_Tracker
orders = []
for _ in range(5):
    table = random.choice(tables)
    order = Order.objects.create(table=table)
    orders.append(order)

    for _ in range(random.randint(1, 5)):
        menu_item = random.choice(menu_items)
        quantity = random.randint(1, 3)
        Order_Tracker.objects.create(
            order_items=menu_item,
            quantity=quantity,
            special_note=fake.sentence(nb_words=6),
            order_ins=order
        )

print("Orders + Order_Tracker created:", len(orders))

# 4️⃣ Create Bills
for order in orders:
    order_items = order.OrderItem.all()
    subtotal = sum(item.order_items.price * item.quantity for item in order_items)
    vat = subtotal * Decimal("0.05")
    discount = subtotal * Decimal(random.choice([0, 0.1, 0.15]))
    total = subtotal + vat - discount

    Bill.objects.create(
        Order_ins=order,
        Bill_Total=round(total, 2),
        Billed_to=fake.name(),
        VAT=round(vat, 2),
        Discount=round(discount, 2)
    )

print("Bills created successfully!")