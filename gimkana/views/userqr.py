from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import F, Count, Sum, Case, When
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView

from auth import SignupRequiredMixin
from ..mixins import IsStartedMixin
from ..models import UserQr, Qr
from ..tables import UsersTable
from .. import utils


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


class UserQrCreateView(SignupRequiredMixin, IsStartedMixin, CreateView):
    model = UserQr

    @staticmethod
    def create_user_qr(qr, username):
        # Create userqr entry and redirect to qr details view
        user_qr, is_new = UserQr.objects.get_or_create(qr_id=qr.id, user=username,
                                                       defaults={
                                                           'is_shop': qr.is_shop,
                                                           'scan_date': datetime.now(),
                                                           'value': qr.value,
                                                       })
        # Preserve the first scan_date on subsequent scans
        if not user_qr.scan_date: 
            user_qr.scan_date = datetime.now()
            user_qr.value = user_qr.value if not utils.is_finished() else 0
            user_qr.save(update_fields=['scan_date', 'value'])

        return redirect('qr-detail', pk=qr.id)

    def get(self, request, *args, **kwargs):
        qr = Qr.objects.get(pk=self.kwargs['pk'])
        username = self.request.user
        return self.create_user_qr(qr, username)


class UserQrTestCreateView(SignupRequiredMixin, CreateView):
    model = UserQr

    def get(self, request, *args, **kwargs):
        import random
        qr_id = random.randint(1, 25)
        username = self.request.user

        kwargs['pk'] = qr_id
        return UserQrCreateView.create_user_qr(qr_id, username, 5)


class UserQrGetHintView(SignupRequiredMixin, IsStartedMixin, CreateView):
    model = UserQr

    def get(self, request, *args, **kwargs):
        qr_id = self.kwargs['pk']
        username = self.request.user

        queryset = UserQr.objects.filter(qr_id=qr_id, user=username)
        userqr = queryset.first()
        if userqr.hints < 2:
            queryset.update(hints=F('hints') + 1, value=F('value') - 1)
        else:
            queryset.update(hints=F('hints') + 1, value=0, scan_date=datetime.now())

        return redirect('qr-detail', pk=qr_id)


@staff_member_required(login_url='/')
def active_user_list_view(request):
    num_users = User.objects.filter(is_staff=False).count()

    table_queryset = (
        UserQr.objects
        .filter(user__is_staff=False, scan_date__isnull=False)
        .exclude(value=0)
        .values('user__username', 'user__email')
        .annotate(
            score=Sum('value'),
            num_qrs=Count(Case(When(is_shop=False, then=1))),
            num_shops=Count(Case(When(is_shop=True, then=1))),
            num_hints=Sum('hints'),
        )
        .order_by('-score', '-num_qrs', '-num_shops', 'num_hints')
    )
    table = UsersTable(table_queryset)
    return render(request, 'auth/user_list.html', {'table': table, 'num_users': num_users})
