import os

# import time
from celery import Celery

from celery import shared_task
# from celery.signals import after_task_publish, before_task_publish


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_pg.settings")
celery_app = Celery("django_celery_pg")
celery_app.config_from_object("django_celery_pg.settings_celery")
celery_app.autodiscover_tasks()

#
# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
#
#
# @shared_task(queue="bp_ping")
# def ping_task():
#     return "pong"
#
#
# @after_task_publish.connect
# def log_task_published(sender, headers, body, routing_key, **kwargs):
#     if routing_key == "bp_link_trechos_classes":
#         logger.info("Task published", extra={"task_id": headers["id"], "task_name": sender})
#
#
# @before_task_publish.connect
# def add_published_timestamp(headers, **kwargs):
#     headers["timestamp"] = time.time()
