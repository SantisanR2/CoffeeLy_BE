from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.secadoSerializer import SecadoSerializer

class SecadoCreateView(views.APIView):
    
    def post(self, request):
        serializer = SecadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)