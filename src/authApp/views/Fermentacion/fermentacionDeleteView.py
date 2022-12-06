from rest_framework import generics, status
from authApp.models.fermentacion import Fermentacion
from rest_framework.response import Response

class FermentacionDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        fermentacion = Fermentacion.objects.filter(id=_id)
        fermentacion.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Fermentacion eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)