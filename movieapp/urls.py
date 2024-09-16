from django.urls import path 
from . import views
urlpatterns = [
  path("filmes",views.filmes,name='filmes')
]