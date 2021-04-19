from django.contrib.auth.mixins import LoginRequiredMixin


class SignupRequiredMixin(LoginRequiredMixin):
    login_url = 'signup'
