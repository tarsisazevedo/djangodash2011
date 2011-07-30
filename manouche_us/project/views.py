from django.template.response import TemplateResponse

from project.forms import SubmitProjectForm


def index(request):
    if request.method == "POST":
        form = SubmitProjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubmitProjectForm()

    context = {}
    context['form'] = form
    return TemplateResponse(request, "index.html", context)
