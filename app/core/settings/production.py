import os
from .base import Base


class Production(Base):
    DEBUG = False
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    ALLOWED_HOSTS = ["www.django-test.lol"]

    CORS_ORIGIN_WHITELIST = [
        os.getenv('DJANGO_CORS_ORIGIN_WHITELIST')
    ]
