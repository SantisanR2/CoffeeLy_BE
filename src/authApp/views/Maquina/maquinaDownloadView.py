from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.maquina import Maquina

class MaquinaDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Maquina.objects.to_csv(None,'id','marca','modelo').decode('utf-8')
        return Response(text, status=status.HTTP_200_OK)