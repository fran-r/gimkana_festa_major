from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def _clean_email(form):
    """
    ensure that email is always lower case and unique.
    """
    email = form.cleaned_data['email'].lower()
    if User.objects.filter(email=email).exists():
        raise ValidationError("Ya existe un usuario con este email.")
    return email


def _clean_username(form):
    """
    ensure that username is always lower case.
    """
    return form.cleaned_data['username'].lower()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Usuario', help_text='*')
    email = forms.EmailField(max_length=100, help_text='*')
    password1 = forms.CharField(
        widget=forms.HiddenInput,
        empty_value='G1mkana$',
    )
    password2 = forms.CharField(
        widget=forms.HiddenInput,
        empty_value='G1mkana$',
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        return _clean_email(self)

    def clean_username(self):
        return _clean_username(self)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Usuario', help_text='*')
    password = forms.CharField(
        widget=forms.HiddenInput,
        empty_value='G1mkana$',
    )

    def clean_username(self):
        return _clean_username(self)
