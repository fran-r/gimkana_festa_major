# TODO: verificar si este directorio es correcto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..models import QrScan


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
