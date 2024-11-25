from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from produto.models import Categoria, Produto

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import path, reverse_lazy
from django.db.models import Q



class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produto/categoria_list.html'


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'produto/categoria_form.html'
    fields = ['nome']  # assuming Categoria has a field 'name'
    success_url = reverse_lazy('listcategoria')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'produto/categoria_form.html'
    fields = ['nome']
    success_url = reverse_lazy('listcategoria')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'produto/categoria_confirm_delete.html'
    success_url = reverse_lazy('listcategoria')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produto_list.html'


class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produto/produto_form.html'
    fields = ['nome','quantidade','preco','categoria']
    success_url = reverse_lazy('listproduto')


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto/produto_form.html'
    fields = ['nome','quantidade','preco','categoria']
    success_url = reverse_lazy('listproduto')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/produto_confirm_delete.html'
    success_url = reverse_lazy('listproduto')




