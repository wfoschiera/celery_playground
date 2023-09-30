import logging

from celery import shared_task
from celery.contrib import rdb

# from celery.signals import after_task_publish, before_task_publish
# from django_celery_pg.celery import celery_app


logger = logging.getLogger("playground")


@shared_task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@shared_task(queue="default")
def ping_task():
    return "pong"


@shared_task(queue="default")
def add(x, y):
    result = x + y
    return result


@shared_task(queue="default")
def mult(x, y):
    result = x * y
    return result


# howto: https://docs.celeryq.dev/en/stable/userguide/debugging.html#debugging
@shared_task(queue="default")
def add_debug(x, y):
    x + y
    rdb.set_trace()


# @after_task_publish.connect
# def log_task_published(sender, headers, body, routing_key, **kwargs):
#     if routing_key == "my_queue_name":
#         logger.info(
#             "Task published", extra={"task_id": headers["id"], "task_name": sender}
#         )
#
#
# @before_task_publish.connect
# def add_published_timestamp(headers, **kwargs):
#     headers["timestamp"] = time.time()
