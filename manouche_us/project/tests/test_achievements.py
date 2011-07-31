from django.utils import unittest

from project.achievements import PEP8Achievement, FakePythonist

class TestPEP8Achievement(unittest.TestCase):
    def test_fake_pythonist_achievement(self):
        pep8_result = 301
        pep8_achievement = PEP8Achievement(pep8_result).get_achievement()

        self.assertTrue(isinstance( pep8_achievement, FakePythonist ))
        self.assertEquals(pep8_achievement.name, "Fake Pythonist")
        self.assertEquals(pep8_achievement.image, 'static/img/fake_pythonist.png')
