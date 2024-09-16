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

    def test_login_falha(self):
        response = self.client.post(reverse('login'), {'email': self.email, 'password': 'senhaerrada'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)   

    def test_register_sucesso(self):
       response = self.client.post(reverse('register'),{'username':'novo_user','email':'user@hotmail.com','password':'senha'})
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)    

    def test_register_falha_falta_atributos(self):
       response =  self.client.post(reverse('register'),{'password':'senha'})  
       self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_falha_senha_atual_incorreta(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('changepass'),{"current_password":"senhaerrada","new_password":"1234"})
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_change_password_sucesso(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('changepass'),{"current_password":self.password,"new_password":"1234"})
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_user_data_sucesso(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.put(reverse('updatedata'), {'username': 'novonome', 'email': 'novo@email.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'novonome')
        self.assertEqual(self.user.email, 'novo@email.com')

    def test_logout_sucesso(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logout_falha_token_invalido(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'tokeninvalido')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)