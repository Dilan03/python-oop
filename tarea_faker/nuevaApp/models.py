from django.db import models

# Create your models here.

class Toyota_Legacy(models.Model):
    #Definir los campos de que tiene la tabla
    primer_nombre = models.CharField(max_length = 50, unique = True)
    primer_apellido = models.CharField(max_length = 50, unique = True)
    correo = models.CharField(max_length = 50, unique = True)
    telefono = models.CharField(max_length = 15, unique = True)

    #Representar el registro como cadena de texto
    def __str__(self):
        return self.primer_nombre