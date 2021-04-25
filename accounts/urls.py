from django.conf.urls import url
from django.contrib.auth.views import LoginView

from .forms import LoginForm
from .views import signup, UserListView

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$',
        LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm),
        name='login'),
    url(r'^users/$', UserListView.as_view(), name='users')
]
