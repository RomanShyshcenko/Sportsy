from celery import Celery
from django.conf import settings

from configurations import importer

# Load Django configurations
importer.install()

app = Celery("core", broker=settings.CELERY_BROKER_URL)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
