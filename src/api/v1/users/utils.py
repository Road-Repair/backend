from django.conf import settings
from rest_framework.response import Response


def set_refresh_cookie(
    response: Response,
    data: dict
) -> Response:
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_REFRESH"],
        value=data["refresh"],
        expires=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
        secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )


def set_access_cookie(
    response: Response,
    data: dict
) -> Response:
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE"],
        value=data["access"],
        expires=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
        secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )
