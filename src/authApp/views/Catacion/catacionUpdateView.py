from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.catacionSerializer import CatacionSerializer
from rest_framework.permissions import AllowAny
from authApp.models.catacion import Catacion

class CatacionUpdateView(views.APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request, pk):
        catacion = Catacion.objects.get(pk=pk)
        serializer = CatacionSerializer(catacion, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'Catacion actualizada'
        }
        return Response(response, status=status.HTTP_200_OK)