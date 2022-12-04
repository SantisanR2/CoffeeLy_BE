from rest_framework import generics, status
from authApp.models.cosecha import Cosecha
from rest_framework.response import Response
from authApp.serializers.cosechaSerializer import CosechaSerializer

class CosechaByLoteView(generics.ListAPIView):
    serializer_class = CosechaSerializer

    def get_queryset(self):
        queryset = Cosecha.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        cosecha = self.get_queryset()
        sCosecha = CosechaSerializer(cosecha, many=True)
        return Response(sCosecha.data, status=status.HTTP_200_OK)