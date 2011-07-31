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
            return HelloGuido()

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

class HelloGuido(object):
    pass
