from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'signup.views.signup', name='site_signup'),
)
