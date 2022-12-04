from rest_framework import generics, status
from authApp.models.fertilizacion import Fertilizacion
from rest_framework.response import Response
from authApp.serializers.fertilizacionSerializer import FertilzacionSerializer

class FertilizacionByLoteView(generics.ListAPIView):
    serializer_class = FertilzacionSerializer

    def get_queryset(self):
        queryset = Fertilizacion.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        fertilizacion = self.get_queryset()
        sFertilizacion = FertilzacionSerializer(fertilizacion, many=True)
        return Response(sFertilizacion.data, status=status.HTTP_200_OK)