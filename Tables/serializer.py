from .models import *
from rest_framework import serializers
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiningTable
        fields="__all__"
        extra_kwargs={
            "created_at":{
                "read_only":True
            }
        }
    