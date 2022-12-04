from rest_framework import generics, status
from authApp.models.maquina import Maquina
from rest_framework.response import Response
from authApp.serializers.maquinaSerializer import MaquinaSerializer

class MaquinaDetailView(generics.RetrieveAPIView):

    def get(self, request, pk):
        maquina = Maquina.objects.get(pk=pk)
        sMaquina = MaquinaSerializer(maquina)
        return Response(sMaquina.data, status=status.HTTP_200_OK)