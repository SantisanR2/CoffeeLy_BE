from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.tostionSerializer import TostionSerializer
from rest_framework.permissions import AllowAny
from authApp.models.tostion import Tostion

class TostionUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        tostion = Tostion.objects.get(pk=pk)
        serializer = TostionSerializer(tostion, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Tostion actualizada',
            'updatedLote': {
                'cantidadEntra': serializer.data['cantidadEntra'],
                'cantidadSale': serializer.data['cantidadSale']
            }
        }
        return Response(response, status=status.HTTP_200_OK)