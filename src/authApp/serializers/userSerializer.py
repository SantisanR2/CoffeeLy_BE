from rest_framework import serializers
from authApp.models.user import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'correo', 'password', 'name', 'finca', 'cedula', 'celular', 'fecha', 'role']
        
