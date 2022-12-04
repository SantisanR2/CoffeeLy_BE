from rest_framework import generics, status
from authApp.models.riego import Riego
from rest_framework.response import Response
from authApp.serializers.riegoSerializer import RiegoSerializer

class RiegoDetailView(generics.RetrieveAPIView):

    def get(self, request, pk):
        riego = Riego.objects.get(pk=pk)
        sRiego = RiegoSerializer(riego)
        return Response(sRiego.data, status=status.HTTP_200_OK)