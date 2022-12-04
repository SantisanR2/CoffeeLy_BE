from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.siembra import Siembra

class SiembraDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Siembra.objects.to_csv(None,'id','fecha','distancia','profundidad','inclinacion','semilla','lote_id','user_id__name').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)