from django.db import models
from .lote import Lote
from .user import User
from postgres_copy import CopyManager

class Siembra(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now=False)
    distancia = models.FloatField('Distancia')
    profundidad = models.FloatField('Profundidad')
    inclinacion = models.FloatField('Inclinacion')
    semilla = models.CharField('Semilla', max_length=50)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(User, related_name='Siembra', on_delete=models.CASCADE, blank=True) 

    objects = CopyManager()