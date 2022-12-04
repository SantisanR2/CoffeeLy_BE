from rest_framework import generics, status
from authApp.models.fermentacion import Fermentacion
from rest_framework.response import Response
from authApp.serializers.fermentacionSerializer import FermentacionSerializer

class FermentacionByLoteView(generics.ListAPIView):
    serializer_class = FermentacionSerializer

    def get_queryset(self):
        queryset = Fermentacion.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        fermentacion = self.get_queryset()
        sFermentacion = FermentacionSerializer(fermentacion, many=True)
        return Response(sFermentacion.data, status=status.HTTP_200_OK)