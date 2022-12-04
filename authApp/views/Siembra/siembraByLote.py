from rest_framework import generics, status
from authApp.models.siembra import Siembra
from rest_framework.response import Response
from authApp.serializers.siembraSerializer import SiembraSerializer

class SiembraByLoteView(generics.ListAPIView):
    serializer_class = SiembraSerializer

    def get_queryset(self):
        queryset = Siembra.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        siembra = self.get_queryset()
        sSiembra = SiembraSerializer(siembra, many=True)
        return Response(sSiembra.data, status=status.HTTP_200_OK)