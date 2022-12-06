from django.db import models
from .lote import Lote
from .user import User
from postgres_copy import CopyManager

class Seleccion(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    defectuosos = models.FloatField('Defectuosos')
    defectos = models.CharField('Defectos', max_length=100)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Seleccion', on_delete=models.CASCADE, blank=True)

    objects = CopyManager()