from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.TextField()
    company = models.TextField()
    precio = models.TextField()
    country = models.TextField()
    calificacion = models.IntegerField()
    dispositivo = models.TextField()
    dificultad = models.TextField()
    categoria = models.TextField()
    version = models.TextField()
    image = models.TextField()