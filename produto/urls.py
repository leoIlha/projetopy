
from django.urls import path, include
from . import views
urlpatterns = [

    #                                   ROTAS CATEGORIAS
    path('listarcategoria', views.CategoriaListView.as_view(), name='listcategoria'),
    path('savecategoria', views.CategoriaCreateView.as_view(), name='savecategoria'),
    path('updatecategoria/<int:pk>', views.CategoriaUpdateView.as_view(), name='updatecategoria'),
    path('deletecategoria/<int:pk>', views.CategoriaDeleteView.as_view(), name='deletecategoria'),

    #                                   ROTAS PRODUTOS

    path('listarproduto', views.ProdutoListView.as_view(), name='listproduto'),
    path('saveproduto', views.ProdutoCreateView.as_view(), name='saveproduto'),
    path('updateproduto/<int:pk>', views.ProdutoUpdateView.as_view(), name='updateproduto'),
    path('deleteproduto/<int:pk>', views.ProdutoDeleteView.as_view(), name='deleteproduto'),

]
