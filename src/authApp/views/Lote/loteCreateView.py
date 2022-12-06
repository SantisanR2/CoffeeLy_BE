from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.loteSerializer import LoteSerializer

class LoteCreateView(views.APIView):
    
    def post(self, request):
        serializer = LoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'id': serializer.data['id']}
        return Response(response, status=status.HTTP_201_CREATED)