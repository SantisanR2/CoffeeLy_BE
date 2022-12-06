from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.seleccionSerializer import SeleccionSerializer

class SeleccionCreateView(views.APIView):
    
    def post(self, request):
        serializer = SeleccionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)