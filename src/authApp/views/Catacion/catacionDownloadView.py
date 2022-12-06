from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.catacion import Catacion

class CatacionDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Catacion.objects.to_csv(None,'id','fecha','tiempo1','temp1','tiempo2','temp2','tiempo3','temp3','puntaje','lote_id','user_id__name').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)