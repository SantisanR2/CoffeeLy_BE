from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.fertilizacion import Fertilizacion

class FertilizacionDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Fertilizacion.objects.to_csv(None,'id','relacion','fecha','lote_id','user_id__name').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)