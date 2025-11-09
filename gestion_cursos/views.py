from django.shortcuts import render

# Create your views here.

# gestion_cursos/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Curso

# 1. Vista para LEER (Listar)
class CursoListView(ListView):
    model = Curso
    template_name = 'gestion_cursos/curso_list.html'
    context_object_name = 'cursos'  # Nombre para usar en el template

# 2. Vista para CREAR
class CursoCreateView(CreateView):
    model = Curso
    template_name = 'gestion_cursos/curso_form.html'
    # Campos que se mostrarán en el formulario
    fields = ['codigo', 'nombre', 'descripcion', 'creditos']
    # Redirige a la lista después de crear
    success_url = reverse_lazy('curso_list')

# 3. Vista para EDITAR (Actualizar)
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = 'gestion_cursos/curso_form.html'
    # No permitimos editar el 'codigo' (Primary Key)
    fields = ['nombre', 'descripcion', 'creditos']
    success_url = reverse_lazy('curso_list')

# 4. Vista para ELIMINAR
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'gestion_cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('curso_list')