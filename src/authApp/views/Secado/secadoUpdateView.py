from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.secadoSerializer import SecadoSerializer
from rest_framework.permissions import AllowAny
from authApp.models.secado import Secado

class SecadoUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        secado = Secado.objects.get(pk=pk)
        serializer = SecadoSerializer(secado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Secado actualizado',
            'updatedLote': {
                'tempAmb': serializer.data['tempAmb'],
                'tempGrano': serializer.data['tempGrano']
            }
        }
        return Response(response, status=status.HTTP_200_OK)