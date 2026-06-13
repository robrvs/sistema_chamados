from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Chamado(models.Model):
    CATEGORIAS = [
        ('computador', 'Computador / Hardware'),
        ('software', 'Instalação / Erro de Software'),
        ('rede', 'Internet / Rede'),
        ('email', 'E-mail Institucional'),
        ('impressora', 'Impressora / Scanner'),
        ('acesso', 'Sistemas / Senhas / Acessos'),
        ('outros', 'Outros Assuntos'),
    ]

    PRIORIDADES = [
        ('baixa', 'Baixa (Não impede o trabalho)'),
        ('media', 'Média (Dificulta o trabalho)'),
        ('alta', 'Alta (Impede o trabalho)'),
    ]

    STATUS_CHOICES = [
        ('aberto', 'Aberto / Aguardando Atendimento'),
        ('atendimento', 'Em Atendimento'),
        ('resolvido', 'Resolvido'),
        ('cancelado', 'Cancelado'),
    ]

    servidor_nome = models.CharField(max_length=100, verbose_name="Nome do Servidor/Usuário")
    setor = models.CharField(max_length=100, verbose_name="Setor/Departamento")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='computador')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='aberto')
    descricao = models.TextField(verbose_name="Descrição do Problema")
    observacao_tecnica = models.TextField(blank=True, null=True, verbose_name="Observações da Resolução")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OS #{self.id} - {self.servidor_nome} ({self.get_categoria_display()})"
    
    class Meta:
        ordering = ['-criado_em']