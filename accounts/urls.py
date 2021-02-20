from django.conf.urls import url

from accounts import views as account_views

urlpatterns = [
    url(r'^signup/$', account_views.signup, name='signup'),
]
