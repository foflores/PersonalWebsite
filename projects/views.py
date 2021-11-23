from django.shortcuts import render, get_object_or_404
from django.conf import settings
from blog.models import Author
from projects.models import Project, ProjectPreview
from markdown import markdown
from os import path


# Create your views here.
def projectsHome(request):
	recentProjects = Project.objects.order_by('created').reverse()
	myInfo = None
	if Author.objects.filter(id=1):
		myInfo = Author.objects.filter(id=1)[0]
	context = {"recentProjects": recentProjects, "myInfo": myInfo}

	return render(request, "projects/home.html", context)

def projectsDetail(request):
	project = get_object_or_404(Project, slug=request.path[1:])
	projectPreviews = ProjectPreview.objects.filter(project=project.id)

	readme = ""
	previews = []
	print(f"{settings.MEDIA_ROOT}{project.readme}")
	if path.isfile(f"{settings.MEDIA_ROOT}{project.readme}"):
		with open(f"{settings.MEDIA_ROOT}{project.readme}", "r", encoding="utf-8") as f:
			readme += markdown(f.read(), extensions=['tables', 'toc'])

	for preview in projectPreviews:
		previews.append(f"{settings.MEDIA_URL}{preview.preview}")

	context = {"readme": readme, "previews": projectPreviews}

	return render(request, 'projects/detail.html', context)
