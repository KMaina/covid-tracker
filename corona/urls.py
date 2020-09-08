from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import SignupForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name = "home"),        
    url(r'^stats/$', views.live_stat, name = "stats"),            
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/visit/(\d+)$', views.visitprofile, name='visitprofile'),
    url(r'^profile/edit/$', views.editprofile, name='editprofile'),
    url(r'^register/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_account, name='activate'),
    url(r'^login/$', views.signIn, name='login'),     
    url(r'^patients_overview/$', views.patients_overview, name='panel'),
    url(r'contact/new/', views.profile, name = 'new-contact'),
    url(r'^doctor/verification/$', views.doc_su, name='doc_su'),
    url(r'^doctor/verification/confirm_doctor/(\d+)$', views.make_doctor, name='make_doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
