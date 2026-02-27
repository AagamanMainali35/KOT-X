from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({'msg':'OK and running'})

