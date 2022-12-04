from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.lote import Lote

class LoteDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Lote.objects.to_csv(None,'id','cantidad','estado','estaCosechado','finca_id__nombre').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)