from django.db import models
from django.conf import settings
from django.utils import timezone


# Paths for file storage
def pathUserFiles(instance, filename):
	return f"users/{instance.user.id}/{filename}"


# Models
class Author(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=pathUserFiles, blank=True, null=True)
	aboutMe = models.TextField(blank=True, null=True)
	github = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)
	resume = models.FileField(upload_to=pathUserFiles, blank=True, null=True)

	def __str__(self):
		return self.user.username


class Post(models.Model):
	slug = models.SlugField(null=True, blank=True)
	showPost = models.BooleanField(default=True)
	created = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	text = models.TextField()

	def __str__(self):
			return self.title

	class Meta():
		get_latest_by = "created"

class PostLink(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postlink")
	title = models.CharField(max_length=50, blank=True, null=True)
	link = models.URLField(blank=True, null=True)
