"""
Module to aggregate all code analyzers
"""
import os
from django.conf import settings

from project.models import Project

class BaseAnalyzer(object):
    def __init__(self, project_id):
        self.project = Project.objects.get(id=project_id)

    def _extract_project_code_from_source(self):
        self.project.extract_code()

    def _remove_extracted_code(self):
        os.system("rm -Rf %s" % os.path.join(
            settings.PROJECT_ROOT,self.project.source))

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
