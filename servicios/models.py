from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='servicios_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=20)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
