from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from categoria.models import Categoria, Produto

from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import path, reverse_lazy
from django.db.models import Q



class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria/categoria_form.html'
    fields = ['nome']  # assuming Categoria has a field 'name'
    success_url = reverse_lazy('categoria_list')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'categoria/categoria_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria_list')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')










