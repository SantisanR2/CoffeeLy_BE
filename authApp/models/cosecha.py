from django.db import models
from .user import User
from .lote import Lote
from postgres_copy import CopyManager

class Cosecha(models.Model):
    fecha = models.DateTimeField('Fecha', auto_now=False)
    cantidad = models.FloatField('Masa')
    defectos = models.FloatField('Defectos')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE,blank=True)
    user = models.ForeignKey(User, related_name='Cosecha', on_delete=models.CASCADE, blank=True)

    objects = CopyManager()