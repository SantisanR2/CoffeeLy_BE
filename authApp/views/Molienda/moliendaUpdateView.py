from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.moliendaSerializer import MoliendaSerializer
from rest_framework.permissions import AllowAny
from authApp.models.molienda import Molienda

class MoliendaUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        molienda = Molienda.objects.get(pk=pk)
        serializer = MoliendaSerializer(molienda, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Molienda actualizada',
            'updatedLote': {
                'cantidadEntra': serializer.data['cantidadEntra'],
                'cantidadSale': serializer.data['cantidadSale']
            }
        }
        return Response(response, status=status.HTTP_200_OK)