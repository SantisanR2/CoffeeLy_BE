from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.finca import Finca

class FincaDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = Finca.objects.to_csv(None,'id','nombre','ubicacion','altitud','clima','inclinacion','lumenes','coordenadas','tierra','ph','cultivos','microorganismos').decode('utf-8')
        return Response(text, status=status.HTTP_200_OK)