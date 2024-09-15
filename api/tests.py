from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.urls import reverse

class TestesAutenticacao(APITestCase):

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


    def test_login_sucesso(self):
        response = self.client.post(reverse('login'), {'email': self.email, 'password': self.password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)