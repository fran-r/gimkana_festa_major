from django.conf.urls import url
from django.contrib.auth.views import LoginView

from accounts import views as account_views
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^login/$',
        LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm),
        name='login'),
]
