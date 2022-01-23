from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import Curso_Formulario

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    
    return render(request, "AppCoder/cursos.html", 
                  {'cursos': Curso.objects.all()})

def profesores(request):
    
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    
    return render(request, "AppCoder/entregables.html")

def formulario_curso(request):
    
    if request.method == "POST":
        
        mi_formulario = Curso_Formulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data
            Curso.objects.create(nombre=informacion['nombre'], camada=informacion['camada'])
            return redirect('Cursos')
    else:
        
        mi_formulario = Curso_Formulario()
    
    return render(request, "AppCoder/formulario_curso.html", {'mi_formulario':mi_formulario})