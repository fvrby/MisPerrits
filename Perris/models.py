from django.db import models
from django.utils import timezone
from django import forms

CONDITION = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
    )

class Adoptar(models.Model):
    nombreCompleto = models.CharField(max_length=150)
    run = models.CharField(max_length=10, primary_key=True)
	correo = models.EmailField()
	telefono = models.CharField(max_length=12)
	def __str__(self):
		return self.correo

class Adoptado(models.Model):
	foto = models.ImageField()
	nombre = models.CharField(max_length=150)
	raza = models.CharField(max_length=50)
	descripcion = models.TextField()
	estado = models.CharField(max_length=60, choices=CONDICION)
	def __str__(self):
		return self.nombre
