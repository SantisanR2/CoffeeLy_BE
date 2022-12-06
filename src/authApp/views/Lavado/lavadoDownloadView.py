from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.lavado import Lavado

class LavadoDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Lavado.objects.to_csv(None,'id','fechaInicio','fechaFinal','cantidadEntra','cantidadSale','cantidadAgua','lote_id','user_id__name','maquina_id').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)