from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from ..models import UserTest


class UserTestListView(LoginRequiredMixin, ListView):
    model = UserTest


class UserTestDetailView(LoginRequiredMixin, DetailView):
    model = UserTest
