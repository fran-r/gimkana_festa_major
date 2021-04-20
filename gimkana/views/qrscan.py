from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from auth.SignupRequiredMixin import SignupRequiredMixin
from ..models import QrScan, Qr


class QrScanByUserListView(SignupRequiredMixin, ListView):
    """
    Generic class-based view listing QRs scanned by current user.
    """
    model = QrScan
    template_name ='gimkana/qrscan_by_user_list.html'

    def get_queryset(self):
        return (
            QrScan.objects
                .filter(scanned_by=self.request.user)
                # .filter(status__exact='o')
                .order_by('status')
        )


class QrScanByUserCreateView(SignupRequiredMixin, CreateView):
    model = QrScan

    def get(self, request, *args, **kwargs):
        qr = Qr.objects.get(id=self.kwargs['qr_id'])
        username = self.request.user

        # Create qrscan entry and redirect to qr details view
        # try-except is included to preserve the first scan_date on subsequent scans
        try:
            QrScan.objects.get(qr=qr, scanned_by=username)
        except QrScan.DoesNotExist as e:
            print(e)
            QrScan(qr=qr, scanned_by=username, scan_date=datetime.now(), status='U').save()

        return redirect(qr)
