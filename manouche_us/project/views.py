from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from project.forms import SubmitProjectForm
from project.models import Project
from project.analyzer import PEP8Analyzer
from project.achievements import PEP8Achievement

def index(request):
    if request.method == "POST":
        form = SubmitProjectForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect("/%s/result/" % instance.id)
    else:
        form = SubmitProjectForm()

    context = {}
    context['form'] = form
    return TemplateResponse(request, "index.html", context)

def analyze_project(request, project_id):
    project = Project.objects.get(id=project_id)
    pep8_analyzer = PEP8Analyzer(project)
    result_pep8 = pep8_analyzer.analyze()
    pep8_badge = PEP8Achievement(result_pep8)
    context = {}
    context['achievements'] = [pep8_badge.get_achievement()]

    return TemplateResponse(request, "project/result.html", context)
