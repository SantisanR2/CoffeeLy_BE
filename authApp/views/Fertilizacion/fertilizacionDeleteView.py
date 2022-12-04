from rest_framework import generics, status
from authApp.models.fertilizacion import Fertilizacion
from rest_framework.response import Response

class FertilizacionDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        fertilizacion = Fertilizacion.objects.filter(id=_id)
        fertilizacion.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Fertilizacion eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)