from django.shortcuts import render
from blog.models import Post
from blog.models import Author

def homeView(request):
	recentProjects = Post.objects.order_by('dateCreated')[:3]
	personalInfo = Author.objects.first()

	context = {"recentProjects": recentProjects, "personalInfo": personalInfo}
	return render(request, "home.html", context)
