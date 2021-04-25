from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.index, name='index', ),
    # url(r'^$', views.QrListView.as_view(), name='qrs'),
    url(r'^$', views.QrScannedListView.as_view(), name='qrs'),
    # url(r'^qrs/$', views.QrListView.as_view(), name='qrs'),

    url(r'^qrs/$', views.QrScannedListView.as_view(), name='qrs'),

    url(r'^qrscan/$', views.qrscan.UserQrTestCreateView.as_view(), name='qrscan-test'),
    url(r'^qrscan/(?P<qr_id>.+)$', views.UserQrCreateView.as_view(), name='qrscan'),

    url(r'^qr/(?P<pk>.+)$', views.QrDetailView.as_view(), name='qr-detail'),
    # url(r'^addqr/(?P<pk>\d+)$', views.QrCreateView.as_view(), name='qr-create'),
    url(r'^myqrs/$', views.UserQrListView.as_view(), name='myqrs'),
]
