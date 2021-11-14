from django.contrib import admin
from blog.models import Post, Author, PostLink


class postLinkAdmin(admin.StackedInline):
	model = PostLink

@admin.register(Author)
class authorAdmin(admin.ModelAdmin):
	list_display = ("user", "id")

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "created", "id")
	inlines = [postLinkAdmin]
