# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url
from portfolio.views import ViewProject, CreateProject, UpdateProject

urlpatterns = patterns('',
    url(r'^view/(?P<public_id>[0-9a-z]*)/(?P<slug>[-\w]+)/$', ViewProject.as_view(), name='portfolio_view'),
    url(r'^create/$', CreateProject.as_view(), name= 'portfolio_create'),
    url(r'^edit/(?P<public_id>[0-9a-z]*)/(?P<slug>[-\w]+)$/', UpdateProject.as_view(), name='portfolio_update'),
    url(r'^delete/(?P<public_id>[0-9a-z]*)/(?P<slug>[-\w]+)$/', '', name='portfolio_delete'),
)
