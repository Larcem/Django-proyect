from django.db import models
from .Pago import Pago
from .University import University

class FaltaPago (models.Model):
    pago =models.ForeignKey( Pago, on_delete=models.CASCADE)
    id_user=models.ForeignKey(University, on_delete=models.CASCADE, default=1)
    semana=models.IntegerField(default=1)
    status =models.BooleanField(default=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    id_falta_pago = models.BigAutoField(primary_key=True)