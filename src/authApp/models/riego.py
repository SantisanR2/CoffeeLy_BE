from django.db import models
from .lote import Lote
from .user import User
from postgres_copy import CopyManager

class Riego(models.Model):
    fecha = models.DateTimeField('Fecha', auto_now=False)
    agua = models.FloatField('Agua')
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Riego', on_delete=models.CASCADE, blank=True)

    objects = CopyManager()