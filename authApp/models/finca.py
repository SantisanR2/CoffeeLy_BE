from django.db import models
from postgres_copy import CopyManager

class Finca(models.Model):
    nombre = models.CharField('Nombre', max_length = 50)
    ubicacion = models.CharField('Ubicacion', max_length = 200)
    altitud = models.FloatField('Altitud')
    clima = models.CharField('Clima', max_length= 30)
    inclinacion = models.FloatField('Inclinacion')
    lumenes = models.FloatField('Lumenes')
    coordenadas = models.CharField('Coordenadas', max_length=50)
    tierra = models.CharField('Tierra', max_length=40)
    ph = models.FloatField('pH')
    cultivos = models.CharField('Cultivos', max_length=500)
    microorganismos = models.CharField('Microorganismos', max_length=500)

    objects = CopyManager()