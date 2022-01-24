from django import forms

class Curso_Formulario(forms.Form):
    
    nombre = forms.CharField()
    camada = forms.IntegerField()
    
class Profesor_Formulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()