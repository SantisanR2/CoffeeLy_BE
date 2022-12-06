from rest_framework import generics, status
from authApp.models.lavado import Lavado
from rest_framework.response import Response

class LavadoDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        lavado = Lavado.objects.filter(id=_id)
        lavado.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Lavado eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)