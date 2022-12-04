from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.despulpado import Despulpado

class DespulpadoDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Despulpado.objects.to_csv(None,'id','fechaInicio','fechaFinal','cantidadCafe','cantidadMucilago','cantidadAgua','lote_id','user_id__name','maquina_id').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)