from rest_framework import serializers
from authApp.models.riego import Riego

class RiegoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Riego
        fields = ['fecha', 'agua', 'lote', 'user']