from django.db import models
from .Estudiante import Estudiante
from .University import University

class Pago (models.Model):
    Estudiante =models.ForeignKey( Estudiante, on_delete=models.CASCADE)
    id_user = models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_pago = models.BigAutoField(primary_key=True)
    semana=models.IntegerField(default=1)
    monto=models.FloatField(default=0.0)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)