from rest_framework import generics, status
from authApp.models.lote import Lote
from rest_framework.response import Response
from authApp.serializers.loteSerializer import LoteSerializer

class LoteDetailView(generics.RetrieveAPIView):

    def get(self, request, pk):
        lote = Lote.objects.get(pk=pk)
        sLote = LoteSerializer(lote)
        return Response(sLote.data, status=status.HTTP_200_OK)