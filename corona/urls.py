from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import SignupForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home, name = "home"),        
    url('^stats/$', views.live_stat, name = "stats"),        
    url('^accounts/profile/$', views.home, name='index'),
    url('^profile/$', views.profile, name='profile'),
    url(r'^profile/visit/(\d+)$', views.visitprofile, name='visitprofile'),
    url('^profile/edit/$', views.editprofile, name='editprofile'),
    url('^register/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_account, name='activate'),
    url(r'^login/$', views.signIn, name='login'),     
    url(r'^patients_overview/$', views.patients_overview, name='panel'),
    url('contact/new/', views.profile, name = 'new-contact'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
