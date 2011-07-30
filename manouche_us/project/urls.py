from django.conf.urls.defaults import *

urlpatterns = patterns("project.views",
                        url(r"^$", 'index', name="index"),
                      )
