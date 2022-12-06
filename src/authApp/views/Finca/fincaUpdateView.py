from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.fincaSerializer import FincaSerializer
from rest_framework.permissions import AllowAny
from authApp.models.finca import Finca

class FincaUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        finca = Finca.objects.get(pk=pk)
        serializer = FincaSerializer(finca, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Finca actualizada',
            'updatedLote': {
                'nombre': serializer.data['nombre'],
                'ubicacion': serializer.data['ubicacion']
            }
        }
        return Response(response, status=status.HTTP_200_OK)