from django.db import models
from .finca import Finca
from postgres_copy import CopyManager

class Lote(models.Model):
    cantidad = models.FloatField('Cantidad')
    estado = models.CharField('Estado', max_length=20, default='Siembra')
    estaCosechado = models.BooleanField('EstaCosechado', default=False)
    finca = models.ForeignKey(Finca, related_name='Lote', on_delete=models.CASCADE)

    objects = CopyManager()