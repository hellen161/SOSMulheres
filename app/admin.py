from django.contrib import admin
from .models import AlertaRapido, AvaliacaoRisco, Denuncia, Informacao, RedeApoio

@admin.register(AlertaRapido)
class AlertaRapidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'localizacao', 'data_criacao')
    list_filter = ('data_criacao',)
    search_fields = ('nome', 'descricao', 'localizacao')

@admin.register(AvaliacaoRisco)
class AvaliacaoRiscoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_criacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao',)

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data_criacao')
    search_fields = ('descricao',)
    list_filter = ('data_criacao',)

@admin.register(Informacao)
class InformacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)

@admin.register(RedeApoio)
class RedeApoioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
