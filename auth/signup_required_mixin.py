from django.contrib.auth.mixins import LoginRequiredMixin


# This is unnecessary. Could have been solved in settings.LOGIN_URL
class SignupRequiredMixin(LoginRequiredMixin):
    login_url = 'signup'
