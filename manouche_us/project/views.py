from django.template.response import TemplateResponse

from project.forms import SubmitProjectForm


def index(request):
    form = SubmitProjectForm()

    context = {}
    context['form'] = form
    return TemplateResponse(request, "index.html", context)
