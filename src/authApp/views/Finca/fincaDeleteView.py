from rest_framework import generics, status
from authApp.models.finca import Finca
from rest_framework.response import Response

class FincaDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        finca = Finca.objects.filter(id=_id)
        finca.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Finca eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)