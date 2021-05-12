from django.contrib.auth.models import User
from django.views.generic import ListView

from auth.SignupRequiredMixin import SignupRequiredMixin


class UserListView(SignupRequiredMixin, ListView):
    model = User

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['num_users'] = User.objects.count()
        return context
