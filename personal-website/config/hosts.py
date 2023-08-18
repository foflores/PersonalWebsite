from django_hosts import patterns, host
from django.contrib import admin


host_patterns = patterns('',
	host("admin", "config.urls", name="admin"),
	host("blog", "blog.urls", name="blog"),
	host("projects", "projects.urls", name="projects"),
)
