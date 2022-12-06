from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.seleccionSerializer import SeleccionSerializer
from rest_framework.permissions import AllowAny
from authApp.models.seleccion import Seleccion

class SeleccionUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        seleccion = Seleccion.objects.get(pk=pk)
        serializer = SeleccionSerializer(seleccion, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Seleccion actualizada',
            'updatedLote': {
                'cantidadEntra': serializer.data['cantidadEntra'],
                'cantidadSale': serializer.data['cantidadSale'],
                'defectuosos': serializer.data['defectuosos']
            }
        }
        return Response(response, status=status.HTTP_200_OK)