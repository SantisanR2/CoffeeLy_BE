from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.riegoSerializer import RiegoSerializer
from rest_framework.permissions import AllowAny
from authApp.models.riego import Riego

class RiegoUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        riego = Riego.objects.get(pk=pk)
        serializer = RiegoSerializer(riego, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Riego actualizada',
            'updatedLote': {
                'fecha': serializer.data['fecha'],
                'agua': serializer.data['agua']
            }
        }
        return Response(response, status=status.HTTP_200_OK)