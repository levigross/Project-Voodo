# -*- coding: UTF-8 -*-
from django.conf.urls import patterns,include, url
from portfolio.views import ViewProject, CreateProject, UpdateProject, DeleteProject, ListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'view/(?P<public_id>[0-9a-z]*)/(?P<slug>[-\w]+)/$', ViewProject.as_view(), name='portfolio_view'),
    url(r'create/$', CreateProject.as_view(), name= 'portfolio_create'),
    url(r'edit/(?P<public_id>[0-9a-z]*)/(?P<slug>[-\w]+)/$', UpdateProject.as_view(), name='portfolio_update'),
    url(r'delete/(?P<slug>[-\w]+)/$', DeleteProject.as_view(), name='portfolio_delete'),
    url(r'list/$', ListView.as_view(), name='portfolio_list'),
    url(r'^admin/', include(admin.site.urls)),
    )
