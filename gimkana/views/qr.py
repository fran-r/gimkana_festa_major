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
        queryset = Qr.objects.filter(id=self.kwargs['pk'])

        user_qr = UserQr.objects.filter(qr=queryset.first(), user=self.request.user).first()
        if user_qr:
            show_hints = 3 if user_qr.is_scanned else user_qr.hints
        else:
            show_hints = 0

        return queryset.annotate(show_hints=Value(show_hints, output_field=IntegerField()))
