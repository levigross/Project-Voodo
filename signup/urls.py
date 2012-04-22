from django.conf.urls.defaults import patterns, url
from signup.views import SiteSignup

urlpatterns = patterns('',
    url(r'^/signup', SiteSignup.as_view(), name='site-signup'),
)
