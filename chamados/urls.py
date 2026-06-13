from django.urls import include, path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.lista_chamados, name='home'),
    path('novo/', views.novo_chamado, name='novo_chamado'),
    path('editar/<int:pk>/', views.atualizar_chamado, name='atualizar_chamado'),
    path('deletar/<int:pk>/', views.deletar_chamado, name='deletar_chamado'),
    path('conta/', include('django.contrib.auth.urls')),
    path('cadastro/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('sobre/', views.pagina_sobre, name='sobre'),
    path('contato/', views.pagina_contato, name='contato'),
    path('', RedirectView.as_view(url='/chamados/', permanent=True))
]