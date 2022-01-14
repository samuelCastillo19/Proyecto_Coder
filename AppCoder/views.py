from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    
    return HttpResponse('Vista inicio')

def cursos(request):
    
    return HttpResponse('Vista Cursos')

def profesores(request):
    
    return HttpResponse('Vista Profesores')

def estudiantes(request):
    
    return HttpResponse('Vista Estudiantes')

def entregables(request):
    
    return HttpResponse('Vista Entregables')