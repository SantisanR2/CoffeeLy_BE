from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.despulpadoSerializer import DespulpadoSerializer
from rest_framework.permissions import AllowAny
from authApp.models.despulpado import Despulpado

class DespulpadoUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        despulpado = Despulpado.objects.get(pk=pk)
        serializer = DespulpadoSerializer(despulpado, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Despulpado actualizado',
            'updatedLote': {
                'cantidadCafe': serializer.data['cantidadCafe'],
                'cantidadMucilago': serializer.data['cantidadMucilago'],
                'cantidadAgua': serializer.data['cantidadAgua']
            }
        }
        return Response(response, status=status.HTTP_200_OK)