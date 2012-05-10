from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
from basesite.views import HomePage, Contact, About

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^$', HomePage.as_view(), name="home_page"),
    url('^contact/$', Contact.as_view(), name="contact_page"),
    url('^about/$', About.as_view(), name="about_page"),
    url(r'^login/', include('login.urls')),
    url(r'^signup/', include('signup.urls') ),
    url('^portfolio/', include('portfolio.urls')),
)
