from django.db import models
from .Estudiante import Estudiante
from .University import University

class Asistencia (models.Model):
    Estudiante =models.ForeignKey( Estudiante, on_delete=models.CASCADE)
    id_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_Asistencia = models.BigAutoField(primary_key=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)