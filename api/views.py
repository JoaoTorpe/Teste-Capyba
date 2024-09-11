
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['POST'])
def login(request):
    return Response({"login"})

@api_view(['POST'])
def register(request):
    ser = UserSerializer(data = request.data)

    if ser.is_valid():
        ser.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def validate_token(request):
    return Response({"validate"})