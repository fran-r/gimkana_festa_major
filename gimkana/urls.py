from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # url(r'^$', views.index, name='index', ),
    url(r'^rules/$', TemplateView.as_view(template_name="rules.html"), name='rules'),
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^$', views.QrScannedListView.as_view(), name='qrs'),
    # url(r'^qrs/$', views.QrListView.as_view(), name='qrs'),

    url(r'^qrs/$', views.QrScannedListView.as_view(), name='qrs'),

    url(r'^qrscan/$', views.userqr.UserQrTestCreateView.as_view(), name='qrscan-test'),
    url(r'^qrscan/(?P<pk>.+)$', views.UserQrCreateView.as_view(), name='qrscan'),
    url(r'^gethint/(?P<pk>.+)$', views.UserQrGetHintView.as_view(), name='get-hint'),

    url(r'^qr/(?P<pk>.+)$', views.QrDetailView.as_view(), name='qr-detail'),
    # url(r'^addqr/(?P<pk>\d+)$', views.QrCreateView.as_view(), name='qr-create'),
    url(r'^myqrs/$', views.UserQrListView.as_view(), name='myqrs'),
]
