from django.urls import path
from AppCoder import views
from django.contrib.auth.decorators import login_required

from Proyecto_Coder.views import editar_perfil

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos/', login_required(views.cursos), name='Cursos'),
    # path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'),
    path('busqueda_camada/', views.busqueda_camada, name='busqueda_camada'),
    path('buscar/', views.buscar, name='buscar'),
    path('formulario_curso/', views.formulario_curso, name='formulario_curso'),
    # path('formulario_profesor/', views.formulario_profesor, name='formulario_profesor'),
    # path('profesores/delete/<id_profe>/', views.profesor_delete, name='profesor_delete'),
    path('curso/delete/<id_curso>/', login_required(views.curso_delete), name='curso_delete'),
    # path('profesor/update/<id_profe>/', views.profesor_update, name='profesor_update'),
    path('profesores/', views.ProfesorListView.as_view(), name='Profesores'),
    path('agregar_profesor/', login_required(views.ProfesorCreateView.as_view()), name='agregar_profesor'),
    path('profesor/update/<pk>/', login_required(views.ProfesorUpdateView.as_view()), name='profesor_update'),
    path('profesores/delete/<pk>/', login_required(views.ProfesorDeleteView.as_view()), name='profesor_delete'),
    path('profesores/view/<pk>/', views.ProfesorDetailView.as_view(), name='profesor_view'),
    path('crear_avatar', views.agregar_avatar, name='crear_avatar')
]