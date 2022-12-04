from django.db import models
from .lote import Lote
from .user import User
from .maquina import Maquina
from postgres_copy import CopyManager

class Fermentacion(models.Model):
    fechaInicio = models.DateTimeField('FechaInicial',auto_now=False)
    fechaFinal = models.DateTimeField('FechaFinal',auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    tempAmb = models.FloatField('TemperaturaAmbiente')
    tempGrano = models.FloatField('TemperaturaGrano')
    brix = models.FloatField('Brix')
    ph = models.FloatField('pH')
    cantidadAgua = models.FloatField('CantidadAgua')
    tipo = models.CharField('Tipo', max_length=100)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Fermentacion', on_delete=models.CASCADE, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, blank=True, default=0)

    objects = CopyManager()