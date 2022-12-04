from rest_framework import generics, status
from authApp.models.tostion import Tostion
from rest_framework.response import Response

class TostionDeleteView(generics.DestroyAPIView):

    def delete(self, request):
        _id = self.request.query_params.get('id')
        tostion = Tostion.objects.filter(id=_id)
        tostion.delete()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Tostion eliminada',
        }
        return Response(response, status=status.HTTP_200_OK)