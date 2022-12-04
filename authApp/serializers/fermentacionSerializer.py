from rest_framework import serializers
from authApp.models.fermentacion import Fermentacion

class FermentacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Fermentacion
        fields = ['fechaInicio', 'fechaFinal', 'cantidadEntra', 'cantidadSale', 'tempAmb', 'tempGrano', 'brix', 'ph', 'cantidadAgua', 'tipo', 'lote', 'user', 'maquina']