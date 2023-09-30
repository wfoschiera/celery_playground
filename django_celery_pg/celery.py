import os

# import time
from celery import Celery

from celery import shared_task
# from celery.signals import after_task_publish, before_task_publish


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_pg.settings")

celery_app = Celery("django_celery_pg.celery", include=[
  "demo_app.tasks",
  "demo_app.basic_canvas"
  ])
celery_app.config_from_object("django_celery_pg.settings_celery")
celery_app.autodiscover_tasks()


# celery_app.conf.task_queues = (
#     # Definindo uma fila com o nome 'default'
#     celery_app.Queue('default', celery_app.Exchange('default'), routing_key='default'),

#     # Definindo uma fila qualquer para testes
#     celery_app.Queue('common', celery_app.Exchange('common'), routing_key='common'),

#     # Definindo uma fila chamada 'priority' com alta prioridade
#     celery_app.Queue('priority', celery_app.Exchange('priority'), routing_key='priority'),
# )

# celery_app.conf.task_default_queue = 'default'

