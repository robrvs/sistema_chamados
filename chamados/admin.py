from django.contrib import admin
from .models import Chamado

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    # Exibe colunas organizadas no painel do administrador do Django
    list_display = ('id', 'servidor_nome', 'setor', 'categoria', 'prioridade', 'status', 'criado_em')
    # Permite filtrar lateralmente por status, prioridade e categoria
    list_filter = ('status', 'prioridade', 'categoria')
    # Adiciona uma barra de pesquisa para buscar por nome ou descrição do problema
    search_fields = ('servidor_nome', 'descricao', 'setor')