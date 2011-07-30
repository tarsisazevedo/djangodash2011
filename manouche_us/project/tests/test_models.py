import os
import mimetypes

from django.conf import settings
from django.utils import unittest

from project.models import Project, ProjectUrlException


class TestModels(unittest.TestCase):
    def test_create_a_project(self):
        project = Project.objects.create(url="foo")
        self.assertTrue(project)

    def test_url_should_be_from_github(self):
        project = Project.objects.create(url="github.com")
        self.assertTrue(project.validate_url())

    def test_url_should_not_be_from_github(self):
        project = Project.objects.create(url="foo")
        self.assertFalse(project.validate_url())

    def test_get_source_of_project(self):
        project = Project.objects.create(url="media/sources/fake-github.tar.gz")
        source = project.get_source()

        self.assertEquals(source.file, settings.MEDIA_URL + "sources/fake-github.tar.gz")
        self.assertEquals(mimetypes.guess_type(source.file), ('application/x-tar', 'gzip'))

    def test_validate_url_is_github_to_download_source(self):
        project = Project.objects.create(url="foo")

        self.assertRaises(ProjectUrlException, project.get_source)

    def test_extract_source_from_tar_file(self):
        project = Project.objects.create(url="media/sources/fake-github.tar.gz")

        source_extracted = project.extract_code()

        self.assertTrue(project.source)
        os.system("rm -Rf %s" % os.path.join(settings.PROJECT_ROOT, project.source))
