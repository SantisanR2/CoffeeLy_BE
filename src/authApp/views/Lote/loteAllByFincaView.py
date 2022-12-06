from rest_framework import generics, status
from authApp.models.lote import Lote
from rest_framework.response import Response
from authApp.serializers.loteSerializer import LoteSerializer

class LoteAllByFincaView(generics.ListAPIView):
    serializer_class = LoteSerializer

    def get_queryset(self):
        queryset = Lote.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(finca=id)
        return queryset

    def get(self, request):
        lote = self.get_queryset()
        sLote = LoteSerializer(lote, many=True)
        return Response(sLote.data, status=status.HTTP_200_OK)