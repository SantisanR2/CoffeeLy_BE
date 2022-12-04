from rest_framework import generics, status
from authApp.models.seleccion import Seleccion
from rest_framework.response import Response

class SeleccionDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        seleccion = Seleccion.objects.filter(id=_id)
        seleccion.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Seleccion eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)