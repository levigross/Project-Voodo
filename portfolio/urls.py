# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from portfolio.views import ViewPortfolio

urlpatterns = patterns('',
    url(r'^view/(?P<public_id>[0-9a-z]*)/$', ViewPortfolio.as_view(), name='portfolio_view'),
    url(r'^create/$', '', name= 'portfolio_create'),
    url(r'^edit/(?P<public_id>[0-9a-z]*)/', '', name='portfolio_edit'),
    url(r'^delete/(?P<public_id>[0-9a-z]*)/', '', name='portfolio_delete'),
)
