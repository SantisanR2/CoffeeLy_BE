from django.db import models
from postgres_copy import CopyManager

class Maquina(models.Model):
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)

    objects = CopyManager()
