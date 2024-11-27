from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('core.urls')),

    path('auth', include('usuarios.urls')),

    path('home', include('core.urls')),
    path('produto/', include('produto.urls')),
    # path('usuarios/', include('usuarios.urls')),
]
