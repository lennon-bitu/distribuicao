# distribution/models.py
from django.db import models

class Transfer(models.Model):
    destination = models.CharField(max_length=255, verbose_name='Destino')
    transfer_number = models.CharField(max_length=50, verbose_name='Nº Trasnf')
    volume = models.PositiveIntegerField(verbose_name='Volume')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Peso')
    observation = models.TextField(blank=True, null=True, verbose_name='Observação')

    def __str__(self):
        return f"{self.transfer_number} - {self.destination}"