from rest_framework import generics, status
from authApp.models.poda import Poda
from rest_framework.response import Response
from authApp.serializers.podaSerializer import PodaSerializer
from django.core.management import call_command


class PodaByLoteView(generics.ListAPIView):
    serializer_class = PodaSerializer

    def get_queryset(self):
        queryset = Poda.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):

        poda = self.get_queryset()
        sPoda = PodaSerializer(poda, many=True)
        return Response(sPoda.data, status=status.HTTP_200_OK)