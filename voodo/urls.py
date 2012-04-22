from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from signup.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',HomeView.as_view(), name='home'),
	url(r'^signup/', include('signup.urls') ),
)