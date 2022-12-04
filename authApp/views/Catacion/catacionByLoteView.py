from rest_framework import generics, status
from authApp.models.catacion import Catacion
from rest_framework.response import Response
from authApp.serializers.catacionSerializer import CatacionSerializer

class CatacionByLoteView(generics.ListAPIView):
    serializer_class = CatacionSerializer

    def get_queryset(self):
        queryset = Catacion.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        catacion = self.get_queryset()
        sCatacion = CatacionSerializer(catacion, many=True)
        return Response(sCatacion.data, status=status.HTTP_200_OK)