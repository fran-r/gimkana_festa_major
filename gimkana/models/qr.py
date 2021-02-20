from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

class Qr(models.Model):
    id = models.IntegerField(primary_key=True)
    # import uuid
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    description = models.TextField(null=False)
    hint = models.TextField(null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String que representa al objeto QR
        """
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de QR
        """
        return reverse('qr-detail', args=[str(self.id)])
