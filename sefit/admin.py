from django.contrib import admin

from .models import Servidor, Afastamento, Permuta, Tp_noturno, Tp_fds, Tp_semanal, Roteiro

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('mat', 'nome', 'sexo', 'email')

@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
    list_display = ('fk_servidor', 'data_criacao','data_inicio', 'data_fim', 'motivo', 'obs')

@admin.register(Permuta)
class PermutaAdmin(admin.ModelAdmin):
    list_display = ('fk_substituto', 'fk_escalado', 'data', 'tipo')

@admin.register(Tp_noturno)
class Tp_noturnoAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'fk_permuta')

@admin.register(Tp_fds)
class Tp_fdsAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'roteiro', 'fk_permuta')


@admin.register(Tp_semanal)
class Tp_semanalAdmin(admin.ModelAdmin):
    list_display = ('turno', 'roteiro', 'fk_permuta')


@admin.register(Roteiro)
class RoteiroAdmin(admin.ModelAdmin):
    list_display = ('id_roteiro', 'posto_base','area_semanal', 'area_fds')

