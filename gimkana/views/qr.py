from django.db.models import BooleanField, IntegerField, Value, Case, When
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

    def get_queryset(self):
        qr_id = self.kwargs['pk']
        queryset = Qr.objects.filter(id=qr_id)

        user_qr, _ = UserQr.objects.get_or_create(qr_id=qr_id, user=self.request.user)
        return queryset.annotate(
            hints=Value(user_qr.hints, output_field=IntegerField()),
            is_scanned=Value(user_qr.is_scanned, output_field=BooleanField()),
        )
