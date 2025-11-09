from django.db import models

# Create your models here.

from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()

    # Este método le dice a Django cómo "mostrar" un objeto Curso
    # (por ejemplo, en el panel de administrador).
    # ¡Debe estar indentado DENTRO de la clase Curso!
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"