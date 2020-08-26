from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.home, name = "home"),
    url('^index/$', views.index_test, name='index'),
    url('^register/$', views.signup, name='signup'),
]