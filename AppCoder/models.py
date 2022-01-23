import email
from django.db import models

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f'Curso: {self.nombre} ({self.camada})'

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Entregable(models.Model):
    
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()