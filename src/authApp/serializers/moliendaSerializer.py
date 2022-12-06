from rest_framework import serializers
from authApp.models.molienda import Molienda

class MoliendaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Molienda
        fields = ['fechaInicio', 'fechaFinal','cantidadEntra', 'cantidadSale', 'cisco', 'factor','lote', 'user', 'maquina']