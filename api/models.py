from django.db import models

GENERO_CHOICES = [
    ('DRAMA' , 'DRAMA'),
    ('COMEDIA' , 'COMEDIA'),
]

class Filme (models.Model):
    nome = models.CharField()
    genero = models.CharField(choices=GENERO_CHOICES)
    ano = models.PositiveIntegerField
    duracao = models.PositiveIntegerField
# Create your models here.
