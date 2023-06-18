from django.contrib import admin

from .models import Servidor, Afastamento, Permuta, Tp_Noturno

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('mat', 'nome', 'sexo', 'email')

@admin.register(Afastamento)
class AfastamentoAdmin(admin.ModelAdmin):
    list_display = ('fk_servidor', 'data_criacao','data_inicio', 'data_fim', 'motivo', 'obs')

@admin.register(Permuta)
class PermutaAdmin(admin.ModelAdmin):
    list_display = ('mat', 'nome', 'sexo', 'email')

@admin.register(tp_noturno)
class tp_noturnoAdmin(admin.ModelAdmin):
    list_display = ('fk_servidor', 'data_criacao','data_inicio', 'data_fim', 'motivo', 'obs')
