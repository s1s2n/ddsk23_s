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
from principal.views import ListadoBarrios, BarriosActualizar, BarriosCrear, BarriosDetalle, BarriosEliminar
#formularioContacto,contactar


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('formulario/',formularioContacto ), 
   # path('contactar/',contactar ), 
    path('barrios/', ListadoBarrios.as_view(template_name = "barrios/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
    path('barrios/detalle/<int:pk>', BarriosDetalle.as_view(template_name = "barrios/detalle.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Categoria o registro  
    path('barrios/crear', BarriosCrear.as_view(template_name = "barrios/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
    path('barrios/editar/<int:pk>', BarriosActualizar.as_view(template_name = "barrios/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
    path('barrios/eliminar/<int:pk>', BarriosEliminar.as_view(), name='barrios/eliminar.html'),    
]


