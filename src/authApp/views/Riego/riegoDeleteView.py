from rest_framework import generics, status
from authApp.models.riego import Riego
from rest_framework.response import Response

class RiegoDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        riego = Riego.objects.filter(id=_id)
        riego.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Riego eliminado',
        }
        return Response(response, status=status.HTTP_200_OK)