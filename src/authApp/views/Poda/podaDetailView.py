from rest_framework import generics, status
from authApp.models.poda import Poda
from rest_framework.response import Response
from authApp.serializers.podaSerializer import PodaSerializer

class PodaDetailView(generics.RetrieveAPIView):

    def get(self, request, pk):
        poda = Poda.objects.get(pk=pk)
        sPoda = PodaSerializer(poda)
        return Response(sPoda.data, status=status.HTTP_200_OK)