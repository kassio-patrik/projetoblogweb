from django.urls import path
from .views import (
    AlunoCreateView
    , AlunoListView
    , AlunoCorrecaoUpdateView
    , AlunoView
    , AlunoDetailView
    , AlunoPDFDetailView
)

urlpatterns = [
    path('cadastrar/aluno', AlunoCreateView.as_view(), name='cadastrar_aluno'),
    path('listar/aluno', AlunoListView.as_view(), name='listar_aluno'),
    path('atualizar/aluno/<int:pk>', AlunoCorrecaoUpdateView.as_view(), name="corrigir_aluno"),
    path('ajax/desabilitar/aluno/<int:pk>', AlunoView.desabilitarAluno, name="ajax_desabilitar_aluno"),
    path('ajax/habilitar/aluno/<int:pk>', AlunoView.habilitarAluno, name="ajax_habilitar_aluno"),
    path('detalhes/aluno/<int:pk>', AlunoDetailView.as_view(), name="detalhes_aluno"),
    path('pdf/venda/<int:pk>', AlunoPDFDetailView.as_view(), name="pdf_aluno"),

]