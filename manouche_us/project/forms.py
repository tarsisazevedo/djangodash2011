from django.forms import ModelForm

from project.models import Project

class SubmitProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ("source", )
