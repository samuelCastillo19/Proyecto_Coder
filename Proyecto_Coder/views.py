from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Proyecto_Coder.forms import UserRegisterForm

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                return redirect("Inicio")
        else:
            return render(request, "login.html", {"form" : form,
                                                "error" : "Usuario y/o contraseña no válida"})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form" : form})
    
def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} creado con éxito!!!')
    else:
        form = UserRegisterForm()
    
    return render(request, "register.html", {'form':form})