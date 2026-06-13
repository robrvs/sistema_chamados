from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory
from .models import Chamado

ChamadoForm = modelform_factory(Chamado, fields=['servidor_nome', 'setor', 'categoria', 'prioridade', 'descricao'])
StatusForm = modelform_factory(Chamado, fields=['status', 'observacao_tecnica'])

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.all()
    
    # Captura os parâmetros de filtro da URL
    filtro_status = request.GET.get('status')
    filtro_prioridade = request.GET.get('prioridade')
    filtro_categoria = request.GET.get('categoria')
    
    # Aplica os filtros dinamicamente se eles forem selecionados
    if filtro_status:
        chamados = chamados.filter(status=filtro_status)
    if filtro_prioridade:
        chamados = chamados.filter(prioridade=filtro_prioridade)
    if filtro_categoria:
        chamados = chamados.filter(categoria=filtro_categoria)
        
    context = {
        'chamados': chamados,
        'filtro_status': filtro_status,
        'filtro_prioridade': filtro_prioridade,
        'filtro_categoria': filtro_categoria,
        # Passamos as listas para gerar os selects dinamicamente no HTML
        'categorias': Chamado.CATEGORIAS,
        'prioridades': Chamado.PRIORIDADES,
        'status_choices': Chamado.STATUS_CHOICES,
    }
    return render(request, 'chamados/lista.html', context)

def novo_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # <-- Alterado aqui de 'lista_chamados' para 'home'
    else:
        form = ChamadoForm()
    return render(request, 'chamados/novo.html', {'form': form, 'titulo': 'Abrir Chamado'})

def atualizar_chamado(request, pk):
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            return redirect('home')  # <-- Alterado aqui de 'lista_chamados' para 'home'
    else:
        form = StatusForm(instance=chamado)
    return render(request, 'chamados/novo.html', {'form': form, 'titulo': f'Atualizar OS #{chamado.id}', 'chamado': chamado})

def deletar_chamado(request, pk):
    # DELETE do CRUD
    chamado = get_object_or_404(Chamado, pk=pk)
    if request.method == 'POST':
        chamado.delete()
        return redirect('home')
    return render(request, 'chamados/confirmar_exclusao.html', {'chamado': chamado})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para o login após cadastrar
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form, 'titulo': 'Cadastro de Novo Usuário'})

def pagina_sobre(request):    
     return render(request, 'chamados/sobre.html')

def pagina_contato(request):
     return render(request, 'chamados/contato.html')