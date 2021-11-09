from django.db import models
from django.utils.timezone import now

class Author(models.Model):
	image = models.URLField(blank=True, null=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	aboutMe = models.TextField()
	github = models.URLField(blank=True, null=True)
	linkedin = models.URLField(blank=True, null=True)
	resume = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name

class Project(models.Model):
	dateCreated = models.DateTimeField(default=now)
	icon = models.URLField(blank=True, null=True)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=50)
	github = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta():
		get_latest_by = "dateCreated"

class Post(models.Model):
	showPost = models.BooleanField(default=True)
	dateCreated = models.DateTimeField(default=now)
	showIcon = models.BooleanField(default=True)
	icon = models.URLField(blank=True, null=True)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
	title = models.CharField(max_length=50)
	text = models.TextField()
	linkTitle = models.CharField(max_length=50, blank=True, null=True)
	link = models.URLField(blank=True, null=True)

	def __str__(self):
		return f"{self.dateCreated} | {self.title}"

	class Meta():
		get_latest_by = "dateCreated"
