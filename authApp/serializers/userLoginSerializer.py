from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from authApp.models.user import User


class UserLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    finca = serializers.PrimaryKeyRelatedField(read_only = True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        correo = data['correo']
        password = data['password']
        user = authenticate(correo=correo, password=password)

        if user is None:
            raise serializers.ValidationError("Credenciales invalidas")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'id': user.id,
                'access': access_token,
                'refresh': refresh_token,
                'correo': user.correo,
                'name': user.name,
                'role': user.role,
                'finca': user.finca,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Credenciales invalidas")