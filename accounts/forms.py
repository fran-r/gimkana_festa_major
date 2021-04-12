from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
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

    class Meta:
        model = User
        fields = ('username', 'email')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Usuario', help_text='*')
    password = forms.CharField(
        widget=forms.HiddenInput,
        # TODO: use the user agent as password
        empty_value='G1mkana$',
    )
