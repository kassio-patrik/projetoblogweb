from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from .models import Aluno, Post
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from easy_pdf.views import PDFTemplateResponseMixin

# Create your views here.
class AlunoCreateView(CreateView):
    model = Aluno
    template_name = 'cadastrar/aluno.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Aluno cadastrado com suceso!')
        return reverse_lazy("listar_aluno")

class AlunoListView(ListView):
    model = Aluno
    template_name = 'listar/aluno.html'
    paginate_by = 3

class AlunoCorrecaoUpdateView(UpdateView):
    model = Aluno
    template_name = 'atualizar/aluno.html'

    fields = '__all__'

    def get_success_url(self):
        messages.success(self.request, 'Aluno atualizado com sucesso!')
        return reverse_lazy('listar_aluno')


class AlunoView(View):
    def desabilitarAluno(self, pk: int):
        Aluno.objects.filter(id=pk).update(excluido=True)
        return HttpResponseRedirect(reverse_lazy('listar_aluno'))

    def habilitarAluno(self, pk: int):
        Aluno.objects.filter(id=pk).update(excluido=False)
        return HttpResponseRedirect(reverse_lazy('listar_aluno'))

class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'detalhes/aluno.html'

class AlunoPDFDetailView(PDFTemplateResponseMixin, DetailView):
    model = Aluno
    template_name = 'detalhes/pdf_aluno.html'
