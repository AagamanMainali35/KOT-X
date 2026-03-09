from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order , Order_Items
from rest_framework import status
from .serializer import OrderSerializer , OrderItemSerializer

@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.prefetch_related("OrderItem").all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_ordersItems(request):
    orders = Order_Items.objects.all()
    serializer = OrderItemSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer=OrderItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message':'Item Added Sucessfully','data':serializer.data,'status':status.HTTP_201_CREATED})

@api_view(['POST'])
def create_Order(request):
    print(request.data)
    print('from view')
    OrderData=OrderSerializer(data=request.data)
    OrderData.is_valid(raise_exception=True)
    OrderData.save()
    return Response({'message':'Order Added','status':status.HTTP_201_CREATED})
