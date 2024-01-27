from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.v1.users.views import (
    AccountViewSet,
    CookieTokenRefreshView,
    LoginView,
    LogoutView,
    UserViewSet,
)

v1_router = DefaultRouter()

v1_router.register("", UserViewSet, basename="users")

urlpatterns = [
    re_path(
        r"^accounts/me/$",
        AccountViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        ),
        kwargs={"pk": "me"},
        name="accounts",
    ),
    path("registry/", include(v1_router.urls)),
    path(
        "auth/token/refresh/",
        CookieTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
