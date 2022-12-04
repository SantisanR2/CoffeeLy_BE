from rest_framework import generics, status
from authApp.models.molienda import Molienda
from rest_framework.response import Response
from authApp.serializers.moliendaSerializer import MoliendaSerializer

class MoliendaByLoteView(generics.ListAPIView):
    serializer_class = MoliendaSerializer

    def get_queryset(self):
        queryset = Molienda.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        molienda = self.get_queryset()
        sMolienda = MoliendaSerializer(molienda, many=True)
        return Response(sMolienda.data, status=status.HTTP_200_OK)