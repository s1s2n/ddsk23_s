"""ddsk23 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal.views import CategoriaActualizar, CategoriaCrear, CategoriaDetalle, CategoriaEliminar, ListadoCategoria, formularioContacto,contactar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/',formularioContacto ), 
    path('contactar/',contactar ), 
    path('categoria/', ListadoCategoria.as_view(template_name = "categoria/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('categoria/detalle/<int:pk>', CategoriaDetalle.as_view(template_name = "categoria/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('categoria/crear', CategoriaCrear.as_view(template_name = "categoria/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('categoria/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "categoria/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('categoria/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='categoria/eliminar.html'),    
]

]
