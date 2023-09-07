from django.conf.urls import include
from django.urls import include, path

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
    # path(r'^$', 'website.views.home.index', name='home'),
    # path(r'^$', include('website.views.home.index')),
    path('', Home.as_view()),
    path('services/', Services.as_view()),
    path('work/', Work.as_view()),
    path('ethos/', Ethos.as_view()),
    path('contact/', Contact.as_view()),
    #path('bugs/$', 'website.views.android_bug.view.bug'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # path(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #path(r'^admin/', include(admin.site.urls)),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

