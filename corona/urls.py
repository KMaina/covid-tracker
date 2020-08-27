from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.home, name = "home"),
    url('^index/$', views.index_test, name='index'),
    url('^accounts/profile/$', views.index_test, name='profile'),
    url('^register/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
]