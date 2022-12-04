from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.cosechaSerializer import CosechaSerializer

class CosechaCreateView(views.APIView):
    
    def post(self, request):
        serializer = CosechaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)