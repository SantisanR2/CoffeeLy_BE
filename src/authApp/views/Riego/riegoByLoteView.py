from rest_framework import generics, status
from authApp.models.riego import Riego
from rest_framework.response import Response
from authApp.serializers.riegoSerializer import RiegoSerializer

class RiegoByLoteView(generics.ListAPIView):
    serializer_class = RiegoSerializer

    def get_queryset(self):
        queryset = Riego.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        riego = self.get_queryset()
        sRiego = RiegoSerializer(riego, many=True)
        return Response(sRiego.data, status=status.HTTP_200_OK)