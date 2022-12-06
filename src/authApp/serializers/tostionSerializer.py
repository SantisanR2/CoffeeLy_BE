from rest_framework import serializers
from authApp.models.tostion import Tostion

class TostionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tostion
        fields = ['fecha', 'cantidadEntra', 'cantidadSale', 'tempInicio','temp1', 'temp2', 'tiempo1', 'tiempo2', 'tempPromedio', 'tiempoPromedio', 'aromas', 'agtron', 'lote', 'user', 'maquina']