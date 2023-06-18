from django.urls import path
from .views import ServidorAPIView

urlpatterns = [
    path('servidor/', ServidorAPIView.as_view(), name='allServidor'),
]
