from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate  
from . import utility

class LoginSerializer(serializers.Serializer):
    password=serializers.CharField(write_only=True,error_messages={
        'required':'Password required',
        'blank': 'Password cannot be empty',
        'invalid':'Wrong Data_Type passed expected : (str->) ',
       
    })
    email=serializers.EmailField(error_messages={
        'required':"email Feild required",
        'blank':'email cant be empty',
        'invalid':'Invalid Email format'
    })
    class Meta:
        model=User
        fields="__all__"
            
    def login(self,validated_data):
        email=validated_data['email']
        password=validated_data['password']
        try:
            userObj=User.objects.get(email=email)  
            result=authenticate(username=userObj.username,password=password)
            if result:
                refresh = RefreshToken.for_user(result)

                payload={
                    "access_Token":f"{str(refresh.access_token)}",
                    "Refresh_Token":f"{str(refresh)}"                    
                }
                return payload
            else: 
                raise serializers.ValidationError('Invalid Credentials Provided')
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid Email Provided')
            