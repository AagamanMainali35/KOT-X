from channels.generic.websocket import WebsocketConsumer
from Order.serializer import *
from .models import Order
import json

# constants.py
class CloseCodes:
    """Custom close codes for your application"""
    
    # Authentication (4000-4099)
    AUTH_REQUIRED = 4000
    
    # Permission (4100-4199)
    NO_PERMISSION = 4100
    
    # Order related (4200-4299)
    ORDER_NOT_FOUND = 4200
    
    
    # Business logic (4400-4499)
    INSUFFICIENT_FUNDS = 4400
    ITEM_OUT_OF_STOCK = 4401
    QUANTITY_EXCEEDED = 4402
