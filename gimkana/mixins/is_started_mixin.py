from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from gimkana.utils import is_started


class IsStartedMixin(UserPassesTestMixin):
    def test_func(self):
        return is_started()

    def handle_no_permission(self):
        return redirect('not-started')
