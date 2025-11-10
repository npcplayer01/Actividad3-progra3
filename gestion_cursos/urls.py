from django.urls import path
from .views import (
    CursoListView,
    CursoCreateView,
    CursoUpdateView,
    CursoDeleteView
)

urlpatterns = [
    # R: Read (Listar)
    # La ruta vacía ('') será la página principal
    path('', CursoListView.as_view(), name='curso_list'),

    # C: Create (Crear)
    path('curso/nuevo/', CursoCreateView.as_view(), name='curso_create'),
    
    # U: Update (Editar)
    path('curso/<str:pk>/editar/', CursoUpdateView.as_view(), name='curso_update'),

    # D: Delete (Eliminar)
    path('curso/<str:pk>/eliminar/', CursoDeleteView.as_view(), name='curso_delete'),
]