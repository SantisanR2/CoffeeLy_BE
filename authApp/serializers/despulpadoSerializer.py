from rest_framework import serializers
from authApp.models.despulpado import Despulpado

class DespulpadoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Despulpado
        fields = ['fechaInicio', 'fechaFinal', 'cantidadCafe', 'cantidadMucilago', 'cantidadAgua', 'lote', 'user', 'maquina']