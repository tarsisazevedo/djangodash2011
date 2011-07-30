from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns("project.views",
                        url(r"^$", 'index', name="index"),
                        url(r"^wait/$", TemplateView.as_view(template_name="projects/wait.html"), name="wait"),
                      )
