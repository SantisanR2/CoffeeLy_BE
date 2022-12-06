from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.fertilizacionSerializer import FertilzacionSerializer
from rest_framework.permissions import AllowAny
from authApp.models.fertilizacion import Fertilizacion

class FertilizacionUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        fertilizacion = Fertilizacion.objects.get(pk=pk)
        serializer = FertilzacionSerializer(fertilizacion, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Fertilizacion actualizado',
            'updatedLote': {
                'relacion': serializer.data['relacion'],
                'fecha': serializer.data['fecha']
            }
        }
        return Response(response, status=status.HTTP_200_OK)