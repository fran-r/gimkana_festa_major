from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

from .qr import Qr


class UserQr(models.Model):
    id = models.IntegerField(primary_key=True)
    qr = models.ForeignKey(Qr, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hints = models.IntegerField(blank=True, default=0)
    scan_date = models.DateTimeField(blank=True, null=True)
    value = models.IntegerField(blank=True, default=5)

    @property
    def is_scanned(self):
        return bool(self.scan_date)

    class Meta:
        ordering = ['qr__num_order']
        unique_together = ['qr_id', 'user_id']

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1}) scanned by {2} on {3} - {4}'\
            .format(self.qr.id, self.qr.name, self.user.username, self.scan_date, self.value)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de QR
        """
        return reverse('qr-detail', args=[str(self.id)])
