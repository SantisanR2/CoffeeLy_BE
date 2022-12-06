from rest_framework import serializers
from authApp.models.lavado import Lavado

class LavadoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lavado
        fields = ['fechaInicio', 'fechaFinal', 'cantidadEntra', 'cantidadSale', 'cantidadAgua', 'lote', 'user', 'maquina']