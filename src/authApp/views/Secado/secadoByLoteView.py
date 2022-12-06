from rest_framework import generics, status
from authApp.models.secado import Secado
from rest_framework.response import Response
from authApp.serializers.secadoSerializer import SecadoSerializer

class SecadoByLoteView(generics.ListAPIView):
    serializer_class = SecadoSerializer

    def get_queryset(self):
        queryset = Secado.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        secado = self.get_queryset()
        sSecado = SecadoSerializer(secado, many=True)
        return Response(sSecado.data, status=status.HTTP_200_OK)