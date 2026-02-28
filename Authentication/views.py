import json
from rest_framework import status
from .serializer import LoginSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 

@api_view(['GET'])
def home(request):
    return Response({'msg':'OK and running'})

@api_view(['POST'])
def login_view(request):
    data=request.data
    serializer=LoginSerializer(data=data)
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
    



