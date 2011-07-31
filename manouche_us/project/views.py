from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from project.forms import SubmitProjectForm
from project.models import Project
from project.analyzer import PEP8Analyzer, ClonneDiggerAnalyzer
from project.achievements import PEP8Achievement, CloneDiggerAchivement

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

    clone_digger = ClonneDiggerAnalyzer(project)
    clone_digger_result = clone_digger.analyze()
    clone_digger_achievement = CloneDiggerAchivement(clone_digger_result)

    context = {}
    context['pep8_achievement'] = pep8_badge.get_achievement()
    context['clone_digger_achievement'] = clone_digger_achievement.get_achievement()

    return TemplateResponse(request, "project/result.html", context)
