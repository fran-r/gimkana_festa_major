from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^usertests/$', views.UserTestListView.as_view(), name='usertests'),
    url(r'^usertest/(?P<pk>.+@.+\..+)$', views.UserTestDetailView.as_view(), name='usertest-detail'),
    url(r'^qrs/$', views.QrListView.as_view(), name='qrs'),
    url(r'^qr/(?P<pk>\d+)$', views.QrDetailView.as_view(), name='qr-detail'),
    url(r'^myqrs/$', views.QrScanByUserListView.as_view(), name='myqrs'),
]
