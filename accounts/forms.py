from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


DEFAULT_PASSWORD = 'G1mkana$'


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
    # TODO: restaurar que se pueda crear cualquier usuario
    # return form.cleaned_data['username'].lower()
    if form.cleaned_data['username'].startswith('00'):
        return form.cleaned_data['username'].lower()
    else:
        return '%'


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': False})

    username = forms.CharField(max_length=100, label='Usuario', help_text='*')
    email = forms.EmailField(max_length=100, help_text='*')
    password1 = forms.CharField(
        widget=forms.HiddenInput,
        empty_value=DEFAULT_PASSWORD,
    )
    password2 = forms.CharField(
        widget=forms.HiddenInput,
        empty_value=DEFAULT_PASSWORD,
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
        empty_value=DEFAULT_PASSWORD,
    )

    def clean_username(self):
        return _clean_username(self)
