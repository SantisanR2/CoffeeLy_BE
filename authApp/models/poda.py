from django.db import models
from .lote import Lote
from .user import User
from postgres_copy import CopyManager

class Poda(models.Model):
    fecha = models.DateTimeField('Fecha', auto_now=False)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Poda', on_delete=models.CASCADE)

    objects = CopyManager()