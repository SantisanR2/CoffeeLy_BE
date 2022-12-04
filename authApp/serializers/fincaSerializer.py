from dataclasses import fields
from rest_framework import serializers
from authApp.models.finca import Finca

class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = ['nombre', 'ubicacion', 'altitud', 'clima', 'inclinacion', 'lumenes', 'coordenadas', 'tierra', 'ph', 'cultivos', 'microorganismos']