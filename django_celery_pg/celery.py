import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_pg.settings")

celery_app = Celery(
    "django_celery_pg.celery",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["demo_app.tasks", "demo_app.basic_canvas"],
)
celery_app.config_from_object("django_celery_pg.settings_celery")
celery_app.autodiscover_tasks()
