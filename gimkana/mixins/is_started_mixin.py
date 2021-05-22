from django.views.generic.base import TemplateResponseMixin

from gimkana.utils import is_started


class IsStartedMixin(TemplateResponseMixin):
    if not is_started():
        template_name = 'gimkana/not_started.html'
