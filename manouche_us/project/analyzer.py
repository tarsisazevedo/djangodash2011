"""
Module to aggregate all code analyzers
"""
import os
from django.conf import settings


class BaseAnalyzer(object):

    def __init__(self, project):
        self.project = project

    def _extract_project_code_from_source(self):
        self.project.extract_code()

    def _remove_extracted_code(self):
        os.system("rm -Rf %s" % os.path.join(
            settings.PROJECT_ROOT, self.project.source))

    def get_project_modules(self):
        self._extract_project_code_from_source()
        modules = [directory for directory in os.listdir(self.project.source)
                    if os.path.isdir(
                        os.path.join(self.project.source, directory)
                    )
                  ]
        return modules

    def analyze(self):
        raise NotImplementedError


class PyLintAnalyzer(BaseAnalyzer):

    def __init__(self, project):
        super(BaseAnalyzer, self).__init__()
        self.config_file_path = os.path.join(
            settings.ANALYZERS_CONFIGURATION_DIR, 'pylint.cfg')

    def analyze(self):
        pass
