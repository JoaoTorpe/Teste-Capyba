from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta(object):

        model = User
        fields = ['id','username','password','email']

class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ['username','email']

#Serializers para configurar o OpenApi
class LoginSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

class RegisterSerializer(serializers.Serializer):
        unsername = serializers.CharField() 
        email = serializers.EmailField()
        password = serializers.CharField()

class ChangepassSerializer(serializers.Serializer):
        current_password = serializers.CharField() 
        new_password = serializers.CharField()
        