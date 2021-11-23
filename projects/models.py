from django.db import models
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
import os
import shutil

# Paths for file storage
def pathProject(instance, filename):
	return f"projects/{instance.slug}/{filename}"

def pathProjectPreviews(instance, filename):
	return f"projects/{instance.project.slug}/previews/{filename}"

# Models
class Project(models.Model):
	showProject = models.BooleanField(default=True)
	slug = models.SlugField(unique=True)
	created = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, related_name="project")
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	icon = models.ImageField(upload_to=pathProject, blank=True, null=True)
	readme = models.FileField(upload_to=pathProject, blank=True, null=True)
	github = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta():
		get_latest_by = "created"

class ProjectPreview(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=50, blank=True, null=True)
	preview = models.FileField(upload_to=pathProjectPreviews, null=True, blank=True)

# Delete files on project delete
@receiver(models.signals.post_delete, sender=ProjectPreview)
def delete_files(sender, instance, *args, **kwargs):
	if instance.preview and os.path.isfile(instance.preview.path):
		os.remove(instance.preview.path)

@receiver(models.signals.post_delete, sender=Project)
def delete_files(sender, instance, *args, **kwargs):
	if instance and os.path.isdir(f"{settings.MEDIA_ROOT}projects/{instance.slug}"):
		shutil.rmtree(f"{settings.MEDIA_ROOT}projects/{instance.slug}")
