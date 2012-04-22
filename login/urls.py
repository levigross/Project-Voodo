# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
	url(r'^login/', 'login.views.Login', name='login-page'),
    

