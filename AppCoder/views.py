from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import AvatarFormulario, Curso_Formulario, Profesor_Formulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    
    avatares = Avatar.objects.filter(user=request.user)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
        
    return render(request, "AppCoder/inicio.html", {'avatar_url':avatar_url})

def cursos(request):
    
    return render(request, "AppCoder/cursos.html", 
                  {'cursos': Curso.objects.all()})

def profesores(request):
    
    return render(request, "AppCoder/profesores.html",
                  {'profesores': Profesor.objects.all()})

def estudiantes(request):
    
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    
    return render(request, "AppCoder/entregables.html")

def formulario_curso(request):
    
    if request.method == "POST":
        mi_formulario = Curso_Formulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            Curso.objects.create(nombre=informacion['nombre'], camada=informacion['camada'])
            return redirect('Cursos')
    else:
        
        mi_formulario = Curso_Formulario()
    
    return render(request, "AppCoder/formulario_curso.html", {'mi_formulario':mi_formulario})

def formulario_profesor(request):
    
    if request.method == "POST":
        
        mi_formulario = Profesor_Formulario(request.POST)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            Profesor.objects.create(nombre=informacion['nombre'], 
                                    apellido=informacion['apellido'], 
                                    email=informacion['email'],
                                    profesion=informacion['profesion'])
            
            return redirect('Profesores')
    else:
        
        mi_formulario = Profesor_Formulario()
    
    return render(request, "AppCoder/formulario_profesor.html", {'mi_formulario':mi_formulario})

def busqueda_camada(request):
    
    return render(request, "AppCoder/busqueda_camada.html")

def buscar(request):
    
    # respuesta = f'Estoy buscando la camada numero: {request.GET["camada"]}'
    
    
    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada)
        return render(request, "AppCoder/resultados_busqueda.html", {"cursos":cursos, "camada":camada})
    
    else:
        
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

def profesor_delete(request, id_profe):
    profesor = Profesor.objects.get(id=id_profe)
    profesor.delete()
    
    return redirect('Profesores')

def curso_delete(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    
    return redirect('Cursos')

def profesor_update(request, id_profe):
    
    profesor = Profesor.objects.get(id=id_profe)
    
    if request.method == "POST":
        
        form = Profesor_Formulario(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            profesor.nombre = info['nombre']
            profesor.apellido = info['apellido']
            profesor.email = info['email']
            profesor.profesion = info['profesion']
            
            profesor.save()
            
            return redirect('Profesores')
    else:
        
        form = Profesor_Formulario(model_to_dict(profesor))
    
    return render(request, "AppCoder/editar_profesor.html", {'form':form, "id_profe": id_profe})

class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "AppCoder/profesores.html"
    context_object_name = 'profesores'
    
class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "AppCoder/ver_profesor.html"
    
class ProfesorCreateView(CreateView):
    model = Profesor
    success_url = reverse_lazy('Profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']    
    template_name = "AppCoder/agregar_profesor.html"
    
class ProfesorUpdateView(UpdateView):
    model = Profesor
    success_url = reverse_lazy('Profesores')
    fields = ['nombre', 'apellido', 'email', 'profesion']    
    template_name = "AppCoder/editar_profesor.html"
    
class ProfesorDeleteView(DeleteView):
    model = Profesor
    success_url = reverse_lazy('Profesores')
    template_name = "AppCoder/profesor_confirm_delete.html"
    

@login_required
def agregar_avatar(request):
    
    if request.method == 'POST':
        
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            
            return redirect('Inicio')
        
    else:
        formulario = AvatarFormulario() 
        
    return render(request, 'AppCoder/crear_avatar.html', {'form': formulario})
    