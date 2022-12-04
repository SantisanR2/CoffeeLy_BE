
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authApp.serializers.userLoginSerializer import UserLoginSerializer
from authApp.models.user import User

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK
            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Usuario ingresado correctamente',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'id': serializer.data['id'],
                'finca': serializer.data['finca'],
                'role': serializer.data['role'],
                'name': serializer.data['name'],
                'authenticatedUser': {
                    'correo': serializer.data['correo'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)