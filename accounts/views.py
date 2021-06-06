from datetime import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    username_str = '{}@gimkana.fm'.format(str(datetime.now()))
    password = 'G1mkana$'
    user = User.objects.create_user(username_str, username_str, password)
    user.save()

    user = authenticate(username=username_str, password=password)
    login(request, user)
    next_url = request.GET.get('next', '/')
    return redirect(next_url)


"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
"""