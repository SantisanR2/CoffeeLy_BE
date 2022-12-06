from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.riego import Riego

class RiegoDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Riego.objects.to_csv(None,'id','fecha','agua','lote_id','user_id__name').decode('utf-8')
        text = text.replace('name','user_nombre',1)
        return Response(text, status=status.HTTP_200_OK)