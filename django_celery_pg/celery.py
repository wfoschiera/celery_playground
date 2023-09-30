import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_pg.settings")

celery_app = Celery("django_celery_pg.celery", include=["demo_app.tasks", "demo_app.basic_canvas"])
celery_app.config_from_object("django_celery_pg.settings_celery")
celery_app.autodiscover_tasks()
