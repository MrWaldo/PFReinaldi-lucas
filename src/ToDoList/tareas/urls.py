from django.urls import path

from .views import tarea
from .views import get_tareas
from .views import add_tarea
from .views import eliminar_tarea
from .views import editar_tarea


urlpatterns = [
    path('', get_tareas),
    path('add/', add_tarea),
    path('tarea/<int:id_tarea>', tarea),
    path('delete/<int:task_id>', eliminar_tarea, name='eliminar_tarea'),
    path('edit/<int:task_id>', editar_tarea, name='editar_tarea'),
]
