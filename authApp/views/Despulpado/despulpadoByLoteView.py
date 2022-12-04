from rest_framework import generics, status
from authApp.models.despulpado import Despulpado
from rest_framework.response import Response
from authApp.serializers.despulpadoSerializer import DespulpadoSerializer

class DespulpadoByLoteView(generics.ListAPIView):
    serializer_class = DespulpadoSerializer

    def get_queryset(self):
        queryset = Despulpado.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        despulpado = self.get_queryset()
        sDespulpado = DespulpadoSerializer(despulpado, many=True)
        return Response(sDespulpado.data, status=status.HTTP_200_OK)