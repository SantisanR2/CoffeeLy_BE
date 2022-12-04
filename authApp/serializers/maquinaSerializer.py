from rest_framework import serializers
from authApp.models.maquina import Maquina

class MaquinaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = ['id','marca', 'modelo']