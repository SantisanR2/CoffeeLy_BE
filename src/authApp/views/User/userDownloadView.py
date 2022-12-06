from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from authApp.models.user import User

class UserDownloadView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        text = User.objects.to_csv(None,'id','name','correo','role','finca_id__nombre','cedula','celular','fecha','last_login').decode('utf-8')
        text = text.replace('nombre','finca_nombre',1)
        return Response(text, status=status.HTTP_200_OK)