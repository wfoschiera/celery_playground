# import zlib
#
# import kombu.compression
from decouple import config
from django.conf import settings

broker_url = settings.CELERY_BROKER_URL
task_always_eager = not broker_url

timezone = settings.TIME_ZONE
worker_prefetch_multiplier = 1
worker_proc_alive_timeout = 30.0
task_acks_late = 1
task_eager_propagates = True
result_extended = True
worker_enable_remote_control = False
worker_send_task_events = False
task_time_limit = 1790
result_chord_join_timeout = 60
result_chord_retry_interval = 5 * 60
task_annotations = {"*": {"expires": 4 * 24 * 60 * 60}}  # TTL de 4 dias
#
# # S3 as the result backend
# result_backend = settings.RESULT_BACKEND
# s3_bucket = settings.S3_BUCKET
# s3_base_path = settings.S3_BASE_PATH
# s3_region = settings.S3_REGION

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#worker-lost-wait
worker_lost_wait = config("CELERY_WORKER_LOST_WAIT", default=120, cast=int)

result_compression = "maybe-gzip"
#
#
# def _try_gzip_decoder(payload):
#     try:
#         return zlib.decompress(payload)
#     except zlib.error:
#         return payload
#
#
# kombu.compression.register(zlib.compress, _try_gzip_decoder, content_type="maybe-gzip")
