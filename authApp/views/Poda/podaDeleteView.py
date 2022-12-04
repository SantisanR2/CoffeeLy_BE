from rest_framework import generics, status
from authApp.models.poda import Poda
from rest_framework.response import Response

class PodaDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        poda = Poda.objects.filter(id=_id)
        poda.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Poda eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)