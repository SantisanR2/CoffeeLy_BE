from django.db import models
from .lote import Lote
from .user import User

class Catacion(models.Model):
    fecha = models.DateField('Fecha',auto_now=False)
    tiempo1 = models.FloatField('Tiempo1')
    temp1 = models.FloatField('Temperatura1')
    tiempo2 = models.FloatField('Tiempo2')
    temp2 = models.FloatField('Temperatura2')
    tiempo3 = models.FloatField('Tiempo3')
    temp3 = models.FloatField('Temperatura3')
    puntaje = models.FloatField('Puntaje')
    tabla = models.FileField(upload_to='docs/', max_length=254)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Catacion', on_delete=models.CASCADE, blank=True)