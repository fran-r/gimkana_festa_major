from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Qr(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    is_shop = models.BooleanField(null=False, blank=False)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    hint = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    image_footer = models.TextField(null=True, blank=True)
    coordinates = models.TextField(null=True, blank=True)
    num_order = models.IntegerField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(null=False, default=True)

    class Meta:
        ordering = ['num_order']

    def __str__(self):
        """
        String que representa al objeto QR
        """
        return '{} - {}'.format(self.num_order, self.title)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de QR
        """
        return reverse('qr-detail', args=[str(self.id)])
