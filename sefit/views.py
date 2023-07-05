from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Servidor, Roteiro, Afastamento, Permuta, Tp_noturno, Tp_fds, Tp_semanal
from .serializers import RoteiroSerializer, ServidorSerializer, AfastamentoSerializers, PermutaSerializer, Tp_noturnoSerializer, Tp_fdsSerializer, Tp_semanalSerializer 


class RoteiroAPIView(generics.ListCreateAPIView):
    queryset = Roteiro.objects.all()
    serializer_class = RoteiroSerializer

class ServidorAPIView(generics.ListCreateAPIView):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

class AfastamentoAPIView(generics.ListCreateAPIView):
    queryset = Afastamento.objects.all()
    serializer_class = AfastamentoSerializers

class PermutaAPIView(generics.ListCreateAPIView):
    queryset = Permuta.objects.all()
    serializer_class = PermutaSerializer


class PermutaByTpAPIView(APIView):
    def get(self, request, tp):
        print(tp)
        if tp == 'fds':
            queryset = Tp_fds.objects.all()
            serializer = Tp_fdsSerializer(queryset, many=True)
        elif tp == 'not':
            queryset = Tp_noturno.objects.all()
            serializer = Tp_noturnoSerializer(queryset, many=True)
        elif tp == 'sem':
            queryset = Tp_semanal.objects.all()
            serializer = Tp_semanalSerializer(queryset, many=True)
        else:
            raise('TP not find!')
        return  Response(serializer.data)