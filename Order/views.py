from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DiningTable, Order, Order_Items
from .serializer import OrderItemSerializer, OrderSerializer


@api_view(["GET"])
def get_order(request, id):
    try:
        table = DiningTable.objects.get(id=id)
        orders = table.orderTable
        serializer = OrderSerializer(orders)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response(
            {"data": f"Order not found", "status": status.HTTP_404_NOT_FOUND},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
def get_all_orders(request):
    orders = Order.objects.prefetch_related("OrderItem").all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_all_ordersItems(request):
    orders = Order_Items.objects.all()
    serializer = OrderItemSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addItem(request):
    print(request.data)
    serializer = OrderItemSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        {
            "message": "Item Added Sucessfully",
            "data": serializer.data,
            "status": status.HTTP_201_CREATED,
        }
    )

@api_view(["POST"])
def create_Order(request):
    print("from view")
    OrderData = OrderSerializer(data=request.data)
    OrderData.is_valid(raise_exception=True)
    OrderData.save()
    return Response({"message": "Order Added", "status": status.HTTP_201_CREATED})


@api_view(["PATCH"])
def update_Order(request, pk):
    Order_Data = Order.objects.get(id=pk)
    serializer = OrderSerializer(data=request.data, instance=Order_Data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
