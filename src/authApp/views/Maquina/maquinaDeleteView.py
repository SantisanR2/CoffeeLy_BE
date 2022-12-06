from rest_framework import generics, status
from authApp.models.maquina import Maquina
from rest_framework.response import Response

class MaquinaDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        maquina = Maquina.objects.filter(id=_id)
        maquina.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Maquina eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)