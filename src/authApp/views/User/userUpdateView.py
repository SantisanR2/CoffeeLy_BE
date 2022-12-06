from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authApp.serializers.userSerializer import UserSerializer
from authApp.models.user import User

class UserUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Usuario actualizado',
            'updatedUser': {
                'correo': serializer.data['correo'],
                'role': serializer.data['role']
            }
        }
        return Response(response, status=status.HTTP_200_OK)