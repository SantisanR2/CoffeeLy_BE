from rest_framework import generics, status
from authApp.models.cosecha import Cosecha
from rest_framework.response import Response

class CosechaDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        cosecha = Cosecha.objects.filter(id=_id)
        cosecha.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Cosecha eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)