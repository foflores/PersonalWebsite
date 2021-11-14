from django.contrib import admin
from projects.models import Project, ProjectPreview

# Register your models here.
class projectPreviewAdmin(admin.StackedInline):
	model = ProjectPreview

@admin.register(Project)
class projectAdmin(admin.ModelAdmin):
	list_display = ("name", "user", "id")
	inlines = [projectPreviewAdmin]
