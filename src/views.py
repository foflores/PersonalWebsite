from django.shortcuts import render
from blog.models import Post
from blog.models import Author
import markdown

def homeView(request):
	recentPosts = Post.objects.order_by('dateCreated').reverse()
	myInfo = Author.objects.get(pk=1)

	context = {"recentPosts": recentPosts, "myInfo": myInfo}
	return render(request, "home.html", context)
