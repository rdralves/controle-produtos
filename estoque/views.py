from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto


@login_required
def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/produto_list.html', {'produtos': produtos})


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'estoque/produto_list.html'
    context_object_name = 'produtos'


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'estoque/produto_detail.html'


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['ref_produto', 'descricao', 'quantidade', 'valor']
    template_name = 'estoque/produto_form.html'
    success_url = reverse_lazy('produto_list')


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['ref_produto', 'descricao', 'quantidade', 'valor']
    template_name = 'estoque/produto_form.html'
    success_url = reverse_lazy('produto_list')


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'estoque/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')
