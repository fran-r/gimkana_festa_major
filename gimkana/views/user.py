from django.contrib.auth.models import User
from django.views.generic import ListView

from auth.SignupRequiredMixin import SignupRequiredMixin


class UserListView(SignupRequiredMixin, ListView):
    model = User

    # num_users = User.objects.all().count()
