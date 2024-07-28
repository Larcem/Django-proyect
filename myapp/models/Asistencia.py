from django.db import models
from .Estudiante import Estudiante
from .University import University

class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    user = models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_asistencia = models.BigAutoField(primary_key=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estudiante: {self.estudiante.nombre}, Status: {'Activo' if self.status else 'Inactivo'}, Creado: {self.created.strftime('%Y-%m-%d %H:%M:%S')}"
