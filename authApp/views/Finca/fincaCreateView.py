from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.fincaSerializer import FincaSerializer

class FincaCreateView(views.APIView):
    
    def post(self, request):
        serializer = FincaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data['id'], status=status.HTTP_201_CREATED)