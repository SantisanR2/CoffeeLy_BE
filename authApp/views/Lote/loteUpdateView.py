from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.loteSerializer import LoteSerializer
from rest_framework.permissions import AllowAny
from authApp.models.lote import Lote

class LoteUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        lote = Lote.objects.get(pk=pk)
        serializer = LoteSerializer(lote, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Lote actualizado',
            'updatedLote': {
                'cantidad': serializer.data['cantidad'],
                'estado': serializer.data['estado'],
                'finca': serializer.data['finca']
            }
        }
        return Response(response, status=status.HTTP_200_OK)