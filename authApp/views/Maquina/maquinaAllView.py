from rest_framework import generics, status
from authApp.models.maquina import Maquina
from rest_framework.response import Response
from authApp.serializers.maquinaSerializer import MaquinaSerializer

class MaquinaAllView(generics.ListAPIView):
    serializer_class = MaquinaSerializer

    def get_queryset(self):
        queryset = Maquina.objects.all()
        return queryset

    def get(self, request):
        maquina = self.get_queryset()
        sMaquina = MaquinaSerializer(maquina, many=True)
        return Response(sMaquina.data, status=status.HTTP_200_OK)