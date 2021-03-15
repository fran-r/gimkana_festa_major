from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from ..models import QrScan, Qr


class QrScanByUserListView(LoginRequiredMixin, ListView):
    """
    Generic class-based view listing QRs scanned by current user.
    """
    model = QrScan
    template_name ='gimkana/qrscan_by_user_list.html'
    paginate_by = 10

    def get_queryset(self):
        return (
            QrScan.objects
                .filter(scanned_by=self.request.user)
                # .filter(status__exact='o')
                .order_by('status')
        )

class QrScanByUserCreateView(LoginRequiredMixin, CreateView):
    model = QrScan

    def get(self, request, *args, **kwargs):
        qr = Qr.objects.get(id=self.kwargs['pk'])
        username = self.request.user
        qrscan_id = '{}_{}'.format(qr.id, username)

        QrScan(id=qrscan_id, qr=qr, scanned_by=username, scan_date=datetime.now(), status='U').save()
        return redirect(qr)
