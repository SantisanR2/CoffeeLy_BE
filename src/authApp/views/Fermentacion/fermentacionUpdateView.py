from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.fermentacionSerializer import FermentacionSerializer
from rest_framework.permissions import AllowAny
from authApp.models.fermentacion import Fermentacion

class FermentacionUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        fermentacion = Fermentacion.objects.get(pk=pk)
        serializer = FermentacionSerializer(fermentacion, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Fermentacion actualizado',
            'updatedLote': {
                'cantidadEntra': serializer.data['cantidadEntra'],
                'cantidadSale': serializer.data['cantidadSale'],
                'cantidadAgua': serializer.data['cantidadAgua']
            }
        }
        return Response(response, status=status.HTTP_200_OK)