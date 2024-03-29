import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

from .qr import Qr


QR_STATUS = (
    ('L', 'Locked'),
    ('U', 'Unlocked'),
    ('S', 'Scanned'),
)


class QrScan(models.Model):
    id = models.TextField(primary_key=True)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                      help_text="Unique ID for this particular QR scan")
    qr = models.ForeignKey(Qr, related_name='qr_id', on_delete=models.CASCADE)
    scan_date = models.DateField(null=True, blank=True)
    scanned_by = models.ForeignKey(User, related_name='scanned_by', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=QR_STATUS,
        blank=True,
        default='L',
        help_text='QR status')

    @property
    def is_scanned(self):
        return self.scan_date

    class Meta:
        ordering = ['qr_id', 'scanned_by']
        unique_together = ['qr_id', 'scanned_by']

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1}) scanned by {2} on {3}'.format(self.qr.id, self.qr.name, self.scanned_by.username, self.scan_date)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de QR
        """
        return reverse('qr-detail', args=[str(self.id)])
