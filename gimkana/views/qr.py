from django.db.models import BooleanField, IntegerField, Value, Case, When, Q
from django.views.generic import DetailView, ListView

from auth import SignupRequiredMixin

from ..mixins import IsStartedMixin
from ..models import Qr, UserQr


# class QrListView(SignupRequiredMixin, IsStartedMixin, ListView):
class QrListView(SignupRequiredMixin, ListView):
    model = Qr

    def get_queryset(self):
        user_scans = (
            UserQr.objects
            .filter(user=self.request.user)
            .filter(Q(scan_date__isnull=False) | Q(value=0))
            .values_list('qr_id')
        )

        return (
            Qr.objects
            .filter(is_shop=False)
            .annotate(
                is_scanned=Case(When(id__in=user_scans, then=Value(True)), default=Value(False),
                                output_field=BooleanField()))
        )


# class QrDetailView(SignupRequiredMixin, IsStartedMixin, DetailView):
class QrDetailView(SignupRequiredMixin, DetailView):
    model = Qr

    def get_queryset(self):
        qr_id = self.kwargs['pk']
        queryset = Qr.objects.filter(pk=qr_id)
        qr = queryset.first()

        user_qr, _ = UserQr.objects.get_or_create(qr_id=qr.id, user=self.request.user,
                                                  defaults={'is_shop': qr.is_shop, 'value': qr.value})
        return queryset.annotate(
            hints=Value(user_qr.hints, output_field=IntegerField()),
            scoring_value=Value(user_qr.value, output_field=IntegerField()),
            is_scanned=Value(user_qr.is_scanned, output_field=BooleanField()),
        )
