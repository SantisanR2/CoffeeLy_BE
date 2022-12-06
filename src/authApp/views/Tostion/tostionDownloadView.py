from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.tostion import Tostion

class TostionDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Tostion.objects.to_csv(None,'id','fecha','cantidadEntra','cantidadSale','tempInicio','temp1','temp2','tiempo1','tiempo2','tempPromedio','tiempoPromedio','aromas','agtron','curva','lote_id','user_id__name','maquina_id').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)