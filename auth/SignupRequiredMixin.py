from django.contrib.auth.mixins import LoginRequiredMixin


class SignupRequiredMixin(LoginRequiredMixin):
    """
    This mixin is used to redirect unauthenticated users to signup view, rather to login view
    """
    login_url = 'signup'
