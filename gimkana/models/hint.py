from django.contrib.auth.models import User
from django.db import models

from .qr import Qr


class Hint(models.Model):
    id = models.IntegerField(primary_key=True)
    qr = models.ForeignKey(Qr, related_name='qr_id', on_delete=models.CASCADE)
    level = models.IntegerField(blank=False, null=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    requested_by = models.ForeignKey(User, related_name='requested_by', on_delete=models.CASCADE)

    class Meta:
        ordering = ['qr_id', 'requested_by']
        unique = ['level']
        unique_together = ['qr_id', 'requested_by']

    def __str__(self):
        """String for representing the Model object."""
        return 'QR: {0} - Pista ({1}) requested by {2}'.format(self.qr.id, self.level, self.scanned_by.username)
