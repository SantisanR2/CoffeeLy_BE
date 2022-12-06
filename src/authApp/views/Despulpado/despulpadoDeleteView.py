from rest_framework import generics, status
from authApp.models.despulpado import Despulpado
from rest_framework.response import Response

class DespulpadoDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        despulpado = Despulpado.objects.filter(id=_id)
        despulpado.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Despulpado eliminado',
        }
        return Response(response, status=status.HTTP_200_OK)