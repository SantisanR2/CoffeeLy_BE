from django.db import models
from .lote import Lote
from .user import User
from .maquina import Maquina
from postgres_copy import CopyManager

class Despulpado(models.Model):
    fechaInicio = models.DateTimeField('FechaInicial',auto_now = False)
    fechaFinal = models.DateTimeField('FechaFinal',auto_now = False)
    cantidadCafe = models.FloatField('CantidadCafe')
    cantidadMucilago = models.FloatField('CantidadMucilago')
    cantidadAgua = models.FloatField('CantidadAgua')
    lote = models.OneToOneField(Lote, on_delete = models.CASCADE, blank = True)
    user = models.ForeignKey(User, related_name='Despulpado', on_delete = models.CASCADE, blank = True)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, blank=True, default=0)

    objects = CopyManager()