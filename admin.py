# admin.py

from django.contrib import admin
from .models import Cliente, Hospedagem, Quarto, Consumo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'endereco']

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ['apartamento', 'valor']

@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display = ['data_entrada', 'data_saida', 'valor', 'cliente', 'quarto']
    list_filter = ['cliente']

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data', 'valor', 'hospedagem']
    list_filter = ['hospedagem']
