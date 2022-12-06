from rest_framework import generics, status
from authApp.models.lavado import Lavado
from rest_framework.response import Response
from authApp.serializers.lavadoSerializer import LavadoSerializer

class LavadoByLoteView(generics.ListAPIView):
    serializer_class = LavadoSerializer

    def get_queryset(self):
        queryset = Lavado.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        lavado = self.get_queryset()
        sLavado = LavadoSerializer(lavado, many=True)
        return Response(sLavado.data, status=status.HTTP_200_OK)