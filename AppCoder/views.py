from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import Curso_Formulario, Profesor_Formulario

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

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