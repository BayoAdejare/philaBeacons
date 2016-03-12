from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^dashboard/$', 'beacons.views.dashboard', name='dashboard'),
    url(r'^report/$', 'beacons.views.report', name='report'),
    url(r'^checkin/$', 'beacons.views.checkin_beacon', name='checkin'),
    url(r'^beacon/(.*)$', 'beacons.views.get_beacon', name='home'),
    url(r'^$', 'beacons.views.dashboard', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)