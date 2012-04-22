from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'signup.views.home', name='home'),
	url(r'^signup/', include('signup.urls') ),
)