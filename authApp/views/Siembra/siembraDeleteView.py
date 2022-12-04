from rest_framework import generics, status
from authApp.models.siembra import Siembra
from rest_framework.response import Response

class SiembraDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        siembra = Siembra.objects.filter(id=_id)
        siembra.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Siembra eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)