from django.db import models
from .lote import Lote
from .user import User
from postgres_copy import CopyManager

class Fertilizacion(models.Model):
    relacion = models.FloatField('Relacion')
    fecha = models.DateTimeField('Fecha', auto_now = False)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Fertilizacion',on_delete=models.CASCADE, blank=True)

    objects = CopyManager()