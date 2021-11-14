from django.shortcuts import render
from blog.models import Post, Author, PostLink


# Create your views here.
def blogHome(request):
	recentPosts = Post.objects.order_by('created').reverse()
	posts = []
	for post in recentPosts:
		links = post.postlink.all()
		posts.append([post, links])

	myInfo = Author.objects.get(pk=1)

	context = {"recentPosts": posts, "myInfo": myInfo}

	return render(request, "blog/home.html", context)
