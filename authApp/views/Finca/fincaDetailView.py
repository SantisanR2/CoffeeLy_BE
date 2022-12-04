from rest_framework import generics, status
from authApp.models.finca import Finca
from rest_framework.response import Response
from authApp.serializers.fincaSerializer import FincaSerializer

class FincaDetailView(generics.RetrieveAPIView):

    def get(self, request, pk):
        finca = Finca.objects.get(pk=pk)
        finquita = FincaSerializer(finca)
        return Response(finquita.data, status=status.HTTP_200_OK)