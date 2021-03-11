from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

from .qr import Qr


class UserTest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, max_length=100)
    user_agent = models.CharField(max_length=100, null=True, blank=True)
    qrs = models.ManyToManyField(Qr, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        String para representar el usuario
        """
        return '{}, {}'.format(self.name, self.email)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un usuario.
        """
        return reverse('usertest-detail', args=[str(self.email)])
        #return reverse('usertest-detail', args=[str(self.name)])
