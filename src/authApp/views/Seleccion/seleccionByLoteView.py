from rest_framework import generics, status
from authApp.models.seleccion import Seleccion
from rest_framework.response import Response
from authApp.serializers.seleccionSerializer import SeleccionSerializer

class SeleccionByLoteView(generics.ListAPIView):
    serializer_class = SeleccionSerializer

    def get_queryset(self):
        queryset = Seleccion.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        seleccion = self.get_queryset()
        sSeleccion = SeleccionSerializer(seleccion, many=True)
        return Response(sSeleccion.data, status=status.HTTP_200_OK)