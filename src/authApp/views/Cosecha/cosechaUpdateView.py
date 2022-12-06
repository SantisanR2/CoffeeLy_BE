from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.cosechaSerializer import CosechaSerializer
from rest_framework.permissions import AllowAny
from authApp.models.cosecha import Cosecha

class CosechaUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        cosecha = Cosecha.objects.get(pk=pk)
        serializer = CosechaSerializer(cosecha, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Cossecha actualizado',
            'updatedCosecha': {
                'fecha': serializer.data['fecha'],
                'cantidad': serializer.data['cantidad'],
                'defectos': serializer.data['defectos']
            }
        }
        return Response(response, status=status.HTTP_200_OK)