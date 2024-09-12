
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  TokenAuthentication
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,username=request.data['username'])

    if user.check_password(request.data['password']):
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token":token.key})


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
@permission_classes([IsAuthenticated])
def logout(request):
   try:
       token = Token.objects.get(user=request.user)
       
       token.delete()
       return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)
   except Token.DoesNotExist:
       return Response({"detail": "Token não encontrado."}, status=status.HTTP_400_BAD_REQUEST)
   
