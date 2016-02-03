from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

#include stuff
from website.views.home.view import Home
from website.views.services.view import Services
from website.views.work.view import Work
from website.views.ethos.view import Ethos
from website.views.contact.view import Contact

urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home.index', name='home'),
    # url(r'^$', include('website.views.home.index')),
    url(r'^$', Home.as_view()),
    url(r'^services/$', Services.as_view()),
    url(r'^work/$', Work.as_view()),
    url(r'^ethos/$', Ethos.as_view()),
    url(r'^contact/$', Contact.as_view()),
    #url(r'^bugs/$', 'website.views.android_bug.view.bug'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

