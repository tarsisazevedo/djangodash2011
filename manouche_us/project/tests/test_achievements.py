from django.utils import unittest
from django.conf import settings

from project.achievements import PEP8Achievement, FakePythonist, NewbiePythonist, SeniorPythonist, YouArePythonic, HelloGuido
from project.achievements import CloneDiggerAchivement, YouAreGod, ManyChildren


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

    def test_senior_pythonist_achievement(self):
        pep8_result = 31
        pep8_achievement = PEP8Achievement(pep8_result).get_achievement()

        self.assertTrue(isinstance( pep8_achievement, SeniorPythonist ))
        self.assertEquals(pep8_achievement.name, "Senior Pythonist")
        self.assertEquals(pep8_achievement.image, settings.STATIC_ROOT + '/img/senior_pythonist.png')

    def test_u_are_pythonist_achievement(self):
        pep8_result = 16
        pep8_achievement = PEP8Achievement(pep8_result).get_achievement()

        self.assertTrue(isinstance( pep8_achievement, YouArePythonic ))
        self.assertEquals(pep8_achievement.name, "You are pythonic")
        self.assertEquals(pep8_achievement.image, settings.STATIC_ROOT + '/img/u_are_pythonic.png')

    def test_guido_achievement(self):
        pep8_result = 0
        pep8_achievement = PEP8Achievement(pep8_result).get_achievement()

        self.assertTrue(isinstance( pep8_achievement, HelloGuido ))
        self.assertEquals(pep8_achievement.name, "Hello Guido")
        self.assertEquals(pep8_achievement.image, settings.STATIC_ROOT + '/img/guido.png')

class TestCloneDigger(unittest.TestCase):
    def test_you_are_god(self):
        clone_digger_result = 81.0
        clone_digger_achievement = CloneDiggerAchivement(clone_digger_result).get_achievement()

        self.assertTrue(isinstance( clone_digger_achievement, YouAreGod ))
        self.assertEquals(clone_digger_achievement.name, "You are God")
        self.assertEquals(clone_digger_achievement.image, settings.STATIC_ROOT + "/img/you_are_god.png")

    def test_many_chidlren(self):
        clone_digger_result = 51.0
        clone_digger_achievement = CloneDiggerAchivement(clone_digger_result).get_achievement()

        self.assertTrue(isinstance( clone_digger_achievement, ManyChildren ))
        self.assertEquals(clone_digger_achievement.name, "Many children")
        self.assertEquals(clone_digger_achievement.image, settings.STATIC_ROOT + "/img/many_children.png")
