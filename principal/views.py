from django.shortcuts import render

# Create your views here.
# librerias del crud
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#importo el modelo de la base de datos de models.py
from .models import *
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class ListadoCategoria(ListView):
    model = Categoria

class CategoriaCrear(SuccessMessageMixin, CreateView):
    model =Categoria
    form = Categoria
    fields = "__all__"
    success_message ='Categoria creada correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class CategoriaDetalle (DetailView):
    model =Categoria

class  CategoriaActualizar(SuccessMessageMixin,UpdateView):
    model =  Categoria
    form = Categoria
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class CategoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoria 
    form = Categoria
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
    



