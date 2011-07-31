import os
from django.conf import settings
from django.utils import unittest

from project.models import Project
from project.analyzer import BaseAnalyzer, PyLintAnalyzer

class BaseAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.project = Project.objects.create(url="media/sources/fake-github.tar.gz")
        self.analyzer = BaseAnalyzer(self.project)

    def tearDown(self):
        self.project.delete()

    def test_base_analyzer_get_project_modules_should_return_a_list_of_all_python_module_inside_its(self):
        python_modules = self.analyzer.get_project_modules()

        self.assertEquals(python_modules, ['manouche_us'])
        self.analyzer._remove_extracted_code()

    def test_base_analyzer_analyze_should_raises_not_implemented_error(self):
        self.assertRaises(NotImplementedError, self.analyzer.analyze)


class PyLintAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.project = Project.objects.create(url="media/sources/fake-github.tar.gz")
        self.pylint_analyzer = PyLintAnalyzer(self.project)

    def tearDown(self):
        self.project.delete()

    def test_py_lint_should_get_correct_config_file_when_instantiate(self):
        import ipdb;ipdb.set_trace()
        self.assertEquals(
            self.pylint_analyzer.config_file_path,
            os.path.join(settings.ANALYZERS_CONFIGURATION_DIR,'pylint.cfg')
        )
