"""
Module to aggregate all code analyzers
"""
import os

from django.conf import settings

from splinter.browser import Browser


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
        root = self.get_project_root()

        abspath_root = settings.PROJECT_ROOT + "/" + self.project.source + root + "/"
        modules = [directory for directory in os.listdir(abspath_root) if os.path.isdir(os.path.join(abspath_root, directory))]

        return modules

    def get_project_root(self):
        self._extract_project_code_from_source()
        root = [directory for directory in os.listdir(self.project.source) if os.path.isdir(os.path.join(self.project.source, directory))]

        return root[0]

    def analyze(self):
        raise NotImplementedError

class CoverageAnalyzer(BaseAnalyzer):
    def analyze(self):
        project_root = self.get_project_root()
        project_modules = self.get_project_modules()

        project_settings = self.project.source + project_root + "/settings.py"

        TEST_RUNNER = 'TEST_RUNNER = "django_nose.NoseTestSuiteRunner"'
        TESTS_APPS = "TESTS_APPS = ('django_nose',)"
        NOSE_ARGS = ['--quiet', "-sd", '--nologcapture', '--with-coverage', '--cover-erase', '--cover-html', '--cover-html-dir=' + self.project.source + project_root, '--with-spec', '--spec-color']

        MODULES = ["--cover-package=" + module for module in project_modules]
        NOSE_ARGS.extend(MODULES)
        NOSE_ARGS = "NOSE_ARGS = " + str(NOSE_ARGS)

        settings_file = open(project_settings, "a")
        settings_file.write(TEST_RUNNER + "\n")
        settings_file.write(TESTS_APPS + "\n")
        settings_file.write(NOSE_ARGS + "\n")
        settings_file.close()

        os.system("python " + self.project.source + project_root + "/manage.py test")

        browser = Browser("zope.testbrowser")
        browser.visit("file://" + settings.PROJECT_ROOT + "/" +  self.project.source + project_root + "/index.html")
        percent = browser.find_by_css("#index tfoot tr .right").text
        return int(percent.replace("%", ""))

class ClonneDiggerAnalyzer(BaseAnalyzer):
    def analyze(self):
        self.get_project_modules()
        os.system("clonedigger " + self.project.source + "/")

        infos = self._extract_infos()

        return self.format_infos(infos)

    def _extract_infos(self):
        browser = Browser("zope.testbrowser")
        browser.visit("file://" + settings.PROJECT_ROOT + "/output.html" )
        infos = browser.find_by_css("p")[3].text
        browser.quit()
        os.system("rm "  + settings.PROJECT_ROOT + "/output.html")

        return infos

    def format_infos(self, infos):
        safe_numbers = infos.partition("(")
        return float(safe_numbers[2].partition("%)")[0])

class PyLintAnalyzer(BaseAnalyzer):

    def __init__(self, project):
        super(BaseAnalyzer, self).__init__()
        self.config_file_path = os.path.join(
            settings.ANALYZERS_CONFIGURATION_DIR, 'pylint.cfg')

    def analyze(self):
        pass

class PEP8Analyzer(BaseAnalyzer):
    def analyze(self):
        self.get_project_modules()
        os.system("pep8 --statistics " + self.project.source + " --count" + " | grep ^[0-9] | cut -d' ' -f1 >> " + self.project.source + "output-pep8.txt")

        import pdb; pdb.set_trace()
