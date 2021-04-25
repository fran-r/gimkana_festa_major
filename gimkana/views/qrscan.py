from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from auth.SignupRequiredMixin import SignupRequiredMixin
from ..models import UserQr, Qr


class UserQrListView(SignupRequiredMixin, ListView):
    """
    Generic class-based view listing QRs scanned by current user.
    """
    model = UserQr
    template_name = 'gimkana/qrscan_by_user_list.html'

    def get_queryset(self):
        print("*****")
        print(UserQr.objects.all())
        print(self.request.user)
        print("*****")
        return (
            UserQr.objects.filter(user=self.request.user)
        )


class UserQrCreateView(SignupRequiredMixin, CreateView):
    model = UserQr

    def get(self, request, *args, **kwargs):
        qr = Qr.objects.get(id=self.kwargs['qr_id'])
        username = self.request.user

        # Create qrscan entry and redirect to qr details view
        # try-except is included to preserve the first scan_date on subsequent scans
        try:
            UserQr.objects.get(qr=qr, user=username)
        except UserQr.DoesNotExist as e:
            print(e)
            UserQr(qr=qr, user=username, scan_date=datetime.now()).save()

        return redirect(qr)


class UserQrTestCreateView(SignupRequiredMixin, CreateView):
    model = UserQr

    def get(self, request, *args, **kwargs):
        import random
        qr_id = random.randint(1, 25)
        qr = Qr.objects.get(id=qr_id)
        username = self.request.user

        # Create qrscan entry and redirect to qr details view
        # try-except is included to preserve the first scan_date on subsequent scans
        try:
            UserQr.objects.get(qr=qr, user=username)
        except UserQr.DoesNotExist as e:
            print(e)
            UserQr(qr=qr, user=username, scan_date=datetime.now()).save()

        return redirect(qr)
