from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    username = forms.CharField(max_length=100, label='Usuario', help_text='*')
    email = forms.EmailField(max_length=100, help_text='*')
    password1 = forms.CharField(
        widget=forms.HiddenInput,
        # TODO: use the user agent as password
        empty_value='G1mkana$',
    )
    password2 = forms.CharField(
        widget=forms.HiddenInput,
        # TODO: use the user agent as password
        empty_value='G1mkana$',
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Usuario', help_text='*')
    password = forms.CharField(
        widget=forms.HiddenInput,
        # TODO: use the user agent as password
        empty_value='G1mkana$',
    )
