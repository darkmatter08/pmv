# Shawn Jain
# 8/20/2013
# PriceMyVet

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from pmv.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmv.views.home', name='home'),
    # url(r'^pmv/', include('pmv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', home),
    url(r'^test$', test),
    url(r'^submit$', submit),
)
