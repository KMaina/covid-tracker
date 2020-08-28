from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.home, name = "home"),
    url('^index/$', views.index_test, name='index'),
    url('contact/new/', views.create_contact, name = 'new-contact'),
    url('accounts/profile/(?P<username>[-_\w.]+)$', views.profile, name= 'profiles'),
]