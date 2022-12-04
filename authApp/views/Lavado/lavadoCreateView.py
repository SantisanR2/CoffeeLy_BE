from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.lavadoSerializer import LavadoSerializer

class LavadoCreateView(views.APIView):
    
    def post(self, request):
        serializer = LavadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)