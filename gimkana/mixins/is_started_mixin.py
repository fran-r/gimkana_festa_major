from django.contrib.auth.mixins import AccessMixin

from gimkana.utils import is_started


class IsStartedMixin(AccessMixin):
    if not is_started():
        template_name = 'gimkana/not_started.html'
