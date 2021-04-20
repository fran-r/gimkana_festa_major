from django.views.generic import DetailView, ListView

from auth.SignupRequiredMixin import SignupRequiredMixin
from ..models import Qr


class QrListView(SignupRequiredMixin, ListView):
    model = Qr


class QrDetailView(SignupRequiredMixin, DetailView):
    model = Qr
