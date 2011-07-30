from django.utils import unittest

from project.forms import SubmitProjectForm

class TestForms(unittest.TestCase):

    def test_submit_form_should_have_only_project_url_field(self):
        form = SubmitProjectForm()
        self.assertEquals(form.fields.keys(), ['url'])
