from rest_framework import generics, status
from authApp.models.molienda import Molienda
from rest_framework.response import Response

class MoliendaDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        molienda = Molienda.objects.filter(id=_id)
        molienda.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Molienda eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)