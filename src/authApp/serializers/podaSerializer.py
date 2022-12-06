from rest_framework import serializers
from authApp.models.poda import Poda

class PodaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Poda
        fields = ['fecha', 'lote', 'user']