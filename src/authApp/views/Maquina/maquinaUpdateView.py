from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.maquinaSerializer import MaquinaSerializer
from rest_framework.permissions import AllowAny
from authApp.models.maquina import Maquina

class MaquinaUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        maquina = Maquina.objects.get(pk=pk)
        serializer = MaquinaSerializer(maquina, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Maquina actualizado',
            'updatedLote': {
                'marca': serializer.data['marca'],
                'modelo': serializer.data['modelo']
            }
        }
        return Response(response, status=status.HTTP_200_OK)