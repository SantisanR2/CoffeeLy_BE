from queue import Empty
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authApp.serializers.userSerializer import UserSerializer
from authApp.models.user import User

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        rol = user.role
        if user.role == 2:
            users = User.objects.all()
            finca = user.finca
            if finca is not None:
                users = users.filter(finca=finca)
            else:
                users = User.objects.none()
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Usuarios mostrados correctamente',
                'users': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        elif user.role == 4:
            users = User.objects.all()
            users = users.filter(finca=None)
            serializer = self.serializer_class(users, many=True)
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Usuarios mostrados correctamente',
                'users': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'No esta autorizado para realizar esta peticion'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)