from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'manouche_us.views.home', name='home'),
    url(r'^manouche_us/', include('manouche_us.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
