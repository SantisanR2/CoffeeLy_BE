from rest_framework import generics, status
from authApp.models.secado import Secado
from rest_framework.response import Response

class SecadoDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        secado = Secado.objects.filter(id=_id)
        secado.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Secado eliminado',
        }
        return Response(response, status=status.HTTP_200_OK)