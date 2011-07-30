from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", include('project.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^wait/$", TemplateView.as_view(template_name="project/wait.html"), name="wait"),
)

urlpatterns += staticfiles_urlpatterns()
