from django.db import models
from .lote import Lote
from .user import User
from .maquina import Maquina
from postgres_copy import CopyManager

class Tostion(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    tempInicio = models.FloatField('TemperaturaInicial')
    temp1 = models.FloatField('TemperaturaCrack1')
    temp2 = models.FloatField('TemperaturaCrack2')
    tiempo1 = models.FloatField('TiempoCrack1')
    tiempo2 = models.FloatField('TiempoCrack2')
    tempPromedio = models.FloatField('TemperaturaPromedio')
    tiempoPromedio = models.FloatField('TiempoPromedio')
    aromas = models.CharField('Aromas', max_length=500)
    agtron = models.FloatField('Agtron')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Tostion', on_delete=models.CASCADE, blank=True)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, blank=True, default=0)

    objects = CopyManager()