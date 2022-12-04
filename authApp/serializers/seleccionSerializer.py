from rest_framework import serializers
from authApp.models.seleccion import Seleccion

class SeleccionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Seleccion
        fields = ['fecha', 'cantidadEntra', 'cantidadSale', 'defectuosos', 'defectos','lote', 'user']