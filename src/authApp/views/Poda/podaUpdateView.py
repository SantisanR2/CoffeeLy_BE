from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.podaSerializer import PodaSerializer
from rest_framework.permissions import AllowAny
from authApp.models.poda import Poda

class PodaUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        poda = Poda.objects.get(pk=pk)
        serializer = PodaSerializer(poda, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Poda actualizada',
            'updatedLote': {
                'fecha': serializer.data['fecha']
            }
        }
        return Response(response, status=status.HTTP_200_OK)