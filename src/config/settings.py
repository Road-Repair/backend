import os
import sys
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

TRUE_VALUES = ["1", "True", "true", "YES", "yes"]
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv("SECRET_KEY", default="yours-secret-key")
DEBUG = os.getenv("DEBUG") in TRUE_VALUES
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="*").split(", ")
PASSWORD_LENGTH = os.getenv("PASSWORD_LENGTH")
PASSWORD_SYMBOLS = os.getenv("PASSWORD_SYMBOLS")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "rest_framework.documentation",
    "drf_spectacular",
    "corsheaders",
    "users",
    "locations",
    "projects",
    "transactions",
    "news",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "config.asgi.application"
# WSGI_APPLICATION = 'config.wsgi.application'

PROD_DB = os.getenv("PROD_DB", default="true") in TRUE_VALUES
if PROD_DB and "test" not in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", default="postgres"),
            "USER": os.getenv("POSTGRES_USER", default="postgres"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
            "HOST": os.getenv("DB_HOST", default="db"),
            "PORT": os.getenv("DB_PORT", default="5432"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_USER_MODEL = "users.CustomUser"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation" ".MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "users.authenticate.CustomAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(os.getenv("ACCESS_TOKEN_LIFETIME", 5))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=int(os.getenv("REFRESH_TOKEN_LIFETIME", 14))
    ),
    "AUTH_COOKIE": os.getenv("AUTH_COOKIE", "access"),
    "AUTH_REFRESH": os.getenv("AUTH_REFRESH", "refresh"),
    "AUTH_COOKIE_DOMAIN": None,
    "AUTH_COOKIE_SECURE": False,
    "AUTH_COOKIE_HTTP_ONLY": True,
    "AUTH_COOKIE_PATH": "/",
    "AUTH_COOKIE_SAMESITE": "Lax",
}

CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CORS_EXPOSE_HEADERS = ["Content-Type", "X-CSRFToken"]
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_TRUSTED_ORIGINS = [os.getenv("CSRF_TRUSTED_ORIGINS", "http://127.0.0.1")]
CORS_TRUSTED_ORIGINS = [os.getenv("CORS_TRUSTED_ORIGINS", "http://127.0.0.1")]
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

SPECTACULAR_SETTINGS = {
    "TITLE": "YellowGrader Documentation",
    "DESCRIPTION": "Documentation for YellowGrader API built with DRF",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "filter": True,  # включить поиск по тегам
    },
}

EMAIL_FILE = True if os.getenv("EMAIL_FILE") == "YES" else False
if EMAIL_FILE:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True if os.getenv("EMAIL_USE_TLS") == "YES" else False
    EMAIL_USE_SSL = False
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")
SERVER_EMAIL = os.getenv("EMAIL_HOST_USER")
