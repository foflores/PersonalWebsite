from django_hosts import patterns, host


host_patterns = patterns('',
	host("admin", "config.urls", name="admin"),
	host("blog", "blog.urls", name="blog"),
	host(r"^projects?$", "projects.urls", name="projects"),
)
