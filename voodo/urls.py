# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

from login.views import HomeView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^login/', include('login.urls')),
)