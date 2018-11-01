from django.db import models
from django.utils import timezone
from django import forms

CONDICION = (
        ('Rescatado', 'Rescatado'),
        ('Disponible', 'Disponible'),
        ('Adoptado', 'Adoptado'),
    )


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Adoptar(models.Model):
	correo = models.EmailField()
	run = models.CharField(max_length=12, primary_key=True)
	nombreCompleto = models.CharField(max_length=150)
	telefono = models.CharField(max_length=12)
	def __str__(self):
		return self.correo

class Adoptado(models.Model):
	foto = models.ImageField()
	nombre = models.CharField(max_length=100)
	raza = models.CharField(max_length=100)
	descripcion = models.TextField()
	estado = models.CharField(max_length=10, choices=CONDICION)
	def __str__(self):
		return self.nombre