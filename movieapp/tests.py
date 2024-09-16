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
        
    def test_filmes_lista(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['response']), 3)

    def test_filmes_search(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'), {'search': 'Ação'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['response']), 2)   

    def test_filmes_ordering_por_ano_de_lancamento(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'), {'ordering': 'ano_de_lancamento'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titulos_filmes = []
        for i in response.data['response']:
           titulos_filmes.append(i['titulo'])
        self.assertEqual(titulos_filmes, ['Filme 1', 'Filme 2', 'Filme 3'])    

    def test_filmes_ordering_por_titulo(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'), {'ordering': 'titulo'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titulos_filmes = []
        for i in response.data['response']:
           titulos_filmes.append(i['titulo'])
        self.assertEqual(titulos_filmes, ['Filme 1', 'Filme 2', 'Filme 3'])        

    def test_filmes_pagination(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'), {'page_size': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['response']), 2)    

    def test_filmes_pagination_com_page(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'), {'page_size': 2,'page':2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titulo_response = response.data['response'][0]['titulo']
        self.assertEqual(len(response.data['response']), 1,)
        self.assertEqual(titulo_response,'Filme 3')     

    def test_filmes_pagination_buscando_page_que_nao_existe(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('filmes'), {'page_size': 2,'page':3})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
           