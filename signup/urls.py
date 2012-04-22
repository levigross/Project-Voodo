from django.conf.urls.defaults import patterns, url
from signup.views import SiteSignup

urlpatterns = patterns('',
    url(r'^$', SiteSignup.as_view(), name='site_signup'),
)
