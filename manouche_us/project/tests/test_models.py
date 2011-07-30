import mimetypes

from django.conf import settings
from django.utils import unittest

from project.models import Project


class TestModels(unittest.TestCase):
    def test_create_a_project(self):
        project = Project.objects.create(url="foo")
        self.assertTrue(project)

    def test_url_should_be_from_github(self):
        project = Project.objects.create(url="github.com")
        self.assertTrue(project.validate_url())

    def test_get_source_of_project(self):
        project = Project.objects.create(url="media/sources/fake.tar.gz")
        source = project.get_source()

        self.assertEquals(source.file, settings.MEDIA_URL + "sources/fake.tar.gz")
        self.assertEquals(mimetypes.guess_type(source.file), ('application/x-tar', 'gzip'))
