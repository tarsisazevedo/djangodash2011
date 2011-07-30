from django.forms import ModelForm, ValidationError

from project.models import Project

class SubmitProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = ("source", )

    def clean_url(self):
        self.instance.url = self.data['url']
        if not self.instance.validate_url():
            raise ValidationError("Url should be from github.com! I'm a fanboy :D")

        return self.cleaned_data['url']
