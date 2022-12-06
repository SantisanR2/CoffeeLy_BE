from rest_framework import serializers
from authApp.models.fertilizacion import Fertilizacion

class FertilzacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Fertilizacion
        fields = ['relacion', 'fecha', 'lote', 'user']