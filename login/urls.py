# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

from login.views import SiteLogin

urlpatterns = patterns('',	
	url(r'^$', SiteLogin.as_view(), name='site-login'),
)