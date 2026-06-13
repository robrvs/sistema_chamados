from django import forms
from .models import Chamado, Comentario

# Register your forms here.
class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'categoria', 'prioridade']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

class ChamadoUpdateForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['status', 'prioridade', 'tecnico_responsavel', 'resolucao_descricao']
        widgets = {
            'resolucao_descricao': forms.Textarea(attrs={'rows': 3}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Adicione um comentário...'}),
        }