from django.db import models
from .Pago import Pago
from .University import University
class servicio(models.Model):
    id_pago=models.ForeignKey(Pago , on_delete=models.CASCADE)
    in_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    id_servicio = models.BigAutoField(primary_key=True)
    tipo=models.CharField(max_length=100)
    status =models.BooleanField(default=False)
    fecha = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    status =models.BooleanField(default=False)
    