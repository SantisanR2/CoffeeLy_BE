from rest_framework import serializers
from authApp.models.cosecha import Cosecha

class CosechaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cosecha
        fields = ['fecha', 'cantidad', 'defectos', 'lote', 'user']