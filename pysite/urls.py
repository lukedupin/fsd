from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#include stuff
from website.views import Home
from website.views import Services
from website.views import Work
from website.views import Ethos
from website.views import Contact

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home.index', name='home'),
    # url(r'^$', include('website.views.home.index')),
    url(r'^$', Home.as_view()),
    url(r'^services/$', Services.as_view()),
    url(r'^work/$', Work.as_view()),
    url(r'^ethos/$', Ethos.as_view()),
    url(r'^contact/$', Contact.as_view()),
    url(r'^bugs/$', 'website.views.android_bug.bug'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
