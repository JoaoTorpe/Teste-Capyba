from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=255)  
    genero = models.CharField(max_length=100)  
    premiado = models.BooleanField(default=False)  
    ano_de_lancamento = models.PositiveIntegerField()  

    def __str__(self):
        return self.titulo