from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

class Qr(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    hint1 = models.TextField(null=True, blank=True)
    hint2 = models.TextField(null=True, blank=True)
    map_url = models.URLField(null=True, blank=True)
    num_order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String que representa al objeto QR
        """
        return self.name or '-'

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de QR
        """
        return reverse('qr-detail', args=[str(self.id)])
