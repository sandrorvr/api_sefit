from rest_framework import serializers
from .models import Servidor

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = ['mat', 'nome', 'sexo', 'email']

