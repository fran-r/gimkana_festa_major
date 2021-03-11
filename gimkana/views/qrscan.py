from datetime import datetime
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView, DetailView

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

class QrScanByUserDetailView(LoginRequiredMixin, DetailView):
    model = QrScan


    # def get_object(self):
    #     #return QrScan.objects.filter(qr=self.request.pk, scanned_by=self.request.user)
    #     #print("********pk: {}".format(self.request.pk))
    #     result = QrScan.objects.filter(qr=3, scanned_by=self.request.user)
    #     print("********result: {}".format(list(result)))
    #     print("********get_object: {}".format(super().get_object()))
    #     return QrScan.objects.filter(qr=3, scanned_by=self.request.user)

    def get(self, request, *args, **kwargs):
        username = request.user.get_username()
        print("********kwargs: {}".format(kwargs))
        try:
            qr_id = kwargs.pop('pk', None)
            kwargs['qr'] = qr_id
            kwargs['scanned_by'] = username
            print("********kwargs: {}".format(kwargs))
            # TODO: no encuentra nada porque está buscando por la key, que es el qr_id
            return super().get(request, *args, **kwargs)
        except Http404:
            # Create element and get its details
            qr_id = kwargs['qr']
            qr_instance = Qr.objects.get(id=qr_id)
            print
            #qr_instance.save()
            user_instance = User.objects.get(username=username)
            #user_instance.save()
            print("********qr_instance: {}".format(qr_instance))
            print("********user_instance: {}".format(user_instance))
            print("********kwargs: {}".format(kwargs))
            scan_date = datetime.now()
            qrscan_id = '{}_{}'.format(qr_id, username)
            QrScan.objects.create(id=qrscan_id, qr=qr_instance, scanned_by=user_instance, scan_date=datetime.now(), status='U')
            return super().get(request, *args, **kwargs)
