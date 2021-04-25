from django.db.models import Value, BooleanField, Case, When
from django.views.generic import DetailView, ListView

from auth.SignupRequiredMixin import SignupRequiredMixin
from ..models import Qr, UserQr


class QrListView(SignupRequiredMixin, ListView):
    model = Qr


class QrScannedListView(SignupRequiredMixin, ListView):
    model = Qr
    template_name = 'gimkana/qr_scanned_list.html'

    def get_queryset(self):
        user_scans = UserQr.objects.filter(user=self.request.user).values_list('qr_id')
        return (
            Qr.objects.annotate(
                is_scanned=Case(When(id__in=user_scans, then=Value(True)), default=Value(False),
                             output_field=BooleanField()))
        )


class QrDetailView(SignupRequiredMixin, DetailView):
    model = Qr
