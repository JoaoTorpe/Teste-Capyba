from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.serializers import UserSerializer
from .models import Filme
from django.urls import reverse


class TestesFilmes(APITestCase):

    def setUp(self):
     self.username = 'test_user'
     self.email = 'test@email.com'
     self.password = 'test_pass'

     data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }
     ser = UserSerializer(data = data)

     if ser.is_valid():
        ser.save()
        self.user = User.objects.get(username=self.username)
        self.user.set_password(self.password)
        self.token, created = Token.objects.get_or_create(user=self.user)
        self.user.save()

     Filme.objects.create(titulo="Filme 1", genero="Ação", premiado=True, ano_de_lancamento=2020)
     Filme.objects.create(titulo="Filme 2", genero="Comédia", premiado=False, ano_de_lancamento=2021)
     Filme.objects.create(titulo="Filme 3", genero="Ação", premiado=True, ano_de_lancamento=2022)
        
    