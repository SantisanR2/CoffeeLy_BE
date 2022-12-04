from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.catacionSerializer import CatacionSerializer

class CatacionCreateView(views.APIView):
    
    def post(self, request):
        serializer = CatacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)