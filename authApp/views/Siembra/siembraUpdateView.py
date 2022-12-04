from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.siembraSerializer import SiembraSerializer
from rest_framework.permissions import AllowAny
from authApp.models.siembra import Siembra

class SiembraUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        siembra = Siembra.objects.get(pk=pk)
        serializer = SiembraSerializer(siembra, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Siembra actualizada',
            'updatedLote': {
                'distancia': serializer.data['distancia'],
                'profundidad': serializer.data['profundidad'],
                'inclinacion': serializer.data['inclinacion']
            }
        }
        return Response(response, status=status.HTTP_200_OK)