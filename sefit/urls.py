from django.urls import path
from .views import ServidorAPIView, RoteiroAPIView, AfastamentoAPIView, \
                    PermutaAPIView, PermutaByTpAPIView 
                    #Tp_noturnoAPIView, Tp_fdsAPIView,Tp_semanalAPIView

urlpatterns = [
    path('servidor/', ServidorAPIView.as_view(), name='allServidor'),
    path('roteiro/', RoteiroAPIView.as_view(), name='allRoteiro'),
    path('afastamento/', AfastamentoAPIView.as_view(), name='allAfastamento'),
    path('permuta/', PermutaAPIView.as_view(), name='allPermuta'),
    path('permuta/<str:tp>/', PermutaByTpAPIView.as_view(), name='allPermutaByTp'),
    #path('permuta_not/', Tp_noturnoAPIView.as_view(), name='allPermuta_not'),
    #path('permuta_fds/', Tp_fdsAPIView.as_view(), name='allPermuta_fds'),
    #path('permuta_sem/', Tp_semanalAPIView.as_view(), name='allPermuta_sem')
]
