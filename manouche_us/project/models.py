from django.db import models
from django.core.files import File

class Project(models.Model):
    url = models.URLField()

    def validate_url(self):
        return "github" in self.url

    def get_source(self):
        return File(self.url)
