from django.db import models
from django.core.files import File


class ProjectUrlException(Exception):
    pass

class Project(models.Model):
    url = models.URLField()

    def validate_url(self):
        return "github" in self.url

    def get_source(self):
        if not self.validate_url():
            raise ProjectUrlException()
        return File(self.url)
