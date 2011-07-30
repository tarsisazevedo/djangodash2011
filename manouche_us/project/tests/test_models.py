from django.util import unittest
from project.models import Project

class TestModels(unittest.TestCase):
    def test_create_a_project(self):
        project = Project.objects.create(url="foo")
        self.assertTrue(project)
