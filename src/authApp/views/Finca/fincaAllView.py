from rest_framework import generics, status
from authApp.models.finca import Finca
from rest_framework.response import Response
from authApp.serializers.fincaSerializer import FincaSerializer

class FincaAllView(generics.RetrieveAPIView):

    serializer_class = FincaSerializer

    def get_queryset(self):
        queryset = Finca.objects.all()
        return queryset

    def get(self, request):
        finca = self.get_queryset()
        sFinca = FincaSerializer(finca, many=True)
        return Response(sFinca.data, status=status.HTTP_200_OK)