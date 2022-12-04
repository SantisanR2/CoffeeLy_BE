from rest_framework import serializers
from authApp.models.secado import Secado

class SecadoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Secado
        fields = ['fechaInicio', 'fechaFinal', 'tempAmb', 'tempGrano', 'humedad', 'densidad', 'lote', 'user', 'maquina']