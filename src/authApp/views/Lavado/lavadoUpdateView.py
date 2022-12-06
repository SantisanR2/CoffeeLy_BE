from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.lavadoSerializer import LavadoSerializer
from rest_framework.permissions import AllowAny
from authApp.models.lavado import Lavado

class LavadoUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        lavado = Lavado.objects.get(pk=pk)
        serializer = LavadoSerializer(lavado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Lavado actualizado',
            'updatedLote': {
                'cantidadEntra': serializer.data['cantidadEntra'],
                'cantidadSale': serializer.data['cantidadSale'],
                'cantidadAgua': serializer.data['cantidadAgua']
            }
        }
        return Response(response, status=status.HTTP_200_OK)