from django.db import models
from .FaltaAsistencia import FaltaAsistencia
from .University import University

class Justificacion (models.Model):
    FaltaAsistencia =models.ForeignKey( FaltaAsistencia, on_delete=models.CASCADE)
    id_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_justificacion = models.BigAutoField(primary_key=True)
    descripcion=models.TextField()
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)