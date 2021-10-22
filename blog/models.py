from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
	dateCreated = models.DateTimeField(default=now)
	show = models.BooleanField(default=True)
	image = models.ImageField(blank=True, null=True)
	title = models.CharField(max_length=50)
	text = models.TextField()
	link = models.URLField(blank=True, null=True)

	class Meta():
		get_latest_by = "dateCreated"

class Author(models.Model):
	image = models.ImageField(blank=True, null=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	aboutMe = models.TextField()
	github = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)
