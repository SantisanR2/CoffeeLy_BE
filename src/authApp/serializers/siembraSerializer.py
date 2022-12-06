from rest_framework import serializers
from authApp.models.siembra import Siembra

class SiembraSerializer (serializers.ModelSerializer):
    class Meta:
        model = Siembra
        fields = ['fecha', 'distancia', 'profundidad', 'inclinacion', 'semilla', 'lote', 'user']