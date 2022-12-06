from rest_framework import serializers
from authApp.models.catacion import Catacion

class CatacionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Catacion
        fields = ['fecha', 'tiempo1', 'temp1', 'tiempo2', 'temp2', 'tiempo3', 'temp3', 'puntaje', 'tabla', 'lote', 'user']