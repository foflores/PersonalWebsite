from django.urls import path, re_path
from projects import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path("", views.projectsHome, name="projectsHome"),
	re_path(r"^[\w]+$", views.projectsDetail, name="projectsDetail"),
] + static("/media/", document_root=settings.MEDIA_ROOT)
