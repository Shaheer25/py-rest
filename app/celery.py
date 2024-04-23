"""
--------------------------------------------CELERY--------------------------------------------------
"""

import os

from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://rest-redis:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://rest-redis:6379"
)

INSTALLED_SERVICES = []

celery.autodiscover_tasks(INSTALLED_SERVICES, force=True)

celery.conf.beat_schedule = {}
