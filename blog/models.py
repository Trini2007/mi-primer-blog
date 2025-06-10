from django.db import models
from django.conf import settings
from django.utils import timezone
class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo
class Formulauno(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200)
    equipo = models.CharField(max_length=200)
    nacimiento = models.IntegerField()
    carreras_ganadas = models.IntegerField()
    campeonatos_corridos = models.IntegerField()
    biografia = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    #hola
# Create your models here.
