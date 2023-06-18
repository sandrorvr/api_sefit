from rest_framework.views import APIView
from rest_framework import generics

from .models import Servidor
from .serializers import ServidorSerializer




class ServidorAPIView(generics.ListCreateAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer
    