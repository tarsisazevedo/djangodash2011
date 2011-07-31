from django.conf import settings


class PEP8Achievement(object):
    FAKE_PYTHONIST = 300
    NEWBIE_PYTHONIST = 100
    SENIOR_PYTHONIST = 30
    U_ARE_PYTHONIC = 15
    GUIDO = 0

    def __init__(self, result_pep8):
        self.result = result_pep8

    def get_achievement(self):
        if self.result > self.FAKE_PYTHONIST:
            return FakePythonist(self.result)
        elif self.result > self.NEWBIE_PYTHONIST:
            return NewbiePythonist(self.result)
        elif self.result > self.SENIOR_PYTHONIST:
            return SeniorPythonist(self.result)
        elif self.result > self.U_ARE_PYTHONIC:
            return YouArePythonic(self.result)
        elif self.result == self.GUIDO:
            return HelloGuido(self.result)

class FakePythonist(PEP8Achievement):
    name = "Fake Pythonist"
    image = settings.STATIC_ROOT + "/img/fake_pythonist.png"

class NewbiePythonist(PEP8Achievement):
    name = "Newbie Pythonist"
    image = settings.STATIC_ROOT + "/img/newbie_pythonist.png"

class SeniorPythonist(PEP8Achievement):
    name = "Senior Pythonist"
    image = settings.STATIC_ROOT + "/img/senior_pythonist.png"

class YouArePythonic(PEP8Achievement):
    name = "You are pythonic"
    image = settings.STATIC_ROOT + "/img/u_are_pythonic.png"

class HelloGuido(PEP8Achievement):
    name = "Hello Guido"
    image = settings.STATIC_ROOT + "/img/guido.png"


class CloneDiggerAchivement(object):
    YOU_ARE_GOD = 80
    MANY_CHILDRENS = 50
    KILL_THE_CLONES = 20

    def __init__(self, result):
        self.result = result

    def get_achievement(self):
        if self.result > self.YOU_ARE_GOD:
            return YouAreGod(self.result)
        elif self.result > self.MANY_CHILDRENS:
            return ManyChildren(self.result)
        else:
            return KillTheClones(self.result)

class YouAreGod(CloneDiggerAchivement):
    name = "You are God"
    image = settings.STATIC_ROOT + "/img/you_are_god.png"

class ManyChildren(CloneDiggerAchivement):
    name = "Many children"
    image = settings.STATIC_ROOT + "/img/many_children.png"

class KillTheClones(CloneDiggerAchivement):
    name = "Kill the clones"
    image = settings.STATIC_ROOT + "/img/kill_the_clones.png"

