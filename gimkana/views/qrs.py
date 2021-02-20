from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from ..models import Qr


class QrListView(LoginRequiredMixin, ListView):
    model = Qr


class QrDetailView(LoginRequiredMixin, DetailView):
    model = Qr
