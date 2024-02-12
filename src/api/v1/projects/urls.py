from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.projects.views import ProjectViewSet

v1_ruter = DefaultRouter()
v1_ruter.register("", ProjectViewSet, basename="projects")

urlpatterns = [path("", include(v1_ruter.urls))]
