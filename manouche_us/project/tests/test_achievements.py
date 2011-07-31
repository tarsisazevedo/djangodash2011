from django.utils import unittest
from django.conf import settings

from project.achievements import PEP8Achievement, FakePythonist, NewbiePythonist

class TestPEP8Achievement(unittest.TestCase):
    def test_fake_pythonist_achievement(self):
        pep8_result = 301
        pep8_achievement = PEP8Achievement(pep8_result).get_achievement()

        self.assertTrue(isinstance( pep8_achievement, FakePythonist ))
        self.assertEquals(pep8_achievement.name, "Fake Pythonist")
        self.assertEquals(pep8_achievement.image, settings.STATIC_ROOT + '/img/fake_pythonist.png')

    def test_newbie_pythonist_achievement(self):
        pep8_result = 101
        pep8_achievement = PEP8Achievement(pep8_result).get_achievement()

        self.assertTrue(isinstance( pep8_achievement, NewbiePythonist ))
        self.assertEquals(pep8_achievement.name, "Newbie Pythonist")
        self.assertEquals(pep8_achievement.image, settings.STATIC_ROOT + '/img/newbie_pythonist.png')
