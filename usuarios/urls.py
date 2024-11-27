from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastro'),  # Corrigido para não ter barra inicial
    path('', views.CustomLoginView.as_view(), name='login'),
]
