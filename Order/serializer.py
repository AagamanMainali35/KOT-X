from rest_framework import serializers 
from .models import Order_Items,Order,Menu  

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order_Items
        fields="__all__"
        read_only_fields=["order_ins"]
        
    def to_representation(self, instance):
        data={
        "OrderItemID":instance.id,
        "Item": instance.order_items.item_name,
        "quantity": instance.quantity,
        "special_note": instance.special_note,
        }
        return data
            
class OrderSerializer(serializers.ModelSerializer):
    OrderItem=OrderItemSerializer(many=True) 
    class Meta:
        model=Order
        fields="__all__"
        
    def create(self, validated_data):
        print('from create')
        print(validated_data)
        items=validated_data.pop('OrderItem',[])
        Orders=Order.objects.create(table=validated_data['table'])
        for json in items:
            Order_Items.objects.create(order_ins=Orders,**json)
        return Orders
    
    def update(self, instance, validated_data):
        pass
    
        
    
        
    
        