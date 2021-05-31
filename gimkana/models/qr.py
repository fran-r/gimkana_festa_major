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

    # Hotfix: This should be a field, but application is running and I don't want to make DB changes.
    # To temporarily disable a QR, set its value to 0 in the admin pages and restore it when available.
    @property
    def is_unavailable(self):
        return bool(self.value == 0)

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
