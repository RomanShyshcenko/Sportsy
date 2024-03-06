import os
import configurations

from celery import app as celery_app


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')


# Load Django configurations
configurations.setup()

__all__ = ("celery_app",)
