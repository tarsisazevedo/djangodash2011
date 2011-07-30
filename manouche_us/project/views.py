from django.template.response import TemplateResponse

from project.forms import SubmitProjectForm


def index(request):
    form = SubmitProjectForm()
    return TemplateResponse(request, "index.html", {"form": form})
