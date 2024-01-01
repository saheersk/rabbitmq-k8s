import os
from datetime import timedelta

from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


SECRET_KEY = config("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS", default="", cast=lambda v: [s.strip() for s in v.split(",")]
)
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    'user'
]

CORS_ORIGIN_WHITELIST = ["http://localhost:5173",]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS')
CORS_ALLOW_HEADERS = ('content-type', 'authorization', 'upgrade', 'sec-websocket-key', 'sec-websocket-protocol')

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    'corsheaders.middleware.CorsMiddleware', 
]

ROOT_URLCONF = "authentication.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "authentication.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DATABASE_NAME", default=""),
        "USER": config("DATABASE_USERNAME", default=""),
        "PASSWORD": config("DATABASE_PASSWORD", default=""),
        "HOST": config("DATABASE_HOST", default=""),
        "PORT": config("DATABASE_PORT", default=""),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

RABBITMQ_HOST =  config("RABBITMQ_HOST", default="")
RABBITMQ_PORT = config("RABBITMQ_PORT", default="")
RABBITMQ_USERNAME = config("RABBITMQ_USERNAME", default="")
RABBITMQ_PASSWORD = config("RABBITMQ_PASSWORD", default="")
RABBITMQ_VIRTUAL_HOST = config("RABBITMQ_VIRTUAL_HOST", default="")

# Celery configuration
# CELERY_BROKER_URL = 'pyamqp://guest:guest@rabbitmq:5672//'
# CELERY_RESULT_BACKEND = 'db+postgresql://authentication_user:authentication_user123@postgres_authentication:5432/authentication_db'
# # CELERY_RESULT_BACKEND = 'rpc://'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Kolkata'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Configure JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_LIFETIME_REFRESH': timedelta(days=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME_SLIDING': timedelta(days=90),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': config('DJANGO_SECRET_KEY'),
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}
