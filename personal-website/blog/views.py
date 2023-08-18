from django.shortcuts import render
from blog.models import Post, Author, PostLink


# Create your views here.
def blogHome(request):
	recentPosts = Post.objects.order_by('created').reverse()
	posts = []
	for post in recentPosts:
		links = post.postlink.all()
		posts.append([post, links])

	myInfo = None
	if Author.objects.filter(id=1):
		myInfo = Author.objects.filter(id=1)[0]

	context = {"recentPosts": posts, "myInfo": myInfo}

	return render(request, "blog/home.html", context)
