from django import forms

class Curso_Formulario(forms.Form):
    
    nombre = forms.CharField()
    camada = forms.IntegerField()