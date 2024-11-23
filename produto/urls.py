
from django.urls import path, include
from . import views
urlpatterns = [

    path('listar', views.CategoriaListView.as_view(), name='categoria_list'),
    path('save', views.CategoriaCreateView.as_view(), name='categoria_form'),
    path('update/<int:pk>', views.CategoriaUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', views.CategoriaDeleteView.as_view(), name='delete')

]
