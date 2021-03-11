from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView, ListView
from ..models import Qr


class QrListView(LoginRequiredMixin, ListView):
    model = Qr


class QrDetailView(LoginRequiredMixin, DetailView):
    model = Qr

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            # Create element and get its details
            qr_id = kwargs['pk']
            # TODO: cambiar QR por QR_scan
            Qr.objects.create(id=qr_id, name='QR-' + str(qr_id), description='No desc yet', hint='No hints')
            return super().get(request, *args, **kwargs)
