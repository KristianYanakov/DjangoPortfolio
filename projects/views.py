from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()

    # return HttpResponse("HELLO WORKING")
    return render(request, 'project_list_designed.html', {'projects': projects})

def single_project(request, project_id):
    # project = Project.objects.get(id=project_id) # my way works but if the id is invalid doesnt return an error

    project = get_object_or_404(Project, id=project_id)
    return render(request, 'single_project.html', {'project': project})




