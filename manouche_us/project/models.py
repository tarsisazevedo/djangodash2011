import tarfile
import uuid
import urllib2

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
        tar_path = self.download_project()
        return File(tar_path)

    def extract_code(self):
        source_tar = self.get_source()
        source = tarfile.open(source_tar.file)

        self.source = settings.MEDIA_URL + "sources/extracted/%s/" % uuid.uuid4()
        source.extractall(path=self.source)
        self.save()

    def download_project(self):
        import ipdb;ipdb.set_trace()
        url = self.url
        if not url.endswith("/"):
            url += "/"
        request_package = urllib2.Request(self.url + "tarball/master")
        package = urllib2.urlopen(request_package)
        local_name = package.info()["Content-Disposition"].split('filename=')[1]
        file_package = open(settings.MEDIA_URL + "sources/" + local_name, "wb")
        file_package.write(package.read())
        file_package.close()

        return settings.MEDIA_URL + "sources/" + local_name
