import tarfile
import uuid

from django.db import models
from django.conf import settings
from django.core.files import File


class ProjectUrlException(Exception):
    pass

class Project(models.Model):
    url = models.URLField()
    source = models.CharField(max_length=200)

    def validate_url(self):
        return "github" in self.url

    def get_source(self):
        if not self.validate_url():
            raise ProjectUrlException()
        return File(self.url)

    def extract_code(self):
        source_tar = self.get_source()
        source = tarfile.open(source_tar.file)

        self.source = settings.MEDIA_URL + "sources/extracted/%s/" % uuid.uuid4()
        source.extractall(path=self.source)
        self.save()
