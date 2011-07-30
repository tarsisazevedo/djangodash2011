from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from project.forms import SubmitProjectForm


def index(request):
    if request.method == "POST":
        form = SubmitProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/wait/")
    else:
        form = SubmitProjectForm()

    context = {}
    context['form'] = form
    return TemplateResponse(request, "index.html", context)
