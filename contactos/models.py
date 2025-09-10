from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
