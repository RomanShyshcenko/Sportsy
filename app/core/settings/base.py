import os
from pathlib import Path
from dotenv import load_dotenv

import datetime
from distutils.util import strtobool
from configurations import Configuration

# Requires for proper work with Pytest now and Celery in the future
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()


class Base(Configuration):

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third party apps
        'rest_framework',
        'django_filters',            # for filtering rest endpoints
        'django.contrib.sites',      # used by django-allauth
        'corsheaders',
        'social_django',

        # Your apps
        'user.apps.UserConfig',

    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'social_django.middleware.SocialAuthExceptionMiddleware',
    )

    ALLOWED_HOSTS = ["*"]
    ROOT_URLCONF = 'core.urls'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WSGI_APPLICATION = 'core.wsgi.application'

    SOCIAL_AUTH_URL_NAMESPACE = 'social'

    ADMINS = (
        ('Author', 'example@example.com'),
    )

    # Postgres
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv("POSTGRES_NAME", 'postgres'),
            'USER': os.getenv("POSTGRES_USER", 'postgres'),
            'PASSWORD': os.getenv("POSTGRES_PASSWORD", 'postgres'),
            'HOST': os.getenv("POSTGRES_HOST", 'localhost'),
            'PORT': os.getenv("POSTGRES_PORT", 5432),
        }
    }

    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    PASSWORD_RESET_TIMEOUT = 280  # 5 minute

    STATIC_URL = 'static/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / ''],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.request',
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]

    # DEBUG was set to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(str(os.getenv('DJANGO_DEBUG', False)))

    # Password Validation
    # https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Custom user app
    AUTH_USER_MODEL = 'user.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            # Make JWT Auth the default authentication mechanism for Django
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        )
    }

    SITE_ID = 1

    # Google configuration
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '13187130725-f3j8mrn0s3loq4olindgq92lnoaeua80.apps.googleusercontent.com'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

    # Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
        'https://www.googleapis.com/auth/userinfo.email'
    ]

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        'social_core.backends.google.GoogleOAuth2',

    )
    SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://localhost:8000/admin/'

    ACTIVATE_JWT = True

    # Remove username functionality. Email is identifier (django-allauth)
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = 'email'  # ( = "username" | "email" | "username_email )
    ACCOUNT_UNIQUE_EMAIL = True
    # ACCOUNT_EMAIL_VERIFICATION = 'optional'

    SOCIAL_AUTH_JSONFIELD_ENABLED = True

    # Email Backend
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'localhost')

    EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT', 1025)
    EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', 'localhost')
    EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', 'example')

    # Automatic mails
    DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL', 'hi@example.com')
    ACCOUNT_EMAIL_SUBJECT_PREFIX = os.getenv('DJANGO_ACCOUNT_EMAIL_SUBJECT_PREFIX', '[Example]')

    # celery broker and result
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', "redis://redis:6380/0")
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', "redis://redis:6380/0")

    # Account verification email
    ACCOUNT_ADAPTER = 'backend.users.adapter.DefaultAccountAdapterCustom'
    URL_FRONT = os.getenv('DJANGO_URL_FRONT', 'localhost:8080')
    # ACCOUNT_CONFIRM_EMAIL_ON_GET = True

    OLD_PASSWORD_FIELD_ENABLED = True
    LOGOUT_ON_PASSWORD_CHANGE = True
