from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.users.views import UserViewSet

v1_router = DefaultRouter()

v1_router.register("users", UserViewSet)

urlpatterns = [
    path("", include(v1_router.urls)),
]
