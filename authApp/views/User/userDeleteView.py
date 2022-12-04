from rest_framework import generics, status
from authApp.models.user import User
from rest_framework.response import Response

class UserDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        user = User.objects.filter(id=_id)
        user.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Usuario eliminado',
        }
        return Response(response, status=status.HTTP_200_OK)