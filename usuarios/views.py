from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from usuarios.models import Usuarios
from django.contrib.auth.models import User



# class CategoriaListView(ListView):
#     model = Categoria
#     template_name = 'produto/categoria_list.html'

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Usuarios
from django.contrib.auth.models import User

class UsuarioCreateView(CreateView):
    model = Usuarios
    template_name = 'core/cadastro_usuarios.html'
    fields = ['nome', 'email', 'senha', 'data_nascimento', 'cpf', 'telefone']

    def form_valid(self, form):
        email = form.cleaned_data['email']
        nome = form.cleaned_data['nome']
        senha = form.cleaned_data['senha']
        data_nascimento = form.cleaned_data['data_nascimento']
        cpf = form.cleaned_data['cpf']
        telefone = form.cleaned_data['telefone']

        # Verifica se já existe um usuário com esse email
        buscauser = User.objects.filter(email=email)

        if buscauser.exists():  # Verifica se a consulta retornou algum resultado
            return HttpResponse('Este email já está cadastrado!')

        # Cria o novo usuário se o email não estiver cadastrado
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        # Redireciona para a página de login após salvar
        return HttpResponseRedirect(reverse_lazy('login'))

class CustomLoginView(LoginView):
    template_name = 'core/base.html'  # O template que será usado para renderizar o login
    success_url = reverse_lazy('home')  # Redireciona para a página inicial após o login bem-sucedido