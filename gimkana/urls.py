from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^qrs/$', views.QrListView.as_view(), name='qrs'),
    url(r'^qrscan/(?P<pk>\d+)$', views.QrScanByUserCreateView.as_view(), name='qrscan-detail'),
    url(r'^qr/(?P<pk>\d+)$', views.QrDetailView.as_view(), name='qr-detail'),
    #url(r'^addqr/(?P<pk>\d+)$', views.QrCreateView.as_view(), name='qr-create'),
    url(r'^myqrs/$', views.QrScanByUserListView.as_view(), name='myqrs'),
]
