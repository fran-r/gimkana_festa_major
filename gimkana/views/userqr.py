from datetime import datetime

from django.db.models import F
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from auth.SignupRequiredMixin import SignupRequiredMixin
from ..models import UserQr


class UserQrListView(SignupRequiredMixin, ListView):
    """
    Generic class-based view listing QRs scanned by current user.
    """
    model = UserQr
    template_name = 'gimkana/user_qr_list.html'

    def get_queryset(self):
        return (
            UserQr.objects.filter(user=self.request.user)
        )


class UserQrCreateView(SignupRequiredMixin, CreateView):
    model = UserQr

    @staticmethod
    def tmp_create_user_qr(qr_id, username):
        # Create userqr entry and redirect to qr details view
        user_qr, is_new = UserQr.objects.get_or_create(qr_id=qr_id, user=username, defaults={'scan_date': datetime.now()})
        # Preserve the first scan_date on subsequent scans
        if not user_qr.scan_date: 
            user_qr.scan_date = datetime.now()
            user_qr.save(update_fields=['scan_date'])

        return redirect('qr-detail', pk=qr_id)

    def get(self, request, *args, **kwargs):
        qr_id = self.kwargs['pk']
        username = self.request.user

        # TODO: es temporal. Incluir en get() cuando se elimine el código de prueba
        return self.tmp_create_user_qr(qr_id, username)


class UserQrTestCreateView(SignupRequiredMixin, CreateView):
    model = UserQr

    def get(self, request, *args, **kwargs):
        import random
        qr_id = random.randint(1, 25)
        username = self.request.user

        kwargs['pk'] = qr_id
        return UserQrCreateView.tmp_create_user_qr(qr_id, username)


class UserQrGetHintView(SignupRequiredMixin, CreateView):
    model = UserQr

    def get(self, request, *args, **kwargs):
        qr_id = self.kwargs['pk']
        username = self.request.user

        # Update userqr entry (was created when entering in the qr-details view) and redirect to qr details view
        (
            UserQr.objects
            .filter(qr_id=qr_id, user=username)
            .update(hints=F('hints') + 1, value=F('value') - 1)
        )

        return redirect('qr-detail', pk=qr_id)
