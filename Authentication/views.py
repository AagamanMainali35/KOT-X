import json
from rest_framework import status
from .serializer import AuthSerializer , UserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.contrib.auth.models import User
from django.http import HttpResponse

@api_view(['GET'])
def home(request):
    return Response({'msg':'OK and running'})

@api_view(['POST'])
def login_view(request):
    data=request.data
    serializer=AuthSerializer(data=data)
    if serializer.is_valid():
        action=serializer.validated_data['action']
        print(action)
        if action=='login':
            payload=serializer.login(serializer.validated_data)
        if action=="register":
            payload=serializer.register(serializer.validated_data)
        response_data = {
        'data': payload,
        'success': True,
        'status_code': status.HTTP_202_ACCEPTED
    }
        return Response(response_data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'message':'Authentication Failed','error':serializer.errors,'status':f'{status.HTTP_401_UNAUTHORIZED}'},status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def get_user_byID(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user)
        return Response({
            "data":serializer.data,
            "status_code": status.HTTP_200_OK  
        }, status=status.HTTP_200_OK)
        
    except User.DoesNotExist:
        return Response({
            'message': "User Not Found",
            'status_code': status.HTTP_404_NOT_FOUND  
        }, status=status.HTTP_404_NOT_FOUND)    
        
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    if not users.exists():
        return Response({
            "data": [],
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": "No users found"
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(users, many=True)
    return Response({
        "data": serializer.data,
        "status_code": status.HTTP_200_OK
    }, status=status.HTTP_200_OK)