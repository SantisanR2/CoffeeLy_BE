from rest_framework import generics, status
from authApp.models.tostion import Tostion
from rest_framework.response import Response
from authApp.serializers.tostionSerializer import TostionSerializer

class TostionByLoteView(generics.ListAPIView):
    serializer_class = TostionSerializer

    def get_queryset(self):
        queryset = Tostion.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(lote=id)
        return queryset

    def get(self, request):
        tostion = self.get_queryset()
        sTostion = Tostion(tostion, many=True)
        return Response(sTostion.data, status=status.HTTP_200_OK)