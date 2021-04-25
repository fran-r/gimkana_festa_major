from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView

from auth.SignupRequiredMixin import SignupRequiredMixin

from .models import User
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class UserListView(ListView):
#class UserListView(SignupRequiredMixin, ListView):
    model = User

    # queryset = GimkanaUser.objects
    #
    # def get_queryset(self, *args, **kwargs):
    #     return self.queryset.all().prefetch_related('user_qrs')
