from rest_framework import serializers
from authApp.models.lote import Lote

class LoteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id', 'cantidad', 'estado', 'estaCosechado','finca']