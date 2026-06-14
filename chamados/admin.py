from django.contrib import admin
from .models import Chamado

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'servidor_nome', 'setor', 'categoria', 'prioridade', 'status', 'criado_em')
    list_filter = ('status', 'prioridade', 'categoria')
    search_fields = ('servidor_nome', 'descricao', 'setor')