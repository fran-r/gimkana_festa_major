from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from gimkana import utils


class IsStartedMixin(UserPassesTestMixin):
    def test_func(self):
        return utils.is_started() or self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('not-started')
