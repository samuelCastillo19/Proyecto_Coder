from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
    path('busqueda_camada/', views.busqueda_camada, name='busqueda_camada'),
    path('buscar/', views.buscar, name='buscar'),
    path('formulario_curso/', views.formulario_curso, name='formulario_curso'),
    path('formulario_profesor/', views.formulario_profesor, name='formulario_profesor'),
    path('profesores/delete/<id_profe>', views.profesor_delete, name='profesor_delete')
]