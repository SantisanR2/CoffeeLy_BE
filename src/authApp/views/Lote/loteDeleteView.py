from rest_framework import generics, status
from authApp.models.lote import Lote
from rest_framework.response import Response

class LoteDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        lote = Lote.objects.filter(id=_id)
        lote.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'lote eliminado',
        }
        return Response(response, status=status.HTTP_200_OK)