from rest_framework import generics, status
from authApp.models.catacion import Catacion
from rest_framework.response import Response

class CatacionDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        catacion = Catacion.objects.filter(id=_id)
        catacion.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Catacion eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)