from rest_framework import serializers

from .models import *
from Tables.models import *

class BillingSerializer(serializers.ModelSerializer):
    """
    feilds:
    Order_ins = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="OrderObj"
    )
    Bill_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Billed_to = models.CharField(max_length=255)
    VAT = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    Discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    Billing_Date = models.DateTimeField(auto_now_add=True)

    payload={
        Order_ins =<ordre_id>,
        Billed_to = <Billing person name>
        Discount = <Discount percentage given>
    }
    """

    Order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), source="Order_ins"
    )
    Name = serializers.CharField(source="Billed_to")

    class Meta:
        model = Bill
        fields = ["Order_id", "Name", "Discount", "Bill_Total", "Billing_Date", "VAT"]
        read_only_fields = ["Bill_Total", "Billing_Date", "VAT"]

    def to_internal_value(self, data):
        extra_feilds = [key for key in data.keys() if key not in self.fields]
        if extra_feilds:
            raise serializers.ValidationError(
                {feild: "This field is not allowed." for feild in extra_feilds}
            )
        return super().to_internal_value(data)

    def to_representation(self, instance):
        """Convert string values to integers/decimals in the output"""
        data = {
            "Order_id": instance.Order_ins.id,
            "Name": instance.Billed_to,
            "Discount": float(instance.Discount),
            "Bill_Total": float(instance.Bill_Total),
            "VAT": float(instance.VAT),
            "Billing_Date": instance.Billing_Date.strftime("%d/%m/%Y %H:%M"),
            "discount_percentage": float(instance.Discount),
            "discounted_value": float(instance.Bill_Total),
        }
        return data

    def validate(self, attrs):
        error = {}
        for key, value in attrs.items():
            if value is None or isinstance(value, str) and value.strip() == "":
                error[key] = "Feild cannot have and Empty string"
        if error:
            raise serializers.ValidationError(error)
        return attrs

    def create(self, validated_data):
        oid = validated_data["Order_ins"]
        oid.table.status='AVAILABLE'
        oid.save()
        name = validated_data["Billed_to"]
        discount = int(validated_data["Discount"])
        vat = 13
        subtotal = 0
        total = 0
        items = oid.OrderItem.all()
        if items:
            for item in items:
                print(
                    f"{item.order_items.price}x{item.quantity}={item.order_items.price*item.quantity}"
                )
                subtotal += item.order_items.price * item.quantity

            if discount > 0:
                discountAmount = (subtotal * discount) / 100
                subtotal -= discountAmount
                subtotal += (subtotal * vat) / 100
        # NOTE: Append to total not subtotal after adding subtotal feild in DB
        else:
            raise serializers.ValidationError("No Items Ordered yet")

        Bill_obj = Bill.objects.create(
            Order_ins=oid, Billed_to=name, VAT=vat, Discount=discount, Bill_Total=total
        )
        return Bill_obj
