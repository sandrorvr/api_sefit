from rest_framework import serializers
from .models import Servidor, Roteiro, Afastamento, Permuta, Tp_noturno, Tp_fds, Tp_semanal

class RoteiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roteiro
        fields = ['id_roteiro', 'posto_base', 'area_semanal', 'area_fds']

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = ['mat', 'nome', 'sexo', 'email']

class AfastamentoSerializers(serializers.ModelSerializer):
    fk_servidor = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    count_days = serializers.SerializerMethodField()

    class Meta:
        model = Afastamento
        fields = [
            'id','fk_servidor','data_inicio','data_fim','motivo', 'count_days', 'obs'
        ]

    def get_count_days(self, obj):
        return abs((obj.data_inicio - obj.data_fim).days)


class PermutaSerializer(serializers.ModelSerializer):
    fk_substituto = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    fk_escalado = serializers.SlugRelatedField(read_only=True, slug_field='nome')
    class Meta:
        model = Permuta
        fields = ['fk_substituto', 'fk_escalado', 'data', 'tipo']


class Tp_noturnoSerializer(serializers.ModelSerializer):
    fk_permuta = PermutaSerializer()
    class Meta:
        model = Tp_noturno
        fields = ['fk_permuta', 'grupo']


class Tp_fdsSerializer(serializers.ModelSerializer):
    fk_permuta = PermutaSerializer()
    class Meta:
        model = Tp_fds
        fields = ['fk_permuta', 'grupo', 'roteiro']


class Tp_semanalSerializer(serializers.ModelSerializer):
    fk_permuta = PermutaSerializer()
    class Meta:
        model = Tp_semanal
        fields = ['fk_permuta', 'turno', 'roteiro']