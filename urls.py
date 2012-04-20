# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'login.views.home', name='home'),
	url(r'^login/', include('login.urls') ),
)